# GSC Coverage — Blocked due to other 4xx (۲۲ جولای ۲۰۲۶)

> منبع: `Downloads/https___zehnati.ir_-Coverage-Drilldown-2026-07-22.xlsx`  
> Issue: **Blocked due to other 4xx issue** · Sitemap scope: All known pages

---

## خلاصه

| مورد | مقدار |
|------|--------|
| تعداد URL در Table | **۵** |
| نوع | همه `wp-admin/admin-ajax.php?action=iguru_like&...` |
| وضعیت لایو | **HTTP 400** · body = `0` |
| شدت واقعی | **پایین** — صفحه محتوایی نیست؛ endpoint لایک قالب iGuru |

گوگل این URLها را نباید ایندکس کند. ۴۰۰ یعنی درخواست نامعتبر (nonce منقضی / بدون session) — **رفتار درست برای admin-ajax لایک**.

---

## لیست URLها

| Last crawled | URL (کوتاه) |
|--------------|-------------|
| 2026-02-17 | `admin-ajax.php?action=iguru_like&post_id=6307&...` |
| 2026-02-17 | `...post_id=6448&...` |
| 2026-02-15 | `...post_id=6464&...` |
| 2026-01-29 | `...post_id=6362&...` (دو nonce متفاوت) |

---

## چرا در GSC آمده؟

دکمه «لایک» قالب/تم **iGuru** احتمالاً با تگ `<a href="...admin-ajax.php?action=iguru_like...">` در HTML بوده؛ ربات گوگل لینک را کشف کرده و خزیده.

---

## چه کار کنید؟

### ۱) اجباری نیست — اولویت پایین
این ۵ URL به رتبه لندینگ‌ها آسیب جدی نمی‌زنند. می‌توانید Validate Fix بزنید و رها کنید تا از گزارش بیفتند.

### ۲) پیشنهادی — جلوگیری از کشف دوباره
- در تم/Elementor: دکمه لایک را از `<a href>` به `<button>` یا `javascript:void(0)` + AJAX ببرید (یا پلاگین like را غیرفعال کنید اگر لازم نیست).
- لینک‌های `admin-ajax.php` را در محتوای قابل خزیدن نگذارید.

### ۳) اختیاری — تسریع حذف از GSC
در Rank Math → Redirections برای **همین ۵ URL دقیق** نوع **۴۱۰ Gone** بزنید (نه ۳۰۱ به خانه).  
فایل: `SEO/05-tracking/rankmath-410-ajax-like-4xx.csv`

### ۴) بعد از اصلاح
GSC → همان issue → **Validate Fix**

---

## چه کار نکنید

- ۳۰۱ همه `admin-ajax.php` به خانه (بی‌فایده / نویز)
- Index کردن این URLها
- نگران «۵ صفحه ۴xx» در برابر ۶۱×۴۰۴ قبلی نباشید — جنس مشکل فرق دارد

---

## داشبورد

Coverage ردیف «مسدود به‌خاطر خطای ۴xx دیگر» → note به‌روز می‌شود: ۵× iguru_like · 400 · اولویت پایین.
