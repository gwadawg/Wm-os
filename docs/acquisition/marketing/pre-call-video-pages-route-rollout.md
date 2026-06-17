---
title: Pre-Call Video Pages Route Rollout
domain: acquisition
owner: marketing-lead
status: draft
last_updated: 2026-06-16
review_cycle: monthly
artifact_type: rollout-plan
---

# Pre-Call Video Pages Route Rollout

## Rollout objective

Render all 7 pre-call objection pages with one reusable template and one centralized content source while preserving existing slugs.

## Source of truth

- Content model: `pre-call-video-pages-content-model.yaml`
- Legacy copy/transcripts: `pre-call-objection-videos.md`
- Canonical template behavior: `pre-call-video-page-template-spec.md`

## Route mapping

| Slug | Route | Template | Content ID | YouTube ID |
|------|-------|----------|------------|------------|
| `whoweare` | `/reversemortgage/whoweare` | `reverse-objection-video-v1` | `whoweare-why-we-do-what-we-do` | `RYnwas5j7iI` |
| `rmopportunity` | `/reversemortgage/rmopportunity` | `reverse-objection-video-v1` | `rm-opportunity-industry` | `wlGAgHRX_QI` |
| `whatmakesusdifferent` | `/reversemortgage/whatmakesusdifferent` | `reverse-objection-video-v1` | `what-makes-waiz-different` | `uYr9nfeGHHs` |
| `burnt` | `/reversemortgage/burnt` | `reverse-objection-video-v1` | `burnt-by-other-agencies` | `8sqNYp6T3Vg` |
| `leads` | `/reversemortgage/leads` | `reverse-objection-video-v1` | `leads-arent-everything` | `HZf-n-7DDm8` |
| `doweguaranteeresults` | `/reversemortgage/doweguaranteeresults` | `reverse-objection-video-v1` | `do-we-guarantee-results` | `Km5e5lM5mrw` |
| `callcenter` | `/reversemortgage/callcenter` | `reverse-objection-video-v1` | `reverse-sales-team-call-center` | `RgjA7v6K3lk` |

## Recommended implementation flow (inside site codebase)

1. Add one route loader that reads by slug from `pages[]` in content model.
2. If slug not found, return custom 404 with link back to main reverse page.
3. Pass normalized `VideoPageData` into template component.
4. Render related links from `related_slugs`.
5. Bind per-route SEO values from content model.

## Minimal renderer pseudocode

```ts
export async function renderVideoPage(slug: string) {
  const page = videoPages.find((p) => p.slug === slug);
  if (!page) return notFound();
  return <VideoDetailTemplate data={page} />;
}
```

## Copy block contract per route

Each route must render these exact blocks from page data:

- `eyebrow`
- `headline`
- `support_line`
- `sales_letter.problem_framing`
- `sales_letter.reframe`
- `sales_letter.mechanism`
- `sales_letter.expected_outcome`
- `sales_letter.next_step`
- `proof_points[]`
- `cta.*`
- `related_slugs[]`

## Launch sequencing

- Phase 1: Launch `whoweare`, `rmopportunity`, `whatmakesusdifferent` first (core trust/opportunity/differentiation trilogy).
- Phase 2: Launch objection handlers `burnt`, `leads`, `doweguaranteeresults`, `callcenter`.
- Phase 3: Add cross-linking sequence widget and measure path completion.

## Related docs

- [Pre-Call Video Page Template Spec](pre-call-video-page-template-spec.md)
- [Pre-Call Video Pages Content Model](pre-call-video-pages-content-model.yaml)
