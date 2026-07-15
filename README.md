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

### روش ۱ (پیشنهادی) — از خود داشبورد
1. `serve.py` را اجرا کنید → http://127.0.0.1:8765/
2. تیک‌ها را بزنید (خودکار در `dashboard-state.json` ذخیره می‌شود)
3. دکمهٔ **«انتشار برای کارفرما»** را بزنید  
   → تیک‌ها داخل `data.js` نوشته می‌شود، به ریپو کپی و `git push` می‌شود

### روش ۲ — اسکریپت
```powershell
cd G:\74-zehnati\zehnati-seo-dashboard
.\sync-from-workspace.ps1 -Push
```

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
| فاز / اقدام / چک‌لیست / کیورد | ✅ از `data.js` (بعد از انتشار) |
| تب آنالیز | ✅ از پوشهٔ `audit/` |
| تیک زدن / انتشار | ❌ فقط لوکال با `serve.py` |
| بررسی زنده Sitemap | ❌ فقط لوکال |

روی نسخه آنلاین تیک‌ها **فقط‌خواندنی** از `data.js` هستند تا کارفرما همان چیزی را ببیند که شما با «انتشار برای کارفرما» فرستاده‌اید.

---

## لوکال با API زنده

```powershell
cd D:\claude-seo\SEO\dashboard
python serve.py
# http://127.0.0.1:8765/
```
