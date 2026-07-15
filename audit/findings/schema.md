# Schema.org Audit - zehnati.ir Homepage

> Source: `zehnati.ir-audit/homepage.html`  
> Generated: 2026-07-15T22:12:00+03:30  
> Result: JSON-LD is present and valid in structure, but the local branch graph and expert/author entity are incomplete.

## Score

**69 / 100**

## JSON-LD Detected

One Rank Math JSON-LD block was found in the homepage head. It uses `https://schema.org` and contains a single `@graph` with these nodes:

| Node | Status | Notes |
|---|---:|---|
| `EducationalOrganization` + `Organization` (`#organization`) | Good | Main brand entity exists with stable `@id`, name, URL, and logo. |
| `WebSite` (`#website`) | Good | Includes `publisher`, `inLanguage`, and `SearchAction`. |
| `ImageObject` (`#logo`) | Good | Logo image is declared with URL, content URL, caption, dimensions, and language. |
| `ImageObject` (homepage primary image) | OK | Primary image exists, but schema dimensions are `200x200` despite the source image being a wide homepage asset. |
| `WebPage` (`#webpage`) | Good | Includes URL, title, publish/modified dates, language, organization reference, website reference, and primary image. |
| `EducationalOrganization` (`#local-tehran`) | Needs fix | Tehran branch has NAP basics but is not typed as `LocalBusiness`. |
| `LocalBusiness` (`#local-isfahan`) | Partial | Isfahan branch is typed correctly but is missing important local trust fields. |

## Validation Notes

- JSON-LD is present in the saved homepage and is syntactically parseable from the Rank Math block.
- `@context` is `https://schema.org`.
- Main entity IDs are stable URL fragments under `https://zehnati.ir/`.
- `WebSite.publisher`, `WebPage.about`, and `WebPage.isPartOf` correctly connect back to the organization graph.
- No `Person`, `Service`, `BreadcrumbList`, `FAQPage`, `Course`, `Review`, or `AggregateRating` schema was detected in the current homepage JSON-LD.
- `twitter:data1` is still `fish-programmer`, despite the page title and positioning referencing `دکتر زهرا جعفری`.

## Main Findings

1. **Tehran branch is not modeled as `LocalBusiness`.**  
   The node `https://zehnati.ir/#local-tehran` exists, but its `@type` is only `EducationalOrganization`. It includes branch basics such as name, phone, email, address, parent organization, area served, and sameAs, but the local business entity is not explicit.

2. **Isfahan `LocalBusiness` is incomplete.**  
   The node `https://zehnati.ir/#local-isfahan` has a useful base: name, URL, telephone, email, parent organization, `PostalAddress`, area served, and sameAs. It still lacks `geo`, `openingHoursSpecification`, `priceRange`, `postalCode`, `hasMap`, and verified branch-specific citation/profile links.

3. **Person schema for Dr Zahra Jafari is missing.**  
   The homepage title names `دکتر زهرا جعفری`, and visible content references Dr Jafari, but the graph does not include a `Person` node for her. This weakens E-E-A-T and entity disambiguation for the expert behind the academy.

4. **Twitter author metadata still exposes `fish-programmer`.**  
   The page has `twitter:label1` = `نویسنده` and `twitter:data1` = `fish-programmer`. This conflicts with the public expert/brand identity and should be corrected in WordPress/Rank Math author settings.

5. **The consultation offer has no `Service` schema.**  
   The homepage targets free کنکور consultation and includes lead CTAs, but the structured data does not describe the service, provider, service area, or action target.

## FAQPage Policy

No `FAQPage` schema was detected, and the saved homepage does not show a clear visible FAQ/Q&A section. This is acceptable. Do not add `FAQPage` only for SEO: Google retired broad FAQ rich results in May 2026. If real FAQ content is later added visibly on the page, `FAQPage` can be used as an informational/AI clarity signal, not as a Google rich-result opportunity.

## Missing Schemas

High priority:

- `LocalBusiness` for the Tehran branch, or dual typing such as `["EducationalOrganization", "LocalBusiness"]`, with complete local fields.
- Enriched `LocalBusiness` for Isfahan with `geo`, opening hours, map/profile links, postal code, and branch-specific identity.
- `Person` for `دکتر زهرا جعفری`, connected to the organization and page where accurate.

Medium priority:

- `Service` for the free کنکور consultation offer if the visible homepage copy clearly supports provider, area served, channel, and CTA details.
- `BreadcrumbList` only where a visible breadcrumb trail exists, especially on service/city/article pages.

Conditional:

- `FAQPage` only if exact visible Q&A content exists on the page. Treat it as Info/GEO support, not a Google FAQ rich-result feature.
- `Course` only on actual course pages with course-specific details, not on the generic homepage.

## Recommended LocalBusiness Shape

Use one stable branch node per city:

```json
{
  "@type": ["EducationalOrganization", "LocalBusiness"],
  "@id": "https://zehnati.ir/#local-tehran",
  "name": "آکادمی ذهن آتی — تهران",
  "parentOrganization": {"@id": "https://zehnati.ir/#organization"},
  "url": "https://zehnati.ir/",
  "telephone": "+98-21-28427259",
  "email": "info@zehnati.ir",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "میدان فاطمی",
    "addressLocality": "تهران",
    "addressRegion": "تهران",
    "addressCountry": "IR"
  },
  "areaServed": ["تهران", "ایران"],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "ADD_REAL_LATITUDE",
    "longitude": "ADD_REAL_LONGITUDE"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "ADD_REAL_PRICE_RANGE",
  "hasMap": "ADD_REAL_MAP_URL"
}
```

Repeat the same pattern for `https://zehnati.ir/#local-isfahan` using the real Isfahan coordinates, postal code, hours, map URL, and verified branch profile links.

## Recommended Person Shape

Add a real expert entity and connect it to the page/organization:

```json
{
  "@type": "Person",
  "@id": "https://zehnati.ir/#dr-zahra-jafari",
  "name": "دکتر زهرا جعفری",
  "alternateName": "Dr Zahra Jafari",
  "worksFor": {"@id": "https://zehnati.ir/#organization"},
  "affiliation": {"@id": "https://zehnati.ir/#organization"},
  "knowsAbout": ["مشاوره کنکور", "برنامه ریزی کنکور", "مشاوره تحصیلی"],
  "sameAs": [
    "ADD_VERIFIED_PROFILE_URLS"
  ]
}
```
