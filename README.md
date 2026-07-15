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
cd D:\claude-seo\zehnati-seo-dashboard
.\sync-from-workspace.ps1 -Push
```

---

## روشن کردن GitHub Pages (یک‌بار — دقیق)

خطای Actions به‌خاطر این بود که Pages هنوز روی **GitHub Actions** تنظیم نشده بود.
برای این پروژهٔ استاتیک، **Deploy from a branch** کافی و ساده‌تر است.

### مراحل در GitHub
1. باز کنید: https://github.com/fishprogrammer/zehnati-seo-dashboard/settings/pages  
2. **Build and deployment → Source** را بگذارید روی:  
   **`Deploy from a branch`**  
3. Branch: **`main`**  
4. Folder: **`/ (root)`**  
5. **Save**

بعد از ۱–۲ دقیقه سایت زنده می‌شود:  
https://fishprogrammer.github.io/zehnati-seo-dashboard/

> اگر قبلاً Source را روی GitHub Actions گذاشته‌اید، همان را به **Deploy from a branch** عوض کنید.  
> فایل workflow Actions از ریپو حذف شد تا هر push خطای قرمز ندهد.

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
