# Sitemap SEO — zehnati.ir

> Source: careful live HTTP probe via `scripts/fetch_page.py` on 2026-07-15.

## What Works

- `https://zehnati.ir/sitemap_index.xml` returns HTTP 200 and is referenced from `robots.txt`.
- The sitemap index exposes six children: `post-sitemap1.xml`, `post-sitemap2.xml`, `post-sitemap3.xml`, `page-sitemap.xml`, `category-sitemap.xml`, and `local-sitemap.xml`.
- Child sitemap fetches returned HTTP 200. Counts from the live probe: posts 200 + 200 + 83, pages 23, categories 17, local 1.
- Homepage, `/about/`, `/contact-us/`, and `/مشاوره-کنکور/` are present in `page-sitemap.xml`.
- `/مشاوره-کنکور/` returns HTTP 200 with a relevant title: `مشاوره کنکور | بهترین مشاور کنکور — ذهن آتی`.

## P0 Landing Coverage Gaps

The sitemap is technically available, but P0 commercial and local landing coverage is still incomplete. The live page checks found:

- `/مشاوره-آنلاین-کنکور/` returns 404.
- `/اصفهان/` returns 404.
- `/تهران/` returns 404.
- `/بهترین-مشاور-کنکور-اصفهان/` returns 404.
- `/بهترین-مشاور-کنکور-تهران/` returns 404.
- `/ثبت-نام/` 301 redirects to an unrelated `ثبت نام بدون کنکور` article.
- `/برنامه-ریزی-کنکور/` 301 redirects to an unrelated `برنامه ریزی کنکور ارشد کامپیوتر 1404` article.
- `/انتخاب-رشته/` 301 redirects to an unrelated `انتخاب رشته ارشد دانشگاه آزاد` article.

`page-sitemap.xml` therefore has a crawlable homepage and one consultation hub, but not the clean architecture needed for primary service, online, registration, planning, selection, and city intent.

## Hub Quality Issue

`/مشاوره-کنکور/` is present and indexable, but the live fetch found 17 H1 elements, including many article titles. That makes the URL behave like a listing/archive instead of a focused commercial hub for `مشاوره کنکور`.

## Recommendations

1. Build and index clean P0 landings for online consultation, Isfahan, Tehran, best-consultant city pages, registration, planning, selection, pricing, and packages.
2. Stop redirecting short commercial slugs like `/ثبت-نام/`, `/برنامه-ریزی-کنکور/`, and `/انتخاب-رشته/` into mismatched articles.
3. Rebuild `/مشاوره-کنکور/` with one H1, clear offer, proof, FAQs, pricing/next-step links, and internal links to child landings.
4. After publishing each landing, verify HTTP 200, self-canonical, indexable meta robots, internal links, and inclusion in `page-sitemap.xml`.
