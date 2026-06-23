---
title: Ad Development Workflow (RM Client Ads)
domain: client-fulfillment
owner: founder
status: active
last_updated: 2026-06-23
review_cycle: monthly
artifact_type: playbook
---

# Ad Development Workflow (RM Client Ads)

Single entry for how Waiz develops **reverse-mortgage client Meta ads** end-to-end: learn from winners, create new scripts, close the loop in Mr. Waiz.

**Bridge spec:** [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md)

## Two modes

| Mode | When | Output |
|------|------|--------|
| **Learn** | Weekly — ad performed well in accounts | Swipe + catalog pattern in `creative-research/` |
| **Create** | On demand — new ad for a client | Concept → script → Higgsfield prompt in chat / `creative-studio/outputs/` |

## Full lifecycle

```
Tag winner (Mr. Waiz) → Capture to swipe (KB) → Promote to catalogs (repeat patterns)
        ↑                                                      ↓
   Performance data ← Launch ← Higgsfield ← Script ← Concept ← Step 0 pull patterns
```

## Create mode — retrieval order (Step 0)

When scripting a new RM ad, agents load sources in this order:

1. This doc + [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md)
2. [script-archetypes-catalog.md](creative-research/script-archetypes-catalog.md) + [editing-styles-catalog.md](creative-research/editing-styles-catalog.md)
3. Relevant [creative-research/swipes/](creative-research/swipes/) (filter: product=RM, format, funnel stage)
4. [losers-log.md](creative-research/losers-log.md) — patterns to avoid
5. On-demand: Mr. Waiz `ad_library` via `supabase:ad:{uuid}` or winners with `status=winner` + `product=reverse`
6. Framework docs: [rm-ad-ideation-matrix.md](creative-studio/rm-ad-ideation-matrix.md), [rm-script-generator.md](creative-studio/rm-script-generator.md), [compliance-gate-checklist.md](creative-studio/compliance-gate-checklist.md)

**Never** pull competitor Apify intel in this flow — use [creator-research](../../../.claude/skills/creator-research/SKILL.md) separately.

### Step 0 contract

Before Step 1 (Concept) in [creative-studio](creative-studio/README.md):

```
1. Read retrieval order (above)
2. Scan script-archetypes + editing-styles catalogs
3. List 2–3 relevant swipes or supabase:ad:{uuid} if user named a winner
4. State: "Patterns I'm building from:" with citations
5. Identify gap: archetype × angle × format not recently proven → ideation seed
6. Proceed to ideation matrix using gap + patterns, not blank page
```

Invoked via [rm-creative-studio](../../../.claude/skills/rm-creative-studio/SKILL.md).

## Learn mode — capture workflow

1. In Mr. Waiz Media Buyer: fill `summary` + `visual_notes`, set `status=winner`, link aliases.
2. In Cursor: run [knowledge-capture](../../../.claude/skills/knowledge-capture/SKILL.md) — "process pending RM ad winners."
3. Agent produces `creative-research/swipes/rm-{date}-{slug}.md` from [swipe template](creative-research/swipes/_TEMPLATE.md).
4. Promote to catalogs when the same pattern appears 3+ times (or founder approves).
5. Log `os_refs` + `supabase:ad:{uuid}` in swipe frontmatter.

## Shortcut commands

| You say | Agent does |
|---------|------------|
| "New RM ad" / "brainstorm" | Step 0 → 4-step creative studio flow |
| "Pull from our winners first" | Step 0 only, then wait |
| "Capture pending RM winners" | Knowledge-capture ad pull mode |
| "Vary this winner" + `supabase:ad:{uuid}` | Load Layer 0 detail, produce variations |

## Acceptance test

Prompt:

> New RM TOF UGC ad for legacy planner archetype — pull from our winners first, then give me 3 concepts.

Expected:

1. Loads workflow + catalogs + recent swipes
2. Cites 1–2 `supabase:ad:{uuid}` or swipe ids
3. Names the gap the new concept fills
4. Runs ideation matrix with compliance flags

## Related

- [Creative Studio](creative-studio/README.md) — outbound script engine
- [Creative Research](creative-research/README.md) — inbound pattern library
- [AI RM Ad Images](ai-rm-ad-image-creation-sop.md) — static ad path (also uses Step 0)
- [RM Ad Playbook](../client-marketing/rm-ad-playbook.md) — strategy layer
