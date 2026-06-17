---
title: Competitor & Market Research
domain: content-engine
owner: founder
status: draft
last_updated: 2026-06-17
review_cycle: monthly
auto_update: true
update_via: knowledge-capture
update_types: [competitor-patterns]
---

# Competitor & Market Research

What others in your space are doing — patterns to learn from, gaps to fill.

## Apify research workflow

1. **Pick scope:** niche keyword, competitor handle, or hashtag cluster
2. **Run actor** (examples):
   - Instagram scraper — top posts by engagement
   - TikTok scraper — trending in niche
   - YouTube transcript — if competitor long-form
3. **Export raw** to archive (never into OS git):
   ```
   wm-content-archive/research/apify/YYYY-MM-DD-platform-niche.json
   ```
4. **Process with knowledge-capture skill:**
   - Strong hooks → `hook-library.md`
   - New angles → `angle-library.md`
   - Patterns → tables below
5. **Optional:** add best swipes to `swipe-file.md`

## Archive layout (sibling to Wm-os)

```
wm-content-archive/
├── transcripts/YYYY-MM-DD-type-topic.md
├── research/apify/YYYY-MM-DD-platform-niche.json
└── published/YYYY-MM-DD-platform-title.md
```

Create locally next to Wm-os; do not commit to this repo.

## Competitor map

| Creator / brand | Platform | What they do well | Gap you can own |
|-----------------|----------|-------------------|-----------------|
| @bigdaddyleads | IG | Bold agency positioning, proof-heavy operator tone, adjacent vertical (insurance/lead gen) | Mortgage-specific journey + lifestyle mix; goofier voice |
| @marcel.stxm | IG | UGC hooks, story + CTA structure, performance short-form | Your lived burn-the-boats story + AI/ops depth |
| @lukaspakter | IG / podcast | Ambitious entrepreneur network energy, long-game brand | Tactical operator content + controversial PD takes |

## Pattern log

| Date | Source | Pattern | Action |
|------|--------|---------|--------|
| 2026-06-17 | Founder refs | Story + hook + CTA (Marcel); bold operator proof (Big Daddy); lifestyle/network brand (Lukas) | Test in format lab + burn-the-boats reels |

## Forum research (manual)

When Apify isn't enough:

- Reddit: `site:reddit.com [topic]`
- YouTube comments on top videos in niche

Log FAQs and language verbatim → knowledge-capture → voice DNA / beliefs.

<!-- knowledge-capture: competitor mentions from calls append to Pattern log -->
