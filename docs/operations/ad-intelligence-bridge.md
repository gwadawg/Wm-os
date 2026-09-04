---
title: Ad Intelligence Bridge — Supabase to Wm-os
domain: operations
owner: founder
status: active
last_updated: 2026-08-24
review_cycle: quarterly
artifact_type: playbook
---

# Ad Intelligence Bridge — Supabase → Wm-os

**Purpose:** Define how owned client ad creatives and performance data in the Mr. Waiz Supabase database feed the Wm-os creative-research knowledge base — without storing daily metrics or full script dumps in git.

**One-sentence job:** When an owned ad beats our winner thresholds over a defined window, we capture why in one distilled swipe and promote repeating patterns to catalogs.

**Production loop (umbrella):** [creative-production-loop.md](../client-fulfillment/media-buying/creative-production-loop.md)

**Ad development entry (RM):** [ad-development-workflow.md](../client-fulfillment/media-buying/ad-development-workflow.md)

## System of record

| System | Role | Stores full scripts / time-series? |
|--------|------|-------------------------------------|
| **Supabase — WM Reporting** | Layer 0: `ad_library`, `meta_ad_insights`, funnel `events` | Yes (canonical operational data) |
| **Wm-os (git)** | Layer 2: distilled swipes, script archetypes, editing styles | No — patterns only |
| **Creative studio outputs** | Layer 3: dated **markdown** scripts (not PNG/MP4) | No — per-ad deliverables |
| **wm-content-archive/ads/** | Optional bulky dumps (Poppy, frames) **outside git** — not an agent stills cache | Yes (outside git) |

Supabase project: **WM Reporting** (`fszmndldcvrrmitfbwde`). Same database as the Mr. Waiz dashboard (`call-center-reporting-template`).

## Four-layer model

```
Layer 0 — Supabase ad tables
  ad_library · ad_library_aliases · meta_ad_insights · events (funnel)

Layer 1 — Capture metadata (v1: swipe frontmatter; v2: columns on ad_library)
  performance_snapshot · knowledge_capture_status · os_refs

Layer 2 — Wm-os distilled knowledge (git)
  creative-research/swipes/ · script-archetypes-catalog · editing-styles-catalog · losers-log

Layer 3 — Content outputs
  creative-studio/outputs/ (markdown scripts only) · client ad batches
  Drive stores the file (humans). Mr. Waiz stores what the agent reads (`summary`, tags, type, KPIs).
```

**Rule:** Layer 0 owns raw creative text and metrics. Layers 2+ never store `meta_ad_insights` daily rows or duplicate full `summary` text from `ad_library`.

## Two pipelines (never merge)

| Pipeline | Source | OS destination | Use when |
|----------|--------|----------------|----------|
| **Owned winners** | Mr. Waiz `ad_library` + performance rollups | `creative-research/` swipes + catalogs | Scripting RM/DSCR client ads |
| **Competitor intel** | Apify, Meta Ad Library, Poppy swipes | `creator-research` / distill into `dscr-dna/dscr-gtm-positioning-brief.md` | External format research only |

Do not pull competitor Apify intel when scripting owned RM ads via [rm-creative-studio](../../.claude/skills/rm-creative-studio/SKILL.md).

## Winner definition (KB-eligible)

A row is eligible for knowledge capture when **all** gates pass:

| Gate | Rule |
|------|------|
| Curated | `summary` non-empty (primary capture input from Media Buyer) |
| Classified | `product` + `ad_format` set |
| Linked | `ad_library_aliases` cover all live Facebook `ad_name` variants |
| Performance | Meets founder thresholds over a fixed date window (see below) |
| Human | `status = 'winner'` and founder queues capture (v1: "capture pending RM winners" in Cursor) |

### Suggested performance thresholds (founder-tunable)

| Metric | Suggested gate |
|--------|----------------|
| Min spend | ≥ $500 in window (enough signal) |
| Qualified rate | ≥ 50% of leads |
| CPQL | Below portfolio median or top quartile for product |
| Funnel | At least 1 appointment booked attributed to ad (via events) |

### Performance snapshot at capture

Store in swipe frontmatter (v1) or `ad_library` metadata (v2):

```json
{
  "window": "2026-03-01..2026-05-31",
  "spend": 4200,
  "leads": 84,
  "qualified": 48,
  "qualified_rate": 0.57,
  "appointments": 22,
  "shows": 14,
  "cpl": 50,
  "cpql": 87.5,
  "client_count": 3
}
```

**Full funnel join:** Snapshot spend **and** leads → qualified → appointments → shows. CPL alone is insufficient for scriptwriters.

## Alias hygiene checklist

Before capture:

1. Confirm primary `ad_name` in `ad_library` is the canonical creative name.
2. Add every live Facebook variant to `ad_library_aliases`.
3. Verify Media Buyer rollup groups variants under one library row.
4. Scrub client names from OS entries (`client_count` only, not client names).

`ad_library` has no `client_id` by design — patterns are cross-client. Scrub PII before distilling.

## Creating new ads in Mr. Waiz (before they're winners)

Log every new creative at launch so performance rolls up to one row.

| Product | Creation SOP | When to log |
|---------|--------------|-------------|
| **RM** (video/static) | [ad-development-workflow.md](../client-fulfillment/media-buying/ad-development-workflow.md) | Before or right after Meta upload |
| **DSCR** (Ideogram static) | [dscr-static-image-generator-project.md](../client-fulfillment/dscr-dna/dscr-static-image-generator-project.md) | After export; ask agent: `Label this ad for Mr. Waiz` |

**Minimum fields at launch:** `ad_name`, `summary`, `visual_notes`, `product`, `ad_format`, `drive_url`, `status=testing`.

**Field guide:**

| Field | Use |
|-------|-----|
| **ad_name** | Short slug — same string in Meta Ads Manager. Canonical rules: [ad-naming-convention.md](../client-fulfillment/media-buying/ad-naming-convention.md) + [ad-name-library.yaml](../client-fulfillment/media-buying/ad-name-library.yaml). Default: `{product}_{concept}_{fmt}_v{#}[letter]`. DSCR rate-card exception: `dscr_[visual]_[spec1]_[spec2]_[spec3]` |
| **summary** | Strategy: funnel stage, audience, hypothesis, named pattern. Primary input for knowledge capture. |
| **visual_notes** | Layout, colors, verbatim on-image copy. |
| **Description / overview (UI)** | One easy sentence — use the `overview` line from the DSCR static generator registration block; paste into summary too if Mr. Waiz has a single description field. |

## Source citation (required in every OS entry)

```text
supabase:ad:{uuid}
```

Swipe frontmatter example:

```yaml
source: own-account
supabase_ref: supabase:ad:a1b2c3d4-e5f6-7890-abcd-ef1234567890
os_refs:
  - creative-research/swipes/rm-2026-06-legacy-planner-burden.md
```

## Routing by finding

| Finding | Destination | Mode |
|---------|-------------|------|
| Full swipe decomposition | `creative-research/swipes/rm-{date}-{slug}.md` | auto for tagged winners |
| Script archetype | `script-archetypes-catalog.md` | ask until 3rd repeat |
| Editing style | `editing-styles-catalog.md` | ask until 3rd repeat |
| Loser / fatigue pattern | `creative-research/losers-log.md` | auto |
| RM angle validated by data | `reverse-mortgage-dna/` | ask |
| DSCR angle | `dscr-dna/dscr-campaign-master-angles.md` (expand) / `dscr-dna/intelligence-icp-dscr.md` (AI) | ask |
| Compliance-sensitive claim | RM compliance guardrails | ask — never auto |

Full matrix: [knowledge-capture routing-table](../../.claude/skills/knowledge-capture/routing-table.md).

## Processing workflow (founder v1)

```
1. Media Buyer curates ad_library row (summary, visual_notes, drive_url)
2. Founder marks status=winner when performance gates pass
3. Founder runs knowledge-capture: "process pending RM ad winners"
4. Agent reads summary + visual_notes; snapshots performance from Mr. Waiz rollup
5. Agent produces swipe(s); promotes to catalog only on repeat or explicit approval
6. Agent logs os_refs in swipe frontmatter
7. v2: update knowledge_capture_status on ad_library
```

### Founder cadence

| Frequency | Action |
|-----------|--------|
| Weekly (15 min) | Tag 1–2 new RM winners in Mr. Waiz; fill summary |
| Weekly (30 min) | Run knowledge-capture on pending winners |
| On new ad request | rm-creative-studio Step 0 pulls catalogs + swipes first |

## How agents pull ads (maturity levels)

| Level | Trigger | Method |
|-------|---------|--------|
| **1 — Manual** | "Capture ad `{uuid}`" or named winner | Supabase MCP `execute_sql` on `ad_library` |
| **2 — Semi-auto** | Filter winners by product | `GET /api/ad-library?status=winner&product=reverse` (v2) |
| **3 — Agent-native** | rm-creative-studio Step 0 | Read catalogs + query Supabase by format/archetype (v2 manifest) |

### Supabase MCP queries

Single ad:

```sql
select al.*, coalesce(json_agg(ala.alias_name) filter (where ala.id is not null), '[]') as aliases
from ad_library al
left join ad_library_aliases ala on ala.library_id = al.id
where al.id = '{uuid}'
group by al.id;
```

RM winners pending capture (v2):

```sql
select id, ad_name, product, ad_format, status, summary, visual_notes, knowledge_capture_status
from ad_library
where product = 'reverse' and status = 'winner'
  and coalesce(knowledge_capture_status, 'none') in ('none', 'pending')
order by updated_at desc;
```

## What never syncs to git

- `meta_ad_insights` daily rows
- Full `summary` duplicated outside swipe decomposition
- Video/mp4/PNG files (humans keep them on Drive; agent reads `summary` / tags / KPIs in Mr. Waiz, not `drive_url`)
- Client names from cross-client winners
- Competitor Apify dumps mixed into owned-winner swipes

## What stays separate

| System | Why separate |
|--------|--------------|
| [creator-research manifest](../content-engine/research/creator-research-manifest.yaml) | Competitor / viral format research |
| [call-intelligence-bridge.md](call-intelligence-bridge.md) | Call transcripts — different extraction schema |
| Creative studio `outputs/` | Per-ad deliverables, not reusable patterns |

## Related

- [Ad development workflow](../client-fulfillment/media-buying/ad-development-workflow.md)
- [Creative research README](../client-fulfillment/media-buying/creative-research/README.md)
- [Knowledge capture skill](../../.claude/skills/knowledge-capture/SKILL.md)
- [rm-creative-studio skill](../../.claude/skills/rm-creative-studio/SKILL.md)
