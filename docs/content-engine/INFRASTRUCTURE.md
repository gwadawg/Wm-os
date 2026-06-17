---
title: Content Engine — Infrastructure
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-17
review_cycle: quarterly
artifact_type: playbook
---

# Content Engine — Infrastructure

**Purpose:** Define where knowledge lives, how lanes stay separate, and how
future ideas, scripts, and captures get stored — before any production starts.

This doc is the routing authority. Skills (`content-engine`, `knowledge-capture`)
follow it. When in doubt, read [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md) first.

## Current phase

| Phase | Status | What happens |
|-------|--------|--------------|
| **1 — KB build** | **Now** | Fill voice DNA, pillars, beliefs, stories, hooks, angles via grilling + knowledge-capture |
| **2 — Ideation** | Later | `/weekly-ideas` pulls from KB; ideas tagged in `angle-library.md` |
| **3 — Scripting** | Later | `/script` writes dated files to `[lane]/scripts/` |
| **4 — Publish log** | Later | Published metadata → `wm-content-archive/published/` (not OS git) |

Do not skip Phase 1 to script or film. Infrastructure first.

## Three lanes

```
┌─────────────────────────────────────────────────────────────┐
│  PERSONAL (@gabeegoertzen)                                  │
│  Journey, beliefs, lifestyle, AI/ops, controversial takes   │
│  Voice: personal-brand-dna.md                               │
│  KB: personal/                                              │
├─────────────────────────────────────────────────────────────┤
│  BUSINESS (Waiz Media)                                      │
│  B2B agency positioning, LO pain, fulfillment, case proof   │
│  Voice: waiz-media-brand-dna.md + product-marketing.md      │
│  KB: business/ + .agents/product-marketing.md               │
├─────────────────────────────────────────────────────────────┤
│  CLIENT (DSCR, RM, etc.)                                    │
│  Ad creative, UGC, compliance-bound scripts                 │
│  Voice: client DNA pods                                     │
│  KB: docs/client-fulfillment/[slug]-dna/                    │
└─────────────────────────────────────────────────────────────┘
```

**Rule:** One piece = one primary lane. Cross-lane repurposing is explicit —
see [repurposing/reels-to-ads-engine.md](repurposing/reels-to-ads-engine.md).

## Directory map (every file)

```
content-engine/
├── README.md                 Index + skills pointer
├── INFRASTRUCTURE.md         ← you are here (routing authority)
├── LANE-BOUNDARIES.md        Personal vs business vs client rules
├── _templates.md             Script frontmatter templates
│
├── _voice/
│   ├── personal-brand-dna.md     Gabe / @gabeegoertzen voice + audience
│   ├── waiz-media-brand-dna.md   Waiz B2B voice (compiled from product-marketing)
│   └── client-voice-template.md  Per-client voice scaffold
│
├── personal/                 @gabeegoertzen lane KB
│   ├── README.md
│   ├── content-pillars.md
│   ├── beliefs.md            B1, B2, …
│   ├── stories.md            S1, S2, …
│   ├── hook-library.md
│   ├── angle-library.md      Ideas + status (idea → scripted → published)
│   ├── _gaps.md              Unresolved topics; weekly review
│   ├── inspiration/
│   │   ├── competitor-research.md
│   │   └── swipe-file.md
│   └── scripts/              OUTPUT — dated scripts only (Phase 3+)
│       └── README.md
│
├── business/                 Waiz Media lane KB
│   ├── README.md
│   ├── content-pillars.md
│   ├── hook-library.md
│   ├── angle-library.md
│   ├── _gaps.md
│   └── scripts/              OUTPUT — dated scripts only (Phase 3+)
│       └── README.md
│
└── repurposing/              Cross-lane pipelines (explicit only)
    └── reels-to-ads-engine.md
```

## Routing decision tree

When new information arrives, ask in order:

1. **Which lane?** → [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md)
2. **What type?** → table below
3. **Auto or ask?** → [knowledge-capture routing-table](../../../.claude/skills/knowledge-capture/routing-table.md)

| Input type | Personal lane | Business lane |
|------------|---------------|---------------|
| Who Gabe is / journey / beliefs | `beliefs.md`, `stories.md`, `personal-brand-dna.md` | — |
| Personal hook or angle idea | `hook-library.md`, `angle-library.md` | — |
| LO pain / agency positioning | — | `product-marketing.md`, `business/hook-library.md` |
| Waiz proof / case study | — | `product-marketing.md` (ask + verify approved) |
| Finished script (reel/carousel/trial) | `personal/scripts/YYYY-MM-DD-format-slug.md` | `business/scripts/…` |
| Raw transcript / video / diary | `wm-content-archive/transcripts/` → distill into KB | same |
| Full Apify JSON | `wm-content-archive/research/apify/` only | same |
| No clear home yet | `personal/_gaps.md` or `business/_gaps.md` | same |

