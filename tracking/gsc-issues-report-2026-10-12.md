# گزارش مشکلات GSC — zehnati.ir

تاریخ بررسی: ۲۰۲۶-۱۰-۱۲ · منبع: Google Search Console (مرورگر)  
آخرین آپدیت Indexing در GSC: ۱۰/۹/۲۶ · CWV: ۱۰/۱۱/۲۶

## خلاصه اجرایی

| متریک | مقدار | وضعیت |
|--------|--------|--------|
| Indexed | **۲۲۸** | ⚠️ افت نسبت به ۲۹۶ (سپتامبر) |
| Not indexed | **۶۷۱** (۹ دلیل) | بحرانی |
| کلیک ۳ماه (Overview) | ۱۴٬۷۵۱ | مثبت |
| Sitemap `/sitemap_index.xml` | Success · ۲۸۶ صفحه | OK |
| HTTPS | ۱۰۶ HTTPS · ۰ Non-HTTPS | OK |
| Breadcrumbs | ۱۰۵ Valid · ۰ Invalid | OK |
| CWV موبایل | ۰ Good · **۱۰۶ Need improvement** · ۰ Poor | بحرانی (LCP) |

## ۱) Page indexing — چرا ایندکس نیستند

| دلیل | صفحات | Validation | اولویت | اقدام |
|------|--------|------------|--------|--------|
| Excluded by `noindex` tag | **۳۶۶** | Failed | بحرانی | لایو درست شد (~۳۵۹ index) · در GSC **Validate fix** |
| Discovered – currently not indexed | **۱۳۰** | Not Started | بالا | لینک داخلی + Request indexing برای P0/P1 |
| Crawled – currently not indexed | **۱۰۹** | Not Started | بالا | عمق محتوا / حذف تکراری / تقویت سیگنال |
| Page with redirect | **۳۲** | Not Started | متوسط | زنجیره ریدایرکت کوتاه نگه دار |
| Not found (404) | **۲۹** | Failed | بحرانی | ۳۰۱ به جایگزین یا حذف از لینک/سایت‌مپ |
| Alternate page with proper canonical | ۲ | Not Started | پایین | معمولاً نرمال |
| Redirect error | ۱ | Not Started | بالا | لوپ/زنجیره خراب |
| Blocked due to 403 | ۱ | Not Started | بالا | دسترسی crawler |
| Blocked by robots.txt | ۱ | Not Started | بالا | استثنا برای URL مهم |
| Blocked due to other 4xx | ۰ | Passed | OK | — |

**نکته noindex:** در سایت robots محتوا از `noindex` به `index` برگشته (به‌جز `/auth/`، login، تگ‌ها، صفحه تکراری مشاوران). عدد ۳۶۶ در GSC تا Validate + recrawl پایین نمی‌آید.

## ۲) Core Web Vitals (موبایل · CrUX)

- **LCP issue: longer than 2.5s (mobile)** → **۱۰۶ URL** · Validation=**Failed**
- Desktop: دادهٔ کافی نیست
- هم‌راستا با کارهای فاز۴: FCP/LCP خانه، WebP، minify، کاهش request

## ۳) Enhancements / امنیت

| گزارش | وضعیت |
|--------|--------|
| Unparsable structured data | **۱ Invalid** — *Incorrect value type* · Not Started |
| Breadcrumbs | سالم (۱۰۵ Valid) |
| HTTPS | سالم |
| Sitemap | Success · last read Oct 5, 2026 |

## ۴) Performance (Overview)

- ۱۴٬۷۵۱ کلیک وب در بازهٔ نمایش‌داده‌شده
- توصیه GSC: صفحهٔ تخمین رتبه کنکور اخیراً **+۱۴۴٪** کلیک داشته — فرصت تقویت

## ۵) کارهای پیش‌رو (اولویت برای پنل فاز ۴)

1. **Validate fix** برای noindex در GSC  
2. **پاکسازی ۲۹×۴۰۴** (۳۰۱ / حذف لینک / سایت‌مپ)  
3. **LCP موبایل ≤۲.۵s** برای ۱۰۶ URL (خانه + قالب مشترک)  
4. صف **۱۳۰ Discovered** + **۱۰۹ Crawled not indexed** (لینک داخلی + کیفیت)  
5. **۱ Unparsable schema** (Incorrect value type)  
6. رفع تکی: redirect error / 403 / robots.txt block  
7. ادامه GBP اصفهان + ۱۵ کیورد P1 (از قبل در پنل)

گزارش کامل JSON/MD مرتبط: `gsc-2026-10-12-noindex-fix-final.md`
