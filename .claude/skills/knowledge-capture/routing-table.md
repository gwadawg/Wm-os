# Knowledge Capture — Routing Table

Finding → target doc → entry format → auto or ask

**Authority:** [docs/content-engine/INFRASTRUCTURE.md](../../../docs/content-engine/INFRASTRUCTURE.md)
and [LANE-BOUNDARIES.md](../../../docs/content-engine/LANE-BOUNDARIES.md).

**Dating:** Bump `last_updated` on target doc frontmatter. Every new row/entry
includes `Source` + `Date`.

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
| Swipe / format | `personal/inspiration/swipe-file.md` | Swipe entry | auto |
| Competitor pattern | `personal/inspiration/competitor-research.md` | Pattern log row | auto |
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
| Compliance-sensitive claim | Client compliance guardrails doc | ask — never auto |

## Apify / research dumps

| Finding type | Target | Mode |
|--------------|--------|------|
| Top hooks (adapted) | `personal/hook-library.md` | auto — mark source Apify |
| Angle ideas | `personal/angle-library.md` | auto |
| Creator pattern | `personal/inspiration/competitor-research.md` | auto |
| Full JSON | `wm-content-archive/research/apify/` only | user saves externally |

## Entry formats

### Hook table row

```
| Hook text | curiosity | Pillar 2 | sales call 2026-06-17 | 2026-06-17 |
```

### Angle block

```markdown
### [Working title]
- **Pillar:**
- **Type:** shareable
- **Format:** trial-concept
- **Hook seed:**
- **Status:** idea
- **Source:** transcript 2026-06-17
```

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
