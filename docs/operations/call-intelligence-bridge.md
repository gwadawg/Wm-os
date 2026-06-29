---
title: Call Intelligence Bridge — Supabase to Wm-os
domain: operations
owner: founder
status: active
last_updated: 2026-06-17
review_cycle: quarterly
artifact_type: playbook
---

# Call Intelligence Bridge — Supabase → Wm-os

**Purpose:** Define how call transcripts and structured extractions in the Mr. Waiz Supabase database feed the Wm-os content engine and acquisition intelligence — without storing full transcripts in git.

**Operational mirror (dashboard repo):** [CALL-INTELLIGENCE.md](https://github.com/waizmedia/call-center-reporting-template/blob/main/docs/CALL-INTELLIGENCE.md) in the Mr. Waiz reporting app.

## System of record

| System | Role | Stores full transcripts? |
|--------|------|--------------------------|
| **Supabase — WM Reporting** | Layer 0/1: all calls, metadata, extractions | Yes (canonical) |
| **Wm-os (git)** | Layer 2: distilled hooks, angles, beliefs, SOP updates | No |
| **Content engine scripts** | Layer 3: dated script outputs | No |
| **wm-content-archive/** | Optional mirror for non-DB raw material (video, Apify) | Yes (outside git) |
| **WM Sales Call Tracker (sheet)** | Funnel KPIs only | No |

Supabase project: **WM Reporting** (`fszmndldcvrrmitfbwde`). Same database as the Mr. Waiz dashboard (`call-center-reporting-template`).

## Four-layer model

```
Layer 0 — Supabase call tables
  acquisition_calls · client_calls · team_calls
  Full transcript + recording + call metadata

Layer 1 — Structured intelligence (call_intelligence overlay)
  extraction JSON · content_eligible · lanes · knowledge_capture_status · os_refs

Layer 2 — Wm-os distilled knowledge (git)
  hook-library · angle-library · product-marketing · acquisition/sales · client DNA

Layer 3 — Content outputs
  content-engine/[lane]/scripts/ · publish log (wm-content-archive/published/)
```

**Rule:** Layer 0 owns raw text. Layers 2+ never store full transcripts in git.

## Call tables and categories

| `call_category` | Source table | `call_subtype` examples | Primary OS destinations |
|-----------------|-------------|-------------------------|-------------------------|
| `sales_acquisition` | `acquisition_calls` | intro, demo, followup, dial, bamfam | `business/`, `.agents/product-marketing.md`, `docs/acquisition/sales/` |
| `client_fulfillment` | `client_calls` | onboarding, launch, checkin, churn | `docs/client-fulfillment/[slug]-dna/` |
| `team_internal` | `team_calls` | leadership, ops, training, standup | `docs/operations/` — content only when Gabe is teaching |
| `personal_content` | any table + `lanes` tag | podcast, interview | `personal/` KB |

**Split distill:** One call may feed multiple lanes. LO pain → business KB; Gabe operator story → personal KB. See [LANE-BOUNDARIES.md](../content-engine/LANE-BOUNDARIES.md).

## Intelligence field contract

Stored in `call_intelligence` overlay (`call_domain` + `call_id`) or inline on call rows:

| Field | Purpose |
|-------|---------|
| `transcript` | Full text on source table (`client_calls`, `team_calls`; `acquisition_calls.transcript` for sales) |
| `transcript_summary` | Short context for agents without loading full text |
| `extraction` | JSON aligned with [sales-calls-demo-analysis.md](../acquisition/sales/sales-calls-demo-analysis.md) |
| `content_eligible` | Skip admin/technical calls (default `true`) |
| `lanes` | e.g. `["business","acquisition"]`, `["personal"]`, `["client:dscr"]` |
| `sensitivity` | `public` \| `internal` \| `client_confidential` |
| `knowledge_capture_status` | `pending` \| `processed` \| `needs_review` \| `skipped` |
| `knowledge_capture_at` | Last OS sync timestamp |
| `os_refs` | Docs touched, e.g. `["business/hook-library.md"]` |

### Extraction JSON shape

```json
{
  "pain_points_verbatim": [],
  "objections": [{ "text": "", "category": "Price/ROI", "outcome": "partial" }],
  "hooks_natural": [],
  "stories": [{ "summary": "", "speaker": "gabe" }],
  "language_patterns": [],
  "competitor_mentions": [],
  "buying_signals": [],
  "content_angles": [{ "title": "", "lane": "business", "format": "reel" }],
  "ops_insights": [{ "topic": "", "suggested_doc": "acquisition/sales/..." }]
}
```

Agents read **extraction first**; load full transcript only when extraction is missing or insufficient.

## Source citation (required in every OS entry)

```text
supabase:call:{uuid}
```

Full hook row example:

```markdown
| Lead systems work you to death | callout | LO pain | supabase:call:a1b2c3d4-… | 2026-06-17 |
```

Include category in angle blocks:

```markdown
- **Source:** supabase:call:{uuid} · client_fulfillment/checkin · 2026-06-17
```

## Routing by extraction finding

| Finding | Destination | Mode |
|---------|-------------|------|
| LO pain verbatim | `.agents/product-marketing.md` § Customer Language | ask |
| B2B hook | `business/hook-library.md` | auto |
| Content angle | `business/angle-library.md` | auto |
| Objection + reframe | `docs/acquisition/sales/` objection docs | ask |
| Discovery pattern | `docs/acquisition/sales/` relevant script doc | ask |
| Gabe operator story | `personal/stories.md` | ask (split distill) |
| Client ICP pain | `docs/client-fulfillment/[slug]-dna/` | ask |
| Process improvement | `docs/operations/` relevant SOP | ask |
| Team teaching / framing | `personal/beliefs.md`, `personal/hook-library.md` | ask |
| Unresolved theme | `[lane]/_gaps.md` | auto |

Full matrix: [knowledge-capture routing-table](../../.claude/skills/knowledge-capture/routing-table.md).

## Processing workflow

```
1. Call ends → transcript stored in Supabase (source table)
2. Optional: AI extraction → call_intelligence.extraction (reuse demo-analysis prompt)
3. Agent or batch queries pending content-eligible calls
4. knowledge-capture reads extraction (+ transcript if needed)
5. Route findings per routing table; write distilled entries to Wm-os
6. Update call_intelligence: status = processed, os_refs = [...], knowledge_capture_at = now()
```

Weekly batch query:

```sql
select call_id, call_category, call_subtype, called_at, transcript_summary
from v_all_calls
where knowledge_capture_status = 'pending'
  and content_eligible = true
order by called_at desc
limit 20;
```

## Keep the OS clean (operating rhythm)

Wm-os is a **compiled index**, not a warehouse. Follow these rules so the KB gets
powerful without getting noisy.

### What belongs in Wm-os

- One-line hooks with `supabase:call:{uuid}` source + date
- Angle blocks with status (`idea` → `scripted`)
- Beliefs/stories **after confirmation**
- Objection/reframe pairs **after review**
- Client DNA updates **scrubbed** (no names/metrics without approval)
- `_gaps.md` rows for unresolved themes

### What never belongs in Wm-os

- Full call transcripts
- Raw Apify JSON or council session dumps
- Unapproved pricing, metrics, or case study claims
- Duplicate content already in canonical manifests

### Weekly capture cap

Process **3–5 calls max** per week, prioritized:

1. Sales / acquisition calls with transcripts
2. Team calls where Gabe is teaching
3. Client check-ins **only** when something content-worthy happened

Mark ops-only client check-ins `knowledge_capture_status = skipped` after review.

### Auto-sync on transcript save

When you paste a transcript into Supabase (dashboard or direct):

1. DB trigger upserts `call_intelligence` → `pending` if transcript exists
2. Calls **without** transcripts show as `skipped` (not in pending queue)
3. Re-saving a processed call does **not** reset status to pending

Migration: `sync_call_intelligence_triggers.sql` in the dashboard repo.

## How agents pull calls (three maturity levels)

| Level | Trigger | Method |
|-------|---------|--------|
| **1 — Manual** | "Capture call `{uuid}`" | Supabase MCP `execute_sql` or paste extraction in chat |
| **2 — Semi-auto** | Weekly pending batch | `/api/calls/intelligence?status=pending` on Mr. Waiz dashboard |
| **3 — Agent-native** | Supabase MCP in Cursor | Query `v_all_calls` directly |

### Supabase MCP queries

By call ID:

```sql
select * from v_all_calls where call_id = '{uuid}';
```

Pending content calls since date:

```sql
select call_id, call_category, call_subtype, called_at, transcript_summary, extraction, lanes
from v_all_calls
where coalesce(knowledge_capture_status, 'pending') = 'pending'
  and coalesce(content_eligible, true) = true
  and called_at >= '2026-06-01'
order by called_at desc
limit 20;
```

With full transcript (knowledge-capture run):

```sql
select call_id, call_category, call_subtype, called_at, transcript, extraction, lanes, sensitivity
from v_all_calls
where call_id = '{uuid}';
```

### HTTP API (Mr. Waiz dashboard)

`GET /api/calls/intelligence` — owner/admin only.

| Param | Purpose |
|-------|---------|
| `id` | Single call by UUID |
| `status` | Filter by `knowledge_capture_status` |
| `category` | Filter by `call_category` |
| `since` | ISO date — calls on or after |
| `include_transcript` | `true` to return full transcript text |
| `all` | `true` to include non-content-eligible calls (default filters them out) |

## Sensitivity rules

| `sensitivity` | Rule |
|---------------|------|
| `client_confidential` | Default for client check-ins. Distill ICP pain into client DNA; no client names or unapproved metrics in business content without scrubbing. |
| `internal` | Default for team calls. Usually `content_eligible = false` unless Gabe said something worth a reel. |
| `public` | Safe for business content angles after review. |

Never auto-edit pricing, compliance claims, or case study proof without explicit approval.

## What never syncs to git

- Full call transcripts
- Raw recording files
- Unredacted client PII from check-in calls
- Duplicate content already in canonical manifests (e.g. [pre-call objection videos](../acquisition/marketing/pre-call-objection-videos-manifest.yaml))

## What stays separate

| System | Why separate |
|--------|--------------|
| WM Sales Call Tracker (Google Sheet) | Outbound KPI logging — not transcript store |
| Google Sheets "Intro Call Review" | QA/training — not connected to main data system |
| [Sales Intelligence Bible](../acquisition/intelligence/wm-sales-intelligence-bible.md) | Compiled downstream reference — fed by call distillation, not raw store |

## Related

- [Content Engine Infrastructure](../content-engine/INFRASTRUCTURE.md)
- [Knowledge capture skill](../../.claude/skills/knowledge-capture/SKILL.md)
- [Sales Calls Demo Analysis](../acquisition/sales/sales-calls-demo-analysis.md) — extraction schema
- [Lane Boundaries](../content-engine/LANE-BOUNDARIES.md)
