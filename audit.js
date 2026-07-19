/* Claude SEO — تب آنالیز: بارگذاری تازه با هر رفرش صفحه */
(function () {
  const DEFAULT_URL = "https://zehnati.ir";
  const CMD_KEY = "zehnati-audit-cmd";

  const COMMANDS = [
    {
      id: "audit",
      label: "audit کامل",
      desc: "آنالیز جامع با subagentهای موازی",
      finding: "FULL-AUDIT-REPORT.md",
      altFinding: "audit-data.json",
      icon: "🔍",
    },
    {
      id: "page",
      label: "یک صفحه",
      desc: "آنالیز عمیق صفحه اصلی",
      finding: "page.md",
      altFinding: "parse-home.json",
      icon: "📄",
    },
    {
      id: "technical",
      label: "فنی",
      desc: "Sitemap، robots، CWV، امنیت",
      finding: "technical.md",
      icon: "⚙️",
    },
    {
      id: "content",
      label: "محتوا / E-E-A-T",
      desc: "کیفیت محتوا و اعتبار",
      finding: "content.md",
      icon: "✍️",
    },
    {
      id: "schema",
      label: "اسکیما",
      desc: "Schema.org — تشخیص و پیشنهاد",
      finding: "schema.md",
      icon: "🏷️",
    },
    {
      id: "local",
      label: "لوکال SEO",
      desc: "GBP، NAP، شعب اصفهان/تهران",
      finding: "local.md",
      icon: "📍",
    },
  ];

  let activeId = sessionStorage.getItem(CMD_KEY) || "technical";
  let statusCache = null;
  let lastLoadedAt = null;

  const IS_LOCAL =
    location.hostname === "127.0.0.1" || location.hostname === "localhost";
  const IS_CLIENT = !IS_LOCAL;

  function cmdText(id) {
    return `/seo ${id} ${DEFAULT_URL}`;
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function mdToHtml(md) {
    if (!md) return "";
    let html = escapeHtml(md);
    html = html.replace(/^### (.+)$/gm, "<h4>$1</h4>");
    html = html.replace(/^## (.+)$/gm, "<h3>$1</h3>");
    html = html.replace(/^# (.+)$/gm, "<h2>$1</h2>");
    html = html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
    html = html.replace(/^- (.+)$/gm, "<li>$1</li>");
    html = html.replace(/(<li>.*<\/li>\n?)+/g, (m) => `<ul>${m}</ul>`);
    html = html.replace(/\n\n/g, "</p><p>");
    html = `<p>${html}</p>`;
    html = html.replace(/<p><(h[234]|ul)/g, "<$1");
    html = html.replace(/<\/(h[234]|ul)><\/p>/g, "</$1>");
    html = html.replace(/<p><\/p>/g, "");
    return html;
  }

  function formatDate(iso) {
    if (!iso) return "—";
    try {
      const d = new Date(iso);
      return d.toLocaleDateString("fa-IR", {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch {
      return iso;
    }
  }

  function setLoadedNote(extra) {
    const el = document.getElementById("auditLoadedAt");
    if (!el || !lastLoadedAt) return;
    const t = formatDate(lastLoadedAt.toISOString());
    el.textContent = (extra ? extra + " · " : "") + "آخرین بارگذاری: " + t;
  }

  function syncScoreFromAudit(status) {
    const score = status?.summary?.health_score;
    if (score == null) return;
    const num = document.getElementById("scoreNum");
    const ring = document.getElementById("scoreRing");
    const label = document.getElementById("scoreLabel");
    if (num) num.textContent = score;
    if (ring) ring.style.setProperty("--pct", score);
    if (label && score < 40) label.textContent = "نیاز به اقدام فوری";
  }

  function renderAuditSummary(raw) {
    const s = raw.summary || {};
    const findings = (s.top_findings || [])
      .map((f) => `<li class="sev-critical">${escapeHtml(f)}</li>`)
      .join("");
    const wins = (s.quick_wins || [])
      .map((w) => `<li>${escapeHtml(w)}</li>`)
      .join("");
    return `
      <div class="audit-fallback">
        <div class="audit-fallback-grid">
          <div class="audit-stat"><span class="n">${s.health_score ?? "—"}</span><span class="l">امتیاز کلی</span></div>
          <div class="audit-stat"><span class="n">${escapeHtml(s.business_type || "—")}</span><span class="l">نوع کسب‌وکار</span></div>
          <div class="audit-stat"><span class="n">${formatDate(raw.generated_at)}</span><span class="l">تولید گزارش</span></div>
        </div>
        <h3>یافته‌های اصلی</h3><ul class="finding-list">${findings || "<li>—</li>"}</ul>
        <h3>اقدام‌های سریع</h3><ul>${wins || "<li>—</li>"}</ul>
        <p class="audit-fallback-lead">منبع: <code>audit-data.json</code> — snapshot آخرین audit است؛ با تغییر سایت به‌خود به‌روز نمی‌شود.</p>
      </div>`;
  }

  function fallbackHtml(id) {
    const D = window.ZEHNATI_SEO;
    if (!D) return "<p>دادهٔ پایه در دسترس نیست.</p>";

    if (id === "audit") {
      const bars = D.score.breakdown
        .map((b) => `<li><strong>${b.name}:</strong> ${b.score}/۱۰۰</li>`)
        .join("");
      const acts = D.actions
        .slice(0, 4)
        .map((a) => `<li class="sev-${a.priority}">${a.title}</li>`)
        .join("");
      return `
        <div class="audit-fallback">
          <p class="audit-fallback-lead">گزارش زنده موجود نیست — fallback از <strong>data.js</strong>:</p>
          <div class="audit-fallback-grid">
            <div class="audit-stat"><span class="n">${D.score.overall}</span><span class="l">امتیاز (تخمین)</span></div>
            <div class="audit-stat"><span class="n">${D.kpis[0].current}</span><span class="l">صفحات ایندکس</span></div>
            <div class="audit-stat"><span class="n">${D.kpis[1].current}</span><span class="l">پست بلاگ</span></div>
          </div>
          <h3>امتیاز دسته‌ها</h3><ul>${bars}</ul>
          <h3>اقدام‌های بحرانی</h3><ul class="finding-list">${acts}</ul>
        </div>`;
    }

    if (id === "page") {
      const h = D.homepage;
      return `
        <div class="audit-fallback">
          <p class="audit-fallback-lead">یافتهٔ <code>page.md</code> موجود نیست — baseline:</p>
          <table class="data audit-table">
            <tr><th>عنصر</th><th>الان</th><th>هدف</th></tr>
            <tr><td>Title</td><td>${escapeHtml(h.titleNow)}</td><td>${escapeHtml(h.titleTarget)}</td></tr>
            <tr><td>Meta</td><td>${escapeHtml(h.descNow)}</td><td>${escapeHtml(h.descTarget)}</td></tr>
            <tr><td>H1</td><td>ندارد</td><td>${escapeHtml(h.h1Target)}</td></tr>
          </table>
        </div>`;
    }

    if (id === "technical") {
      const items = D.techStatus
        .map(
          (t) =>
            `<div class="status-item"><div class="dot ${t.status}"></div><div><strong>${t.name}</strong><span>${t.detail}</span></div></div>`
        )
        .join("");
      return `<div class="audit-fallback"><p class="audit-fallback-lead">یافتهٔ زنده نیست — baseline:</p><div class="status-list">${items}</div></div>`;
    }

    if (id === "content" || id === "schema" || id === "local") {
      return IS_CLIENT
        ? `<div class="audit-fallback"><p class="audit-fallback-lead">گزارش این بخش هنوز آماده نیست.</p></div>`
        : `<div class="audit-fallback"><p class="audit-fallback-lead">فایل <code>${id}.md</code> یافت نشد. دستور را در Cursor اجرا کنید و صفحه را رفرش کنید.</p></div>`;
    }

    return "";
  }

  function staticPathsFor(name) {
    const rootFiles = new Set([
      "FULL-AUDIT-REPORT.md",
      "ACTION-PLAN.md",
      "audit-data.json",
    ]);
    if (rootFiles.has(name)) return ["./audit/" + name, "audit/" + name];
    return ["./audit/findings/" + name, "audit/findings/" + name];
  }

  function formatOf(name) {
    if (name.endsWith(".json")) return "json";
    if (name.endsWith(".md")) return "markdown";
    return "text";
  }

  async function fetchJson(url) {
    const bust =
      url + (url.includes("?") ? "&" : "?") + "_=" + Date.now();
    const res = await fetch(bust, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    return res.json();
  }

  async function fetchText(url) {
    const bust =
      url + (url.includes("?") ? "&" : "?") + "_=" + Date.now();
    const res = await fetch(bust, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    return res.text();
  }

  async function loadStatus() {
    try {
      statusCache = await fetchJson("/api/audit/status");
    } catch {
      try {
        statusCache = await fetchJson("./audit/status.json");
      } catch {
        statusCache = {
          ok: true,
          mode: "static",
          findings: [],
          summary: window.ZEHNATI_SEO
            ? { health_score: window.ZEHNATI_SEO.score.overall }
            : null,
        };
      }
    }
    syncScoreFromAudit(statusCache);
    return statusCache;
  }

  async function loadFinding(cmd) {
    const names = [cmd.finding];
    if (cmd.altFinding) names.push(cmd.altFinding);

    for (const name of names) {
      try {
        const data = await fetchJson(
          "/api/audit/finding?name=" + encodeURIComponent(name)
        );
        if (data.exists) return { ...data, picked: name };
      } catch {
        /* try static next */
      }
    }

    for (const name of names) {
      for (const path of staticPathsFor(name)) {
        try {
          const content = await fetchText(path);
          return {
            ok: true,
            exists: true,
            name,
            picked: name,
            format: formatOf(name),
            content,
            path,
            mode: "static",
          };
        } catch {
          /* try next path */
        }
      }
    }
    return { exists: false };
  }

  function renderCards() {
    const el = document.getElementById("auditCards");
    if (!el) return;
    const available = new Set((statusCache && statusCache.findings) || []);
    el.innerHTML = COMMANDS.map((c) => {
      const hasFile =
        available.has(c.finding) ||
        (c.altFinding && available.has(c.altFinding));
      const active = c.id === activeId ? " active" : "";
      const dot = hasFile ? "has-data" : "no-data";
      return `<button type="button" class="audit-card${active}" data-audit-id="${c.id}" aria-pressed="${c.id === activeId}">
        <span class="audit-card-icon">${c.icon}</span>
        <span class="audit-card-label">${c.label}</span>
        <span class="audit-card-cmd" dir="ltr">${cmdText(c.id)}</span>
        <span class="audit-card-dot ${dot}" title="${hasFile ? "گزارش موجود" : "هنوز اجرا نشده"}"></span>
      </button>`;
    }).join("");

    el.querySelectorAll(".audit-card").forEach((btn) => {
      btn.addEventListener("click", () => selectCommand(btn.dataset.auditId));
    });
  }

  function renderMeta(cmd, data, status) {
    const meta = document.getElementById("auditMeta");
    if (!meta) return;
    const hasReport = data && data.exists;
    const score =
      status?.summary?.health_score ??
      (window.ZEHNATI_SEO ? window.ZEHNATI_SEO.score.overall : "—");

    meta.innerHTML = IS_CLIENT
      ? `
      <div class="audit-meta-item"><span class="k">وضعیت گزارش</span><span class="v ${hasReport ? "ok" : "warn"}">${hasReport ? "موجود" : "در انتظار"}</span></div>
      <div class="audit-meta-item"><span class="k">آخرین به‌روزرسانی</span><span class="v">${formatDate(data?.modified || status?.last_modified)}</span></div>
      <div class="audit-meta-item"><span class="k">امتیاز</span><span class="v score">${score}<small>/۱۰۰</small></span></div>`
      : `
      <div class="audit-meta-item"><span class="k">دستور</span><code dir="ltr" class="audit-cmd-display">${cmdText(cmd.id)}</code></div>
      <div class="audit-meta-item"><span class="k">وضعیت گزارش</span><span class="v ${hasReport ? "ok" : "warn"}">${hasReport ? "زنده از فایل" : "fallback"}</span></div>
      <div class="audit-meta-item"><span class="k">آخرین تغییر فایل</span><span class="v">${formatDate(data?.modified || status?.last_modified)}</span></div>
      <div class="audit-meta-item"><span class="k">امتیاز</span><span class="v score">${score}<small>/۱۰۰</small></span></div>`;
  }

  async function renderDetail(cmd) {
    const body = document.getElementById("auditBody");
    const title = document.getElementById("auditTitle");
    const note = document.getElementById("auditNote");
    if (!body || !title) return;

    title.textContent = cmd.label + " — " + cmd.desc;
    body.innerHTML = '<p class="audit-loading">در حال بارگذاری از سرور…</p>';
    if (note) note.textContent = "";

    let data;
    try {
      data = await loadFinding(cmd);
    } catch {
      body.innerHTML = fallbackHtml(cmd.id);
      if (note) {
        note.textContent = IS_CLIENT
          ? "گزارش این بخش هنوز منتشر نشده است."
          : "گزارش audit پیدا نشد. لوکال: serve.py یا پوشه audit/ · آنلاین: بعد از sync و push.";
        note.className = "audit-note err";
      }
      return;
    }

    renderMeta(cmd, data, statusCache);

    if (data.exists) {
      if (data.format === "json") {
        const looksLikeError =
          /Error:|File not found|CategoryInfo/i.test(data.content) ||
          !data.content.trim().startsWith("{");
        if (looksLikeError) {
          body.innerHTML = fallbackHtml(cmd.id);
          if (note) {
            note.textContent = "فایل " + data.name + " خطا دارد.";
            note.className = "audit-note warn";
          }
          return;
        }
        try {
          const parsed = JSON.parse(data.content);
          if (cmd.id === "audit" && data.picked === "audit-data.json") {
            body.innerHTML = renderAuditSummary(parsed);
          } else if (cmd.id === "page") {
            body.innerHTML = `<pre class="audit-pre">${escapeHtml(JSON.stringify(parsed, null, 2))}</pre>`;
          } else {
            body.innerHTML = `<pre class="audit-pre">${escapeHtml(JSON.stringify(parsed, null, 2))}</pre>`;
          }
        } catch {
          body.innerHTML = `<pre class="audit-pre">${escapeHtml(data.content)}</pre>`;
        }
      } else if (data.format === "markdown") {
        body.innerHTML = `<article class="audit-md">${mdToHtml(data.content)}</article>`;
      } else {
        body.innerHTML = `<pre class="audit-pre">${escapeHtml(data.content)}</pre>`;
      }
      if (note) {
        note.textContent = IS_CLIENT
          ? "گزارش به‌روز از آخرین انتشار."
          : "منبع فایل: " +
            data.name +
            " — F5 فقط فایل را از دیسک می‌خواند؛ برای وضعیت جدید سایت باید audit دوباره اجرا یا فایل findings آپدیت شود.";
        note.className = "audit-note ok";
      }
    } else {
      body.innerHTML = fallbackHtml(cmd.id);
      if (note) {
        note.textContent = IS_CLIENT
          ? "گزارش این بخش هنوز آماده نیست."
          : "فایل گزارش نیست. دستور را در Cursor اجرا کنید، سپس صفحه را رفرش کنید (F5).";
        note.className = "audit-note warn";
      }
    }
  }

  async function selectCommand(id) {
    activeId = id;
    sessionStorage.setItem(CMD_KEY, id);
    renderCards();
    const cmd = COMMANDS.find((c) => c.id === id);
    if (cmd) await renderDetail(cmd);
  }

  async function refresh() {
    const btn = document.getElementById("btnAuditRefresh");
    if (btn) btn.disabled = true;
    setLoadedNote("در حال بارگذاری…");
    try {
      await loadStatus();
      renderCards();
      await selectCommand(activeId);
      lastLoadedAt = new Date();
      setLoadedNote();
    } catch {
      setLoadedNote("خطا در بارگذاری");
    } finally {
      if (btn) btn.disabled = false;
    }
  }

  function bindToolbar() {
    if (!IS_CLIENT) {
      document.getElementById("btnAuditCopy")?.addEventListener("click", async () => {
        const btn = document.getElementById("btnAuditCopy");
        try {
          await navigator.clipboard.writeText(cmdText(activeId));
          btn.textContent = "کپی شد ✓";
          setTimeout(() => (btn.textContent = "کپی دستور Cursor"), 1500);
        } catch {
          btn.textContent = "خطا در کپی";
        }
      });
    }
    document.getElementById("btnAuditRefresh")?.addEventListener("click", refresh);
  }

  async function init() {
    if (!document.getElementById("panel-audit")) return;
    bindToolbar();
    await refresh();

    window.addEventListener("pageshow", (ev) => {
      if (ev.persisted) refresh();
    });
  }

  window.ZehnatiAudit = { refresh, selectCommand };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
