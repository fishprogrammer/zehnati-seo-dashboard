# Dashboard

Static HTML dashboard (GitHub Pages copy). Online: https://fishprogrammer.github.io/zehnati-seo-dashboard/

برای ویرایش تیک‌ها و publish، سرور محلی workspace را اجرا کنید (نه این کپی):

```powershell
cd E:\74-zehnati\claude-seo\SEO\dashboard
py -3 serve.py
```

سپس http://127.0.0.1:8876/

- Progress and checklist data live in `data.js`.
- Audit snapshots live under `audit/`.
- Online build is read-only; editing ticks requires the local workspace + publish/sync step.
