# SXO — Homepage Intent and Conversion Fit

> Source: careful live homepage and key-URL probe via `scripts/fetch_page.py` on 2026-07-15.

## What Works

- Homepage directly matches the target offer:
  - Title: `مشاوره رایگان کنکور | آکادمی ذهن آتی — دکتر زهرا جعفری`
  - H1: `مشاوره رایگان کنکور در ذهن آتی`
  - Meta: mentions 9 years, 500+ rankers, Isfahan, Tehran, and online coverage.
- The homepage has one H1 and returns HTTP 200.
- CTAs are discoverable: `tel:02128427259` and a Didar form link.
- The page contains `دکتر زهرا جعفری`, `اصفهان`, `تهران`, `LocalBusiness`, and `EducationalOrganization` signals.
- `/about/` and `/contact-us/` are live, have one H1 each, and support trust/contact intent.

## Intent Match

Homepage intent is strong for `مشاوره رایگان کنکور`. The offer, CTA, and first-step action are clear enough for lead generation.

The main SXO weakness is expectation-setting. A user considering a high-trust education consultation still needs more before submitting a form:

- What exactly happens after the free consultation request?
- Who reviews the student situation?
- Is the first call with Dr. Zahra Jafari, a branch team, or a counselor?
- What does the free consultation include and exclude?
- How are online, Isfahan, and Tehran paths different?
- What proof supports `۵۰۰+ رتبه برتر` and the branch claims?

## Hub Fit

The homepage should stay focused on free consultation. The broader hub `/مشاوره-کنکور/` should carry commercial comparison, service depth, pricing paths, packages, and internal links. Today it returns HTTP 200, but the live probe found 17 H1s and article/listing behavior. That forces the homepage to carry too much of the commercial journey.

## CTA and Journey Gaps

Several next-step pages are absent or mismatched:

- `/مشاوره-آنلاین-کنکور/` is 404.
- `/ثبت-نام/` redirects to an unrelated no-exam registration article.
- `/برنامه-ریزی-کنکور/` redirects to an unrelated graduate computer entrance article.
- `/انتخاب-رشته/` redirects to an unrelated graduate Azad selection article.
- `/اصفهان/` and `/تهران/` are 404.

These gaps reduce post-click confidence and make the homepage CTA feel isolated.

## Recommendations

1. Add a near-CTA `بعد از ثبت درخواست چه می‌شود؟` section with call timing, counselor flow, and expected outcome.
2. Add proof before the form: testimonials, rank examples, advisor credentials, branch photos/map, and concise outcome metrics.
3. Segment users into parent, student, online, Isfahan, and Tehran blocks with separate CTA copy.
4. Rebuild `/مشاوره-کنکور/` as the main commercial hub with one H1 and links to pricing, package, online, registration, planning, selection, and city pages.
5. Fix the broken/mismatched journey URLs so CTA users have credible next pages after the homepage.
