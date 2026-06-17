---
name: knowledge-capture
description: Extracts hooks, angles, beliefs, objections, voice patterns, and stories from transcripts, sales calls, articles, notes, and Apify research dumps; routes distilled entries into content-engine and acquisition docs. Use when the user pastes a transcript, call recording text, research export, or asks to update the knowledge base from new information.
disable-model-invocation: true
---

# Knowledge Capture

Turn raw inputs into **distilled OS updates**. Never store full transcripts in the OS — archive raw externally (`wm-content-archive/transcripts/`).

## Input types

| Type | Examples |
|------|----------|
| `transcript` | Sales call, discovery, client call, podcast |
| `notes` | Voice memo text, bullet dump |
| `article` | Blog, thread, competitor post |
| `apify` | JSON export from Instagram/TikTok scraper |
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

Capture **verbatim quotes** when possible (product-marketing standard).

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

- [content-engine](../content-engine/SKILL.md) — consumes updated KB for ideation
- [waiz-business-os](../waiz-business-os/SKILL.md) — doc standards

## Do not

- Paste 10k+ word transcripts into any `.md` in the repo
- Auto-edit `status: active` spine docs without explicit approval
- Duplicate URLs already in canonical manifests (e.g. pre-call objection videos)
