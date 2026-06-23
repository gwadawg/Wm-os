---
name: knowledge-capture
description: Extracts hooks, angles, beliefs, objections, voice patterns, and stories from transcripts, sales calls, articles, notes, and Apify research dumps; routes distilled entries into content-engine and acquisition docs. Use when the user pastes a transcript, call recording text, research export, or asks to update the knowledge base from new information.
disable-model-invocation: true
---

# Knowledge Capture

Turn raw inputs into **distilled OS updates**. Never store full transcripts in the OS — raw calls live in Supabase; optional mirror in `wm-content-archive/transcripts/`.

## Supabase pull mode

When the user references a call by UUID, pending batch, or points to the Mr. Waiz database:

1. Read [call-intelligence-bridge.md](../../../docs/operations/call-intelligence-bridge.md)
2. Pull call via **Supabase MCP** (`v_all_calls`) or dashboard `GET /api/calls/intelligence`
3. Read `extraction` JSON first; load `transcript` only if extraction is empty or insufficient
4. Route findings per [routing-table.md](routing-table.md)
5. Cite every entry: `supabase:call:{uuid}` in Source column
6. After confirmed updates, note that `call_intelligence.knowledge_capture_status` should be set to `processed` and `os_refs` updated in Supabase

## Supabase ad pull mode (owned winners)

When the user says "capture pending RM ad winners", references `supabase:ad:{uuid}`, or points to Mr. Waiz `ad_library`:

1. Read [ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md)
2. Pull ad via **Supabase MCP** on `ad_library` (+ `ad_library_aliases`) or v2 `GET /api/ad-library/intelligence`
3. Read `summary` + `visual_notes` first (usually sufficient — no Drive video required)
4. Snapshot performance funnel metrics at capture time (spend, leads, qualified, appointments, shows)
5. Route findings per [routing-table.md](routing-table.md) § Owned client ads
6. Cite every entry: `supabase:ad:{uuid}`
7. After confirmed updates, set `knowledge_capture_status = 'processed'` and `os_refs` on `ad_library` (v2)
8. Keep [ad-development-workflow.md](../../../docs/client-fulfillment/media-buying/ad-development-workflow.md) and creative-research catalogs in sync

### Supabase ad queries

Single ad with aliases:

```sql
select al.*, coalesce(json_agg(ala.alias_name) filter (where ala.id is not null), '[]') as aliases
from ad_library al
left join ad_library_aliases ala on ala.library_id = al.id
where al.id = '{uuid}'
group by al.id;
```

RM winners pending capture:

```sql
select id, ad_name, product, ad_format, status, summary, visual_notes, knowledge_capture_status
from ad_library
where product = 'reverse' and status = 'winner'
  and coalesce(knowledge_capture_status, 'none') in ('none', 'pending')
order by updated_at desc limit 20;
```

**Weekly cap:** Process 1–3 owned RM winners max per session. Scrub client names from OS entries.

### Supabase queries

Single call with transcript:

```sql
select call_id, call_category, call_subtype, called_at, transcript, extraction, lanes, sensitivity
from v_all_calls where call_id = '{uuid}';
```

Pending content-eligible calls:

```sql
select call_id, call_category, call_subtype, called_at, transcript_summary, extraction
from v_all_calls
where knowledge_capture_status = 'pending'
  and content_eligible = true
order by called_at desc limit 20;
```

**Weekly cap:** Process 3–5 calls max. Prioritize sales > Gabe teaching > client check-ins.
Skip ops-only client calls (`knowledge_capture_status = skipped`).

**Client calls:** Default route to client DNA, not business hooks. Scrub names/metrics.

## Input types

| Type | Examples |
|------|----------|
| `transcript` | Sales call, discovery, client call, podcast |
| `notes` | Voice memo text, bullet dump |
| `article` | Blog, thread, competitor post |
| `apify` | JSON export from Instagram / Meta Ads scraper (via creator-research `/apify-capture`) |
| `forum` | Reddit/comment research paste |

