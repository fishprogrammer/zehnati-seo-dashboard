# Technical SEO Audit - zehnati.ir

> Live check time: **2026-07-15T22:12:19+03:30**  
> Business type: local-service / education - Zehn Ati Academy, Isfahan/Tehran  
> Technical score: **48/100**

## Executive Summary

Crawl and basic indexability are in good shape: robots.txt is live, the sitemap index and all discovered child sitemaps return 200, the homepage is indexable with a correct canonical, title, meta description, one H1, viewport, and GA4. The `/about/` page was rechecked live and now has exactly one H1.

The main remaining risks are commercial-page and server configuration issues: the pricing landing page still returns 404, the main counseling hubs still have many H1 tags, core security headers are missing, PHP is exposed through `X-Powered-By`, and `fish-programmer` is still present in homepage Twitter metadata.

## 1. Crawlability

- `robots.txt`: **200** -> final `https://zehnati.ir/robots.txt`

```txt
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://zehnati.ir/sitemap_index.xml
```

- Explicit AI crawler rules: `{"GPTBot": false, "ChatGPT-User": false, "ClaudeBot": false, "PerplexityBot": false, "Bytespider": false, "Google-Extended": false, "CCBot": false}`

### Sitemaps

- `https://zehnati.ir/sitemap_index.xml` -> **200** | child_count=6
- `https://zehnati.ir/sitemap.xml` -> **200** | final `https://zehnati.ir/sitemap_index.xml`
- `https://zehnati.ir/post-sitemap1.xml` -> 200 (sample URLs: 5)
- `https://zehnati.ir/post-sitemap2.xml` -> 200 (sample URLs: 5)
- `https://zehnati.ir/post-sitemap3.xml` -> 200 (sample URLs: 5)
- `https://zehnati.ir/page-sitemap.xml` -> 200 (sample URLs: 5)
- `https://zehnati.ir/category-sitemap.xml` -> 200 (sample URLs: 5)
- `https://zehnati.ir/local-sitemap.xml` -> 200 (sample URLs: 1)

## 2. Indexability - Key URLs

- `/`: **200** -> final `https://zehnati.ir/` | robots `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` | H1 x 1 | title: مشاوره رایگان کنکور | آکادمی ذهن آتی — دکتر زهرا جعفری
  - H1s: ["مشاوره رایگان کنکور در ذهن آتی"]
- `/about/`: **200** -> final `https://zehnati.ir/about/` | robots `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` | H1 x 1 | title: درباره آکادمی ذهن آتی | دکتر زهرا جعفری
  - H1s: ["درباره آکادمی ذهن آتی"]
- `/contact-us/`: **200** -> final `https://zehnati.ir/contact-us/` | robots `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` | H1 x 1 | title: تماس با ذهن آتی | مشاوره رایگان کنکور
  - H1s: ["ارتباط با ما"]
- `/مشاوره-کنکور/`: **200** -> final `https://zehnati.ir/%D9%85%D8%B4%D8%A7%D9%88%D8%B1%D9%87-%DA%A9%D9%86%DA%A9%D9%88%D8%B1/` | robots `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` | H1 x 17 | title: مشاوره کنکور | بهترین مشاور کنکور — ذهن آتی
  - H1s: ["مشاوره کنکور", "مشاوره کنکور", "مشاور تحصیلی", "غیبت در کنکور؛ اگر سر جلسه کنکور نریم چی میشه؟", "بهترین روش مطالعه جامعه شناسی برای کنکور", "رتبه لازم برای رشته فیزیوتراپی، چگونه می‌توان به رشته فیزیوتراپی دست یافت؟", "شرایط ثبت نام دانشگاه غیرانتفاعی ۱۴۰۳", "بررسی انواع دام‌های تستی در کنکور", "همه چیز درباره کنکور اردیبهشت", "کارنامه سبز کنکور"]
- `/مشاوره-کنکور-تجربی/`: **200** -> final `https://zehnati.ir/%D9%85%D8%B4%D8%A7%D9%88%D8%B1%D9%87-%DA%A9%D9%86%DA%A9%D9%88%D8%B1-%D8%AA%D8%AC%D8%B1%D8%A8%DB%8C/` | robots `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` | H1 x 17 | title: مشاوره کنکور تجربی - ذهن آتی
  - H1s: ["مشاوره کنکور تجربی", "اسما نوایی ارده", "قبولی پزشکی دانشگاه علوم پزشکی زنجان", "داستان قبولی زهرا صادقی", "بهترین منابع کنکور", "فراموش نکردن مطالب", "آزمون عملی کنکور هنر رشته گرافیک", "برای مدرسه بخونیم یا کنکور؟", "ستایش شجاعیان", "قبولی پزشکی زنجان"]
