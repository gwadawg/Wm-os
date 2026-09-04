# Knowledge Capture — Routing Table

Finding → target doc → entry format → auto or ask

**Authority:** [docs/content-engine/INFRASTRUCTURE.md](../../../docs/content-engine/INFRASTRUCTURE.md)
and [LANE-BOUNDARIES.md](../../../docs/content-engine/LANE-BOUNDARIES.md).

**Dating:** Bump `last_updated` on target doc frontmatter. Every new row/entry
includes `Source` + `Date`. For Supabase calls, use `supabase:call:{uuid}` as Source.

## Personal lane

| Finding type | Target doc | Entry format | Mode |
|--------------|------------|--------------|------|
| Hook (spoken) | `personal/hook-library.md` | Table row: Hook, Type, Pillar, Source, Date | auto |
| Content angle | `personal/angle-library.md` | Idea block with tags | auto |
| Belief / philosophy | `personal/beliefs.md` | New B# section | ask |
| Personal story | `personal/stories.md` | New S# section | ask |
| Audience phrase | `_voice/personal-brand-dna.md` § Customer Language | Bullet with quote | ask |
| Voice tone change | `_voice/personal-brand-dna.md` § Brand Voice | Edit | ask |
| New pillar | `personal/content-pillars.md` | New pillar section | ask |
| Swipe / creator ref | `personal/inspiration/swipe-file.md` | Swipe entry with `Production format` | auto |
| Competitor pattern | `personal/inspiration/competitor-research.md` | Pattern log row | auto |
| New production format | `personal/format-library.md` | New format section | ask |
| Carousel layout / size / export rule | `docs/content-engine/carousel-production.md` | Edit SOP quality bar | ask — do not create a second carousel SOP |
| No home for theme | `personal/_gaps.md` | Open gaps row | auto |

## Business lane (Waiz Media)

| Finding type | Target doc | Entry format | Mode |
|--------------|------------|--------------|------|
| LO pain verbatim | `.agents/product-marketing.md` § Customer Language | Bullet | ask |
| Objection + reframe | `.agents/product-marketing.md` § Objections | Table row | ask |
| B2B hook | `business/hook-library.md` | Table row | auto |
| Positioning insight | `.agents/product-marketing.md` | Section edit | ask |
| Case study proof | `.agents/product-marketing.md` § Proof Points | ask + verify approved |
| Content angle | `business/angle-library.md` | Idea block with tags | auto |
| B2B content gap | `business/_gaps.md` | Open gaps row | auto |

## Acquisition / sales (if call is Waiz sales)

| Finding type | Target doc | Mode |
|--------------|------------|------|
| Discovery question pattern | `docs/acquisition/sales/` relevant script doc | ask |
| Objection | `docs/acquisition/sales/wm-reframe-beliefs.md` or objection docs | ask |
| ICP language | `.agents/product-marketing.md` | ask |

## Client fulfillment (if call mentions client product)

| Finding type | Target doc | Mode |
|--------------|------------|------|
| ICP pain (DSCR) | `docs/client-fulfillment/dscr-dna/` angle or ICP docs | ask |
| ICP pain (RM) | `docs/client-fulfillment/reverse-mortgage-dna/` | ask |
| Borrower objection + response | `docs/client-fulfillment/reverse-mortgage-dna/rm-borrower-objections.md` | ask |
| Compliance-sensitive claim | Client compliance guardrails doc | ask — never auto |

## Team / internal calls (`team_internal`)

| Finding type | Target doc | Mode |
|--------------|------------|------|
| Process improvement | Relevant SOP under `docs/operations/` | ask |
| Gabe teaching / framing | `personal/beliefs.md`, `personal/hook-library.md` | ask |
| Internal-only ops note | Stay in Supabase; mark `knowledge_capture_status = skipped` | — |

## Apify / research dumps

Orchestrated by [creator-research](../creator-research/SKILL.md) via `/apify-capture`.
Cite sources as `apify:{platform}:{archive-filename}` (e.g. `apify:instagram:2026-06-18-marcel-stxm.json`).

