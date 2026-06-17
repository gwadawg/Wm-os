---
title: Pre-Call Video Pages SEO, Conversion, and QA
domain: acquisition
owner: marketing-lead
status: draft
last_updated: 2026-06-16
review_cycle: monthly
artifact_type: launch-checklist
---

# Pre-Call Video Pages SEO, Conversion, and QA

## SEO requirements (per page)

- Unique page title from content model field `page_title`.
- Unique meta description from `meta_description`.
- Canonical URL set to each final route path.
- OpenGraph fields:
  - `og:title` from `page_title`
  - `og:description` from `meta_description`
  - `og:url` from final route
  - `og:type=video.other` or `website` based on platform standards
- Twitter/X card:
  - `summary_large_image`
  - matching title/description
- Include standard noindex guard for unpublished draft routes.

## Internal linking requirements

- Add 3 related page links under each video from `related_slugs`.
- Add optional "Next question" progression link using sequence order:
  - `whoweare` -> `rmopportunity` -> `whatmakesusdifferent` -> `burnt` -> `leads` -> `doweguaranteeresults` -> `callcenter`
- Keep link anchor copy objection-focused, not generic "read more."

## Conversion requirements

- Primary CTA above fold:
  - Label: `Book Your Strategy Call`
  - URL from model `cta.primary_url`
- Primary CTA repeated near bottom after proof/related section.
- Secondary CTA optional and lower emphasis.
- Ensure all CTAs preserve UTM parameters if present.

## Analytics tracking requirements

- Fire these events:
  - `video_page_view` with `{ slug, objectionAngle }`
  - `video_play_click` with `{ slug, youtubeId }`
  - `video_page_cta_primary_click` with `{ slug, ctaUrl }`
  - `video_page_cta_secondary_click` with `{ slug, ctaUrl }`
  - `video_page_related_click` with `{ slug, targetSlug }`
- Add event validation in QA before launch.

## Compliance requirements

- Do not publish invented pricing or terms.
- Guarantee language must remain aligned with founder-approved offer docs.
- If guarantees are mentioned, add internal legal/compliance review check.

## Pre-launch QA checklist

## Content fidelity

- [ ] Route slug maps to correct content `id`.
- [ ] Headline/eyebrow match source model.
- [ ] YouTube embed ID is correct.
- [ ] Sales letter sections render in correct order.
- [ ] No unsupported claims added.

## UX and visual

- [ ] Hero spacing and hierarchy match premium template.
- [ ] Embed displays correctly on mobile, tablet, desktop.
- [ ] Section contrast and typography match site brand tokens.
- [ ] CTA visible above fold on common desktop and mobile viewport sizes.
- [ ] Related links are tappable and readable on mobile.

## Technical and SEO

- [ ] Title/meta/canonical render correctly for each slug.
- [ ] OG/Twitter tags render in page source.
- [ ] 404 behavior works for unknown slug.
- [ ] No console errors on load and play interaction.

## Tracking and links

- [ ] Event `video_page_view` fires once per page load.
- [ ] Event `video_play_click` fires when user starts video.
- [ ] CTA events fire with correct route slug payload.
- [ ] Related click event captures source and destination slugs.
- [ ] CTA links resolve to expected destination URLs.

## Post-launch monitoring (first 14 days)

- Track top metrics by route:
  - page views
  - video play rate
  - CTA click-through rate
  - progression rate to next question page
- Flag low performers for copy and headline iteration.

## Related docs

- [Pre-Call Video Pages Content Model](pre-call-video-pages-content-model.yaml)
- [Pre-Call Video Page Template Spec](pre-call-video-page-template-spec.md)
- [Pre-Call Video Pages Route Rollout](pre-call-video-pages-route-rollout.md)
