# Local SEO — zehnati.ir

> Source: careful live HTTP and JSON-LD probe via `scripts/fetch_page.py` on 2026-07-15.

## What Works

- Homepage and contact page mention both `اصفهان` and `تهران`.
- Phone CTA is crawlable as `tel:02128427259`, and schema uses `+98-21-28427259`.
- Homepage JSON-LD includes branch-level entities:
  - Tehran: `EducationalOrganization`, `آکادمی ذهن آتی — تهران`, `میدان فاطمی`, `تهران`.
  - Isfahan: `LocalBusiness`, `آکادمی ذهن آتی — اصفهان`, `خیابان وحید`, `اصفهان`.
- Contact page title and meta support local conversion: `تماس با ذهن آتی | مشاوره رایگان کنکور` and branch mentions for Isfahan/Tehran.
- `local-sitemap.xml` returns HTTP 200.

## NAP Assessment

The NAP foundation exists but is not strong enough for two-city local SEO:

- Name: brand is consistent as `ذهن آتی` / `آکادمی ذهن آتی`.
- Address: city and street-level branch data exists in schema, but the live schema does not expose postal code, geo coordinates, opening hours, `hasMap`, or branch-specific URLs.
- Phone: phone is consistent and discoverable, but the same phone is used for both branches. That can be acceptable for a hybrid academy, but branch pages should explain the routing.
- Schema mismatch: Isfahan is typed as `LocalBusiness`, while Tehran is typed as `EducationalOrganization`. For local pack/entity clarity, Tehran should also have a local business-compatible type or a separate local branch node.

## City Landing Coverage

The highest-risk local issue is coverage. The checked local slugs are not live commercial landings:

- `/اصفهان/` returns 404.
- `/تهران/` returns 404.
- `/بهترین-مشاور-کنکور-اصفهان/` returns 404.
- `/بهترین-مشاور-کنکور-تهران/` returns 404.
- `local-sitemap.xml` only points to `locations.kml`, not city landing pages.

This leaves homepage/contact/schema carrying all local relevance, which is too thin for competitive `مشاور کنکور اصفهان` and `مشاور کنکور تهران` intent.

## GBP Signals

No Google Business Profile URL, review source, map profile URL, review markup, or branch-specific citation link was confirmed in the homepage schema. Social links are visible on the page, but they are not connected as strong structured `sameAs` evidence for each branch.

## Recommendations

1. Create dedicated Isfahan and Tehran city hubs with visible NAP, map, route/appointment expectations, branch proof, FAQs, and CTAs.
2. Add city-service pages for `بهترین مشاور کنکور اصفهان`, `بهترین مشاور کنکور تهران`, and online/hybrid variants.
3. Normalize branch schema: complete `PostalAddress`, add `openingHours`, `geo`, `hasMap`, branch `url`, and consistent local-compatible types.
4. Add eligible GBP links and review/citation proof, keeping NAP identical across GBP, website copy, schema, and footer/contact blocks.
5. Link homepage, contact page, and `/مشاوره-کنکور/` to both city hubs with descriptive Persian anchors.