Ask if unclear: **"What type of input is this, and which lane should benefit (personal / business / client)?"**

## Workflow

```
1. Read INFRASTRUCTURE.md + LANE-BOUNDARIES.md
2. Read input (in context — not saved to OS unless archive)
3. Detect lane: personal | business | client
4. Extract findings by category (below)
5. Route each finding per routing-table.md
6. Auto-update low-risk docs OR ask for high-impact changes
7. Bump last_updated on every KB file touched
8. Log gaps in [lane]/_gaps.md
9. Summarize what changed + what needs confirmation
```

## Extraction categories

From **content-strategy** call transcript methodology:

| Category | Look for |
|----------|----------|
| **Questions asked** | FAQ / content ideas → angle-library |
| **Pain points** | Verbatim phrases → beliefs, angles, product-marketing |
| **Objections** | Reframe pairs → acquisition/sales or angles |
| **Language patterns** | Exact phrases → voice DNA, hook-library |
| **Stories** | Narrative arcs → stories.md |
| **Hooks** | Punchy openers said naturally → hook-library |
| **Competitor mentions** | Names + comparisons → competitor-research |
| **Beliefs / frames** | Strong opinions → beliefs.md |
| **Format decomposition** | Hook, beats, visual, audio, engagement → swipe-file (Apify) |

Capture **verbatim quotes** when possible (product-marketing standard). For Apify
scrapes, **adapt hooks** — do not copy competitor lines verbatim into hook-library.

## Auto-update vs ask-first

| Finding | Action |
|---------|--------|
| Hook, angle idea, story candidate | **Auto-append** with source + date |
| Swipe / competitor pattern | **Auto-append** to inspiration docs |
| New belief or positioning shift | **Ask first** |
| Voice DNA personality/tone change | **Ask first** |
| New content pillar | **Ask first** → or log in `_gaps.md` |
| Client compliance-sensitive claim | **Ask first** + flag compliance |
| Product-marketing pricing/offer change | **Ask first** |

When asking, use:

> "Found: [quote/summary]. Add to [doc/section]? (yes / edit / skip / gap only)"

## Gap detection

After extraction, if a theme appears **2+ times** with no OS home:

1. Append row to `docs/content-engine/personal/_gaps.md`
2. Include suggested target doc
3. Do not create new top-level docs without user approval

## Output summary (required)

```markdown
## Knowledge capture — [date] — [input type]

### Auto-updated
- hook-library.md: +2 hooks
- angle-library.md: +1 angle

### Needs confirmation
- [ ] Belief candidate: "..." → beliefs.md?

### Gaps logged
- _gaps.md: "investor mindset shift" → no pillar yet

### Archive reminder
Save raw to: wm-content-archive/transcripts/YYYY-MM-DD-[topic].md
```

## Routing

Full matrix: [routing-table.md](routing-table.md)

## Lane routing

- **Personal content fuel** → `docs/content-engine/personal/*`
- **Waiz positioning / LO language** → `.agents/product-marketing.md` (ask-first) + `business/*`
- **Client product** → relevant `docs/client-fulfillment/[dna]/*` (ask-first for compliance)

## Related

- [call-intelligence-bridge.md](../../../docs/operations/call-intelligence-bridge.md) — Supabase call pull contract
- [ad-intelligence-bridge.md](../../../docs/operations/ad-intelligence-bridge.md) — Supabase owned-ad pull contract
- [creator-research](../creator-research/SKILL.md) — Apify capture + format remix
- [content-engine](../content-engine/SKILL.md) — consumes updated KB for ideation
- [waiz-business-os](../waiz-business-os/SKILL.md) — doc standards

## Do not

- Paste 10k+ word transcripts into any `.md` in the repo
- Auto-edit `status: active` spine docs without explicit approval
- Duplicate URLs already in canonical manifests (e.g. pre-call objection videos)
