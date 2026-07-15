#!/usr/bin/env python3
"""Local SEO dashboard server for zehnati.ir.

Serves the static dashboard and proxies live HTTP status checks
(avoids browser CORS limits). Also persists checkbox state and can
publish to the GitHub Pages repo.

Usage:
    python serve.py
    # then open http://127.0.0.1:8765/
"""

from __future__ import annotations

import json
import mimetypes
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import apply_dashboard_state as dash_state

ROOT = Path(__file__).resolve().parent
AUDIT_DIR = ROOT.parents[1] / "claude-seo" / "zehnati.ir-audit"
PUBLISH_REPO = Path(r"D:\claude-seo\zehnati-seo-dashboard")
PORT = 8765
ALLOWED_HOSTS = {"zehnati.ir", "www.zehnati.ir"}

ALLOWED_FINDINGS = {
    "FULL-AUDIT-REPORT.md",
    "ACTION-PLAN.md",
    "audit-data.json",
    "page.md",
    "parse-home.json",
    "technical.md",
    "content.md",
    "schema.md",
    "local.md",
    "performance.md",
    "sitemap.md",
    "visual.md",
    "geo.md",
    "google.md",
    "sxo.md",
}


def check_url(raw: str, method: str = "HEAD") -> dict:
    parsed = urlparse(raw)
    if parsed.scheme not in ("http", "https") or parsed.hostname not in ALLOWED_HOSTS:
        return {"ok": False, "error": "host_not_allowed", "status": None}

    req = urllib.request.Request(
        raw,
        method=method,
        headers={"User-Agent": "ZehnatiSEO-Dashboard/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            body = resp.read().decode("utf-8", errors="replace") if method == "GET" else ""
            return {
                "ok": True,
                "status": resp.status,
                "url": raw,
                "final_url": resp.geturl(),
                "body": body,
            }
    except urllib.error.HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8", errors="replace") if method == "GET" else ""
        except Exception:  # noqa: BLE001
            body = ""
        return {
            "ok": True,
            "status": exc.code,
            "url": raw,
            "error": str(exc.reason),
            "body": body,
        }
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "status": None, "url": raw, "error": str(exc), "body": ""}


def probe_site() -> dict:
    """Live re-check of homepage SEO signals + sitemap + robots."""
    home = check_url("https://zehnati.ir/", method="GET")
    robots = check_url("https://zehnati.ir/robots.txt", method="GET")
    sitemap = check_url("https://zehnati.ir/sitemap_index.xml", method="HEAD")

    html = (home.get("body") or "").lower()
    robots_txt = robots.get("body") or ""

    title_m = re.search(r"<title[^>]*>(.*?)</title>", home.get("body") or "", re.I | re.S)
    meta_desc_m = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
        home.get("body") or "",
        re.I | re.S,
    )
    if not meta_desc_m:
        meta_desc_m = re.search(
            r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']',
            home.get("body") or "",
            re.I | re.S,
        )
    robots_meta_m = re.search(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
        home.get("body") or "",
        re.I | re.S,
    )
    h1_count = len(re.findall(r"<h1\b", html))

    homepage = {
        "status": home.get("status"),
        "ok": home.get("ok") and home.get("status") == 200,
        "title": (title_m.group(1).strip() if title_m else None),
        "meta_description": (meta_desc_m.group(1).strip() if meta_desc_m else None),
        "meta_robots": (robots_meta_m.group(1).strip() if robots_meta_m else None),
        "noindex": "noindex" in ((robots_meta_m.group(1) if robots_meta_m else "") or "").lower(),
        "has_h1": h1_count > 0,
        "h1_count": h1_count,
        "has_ga": any(x in html for x in ("gtag(", "googletagmanager", "google-analytics", "ga(")),
        "has_rankmath": "rank-math" in html or "rank_math" in html,
        "has_litespeed": "litespeed" in html,
        "has_educational_org": "educationalorganization" in html,
        "has_local_business": "localbusiness" in html,
        "has_wpcp_error": "wpcp-error" in html or "wpcp_error" in html,
        "ssl": True,
    }

    checklist_hints = {
        "w1-sitemap": sitemap.get("status") == 200,
        "w1-ga4": homepage["has_ga"],
        "w1-rankmath": homepage["has_rankmath"],
        "w1-error": not homepage["has_wpcp_error"],
        "w1-schema-org": homepage["has_educational_org"],
        "w1-schema-isf": homepage["has_local_business"],
        "w1-gsc": None,
        "w1-psi": None,
        "w1-gbp-isf": None,
    }

    return {
        "ok": True,
        "checked_at": datetime.now(tz=timezone.utc).isoformat(),
        "sitemap": {
            "status": sitemap.get("status"),
            "ok": sitemap.get("status") == 200,
            "url": "https://zehnati.ir/sitemap_index.xml",
        },
        "robots": {
            "status": robots.get("status"),
            "ok": robots.get("status") == 200,
            "mentions_sitemap": "sitemap:" in robots_txt.lower(),
            "snippet": robots_txt[:400],
        },
        "homepage": homepage,
        "checklist_hints": checklist_hints,
    }