## File naming

### Knowledge base docs (stable names)

KB files keep fixed names (`beliefs.md`, `stories.md`, etc.). Do not date KB
filenames — date **inside** the file (frontmatter + entry tables).

### Scripts (Phase 3+)

```
[lane]/scripts/YYYY-MM-DD-[format]-[slug].md

Examples:
  personal/scripts/2026-06-20-reel-rio-one-way-ticket.md
  personal/scripts/2026-06-22-carousel-adhd-systems.md
  business/scripts/2026-06-25-reel-lo-qualification-myth.md
```

| Segment | Values |
|---------|--------|
| `YYYY-MM-DD` | Script creation date (ISO) |
| `format` | `reel` \| `carousel` \| `trial-concept` |
| `slug` | kebab-case, 3–6 words, topic-specific |

### Archive (outside git)

```
wm-content-archive/
├── transcripts/YYYY-MM-DD-[type]-[topic].md
├── research/apify/YYYY-MM-DD-[platform]-[niche].json
└── published/YYYY-MM-DD-[platform]-[slug].md
```

Sibling to `Wm-os/`. Never commit raw transcripts or Apify dumps to OS.

## Frontmatter standards

### Knowledge base docs (all `personal/` and `business/` KB files)

```yaml
---
title: [Human title]
domain: content-engine
owner: founder
status: draft | active | archived
last_updated: YYYY-MM-DD      # bump on EVERY edit
review_cycle: weekly | monthly | quarterly
auto_update: true             # if knowledge-capture may append
update_via: knowledge-capture # when auto_update true
update_types: [hooks, beliefs, stories, ...]  # optional
---
```

**Dating rule:** Any agent or human edit to a KB file must update
`last_updated` to today's date in frontmatter.

### In-file entry dating

| Location | Required fields |
|----------|-----------------|
| `hook-library.md` table | `Source`, `Date` columns on every row |
| `angle-library.md` ideas | `Status`; add `Source: …` when from capture |
| `beliefs.md` / `stories.md` | `Entries log` table: ID, Added, Source |
| `_gaps.md` | `Date`, `Source`, `Status` on every row |

### Script files (Phase 3+)

Use templates in [`_templates.md`](_templates.md). Required fields:

```yaml
lane: personal | business | client
format: reel | carousel | trial-concept
date: YYYY-MM-DD
status: concept | scripted | filmed | published
source_idea:   # link to angle-library title or hook
belief_ref:    # optional B1, story_ref S2
```

## Knowledge update workflow

When Gabe shares diary entries, video transcripts, grilling answers, or notes:

```
1. Raw input → wm-content-archive/transcripts/ (optional save)
2. knowledge-capture skill extracts findings
3. Route per routing-table.md → correct lane + doc
4. Append with Source + Date; bump last_updated on target doc
5. Log unresolved items in [lane]/_gaps.md
6. Summarize what changed (no full transcript in OS)
```

| Change type | Action |
|-------------|--------|
| New hook / angle | Auto-append + date |
| New story / belief | Append (grilling or confirmed capture) |
| Voice / positioning shift | Ask Gabe before editing DNA |
| New pillar | Ask or log in `_gaps.md` |
| Script created | New file in `scripts/` + update angle `status: scripted` |

## Personal vs business — quick reference

| | Personal | Business |
|---|----------|----------|
| **Account** | @gabeegoertzen | Waiz Media brand |
| **Audience** | Entrepreneurs, lifestyle, ambitious operators | LOs, brokers, marketing leads |
| **Voice doc** | `personal-brand-dna.md` | `waiz-media-brand-dna.md` |
| **Positioning source** | Grilling + stories/beliefs | `.agents/product-marketing.md` |
| **Stories** | `personal/stories.md` (Gabe's life) | Case studies in product-marketing (approved) |
| **Never mix** | Waiz sales CTAs, client pricing | Gabe's Rio journey, personal hot takes |

Full rules: [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md).

## Agent instructions

Before any content-engine or knowledge-capture task:

1. Read this file + `LANE-BOUNDARIES.md`
2. Detect lane (`personal` \| `business` \| `client:[slug]`)
3. Load that lane's KB in order (see lane README)
4. Write outputs only to paths in this doc
5. Bump `last_updated` on every KB file touched
6. Do not create scripts unless Gabe explicitly requests Phase 3

## Related

- [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md)
- [Personal lane README](personal/README.md)
- [Business lane README](business/README.md)
- [Knowledge capture routing](../../../.claude/skills/knowledge-capture/routing-table.md)
