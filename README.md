# Zehnati SEO Dashboard

داشبورد SEO آکادمی ذهن آتی — نسخهٔ وب برای کارفرما.

**منبع کار لوکال:** `D:\claude-seo\SEO\dashboard`  
**این ریپو:** نسخهٔ قابل نشر روی GitHub Pages

---

## آدرس آنلاین (بعد از روشن کردن Pages)

```
https://fishprogrammer.github.io/zehnati-seo-dashboard/
```

---

## روزمره: همان چیزی که لوکال می‌بینید → آنلاین

```powershell
cd G:\74-zehnati\zehnati-seo-dashboard
.\sync-from-workspace.ps1
git add -A
git commit -m "Update dashboard"
git push
```

اسکریپت `sync-from-workspace.ps1` این‌ها را از workspace کپی می‌کند:

- `index.html`, `data.js`, `audit.js`
- گزارش‌های `claude-seo/zehnati.ir-audit` → پوشهٔ `audit/`

---

## روشن کردن GitHub Pages (یک‌بار)

1. برو: https://github.com/fishprogrammer/zehnati-seo-dashboard/settings/pages  
2. **Source:** Deploy from a branch  
3. **Branch:** `main` / folder: `/ (root)`  
4. Save  

بعد از ۱–۲ دقیقه لینک بالا فعال می‌شود.

اگر از workflow استفاده می‌کنید (فایل `.github/workflows/pages.yml`)، در همان صفحه Source را روی **GitHub Actions** بگذارید.

---

## محدودیت نسخه آنلاین

| قابلیت | آنلاین |
|--------|--------|
| فاز / اقدام / چک‌لیست / کیورد | ✅ از `data.js` |
| تب آنالیز (فایل‌های audit) | ✅ از پوشهٔ `audit/` |
| بررسی زنده Sitemap (`serve.py`) | ❌ فقط لوکال |

تیک‌های فقط داخل مرورگر (`localStorage`) بین دستگاه‌ها مشترک نیستند. برای کارفرما پیشرفت را در `data.js` با `done: true` ثبت و push کنید.

---

## لوکال با API زنده

```powershell
cd D:\claude-seo\SEO\dashboard
python serve.py
# http://127.0.0.1:8765/
```
