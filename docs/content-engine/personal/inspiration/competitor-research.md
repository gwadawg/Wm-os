---
title: Competitor & Market Research
domain: content-engine
owner: founder
status: draft
last_updated: 2026-06-26
review_cycle: monthly
auto_update: true
update_via: knowledge-capture
update_types: [competitor-patterns]
---

# Competitor & Market Research

What others in your space are doing — patterns to learn from, gaps to fill.

**Skill:** [creator-research](../../../../.claude/skills/creator-research/SKILL.md) —
`/scrape-help`, `/apify-capture`, `/remix`

**Manifest:** [creator-research-manifest.yaml](../../research/creator-research-manifest.yaml)

## Apify research workflow

1. **Pick scope** (prompt each session — no fixed schedule):
   - IG profile: `@[handle]` — top N posts by engagement
   - IG hashtag: `#[tag]` — top N Reels
   - Meta Ad Library: keyword search — ads running 30+ days
2. **Run actor** in Apify UI (see manifest for actor IDs and example inputs):
   - Instagram: `apify/instagram-scraper`
   - Meta Ads: `apify/facebook-ads-scraper` (same method as DSCR `_research/` scrapes; distill into [GTM Brief](../../../client-fulfillment/dscr-dna/dscr-gtm-positioning-brief.md))
3. **Export raw** to archive (never into OS git):
   ```
   wm-content-archive/research/apify/YYYY-MM-DD-platform-scope.json
   ```
4. **Process:** `/apify-capture [path]` — distills hooks, swipes, remix-candidates
5. **Remix:** `/remix [swipe-id]` — trial-concept in your voice

### Meta Ad Library search URL

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q={keyword}&search_type=keyword_unordered&media_type=all
```

Replace `{keyword}` with niche term (e.g. `loan officer`, `entrepreneur`).

## Viral ranking rules

| Platform | Sort by | Filter | Top N (default) |
|----------|---------|--------|-----------------|
| **Instagram** | Likes + comments; prefer high view-to-like on Reels | User sets `min_views` at prompt time | 20 |
| **Meta Ads** | Days running (longevity = likely converting) | Active ads, `min_days_running: 30` | 15 |

Remix score ≥ 7 → `swipe-file.md` + `angle-library.md` with `status: remix-candidate`.

## Weekly scrape prompt template

Copy and fill before each Apify run:

```
This week's scrape:
- Platform: instagram | meta_ads
- Scope: @[handle] | #{hashtag} | keyword "{keyword}"
- Limit: N items
- Save as: wm-content-archive/research/apify/YYYY-MM-DD-{platform}-{slug}.json
- Then: /apify-capture
```

Cadence: **1 scrape/week max** unless launching new niche.

## Archive layout (sibling to Wm-os)

```
wm-content-archive/
├── transcripts/YYYY-MM-DD-type-topic.md
├── research/apify/YYYY-MM-DD-platform-niche.json
└── published/YYYY-MM-DD-platform-title.md
```

Bootstrap once:

```bash
mkdir -p ../wm-content-archive/research/apify
mkdir -p ../wm-content-archive/transcripts
mkdir -p ../wm-content-archive/published
```

## Competitor map

| Creator / brand | Platform | What they do well | Gap you can own |
|-----------------|----------|-------------------|-----------------|
| @bigdaddyleads | IG | Bold agency positioning, proof-heavy operator tone, adjacent vertical (insurance/lead gen) | Mortgage-specific journey + lifestyle mix; goofier voice |
| @marcel.stxm | IG | UGC hooks, story + CTA structure, performance short-form | Your lived burn-the-boats story + AI/ops depth |
| @lukaspakter | IG / podcast | Ambitious entrepreneur network energy, long-game brand | Tactical operator content + controversial PD takes |

## Pattern log

| Date | Source | Pattern | Action |
|------|--------|---------|--------|
| 2026-06-26 | Apify @bigdaddyleads (25 reels) | Incredulous callout yap; dirty-secret rant; 4-question list yap; "am I wrong?" close; ultra-short reaction hooks | 5 remix-candidates in swipe-file — `/remix` top 3 for yap trials |
| 2026-06-26 | Apify @marcel.stxm (7 posts) | Recent feed = carousels + 1 viral reel; caption hooks ("unemploy yourself") stronger than video for yap | Use `resultsType: reels` or caption-only yap; hook library not full UGC |
| 2026-06-17 | Founder refs | Story + hook + CTA (Marcel); bold operator proof (Big Daddy); lifestyle/network brand (Lukas) | Test in format lab + burn-the-boats reels |

## Forum research (manual)

When Apify isn't enough:

- Reddit: `site:reddit.com [topic]`
- YouTube comments on top videos in niche

Log FAQs and language verbatim → knowledge-capture → voice DNA / beliefs.

## First-run validation

After implementing creator-research workflow:

1. Small IG profile scrape (e.g. `@marcel.stxm`, 10 posts) in Apify UI
2. Save JSON with correct archive naming
3. `/apify-capture` — verify swipe + hook + pattern log updates
4. `/remix` on top swipe — trial-concept in `personal/scripts/`
5. Close Apify gap in `personal/_gaps.md`

<!-- knowledge-capture: competitor mentions from calls append to Pattern log -->
