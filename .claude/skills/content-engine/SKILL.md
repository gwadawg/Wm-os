---
name: content-engine
description: Runs weekly content ideation and scripting for personal brand, Waiz Media business, and client lanes. Generates reel, carousel, and trial-concept ideas with searchable/shareable tags and 40/30/20/10 scoring. Use when the user asks for content ideas, weekly batch, scripts, carousels, trial reels, or content-engine workflows.
disable-model-invocation: true
---

# Content Engine

Orchestrates ideation → selection → scripting for `docs/content-engine/`.

## Before any task

1. Read [docs/content-engine/INFRASTRUCTURE.md](../../docs/content-engine/INFRASTRUCTURE.md)
2. Read [docs/content-engine/LANE-BOUNDARIES.md](../../docs/content-engine/LANE-BOUNDARIES.md)
3. Read [docs/content-engine/README.md](../../docs/content-engine/README.md)
4. **Detect lane** (see below)
5. Load voice + KB for that lane
6. For business lane, also read [`.agents/product-marketing.md`](../../.agents/product-marketing.md) if present

**Phase check:** Default phase is KB build (Phase 1). Do not run `/weekly-ideas`
or `/script` unless Gabe explicitly requests ideation or scripting.

## Lane detection

| Signal | Lane |
|--------|------|
| User says `personal` | personal |
| User says `business` or Waiz Media | business |
| User says `client:dscr` / `client:rm` or client DNA doc open | client → load `docs/client-fulfillment/[slug]-dna/` |
| Travel, beliefs, journey, lifestyle | personal |
| LO/agency B2B positioning | business |

If ambiguous, ask: **"Personal, business, or client (which product)?"**

### Load by lane

**Personal:** `_voice/personal-brand-dna.md` → `personal/content-pillars.md` → `beliefs.md` → `stories.md` → `hook-library.md` → `angle-library.md` → optional `inspiration/`

**Business:** `.agents/product-marketing.md` → `_voice/waiz-media-brand-dna.md` → `business/content-pillars.md` → `business/hook-library.md`

**Client:** Client DNA README + compliance + angle library; use `rm-creative-studio` or client playbooks for ad scripts

## Commands

### `/weekly-ideas [lane] [count]`

Default: lane from context, count = 15–20.

**Steps:**
1. Research pulse — skim `personal/inspiration/competitor-research.md` (and new Apify archive if user mentions it)
2. Pull ideas from pillars, beliefs, stories, hooks, angles, swipes
3. Mix formats: ~60% reel, ~25% trial-concept, ~15% carousel (adjust if user specifies)
4. Tag each idea:
   - **discoverability:** searchable | shareable | both
   - **format:** reel | carousel | trial-concept
   - **pillar**
   - **buyer stage** (if B2B): awareness | consideration | decision | implementation
5. **Score** each idea (1–10 weighted):

| Factor | Weight |
|--------|--------|
| Customer / audience impact | 40% |
| Content-market fit | 30% |
| Search / discovery potential | 20% |
| Resource cost to film | 10% |

6. Output table sorted by total score; mark top 5 as `recommended`

**Output format:**

```markdown
## Weekly ideas — [lane] — [date]

| # | Title | Format | Pillar | Type | Score | Status |
|---|-------|--------|--------|------|-------|--------|
| 1 | ... | reel | ... | shareable | 8.2 | recommended |

### Detail (top 5)
#### 1. [Title]
- Hook seed:
- Why now:
- Trial vs full prod:
```

Offer to append selected ideas to `angle-library.md`.

Full SOP: [weekly-workflow.md](weekly-workflow.md)

### `/script [idea title or #]`

1. Confirm lane + format
2. Load voice DNA + relevant belief/story if linked
3. Apply template from [format-templates.md](format-templates.md)
4. For **reel** / UGC: also follow [ugc-scriptwriter](../ugc-scriptwriter/SKILL.md)
5. For **carousel**: also follow [copywriting](../copywriting/SKILL.md)
6. Save to `[lane]/scripts/YYYY-MM-DD-format-slug.md`
7. Set frontmatter `status: scripted`

Include **editor_notes** (cuts, b-roll, text overlays) — user films, editor cuts.

### `/select-ideas`

User marks ideas: `film-this-week` | `save-for-later` | `archive`. Update `angle-library.md` statuses.

## Format selection guide

| Format | Use when |
|--------|----------|
| **trial-concept** | Test hook/angle fast; low edit cost; validate before full script |
| **reel** | Story, belief, or tactical piece with clear spoken arc |
| **carousel** | List, framework, myth-bust, searchable topic |

Templates: [format-templates.md](format-templates.md)

## Quality bar

- Hooks in first 1–2 seconds of spoken content
- One clear idea per piece (especially trials)
- Personal lane: sound like personal-brand-dna, not Waiz sales copy
- Business lane: no unapproved pricing or guaranteed outcomes
- Client lane: compliance doc loaded before script finalizes

## Related skills

- [knowledge-capture](../knowledge-capture/SKILL.md) — feed transcripts into KB
- [brainstorming](../brainstorming/SKILL.md) — optional deep ideation
- [marketing-psychology](../marketing-psychology/SKILL.md) — angle sharpening
- [rm-creative-studio](../rm-creative-studio/SKILL.md) — client RM ads

## OS paths

- Index: `docs/content-engine/README.md`
- Templates (duplicate): `docs/content-engine/_templates.md`
- Repurpose: `docs/content-engine/repurposing/reels-to-ads-engine.md`