def _iso_mtime(path: Path) -> str | None:
    if not path.is_file():
        return None
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _read_finding(name: str) -> dict:
    if name not in ALLOWED_FINDINGS:
        return {"ok": False, "error": "not_allowed"}

    candidates = [AUDIT_DIR / name, AUDIT_DIR / "findings" / name]
    path = next((p for p in candidates if p.is_file()), None)
    if path is None:
        return {"ok": True, "exists": False, "name": name}

    content = path.read_text(encoding="utf-8", errors="replace")
    suffix = path.suffix.lower()
    if suffix == ".json":
        fmt = "json"
    elif suffix == ".md":
        fmt = "markdown"
    else:
        fmt = "text"

    return {
        "ok": True,
        "exists": True,
        "name": name,
        "path": str(path.relative_to(AUDIT_DIR.parents[1])),
        "format": fmt,
        "content": content,
        "modified": _iso_mtime(path),
    }


def _audit_status() -> dict:
    findings: list[dict] = []
    latest: str | None = None

    def add_file(rel: str, path: Path) -> None:
        nonlocal latest
        if not path.is_file():
            return
        mtime = _iso_mtime(path)
        if mtime and (latest is None or mtime > latest):
            latest = mtime
        findings.append({"name": rel, "modified": mtime, "size": path.stat().st_size})

    if AUDIT_DIR.is_dir():
        for item in sorted(AUDIT_DIR.iterdir()):
            if item.is_file():
                add_file(item.name, item)
        findings_dir = AUDIT_DIR / "findings"
        if findings_dir.is_dir():
            for item in sorted(findings_dir.iterdir()):
                if item.is_file():
                    add_file(item.name, item)

    summary = None
    summary_path = AUDIT_DIR / "audit-data.json"
    if summary_path.is_file():
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            summary = None

    return {
        "ok": True,
        "audit_dir": str(AUDIT_DIR),
        "exists": AUDIT_DIR.is_dir(),
        "findings": [f["name"] for f in findings],
        "files": findings,
        "last_modified": latest,
        "summary": summary.get("summary") if isinstance(summary, dict) else None,
    }


