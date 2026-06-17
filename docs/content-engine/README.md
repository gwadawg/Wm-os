---
title: Content Engine
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-17
review_cycle: monthly
artifact_type: index
---

# Content Engine

Production layer for **personal brand** (@gabeegoertzen), **Waiz Media
business**, and **client creative**. Client fulfillment DNA stays in
`docs/client-fulfillment/`; this engine routes knowledge, ideation, scripting,
and repurposing.

## Start here (infrastructure first)

| Doc | Purpose |
|-----|---------|
| [**INFRASTRUCTURE.md**](INFRASTRUCTURE.md) | Where everything goes, naming, dating, phases |
| [**LANE-BOUNDARIES.md**](LANE-BOUNDARIES.md) | Personal vs business vs client — no voice bleed |
| [Personal lane README](personal/README.md) | @gabeegoertzen KB map |
| [Business lane README](business/README.md) | Waiz Media KB map |

**Current phase:** KB build (Phase 1). Filling voice, beliefs, stories, hooks.
Scripting and filming come later.

## Lanes

| Lane | When to use | Voice doc | KB | Script output |
|------|-------------|-----------|-----|---------------|
| `personal` | Journey, beliefs, lifestyle, Gabe operator content | [`_voice/personal-brand-dna.md`](_voice/personal-brand-dna.md) | `personal/` | `personal/scripts/` |
| `business` | Waiz B2B, LO audience, agency positioning | [`_voice/waiz-media-brand-dna.md`](_voice/waiz-media-brand-dna.md) | `business/` + [`.agents/product-marketing.md`](../.agents/product-marketing.md) | `business/scripts/` |
| `client` | Client ad creative, UGC, fulfillment | Client DNA + [`_voice/client-voice-template.md`](_voice/client-voice-template.md) | `docs/client-fulfillment/` | client DNA folders |

**Lane detection:** User says `personal`, `business`, or `client:[slug]` — or
context makes it obvious. When ambiguous, ask once. See
[LANE-BOUNDARIES.md](LANE-BOUNDARIES.md).

## Skills

| Skill | Use when |
|-------|----------|
| [content-engine](../../.claude/skills/content-engine/SKILL.md) | Weekly ideation, `/script` *(Phase 2–3)* |
| [knowledge-capture](../../.claude/skills/knowledge-capture/SKILL.md) | Transcript / diary / notes → update KB **now** |
| [ugc-scriptwriter](../../.claude/skills/ugc-scriptwriter/SKILL.md) | Reel and UGC scripting *(Phase 3)* |
| [copywriting](../../.claude/skills/copywriting/SKILL.md) | Carousel copy *(Phase 3)* |

## Phases (when to use what)

```
Phase 1 — KB BUILD (now)
  Grilling, diary, transcripts → knowledge-capture → personal/ or business/
  Bump last_updated on every edit

Phase 2 — IDEATION (later)
  /weekly-ideas → angle-library.md

Phase 3 — SCRIPTING (later)
  /script → [lane]/scripts/YYYY-MM-DD-format-slug.md

Phase 4 — PUBLISH LOG (later)
  wm-content-archive/published/ (outside git)
```

## Archive (outside OS git)

```
wm-content-archive/          ← sibling to Wm-os, not committed
├── transcripts/
├── research/apify/
└── published/
```

Raw material never lives in compiled docs. Distill via **knowledge-capture**.

## Directory map

```
content-engine/
├── INFRASTRUCTURE.md      ← routing authority
├── LANE-BOUNDARIES.md     ← personal vs business rules
├── _voice/                ← brand DNA
├── personal/              ← @gabeegoertzen KB + scripts/
├── business/              ← Waiz Media KB + scripts/
└── repurposing/           ← explicit cross-lane pipelines
```

## Related

- [DSCR DNA](../client-fulfillment/dscr-dna/README.md)
- [Reverse Mortgage DNA](../client-fulfillment/reverse-mortgage-dna/README.md)
- [Creative Studio](../client-fulfillment/media-buying/creative-studio/)
