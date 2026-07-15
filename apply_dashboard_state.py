# -*- coding: utf-8 -*-
"""Merge dashboard checkbox state into data.js done flags."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "dashboard-state.json"
DATA_FILE = ROOT / "data.js"
TZ = timezone(timedelta(hours=3, minutes=30))


def load_state(path: Path | None = None) -> dict:
    p = path or STATE_FILE
    if not p.exists():
        return {"actions": {}, "checks": {}, "selectedPhase": None}
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(state: dict, path: Path | None = None) -> dict:
    p = path or STATE_FILE
    out = {
        "actions": state.get("actions") or {},
        "checks": state.get("checks") or {},
        "selectedPhase": state.get("selectedPhase"),
        "updated_at": datetime.now(TZ).isoformat(timespec="seconds"),
    }
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def _set_done_for_id(text: str, item_id: str, done: bool) -> tuple[str, bool]:
    """Set done flag for the object that has this id."""
    pat = re.compile(
        rf'(id:\s*"{re.escape(item_id)}"(?:(?!\bid\s*:).)*?\bdone:\s*)(true|false)',
        re.S,
    )
    new_text, n = pat.subn(rf"\g<1>{str(done).lower()}", text, count=1)
    return new_text, n == 1


def apply_state_to_data_js(state: dict, data_path: Path | None = None) -> dict:
    data_path = data_path or DATA_FILE
    text = data_path.read_text(encoding="utf-8")
    actions = state.get("actions") or {}
    checks = state.get("checks") or {}
    updated = []
    missing = []

    for item_id, done in {**checks, **actions}.items():
        text2, ok = _set_done_for_id(text, str(item_id), bool(done))
        if ok:
            text = text2
            updated.append(item_id)
        else:
            missing.append(item_id)

    # bump updatedAtFa lightly via meta.updatedAt if present
    stamp = datetime.now(TZ).strftime("%Y-%m-%d")
    text = re.sub(
        r'(updatedAt:\s*")[^"]*(")',
        rf"\g<1>{stamp}\2",
        text,
        count=1,
    )

    data_path.write_text(text, encoding="utf-8")
    return {
        "ok": True,
        "data_file": str(data_path),
        "updated": updated,
        "missing": missing,
        "updated_count": len(updated),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Apply dashboard-state.json to data.js")
    ap.add_argument("--state", type=Path, default=STATE_FILE)
    ap.add_argument("--data", type=Path, default=DATA_FILE)
    args = ap.parse_args()
    state = load_state(args.state)
    result = apply_state_to_data_js(state, args.data)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
