# GSC noindex fix — 2026-10-12

Source: Coverage Drilldown «Excluded by noindex tag» (366 URLs)

## Result

| وضعیت | تعداد |
|--------|-------|
| محتوای ایندکس‌پذیر (لایو index) | ~358 |
| عمداً noindex مانده | 7 |
| محتوای مشکل‌دار باقی‌مانده | 0 |

## عمداً noindex (درست است)

- /auth/ — صفحه ورود
- /?login=true&type=register — ثبت‌نام
- /top-consultants-zehnati/ — صفحه تکراری مشاوران
- /tag/... — ۴ تگ (tag archive)

## کار انجام‌شده

- robots محتوا از 
oindex به index (Rank Math) + purge LiteSpeed
- نمونهٔ لایو بعد از purge: ollow, index
- چند URL که WAF روی path= 403 می‌داد با search/id مستقیم درست شد

## قدم بعدی در GSC

Page indexing → Excluded by «noindex» tag → **Validate fix**

گوگل معمولاً چند روز تا چند هفته طول می‌کشد تا لیست Coverage را به‌روز کند.
