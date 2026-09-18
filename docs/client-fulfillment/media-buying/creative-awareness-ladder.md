---
title: Creative Awareness Ladder (Scale Campaign Coverage Map)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-09-18
review_cycle: monthly
artifact_type: reference
---

# Creative Awareness Ladder

Coverage map for the Scale campaign. Every ad in a Scale ad set occupies one
**rung** for one **persona**. An empty cell is not a neutral gap — it is the
standing creative brief, and it is what the next wave's concept slate is drawn
from.

**Used by:** [creative-testing-structure.md](creative-testing-structure.md)
(structure) · [performance-learnings.md](performance-learnings.md) (wave log) ·
[rm-creative-studio](../../../.claude/skills/rm-creative-studio/SKILL.md)
(Step 0 brief intake)

## The four rungs

Mapped onto the vocabulary already in
[frameworks-reference.md](creative-studio/frameworks-reference.md) so we do not
invent a fifth taxonomy.

| Rung | Schwartz awareness | House stage | Job of the ad | Product name allowed? |
|------|--------------------|-------------|---------------|----------------------|
| **Problem** | Unaware / Problem-aware | TOF | Name the invisible pain; break the pattern | Never |
| **Solution** | Solution-aware | MOF | Differentiate the mechanism; bust the myth | In context only |
| **Proof** | Product-aware | MOF/BOF | Show it working for someone like me | Yes, in context |
| **Offer** | Most-aware | BOF | Reduce risk; convert the hand-raise | Yes, directly |

Why the ladder is worth the discipline: Meta sequences a prospect down these
rungs as engagement signals accrue, so a Problem-rung ad that rarely converts
directly is still doing paid work by feeding the rungs below it. Judge a Scale
ad set blended, never rung by rung.

## RM coverage grid

Personas per [rm-archetypes-canonical.md](creative-studio/rm-archetypes-canonical.md)
(**active 3** — Widowed · Married Couple · Pre-Retiree). Concept slugs per
[ad-name-library.yaml](ad-name-library.yaml).

| Rung | Widowed Homeowner | Married Couple | Pre-Retiree |
|------|-------------------|----------------|-------------|
| **Problem** | `equity-trap`, `grandkids-visit` | `equity-trap`, `inflation-hedge`, `legacy-planner` | `inflation-hedge` |
| **Solution** | `myth-scary` | `strategic-options`, `keep-rate` (HomeSafe Second only) | `strategic-options` |
| **Proof** | `named-proof` | `named-proof`, `comment-reply` | — **gap** |
| **Offer** | — **gap** | — **gap** | — **gap** |

**Veteran column removed (2026-09).** Persona deprecated — never used in live
creative. Do not treat empty Veteran cells as briefs to fill.

`breaking-news` is persona-agnostic and sits across the Problem/Solution
boundary; treat it as a Problem-rung slot for whichever persona the headline
names. It is compliance-sensitive — verify lender rules before shipping.

### What the grid says

Two findings, in order of how much they cost us.

1. **The Offer rung is empty for every persona.** We have no registered
   direct-response concept at all. The month-1 SOP's own creative direction
   table lists BOF angles ("Get a free rate quote in 60 seconds",
   "We closed in 21 days") but none of them were ever registered as concept
   slugs, so nothing in the library can fill the rung. Every Scale ad set is
   currently a three-rung ladder at best, which means the account depends on
   the landing page to do all the closing work.
2. **Proof is thin and format-locked.** `named-proof` and `comment-reply` are
   the only Proof-rung concepts, both carry a dramatization disclosure
   requirement, and neither serves Pre-Retiree well yet.

## Standing brief backlog

Drawn straight from the empty cells, ordered by leverage. These are
**proposals, not registered slugs** — register in
[ad-name-library.yaml](ad-name-library.yaml) per its registration checklist
when the first ad in the family is actually built, not before.