def _json_response(handler: SimpleHTTPRequestHandler, payload: dict, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
    handler.send_header("Pragma", "no-cache")
    handler.end_headers()
    handler.wfile.write(body)


def _read_json_body(handler: SimpleHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length") or 0)
    raw = handler.rfile.read(length) if length else b"{}"
    if not raw:
        return {}
    return json.loads(raw.decode("utf-8"))


def _sync_publish_repo(push: bool = True) -> dict:
    if not PUBLISH_REPO.is_dir() or not (PUBLISH_REPO / ".git").is_dir():
        return {"ok": False, "error": f"publish_repo_missing: {PUBLISH_REPO}"}

    state = dash_state.load_state()
    applied = dash_state.apply_state_to_data_js(state, ROOT / "data.js")

    dest = PUBLISH_REPO
    for name in ("index.html", "data.js", "audit.js"):
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, dest / name)

    audit_dest = dest / "audit"
    findings_dest = audit_dest / "findings"
    findings_dest.mkdir(parents=True, exist_ok=True)
    for name in ("audit-data.json", "FULL-AUDIT-REPORT.md", "ACTION-PLAN.md"):
        src = AUDIT_DIR / name
        if src.exists():
            shutil.copy2(src, audit_dest / name)
    src_findings = AUDIT_DIR / "findings"
    if src_findings.is_dir():
        for f in src_findings.iterdir():
            if f.is_file() and f.suffix in {".md", ".json"} and not f.name.startswith("_"):
                shutil.copy2(f, findings_dest / f.name)

    names = [p.name for p in sorted(audit_dest.glob("*")) if p.is_file()]
    names += [p.name for p in sorted(findings_dest.glob("*")) if p.is_file()]
    score = None
    ap = audit_dest / "audit-data.json"
    if ap.exists():
        try:
            score = (json.loads(ap.read_text(encoding="utf-8")).get("summary") or {}).get(
                "health_score"
            )
        except Exception:  # noqa: BLE001
            score = None
    (audit_dest / "status.json").write_text(
        json.dumps(
            {
                "ok": True,
                "mode": "static",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "findings": names,
                "summary": {"health_score": score} if score is not None else None,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    if not push:
        return {"ok": True, "pushed": False, "applied": applied, "repo": str(dest)}

    def git(*args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=str(dest),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    git("add", "-A")
    status = git("status", "--porcelain")
    if not (status.stdout or "").strip():
        return {
            "ok": True,
            "pushed": False,
            "unchanged": True,
            "applied": applied,
            "repo": str(dest),
            "message": "no file changes to push",
            "pages_url": "https://fishprogrammer.github.io/zehnati-seo-dashboard/",
        }

    msg = f"Publish dashboard state {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    commit = git("commit", "-m", msg)
    if commit.returncode != 0:
        return {
            "ok": False,
            "error": "git_commit_failed",
            "stderr": commit.stderr,
            "stdout": commit.stdout,
            "applied": applied,
        }
    push_res = git("push", "origin", "main")
    if push_res.returncode != 0:
        return {
            "ok": False,
            "error": "git_push_failed",
            "stderr": push_res.stderr,
            "stdout": push_res.stdout,
            "applied": applied,
        }
    return {
        "ok": True,
        "pushed": True,
        "applied": applied,
        "repo": str(dest),
        "pages_url": "https://fishprogrammer.github.io/zehnati-seo-dashboard/",
        "commit_message": msg,
    }


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_OPTIONS(self):  # noqa: N802
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/check":
            qs = parse_qs(parsed.query)
            target = (qs.get("url") or [""])[0]
            payload = check_url(target)
            payload.pop("body", None)
            _json_response(self, payload)
            return

        if path == "/api/site/probe":
            _json_response(self, probe_site())
            return

        if path == "/api/audit/status":
            _json_response(self, _audit_status())
            return

        if path == "/api/audit/finding":
            qs = parse_qs(parsed.query)
            name = (qs.get("name") or [""])[0].strip()
            if not name:
                _json_response(self, {"ok": False, "error": "missing_name"}, status=400)
                return
            result = _read_finding(name)
            status = 200 if result.get("ok", True) else 404
            _json_response(self, result, status=status)
            return

        if path == "/api/dashboard-state":
            _json_response(self, {"ok": True, "state": dash_state.load_state()})
            return

        return super().do_GET()

    def do_POST(self):  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            body = _read_json_body(self)
        except Exception as exc:  # noqa: BLE001
            _json_response(self, {"ok": False, "error": f"bad_json: {exc}"}, status=400)
            return

        if path == "/api/dashboard-state":
            saved = dash_state.save_state(body.get("state") or body)
            _json_response(self, {"ok": True, "state": saved})
            return

        if path == "/api/publish":
            if body.get("state"):
                dash_state.save_state(body["state"])
            push = body.get("push", True)
            result = _sync_publish_repo(push=bool(push))
            status = 200 if result.get("ok") else 500
            _json_response(self, result, status=status)
            return

        _json_response(self, {"ok": False, "error": "not_found"}, status=404)

    def end_headers(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/") or path.endswith((".js", ".html")):
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            self.send_header("Pragma", "no-cache")
        if path.endswith(".js"):
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
        elif path.endswith(".css"):
            ctype, _ = mimetypes.guess_type(path)
            if ctype:
                self.send_header("Content-Type", ctype)
        super().end_headers()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Zehnati SEO dashboard -> http://127.0.0.1:{PORT}/")
    print(f"Audit dir: {AUDIT_DIR}")
    print(f"Publish repo: {PUBLISH_REPO}")
    print("Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
