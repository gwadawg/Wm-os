---
title: Content Engine — Infrastructure
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-24
review_cycle: quarterly
artifact_type: playbook
---

# Content Engine — Infrastructure

**Purpose:** Define where knowledge lives, how lanes stay separate, and how
future ideas, scripts, and captures get stored — before any production starts.

This doc is the routing authority. Skills (`content-engine`, `creator-research`,
`knowledge-capture`) follow it. When in doubt, read [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md) first.

## Current phase

| Phase | Status | What happens |
|-------|--------|--------------|
| **1 — KB build** | **Now** | Fill voice DNA, pillars, beliefs, stories, hooks, angles via grilling + knowledge-capture |
| **2 — Ideation** | Later | `/weekly-ideas` pulls from KB; ideas tagged in `angle-library.md` |
| **3 — Scripting** | Later | `/script` writes dated files to `[lane]/scripts/` |
| **4 — Production handoff** | Later | `/push-clickup` / `/push-clip` → ClickUp — [clickup-personal-brand-pipeline.md](clickup-personal-brand-pipeline.md) |
| **5 — Publish log** | Later | Published metadata → `wm-content-archive/published/` (not OS git) |

Repurpose call projects: `personal/projects/` — structure only; lifecycle in
[personal/projects/lifecycle.md](personal/projects/lifecycle.md).

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
├── research/
│   └── creator-research-manifest.yaml  Apify actors, watchlist, archive naming
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
│   ├── angle-library.md      Ideas + status (idea → remix-candidate → selected → scripted → published)
│   ├── format-library.md     Production formats (yap, VO montage, etc.)
│   ├── _gaps.md              Unresolved topics; weekly review
│   ├── projects/             Repurpose projects — PROJECT.md + clip briefs
│   │   ├── README.md         Active / completed index (max 2 active)
│   │   └── lifecycle.md      Storage layers, WIP limits, archive rules
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
| Call → clip repurpose project | `personal/projects/[slug]/` — [lifecycle](personal/projects/lifecycle.md) | — |
| Raw transcript / video / diary | `wm-content-archive/transcripts/` → distill into KB | same |
| Full Apify JSON | `wm-content-archive/research/apify/` only | same |
| Apify distilled (hooks, swipes, remix) | `creator-research` `/apify-capture` → inspiration + angle-library | same |
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

**Repurpose projects** (`personal/projects/`) stay in git — small distilled
briefs only. Demote via index when complete; see
[personal/projects/lifecycle.md](personal/projects/lifecycle.md).

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
| `angle-library.md` ideas | `Status` (`idea`, `remix-candidate`, `selected`, `scripted`, `published`); `Source`, `format_ref` when from Apify |
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

## Layer 0 — Supabase call store

Sales, client, and team call transcripts live in the **WM Reporting** Supabase
project (Mr. Waiz dashboard). Wm-os never stores full transcripts in git.

| Layer | System | Contents |
|-------|--------|----------|
| 0 | `acquisition_calls`, `client_calls`, `team_calls` | Full transcript + metadata |
| 1 | `call_intelligence` overlay | Extraction JSON, lanes, capture status |
| 2 | Wm-os `docs/content-engine/` | Distilled hooks, angles, beliefs |
| 2b | Wm-os `personal/projects/` | Clip structure for active repurpose work — [lifecycle](personal/projects/lifecycle.md) |
| 3 | `[lane]/scripts/` | Dated content outputs |

Bridge spec: [call-intelligence-bridge.md](../operations/call-intelligence-bridge.md)

Operational mirror: Mr. Waiz `docs/CALL-INTELLIGENCE.md` in the dashboard repo.

**Source citation for call-derived entries:** `supabase:call:{uuid}`

**Source citation for Apify-derived entries:** `apify:{platform}:{archive-filename}`

## Knowledge update workflow

When Gabe shares diary entries, video transcripts, grilling answers, notes, or
points to a Supabase call:

```
1. Raw input → Supabase call store OR wm-content-archive/transcripts/ (optional)
2. knowledge-capture skill extracts findings (read extraction JSON first)
3. Route per routing-table.md → correct lane + doc
4. Append with Source + Date; bump last_updated on target doc
5. Log unresolved items in [lane]/_gaps.md
6. Summarize what changed (no full transcript in OS)
7. Mark call knowledge_capture_status = processed in Supabase; record os_refs
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

- [ClickUp personal brand pipeline](clickup-personal-brand-pipeline.md)
- [Creator research manifest](research/creator-research-manifest.yaml)
- [Call intelligence bridge](../operations/call-intelligence-bridge.md)
- [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md)
- [Personal lane README](personal/README.md)
- [Business lane README](business/README.md)
- [Knowledge capture routing](../../../.claude/skills/knowledge-capture/routing-table.md)