- `/قیمت-مشاوره-کنکور/`: **404** -> final `https://zehnati.ir/%D9%82%DB%8C%D9%85%D8%AA-%D9%85%D8%B4%D8%A7%D9%88%D8%B1%D9%87-%DA%A9%D9%86%DA%A9%D9%88%D8%B1/` | robots `follow, noindex` | H1 x 1 | title: Page Not Found - ذهن آتی
  - H1s: ["صفحه پیدا نشد."]

## 3. Homepage Checks

- robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large`
- canonical: `https://zehnati.ir/`
- title: `مشاوره رایگان کنکور | آکادمی ذهن آتی — دکتر زهرا جعفری`
- meta description present: `True`
- H1 count: `1` | H1s: `["مشاوره رایگان کنکور در ذهن آتی"]`
- GA4: `["G-Y0GZ4B5T0Y"]`
- viewport: `True`
- html lang: `fa-IR`
- fish-programmer present: `True` | twitter:data1=`fish-programmer`

## 4. Security / Headers

- HTTP -> HTTPS: status `301` | Location `https://zehnati.ir/`
- Missing security headers: `["strict-transport-security", "content-security-policy", "x-frame-options", "x-content-type-options", "referrer-policy", "permissions-policy"]`
- X-Powered-By: `PHP/8.3.31`
- Server: `None`

## 5. IndexNow / llms.txt

- IndexNow key checks: `{"https://zehnati.ir/indexnow-key.txt": 404, "https://zehnati.ir/.well-known/indexnow-key": 404}`
- llms.txt: status `404`

## 6. Structured Data / Rendering Signals

- JSON-LD types on homepage: `["EducationalOrganization", "ImageObject", "LocalBusiness", "Organization", "PostalAddress", "SearchAction", "WebPage", "WebSite"]`
- Core SEO content is present in raw HTML; this is WordPress/Elementor, not a pure SPA shell.
- Homepage HTML size: ~134022 bytes | script tags: ~29

## Findings

### 1. Pricing landing page returns 404

**Severity:** high  
The requested transactional URL /قیمت-مشاوره-کنکور/ returns HTTP 404.

**Recommendation:** Create a dedicated pricing/consultation-cost landing page or 301 it to the closest relevant commercial page, then add it to sitemap and internal links.

### 2. Too many H1 tags on /مشاوره-کنکور/

**Severity:** high  
/مشاوره-کنکور/ returns 200 but has 17 H1 tags, which weakens hub-page structure.

**Recommendation:** Keep one page-level H1 and demote card/archive/widget titles to H2/H3.

### 3. Too many H1 tags on /مشاوره-کنکور-تجربی/

**Severity:** high  
/مشاوره-کنکور-تجربی/ returns 200 but has 17 H1 tags, which weakens hub-page structure.

**Recommendation:** Keep one page-level H1 and demote card/archive/widget titles to H2/H3.

### 4. Core security headers are missing

**Severity:** medium  
Homepage is missing: strict-transport-security, content-security-policy, x-frame-options, x-content-type-options, referrer-policy, permissions-policy

**Recommendation:** Set HSTS, X-Content-Type-Options, X-Frame-Options or CSP frame-ancestors, Referrer-Policy, and Permissions-Policy at server/CDN level. Test CSP in Report-Only first.

### 5. X-Powered-By exposes PHP

**Severity:** low  
x-powered-by: PHP/8.3.31

**Recommendation:** Disable expose_php or strip this header at LiteSpeed/web server level.

### 6. fish-programmer remains in homepage metadata

**Severity:** medium  
twitter:data1=fish-programmer; fish_programmer=True

**Recommendation:** Update the WordPress/Rank Math author or social metadata to Dr. Zahra Jafari or Zehn Ati Academy.

### 7. robots.txt has no explicit AI crawler policy

**Severity:** info  
No dedicated User-agent rule was found for GPTBot, ClaudeBot, PerplexityBot, Bytespider, Google-Extended, or CCBot.

**Recommendation:** Decide the GEO/AI-crawler policy and express it explicitly in robots.txt.

### 8. IndexNow is not configured

**Severity:** info  
IndexNow key file was not found at /indexnow-key.txt or /.well-known/indexnow-key.

**Recommendation:** Enable IndexNow through Rank Math or a dedicated plugin to speed up Bing/Yandex discovery.

### 9. llms.txt is missing

**Severity:** low  
https://zehnati.ir/llms.txt returns 404.

**Recommendation:** Add a concise llms.txt at the site root for LLM/GEO discovery if this is part of the content strategy.

