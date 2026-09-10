---
name: seo-check
description: Review SEO on request or when public web changes affect crawlability, indexing, canonical URLs, redirects, metadata, or search-facing content. Skip native apps, private dashboards, and UI-only changes without a search or sharing impact.
---

# Review the affected public pages

1. Establish which routes should be public and indexable, their intended audience, and the changed behavior. Inspect the existing framework and route conventions; do not assume Next.js or a rendering strategy.
2. Check the relevant source and rendered output when available:
   - HTTP status, redirects, canonical URLs, robots directives, and sitemap entries agree with the intended indexability. Preserve intentional access controls and noindex behavior.
   - Public content and internal links are discoverable in the supported rendering path. Check changed navigation or pagination when it affects discovery.
   - Titles and descriptions accurately identify the page. Avoid invented character quotas, keyword-density rules, or unsupported ranking promises.
   - Document language and alternate-language links are consistent when the site supports them. Review social preview metadata if sharing is in scope.
   - Structured data reflects visible, supported facts and the applicable schema. Do not invent reviews, prices, availability, or other product data.
   - Meaningful images have appropriate alternative text; decorative images may use empty alt text. Check image sizing and loading when relevant to the reported issue.
3. Investigate performance only when it affects the task. Use measured evidence and distinguish local or lab results from real-user data; do not invent universal timing thresholds.
4. Report actionable issues with the affected route or file, evidence, and a specific correction. Identify checks that need a deployed URL or external indexing data.

Consult current official search-engine or framework documentation when a rule is uncertain. Local source or rendering checks do not prove indexing, rankings, or traffic. Changing access controls, publishing a site, or submitting external changes requires authorization for that exact effect; an SEO review alone does not grant it.
