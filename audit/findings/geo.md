# GEO / AI Search Readiness — zehnati.ir

> Source: careful live `robots.txt`, `llms.txt`, sitemap, homepage, and JSON-LD probe via `scripts/fetch_page.py` on 2026-07-15.

## AI Crawler Access

`robots.txt` returns HTTP 200 and is permissive:

```txt
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://zehnati.ir/sitemap_index.xml
```

No explicit rules were found for AI crawlers such as GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, or Applebot-Extended. This means AI crawlers are not blocked by robots rules, but they also are not guided toward preferred source pages.

## llms.txt

`https://zehnati.ir/llms.txt` returns HTTP 404. For GEO this is a missed opportunity because the site has a clear entity, expert-led proposition, hybrid service model, and two city markets that could be summarized in a canonical crawler-friendly file.

## Citability

The site has some citable facts:

- Brand: `ذهن آتی` / `آکادمی ذهن آتی`.
- Offer: `مشاوره رایگان کنکور`.
- Expert signal: `دکتر زهرا جعفری`.
- Locations: Isfahan and Tehran.
- Phone: `02128427259`.
- Schema: Organization/EducationalOrganization plus Isfahan `LocalBusiness` and Tehran branch signals.

The weak point is source depth. AI systems need stable, extractable pages that answer factual questions directly. Current gaps include:

- No `llms.txt`.
- No clean city pages for Isfahan/Tehran.
- No strong pages for online consultation, pricing, packages, registration, planning, or selection.
- `/مشاوره-کنکور/` has 17 H1s and listing behavior, reducing its reliability as a citation source.
- `sameAs` in homepage schema is mostly self-referential rather than connected to verified external profiles, GBP, or citation sources.
- The page still contains `fish-programmer`, which muddies author/entity interpretation.

## Recommendations

1. Publish `/llms.txt` with canonical facts: brand, Dr. Zahra Jafari, services, cities, phone, official pages, and preferred citation URLs.
2. Create stable source pages for `مشاوره آنلاین کنکور`, Isfahan branch, Tehran branch, pricing/packages, registration flow, planning method, selection service, and results/testimonials.
3. Add concise factual blocks on homepage/about/contact that mirror schema exactly and are easy for AI systems to quote.
4. Expand `sameAs` with verified profiles and GBP URLs where eligible.
5. Remove stale `fish-programmer` author/entity signals from rendered metadata and schema.
6. Keep AI crawlers allowed unless business/legal policy requires selective restriction.