| Finding type | Target | Mode |
|--------------|--------|------|
| Top hooks (adapted) | `personal/hook-library.md` | auto — never verbatim |
| Angle ideas | `personal/angle-library.md` | auto |
| Remix candidate (score ≥7) | `personal/angle-library.md` | auto — `status: remix-candidate`, `format_ref: swipe-id` |
| Viral format decomposition | `personal/inspiration/swipe-file.md` | auto — full decomposition block |
| Trending audio/visual | `personal/inspiration/swipe-file.md` § Format patterns | auto |
| Creator pattern | `personal/inspiration/competitor-research.md` Pattern log | auto |
| Ad longevity pattern | `personal/inspiration/competitor-research.md` Pattern log | auto — meta_ads only |
| Full JSON | `wm-content-archive/research/apify/` only | user saves externally |

**Do not route competitor Apify findings into owned-winner swipes** — separate pipeline per
[ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md).

## Owned client ads (Mr. Waiz ad_library)

Orchestrated when founder tags `status=winner` or says "capture pending RM ad winners."
Cite sources as `supabase:ad:{uuid}`.

| Finding type | Target doc | Entry format | Mode |
|--------------|------------|--------------|------|
| Full swipe decomposition | `client-fulfillment/media-buying/creative-research/swipes/rm-{date}-{slug}.md` | Swipe template + performance snapshot in frontmatter | auto for tagged winners |
| Script archetype | `creative-research/script-archetypes-catalog.md` | Table row with Source swipe | ask until 3rd repeat |
| Editing style | `creative-research/editing-styles-catalog.md` | Table row with Source swipe | ask until 3rd repeat |
| Loser / fatigue pattern | `creative-research/losers-log.md` | Log row with reason + date | auto |
| RM angle validated by data | `reverse-mortgage-dna/` angle docs | ask | ask |
| DSCR angle | `dscr-dna/intelligence-icp-dscr.md` + `dscr-dna/dscr-campaign-master-angles.md` | ask | ask |
| Compliance-sensitive claim | RM compliance guardrails | — | ask — never auto |
| Unresolved theme | `client-fulfillment/media-buying/_gaps.md` | Gap row | auto |

## Entry formats

### Hook table row

```
| Hook text | curiosity | Pillar 2 | supabase:call:{uuid} | 2026-06-17 |
```

### Angle block

```markdown
### [Working title]
- **Pillar:**
- **Type:** shareable
- **Format:** trial-concept
- **Hook seed:**
- **Status:** idea | remix-candidate
- **Format ref:** swipe-YYYY-MM-DD-01
- **Source:** supabase:call:{uuid} · client_fulfillment/checkin · 2026-06-17
```

Apify-derived angles use `Source: apify:{platform}:{archive-filename} · YYYY-MM-DD`.

### Swipe entry

```markdown
### [@handle — short label]
- **URL / platform:**
- **Production format:** yap | vo-montage | talking-head-broll | concept-edit
- **Content format:** reel | carousel | trial-concept
- **What works:** (hook, structure, visual, pacing)
- **Adapt for pillar:**
- **Status:** saved
- **Source:** founder share · 2026-06-18
```

Also append a pattern log row to `competitor-research.md` when a new creator is shared.

### Gap row

```
| 2026-06-17 | sales call | [theme] | personal/beliefs.md or new pillar | open |
```

## Frontmatter targets with auto_update

Docs with `auto_update: true` in frontmatter expect knowledge-capture append operations:

- `personal/hook-library.md`
- `personal/angle-library.md`
- `personal/beliefs.md` (beliefs = ask despite flag)
- `personal/stories.md`
- `personal/_gaps.md`
- `business/hook-library.md`
- `business/angle-library.md`
- `business/_gaps.md`
- `_voice/personal-brand-dna.md` (language only, ask)

Look for HTML comments: `<!-- knowledge-capture: ... -->` for insertion points.
