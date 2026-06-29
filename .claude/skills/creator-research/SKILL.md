---
name: creator-research
description: Processes Apify scrape exports (Instagram, Meta Ads) into viral format decompositions, swipe files, and remix-ready angles for the content engine. Use when the user runs Apify, saves JSON to wm-content-archive, wants to capture competitor formats, remix viral videos, or asks /apify-capture, /remix, /scrape-help.
disable-model-invocation: true
---

# Creator Research

Turn **manual Apify scrapes** into distilled formats and remix scripts for
`docs/content-engine/`. Raw JSON stays in `wm-content-archive/` — never in OS git.

## Before any task

1. Read [docs/content-engine/INFRASTRUCTURE.md](../../docs/content-engine/INFRASTRUCTURE.md)
2. Read [docs/content-engine/LANE-BOUNDARIES.md](../../docs/content-engine/LANE-BOUNDARIES.md)
3. Read [creator-research-manifest.yaml](../../docs/content-engine/research/creator-research-manifest.yaml)
4. Detect lane: **personal** (default) | **business** (B2B remix — extra angle check)

## Archive policy

- Raw JSON: `../wm-content-archive/research/apify/YYYY-MM-DD-{platform}-{scope-slug}.json`
- Never paste full Apify dump into OS docs
- Cite sources as `apify:{platform}:{archive-filename}`

## Commands

### `/scrape-help [platform]`

Print setup from manifest for the requested platform (`instagram` | `meta_ads`).

**Output:**

1. Apify actor ID + link
2. Scope types (profile, hashtag, keyword search URL, etc.)
3. Recommended input shape (example JSON fields)
4. Sort/rank rule (engagement vs days-running)
5. Archive filename template
6. Reminder: save export to `wm-content-archive/research/apify/` then run `/apify-capture`

User prompts scope at run time — no fixed scrape schedule.

### `/apify-capture [archive-path]`

Process a saved Apify export into the content-engine KB.

**Steps:**

1. Resolve path: user-provided path, or newest file in `wm-content-archive/research/apify/`
2. Read JSON in context (do not save to OS)
3. Detect platform from filename or manifest `platforms` keys
4. Rank items per manifest `viral_thresholds` and platform `sort_by`
5. For top performers, run **format decomposition** on each:

| Field | What to extract |
|-------|-----------------|
| **Hook** | First 1–3 seconds / opening line |
| **Structure** | Beats: setup → tension → payoff → CTA |
| **Visual format** | Talking head, text-on-screen, b-roll cuts, carousel, UGC |
| **Audio** | Trending sound, voiceover, silence + captions |
| **Engagement** | Views, likes, comments, or days-running (ads) |
| **Remix potential** | 1–10 — how easily this maps to user's pillars/voice |

6. Delegate routing to [knowledge-capture](../knowledge-capture/SKILL.md) per
   [routing-table.md](../knowledge-capture/routing-table.md) § Apify
7. **Adapt hooks** — never copy verbatim; rewrite for user's voice DNA
8. Assign swipe IDs: `swipe-YYYY-MM-DD-NN` (increment per capture session)
9. Remix score ≥ 7 → `swipe-file.md` + `angle-library.md` with `status: remix-candidate`
10. Bump `last_updated` on every KB file touched
11. Output required knowledge-capture summary (see knowledge-capture skill)

**Swipe entry format** — append to `personal/inspiration/swipe-file.md`:

```markdown
### swipe-YYYY-MM-DD-01 — @creator / ad title
- **ID:** swipe-YYYY-MM-DD-01
- **URL / platform:** [url] · instagram | meta_ads
- **Format:** reel | carousel | ad
- **Hook:**
- **Format beats:** setup → … → CTA
- **Visual format:**
- **Audio:**
- **Engagement:** views/likes or days-running
- **Remix score:** 8/10
- **Remix notes:** which pillar, what to swap in
- **Adapt for pillar:**
- **Status:** remix-candidate | saved | adapted | used
- **Source:** apify:instagram:2026-06-18-marcel-stxm.json · 2026-06-18
```

**Remix-candidate angle block** — append to `personal/angle-library.md`:

```markdown
### [Working title — remix of @creator format]
- **Pillar:**
- **Type:** shareable
- **Format:** trial-concept
- **Hook seed:**
- **Status:** remix-candidate
- **Format ref:** swipe-YYYY-MM-DD-01
- **Source:** apify:instagram:2026-06-18-marcel-stxm.json · 2026-06-18
```

### `/remix [swipe-id or angle title]`

Adapt a proven viral format into a trial script in your voice.

**Steps:**

1. Load swipe entry (by ID) or angle with `format_ref`
2. Load lane voice DNA:
   - Personal: `_voice/personal-brand-dna.md` → beliefs/stories if linked
   - Business: `_voice/waiz-media-brand-dna.md` + `.agents/product-marketing.md`
3. Decompose source format beat-by-beat from swipe entry
4. Map each beat to **your** belief, story, or hook — same structure, different substance
5. Apply [format-templates.md](../content-engine/format-templates.md) — **trial-concept** default
6. For spoken reels, follow [ugc-scriptwriter](../ugc-scriptwriter/SKILL.md)
7. Save to `[lane]/scripts/YYYY-MM-DD-trial-concept-[slug].md`
8. Update linked angle `status: scripted`
9. Update swipe `status: adapted` or `used`

**Quality bar:**

- Not verbatim copy — adapt hook, examples, and CTA to your lane
- Personal: sound like Gabe, not Waiz sales copy
- Business: no unapproved pricing or guaranteed outcomes
- One clear idea per trial; film fast to validate format

## Weekly cadence

- **1 scrape/week max** unless launching new niche
- Run `/apify-capture` before `/weekly-ideas` when new archive file exists
- Prioritize `remix-candidate` angles as trial-concepts in weekly session

## First-run validation

See manifest `first_run` section. After your first real scrape:

1. Confirm swipe + hook + pattern log updates
2. Run `/remix` on top swipe
3. Close Apify gap row in `personal/_gaps.md`

## Related skills

- [knowledge-capture](../knowledge-capture/SKILL.md) — distillation routing
- [content-engine](../content-engine/SKILL.md) — `/weekly-ideas`, `/script`
- [ugc-scriptwriter](../ugc-scriptwriter/SKILL.md) — reel/trial spoken lines

## OS paths

- Manifest: `docs/content-engine/research/creator-research-manifest.yaml`
- Inspiration: `docs/content-engine/personal/inspiration/`
- Scripts: `docs/content-engine/[lane]/scripts/`