| Priority | Proposed slug | Rung | Persona | Angle direction |
|----------|---------------|------|---------|-----------------|
| 1 | `estimate-request` | Offer | Any | "See what your home could unlock — no obligation, no credit pull" |
| 2 | `closing-timeline` | Proof | Any | Concrete timeline proof — how long it actually took, start to funded |
| 3 | `title-stays-yours` | Solution | Widowed | Myth-bust: you keep the title and the deed |
| 4 | `heirs-equity` | Solution | Married Couple · **trigger: heirs** | Myth-bust: heirs receive the remaining equity |
| 5 | `advisor-blindspot` | Solution | Pre-Retiree · Strategic Retiree tone | "Most advisors never bring this up" — strategic framing |
| 6 | `roof-repair` | Problem | Widowed, Married Couple | The specific deferred repair, not abstract "expenses" |
| 7 | `medical-reserve` | Problem | Any | One large medical bill away from real trouble |

**Removed from backlog:** `veteran-earned`, `veteran-independence` — Veteran
persona deprecated.

Slug rules, restated from the library: lowercase kebab, 2–4 tokens, noun-led,
no funnel stage in the slug, no format in the slug.

## Compliance constraints that shape the grid

These are hard gates, not preferences. Full checklist in
[compliance-gate-checklist.md](creative-studio/compliance-gate-checklist.md).

- **No age in copy.** "Retired homeowners", never "seniors over 62". Age is an
  eligibility and targeting fact, never ad copy.
- **No product name at the Problem rung.** "Reverse mortgage" never opens a TOF
  ad; use "home equity program".
- **No tax advice.** This is why the otherwise-written "Tax-Free Cash" angle
  cannot ship and does not appear in this grid.
- **`keep-rate` is product-gated.** HomeSafe Second clients only — never on a
  HECM-only client.
- **All testimonials are composites** and require the dramatization
  disclosure. That applies to both Proof-rung formats we have.
- **Special Ad Category (Housing)** protected-class rules apply to every rung.

## Format spread is part of coverage

A ladder whose four rungs are all statics still risks Entity-ID collapse,
because format is one of the dimensions Andromeda clusters on. Aim for at least
two formats across the filled rungs, and prefer that adjacent rungs differ.
Format codes per [ad-name-library.yaml](ad-name-library.yaml): `st`, `ugc`,
`t1`, `t2`, `edu`.

A reasonable default spread: Problem as `t2` or `ugc`, Solution as `st` or
`edu`, Proof as `t1`, Offer as `st`.

## DSCR coverage

One constraint bucket = one cold ad set. Buckets per
[dscr-creative-taxonomy.md](../dscr-dna/dscr-creative-taxonomy.md).
Day-1 structure: [dscr-campaign-launch-sop.md](dscr-campaign-launch-sop.md).

| Rung | DENIED | DEADLINE | IDLE |
|------|--------|----------|------|
| **Problem** | `nodocs-speed` | `balloon-exit` | `cashout-grow` (belief) |
| **Solution** | `nodocs-speed` | `balloon-exit` | `cashout-grow` |
| **Proof** | — **gap** | — **gap** | — **gap** |
| **Offer** | warm_convert (checklist) | warm_convert | warm_convert + outcome |

Proof rung empty across buckets; no DSCR swipes yet ([_gaps.md](_gaps.md)).
Checklist / authority live in **warm_convert**, not cold. Do not import RM
benchmarks or RM tone into DSCR.

## Related

- [dscr-campaign-launch-sop.md](dscr-campaign-launch-sop.md) — day-1 Meta structure
- [creative-testing-structure.md](creative-testing-structure.md) — where the ladder is used
- [creative-testing-scorecard.md](creative-testing-scorecard.md) — how rungs are judged
- [ad-copy-angle-library-rm.md](ad-copy-angle-library-rm.md) — written copy per angle
- [rm-ad-ideation-matrix.md](creative-studio/rm-ad-ideation-matrix.md) — concept generation
- [losers-log.md](creative-research/losers-log.md) — retired patterns
