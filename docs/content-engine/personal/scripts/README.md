---
title: Personal Lane — Script Output
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-17
artifact_type: index
---

# Personal Scripts — Output Folder

**Phase 3 only.** Do not create scripts until Gabe explicitly requests production.

## What goes here

Finished scripts for @gabeegoertzen content:

- Reels, carousels, trial-concepts
- Lane: always `personal` in frontmatter

## Naming

```
YYYY-MM-DD-[format]-[slug].md

Examples:
  2026-06-20-reel-rio-one-way-ticket.md
  2026-06-22-carousel-adhd-systems.md
  2026-06-24-trial-concept-skate-metaphor.md
```

## Template

Use frontmatter from [`../../_templates.md`](../../_templates.md). Required:
`lane: personal`, `date`, `format`, `status`, `source_idea`.

## After scripting

1. Update matching entry in [`../angle-library.md`](../angle-library.md) →
   `status: scripted`
2. Bump `last_updated` on angle-library
3. Optional: log publish metadata in `wm-content-archive/published/` when live

## Not here

| Asset | Correct location |
|-------|------------------|
| Raw video / transcript | `wm-content-archive/` |
| Waiz Media B2B scripts | `business/scripts/` |
| Client ad scripts | `docs/client-fulfillment/` |
| KB updates (beliefs, stories) | Parent `personal/` docs |
