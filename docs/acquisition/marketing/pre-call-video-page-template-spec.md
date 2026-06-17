---
title: Pre-Call Video Page Template Spec
domain: acquisition
owner: marketing-lead
status: draft
last_updated: 2026-06-16
review_cycle: monthly
artifact_type: implementation-spec
---

# Pre-Call Video Page Template Spec

## Goal

Define one premium page template that can render all pre-call objection videos as native routes inside the same website and domain.

## Route contract

- Base path: `/reversemortgage/{slug}`
- Supported slugs:
  - `whoweare`
  - `rmopportunity`
  - `whatmakesusdifferent`
  - `burnt`
  - `leads`
  - `doweguaranteeresults`
  - `callcenter`

## Section order

1. Hero
2. Video embed
3. Why this matters (short sales letter)
4. Proof strip
5. Related question pages
6. CTA block
7. Trust footer

## Content API (template props)

```ts
type VideoPageData = {
  id: string;
  slug: string;
  pageTitle: string;
  metaDescription: string;
  eyebrow: string;
  headline: string;
  supportLine: string;
  youtubeId: string;
  watchUrl: string;
  objectionAngle: string;
  salesLetter: {
    problemFraming: string;
    reframe: string;
    mechanism: string;
    expectedOutcome: string;
    nextStep: string;
  };
  proofPoints: string[];
  cta: {
    primaryLabel: string;
    primaryUrl: string;
    secondaryLabel?: string;
    secondaryUrl?: string;
  };
  relatedSlugs: string[];
};
```

## UX and visual rules (premium style)

- Use existing design tokens from the site (color, type scale, spacing, radius, shadow).
- Keep max content width constrained for readability (`~720-820px` body text lane).
- Use generous vertical rhythm between sections (`56-96px` depending breakpoint).
- Apply subtle hierarchy shifts:
  - Eyebrow uppercase/small caps style
  - Strong H1
  - Calm supporting copy
- Keep motion restrained:
  - Fade/translate section reveal only
  - No aggressive parallax or autoplay effects
- Embed video in a polished frame:
  - 16:9 lock
  - Rounded corners
  - Soft elevation

## Section implementation details

## 1) Hero

- Required: `eyebrow`, `headline`, `supportLine`
- Layout:
  - Center-aligned on mobile
  - Optional split layout on desktop if brand allows
- Objective: clarify the objection this page resolves in 3-8 seconds

## 2) Video embed

- Use YouTube embed by `youtubeId`
- Include accessible title and lazy loading
- Keep controls visible; avoid autoplay by default

## 3) Why this matters

- Render five short paragraphs from `salesLetter`:
  - Problem framing
  - Reframe
  - Mechanism
  - Expected outcome
  - Next step
- Keep each paragraph concise and readable on mobile

## 4) Proof strip

- Render 2-4 approved bullets from `proofPoints`
- Do not introduce unapproved claims or guarantee numbers

## 5) Related question pages

- Render 3 related cards from `relatedSlugs`
- Card content:
  - Question-style title
  - One-line value statement
  - Link to route

## 6) CTA block

- Primary button: strategy call
- Optional secondary link for comparison page
- Repeat CTA near bottom even if one appears above the fold

## 7) Trust footer

- Two short lists:
  - Who this is for
  - Who this is not for
- Keep language direct and non-judgmental

## Content and compliance guardrails

- Pull copy from:
  - `pre-call-objection-videos.md`
  - `pre-call-video-pages-content-model.yaml`
- Keep claim fidelity:
  - Do not invent pricing
  - Do not invent guarantee terms
  - Validate offer language against founder-approved terms before publishing

## Performance and accessibility

- Lazy-load embeds
- Maintain good LCP by prioritizing hero content before iframe load
- Meet WCAG basics:
  - Keyboard focus states
  - Semantic heading order
  - Contrast-compliant text/buttons

## Analytics events

- `video_page_view` (on route load)
- `video_play_click` (when user initiates play)
- `video_page_cta_primary_click`
- `video_page_cta_secondary_click`
- `video_page_related_click`

## Related docs

- [Pre-Call Objection Video Assets](pre-call-objection-videos.md)
- [Pre-Call Video Pages Content Model](pre-call-video-pages-content-model.yaml)
