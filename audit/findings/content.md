# Content & E-E-A-T Audit — zehnati.ir

> **Scope:** saved homepage HTML plus live probes of priority commercial, local, about, and contact URLs  
> **Business:** education/local entrance-exam counseling brand led by دکتر زهرا جعفری  
> **Generated:** 2026-07-15T22:08:00+03:30

## Score

**Content score: 44/100**

The site has moved in the right direction on basic homepage SEO: the title, meta description, H1, branch mentions, and CTA language now align with «مشاوره رایگان کنکور» and the دکتر زهرا جعفری / ذهن آتی brand. The content system is still not strong enough for competitive education SEO because the trust entity is inconsistent, the homepage is thin as a service explanation, multiple P0 landings are missing or redirected to mismatched legacy posts, and the main `/مشاوره-کنکور/` hub behaves like a mixed archive rather than a polished commercial page.

## What Works

- The homepage title and meta description target «مشاوره رایگان کنکور»، ذهن آتی، دکتر زهرا جعفری، اصفهان، تهران، and online consultation.
- The homepage has one visible H1: «مشاوره رایگان کنکور در ذهن آتی».
- The page includes conversion paths and proof assets: consultation request, contact page links, report-card/interview, satisfaction, webinar, voice-content, branch mentions, and a lead form.
- `/about/` returns 200, has one H1, and positions the academy around دکتر زهرا جعفری with proof claims such as ۲۰۰۰+ قبولی and ۵۰۰ رتبه دو و سه‌رقمی.
- `/contact-us/` returns 200 and has a useful contact meta description with phone number, Isfahan/Tehran branch mentions, and online consultation language.
- Organization-level schema exists, and the broader audit shows useful education/local entity foundations, but the entity graph still needs cleanup.

## Top Findings

### 1. E-E-A-T is undermined by `fish-programmer` author signals

**Severity:** Critical

The homepage still exposes `fish-programmer` in author-related metadata (`twitter:data1`) and the live probes show `fish-programmer` present in homepage, `/مشاوره-کنکور/`, `/about/`, `/contact-us/`, and redirected legacy pages. For a counseling brand led by دکتر زهرا جعفری, this sends the wrong expertise signal to Google, social previews, and AI answer engines.

**Recommendation:** Replace every `fish-programmer` author/byline/schema/social signal with either دکتر زهرا جعفری or a verified آکادمی ذهن آتی organization author. Add a real `Person` entity for دکتر زهرا جعفری with credentials, role, image, `sameAs`, `worksFor`, and a link to `/about/`. Keep the developer identity out of public page metadata.

### 2. Homepage is still thin as a commercial service explanation

**Severity:** High

The homepage now has correct headline/meta intent, but the visible content is still mostly a hero, proof/asset links, branch notes, and CTA/form elements. It does not clearly explain the consultation method, student fit, parent/student pain points, what the free session includes, how ongoing follow-up works, what makes دکتر جعفری credible, pricing/package expectations, or common objections. Raw page text counts are inflated by Elementor templates, popups, nav, footer, and repeated assets; the actual service narrative remains light.

**Recommendation:** Add 700-1,000 words of concise, useful homepage copy. Include a 150-200 word intro, service blocks for حضوری/آنلاین, a short دکتر زهرا جعفری bio, method/process steps, branch details, proof with context, FAQ, and internal links to the core service/local landings.

### 3. P0 service and local landings are missing or mismatched

**Severity:** Critical

Live probes confirm major P0 gaps. `/مشاوره-آنلاین-کنکور/`, `/اصفهان/`, `/تهران/`, `/بهترین-مشاور-کنکور-اصفهان/`, `/بهترین-مشاور-کنکور-تهران/`, and `/قیمت-مشاوره-کنکور/` return 404. `/ثبت-نام/` redirects to «ثبت نام بدون کنکور», `/برنامه-ریزی-کنکور/` redirects to an ارشد کامپیوتر article, and `/انتخاب-رشته/` redirects to an ارشد دانشگاه آزاد article. These redirects capture the slug but not the intent.

**Recommendation:** Build or repair the P0 landing set before scaling articles: `/مشاوره-کنکور/`, `/مشاوره-آنلاین-کنکور/`, `/قیمت-مشاوره-کنکور/`, `/ثبت-نام/`, `/برنامه-ریزی-کنکور/`, `/انتخاب-رشته/`, `/اصفهان/`, `/تهران/`, and city-specific best-consultant pages. Each page should have one intent, one H1, 700-1,200 words of service-specific content, proof, FAQs, CTA, schema, and links to related service/city pages.

### 4. `/مشاوره-کنکور/` is live but not quality-ready

**Severity:** High

`/مشاوره-کنکور/` returns 200 with a relevant title and meta description, but the page has 17 H1 elements. The H1 list includes the main service title plus unrelated article/widget titles such as stress, study methods, teacher comparisons, sleep, deleted topics, and other posts. The live probe also did not find دکتر زهرا جعفری on the page. This is a weak commercial hub for the site’s most important category.

**Recommendation:** Rebuild `/مشاوره-کنکور/` as the canonical consultation hub. Use exactly one H1, remove archive/widget titles from primary content, add دکتر جعفری authority, explain the counseling model, cover رشته‌های تجربی/ریاضی/انسانی, include online/in-person options, results/proof, pricing/registration path, FAQ, and strong internal links to child pages.

### 5. About/contact trust pages exist but need stronger citation blocks

**Severity:** Medium

`/about/` is much better than before: it is live, has one H1, and mentions دکتر زهرا جعفری. `/contact-us/` is live and has a strong contact meta description, but the live page text does not mention دکتر جعفری. Both pages still need more structured trust content for credentials, legal/business identity, branch NAP, operating hours, service area, consultation process, and proof sources.

**Recommendation:** Make `/about/` the canonical founder and academy trust page. Add credentials, years of experience, methodology, media/social profiles, measurable results with context, and links to service pages. Expand `/contact-us/` with separate Isfahan and Tehran branch blocks, consistent phone/address/hours, map links, expected response time, and a short explanation of what happens after submitting the form.

### 6. AI citation readiness is low

**Severity:** High

AI systems need short, consistent, extractable facts. The site currently has useful brand signals, but the facts are fragmented: wrong author identity, missing/weak Person entity for دکتر زهرا جعفری, missing P0 city/service pages, no visible homepage FAQ, inconsistent local branch depth, and a main service hub polluted by unrelated H1s. This makes it less likely to be cited for «بهترین مشاور کنکور اصفهان»، «مشاوره کنکور آنلاین»، «مشاوره رایگان کنکور»، or «دکتر زهرا جعفری».

**Recommendation:** Add citation-ready blocks across the homepage and P0 landings: "About ذهن آتی", "Who is دکتر زهرا جعفری?", "Services", "Branches", "How consultation works", "Results", "Pricing/registration", and "FAQ". Mirror those blocks in `Person`, `LocalBusiness`, `Service`, and `FAQPage` schema only where the same content is visibly present.

## Priority Roadmap

1. Remove `fish-programmer` from all public metadata, schema, bylines, and social cards.
2. Rebuild `/مشاوره-کنکور/` as a clean service hub with one H1 and Dr. Jafari trust signals.
3. Create missing P0 pages for online consultation, price, registration, planning, انتخاب رشته, Isfahan, Tehran, and city-specific best-consultant intent.
4. Expand homepage copy so it explains the offer, method, expert, proof, branches, and next step.
5. Strengthen `/about/` and `/contact-us/` into citation-ready trust assets.
6. Add schema after the visible content is corrected, not as a substitute for content.
