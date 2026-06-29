# Weekly Content Workflow

Full operating loop for a weekly content session (~60–90 min).

## Pre-session (5 min)

- [ ] Lane confirmed: personal | business | client
- [ ] Voice doc loaded
- [ ] If new file in `wm-content-archive/research/apify/`, run `/apify-capture` first
- [ ] Optional: paste transcript for knowledge-capture

## Step 1 — Research pulse (5 min)

1. Read `personal/inspiration/competitor-research.md` Pattern log
2. Check `angle-library.md` for `status: remix-candidate` and recent `swipe-file.md` entries
3. If user has `wm-content-archive/research/apify/YYYY-MM-DD-*.json`, run `/apify-capture` on it
4. Note 2–3 patterns to exploit this week (include remix-candidates)

## Step 2 — Idea generation (20 min)

Run `/weekly-ideas`:

- Minimum 15 ideas if user didn't specify count
- Include at least **2 remix-candidates** from swipe-file as trial-concepts when available
- Balance pillars — don't stack one pillar unless user asks
- Include at least 3 **trial-concepts** for fast validation
- Tag searchable vs shareable on every idea

### Buyer stage mapping (business / B2B-adjacent personal)

| Stage | Modifier examples | Content job |
|-------|-------------------|-------------|
| Awareness | what is, myth, mistake | Pattern interrupt, educate |
| Consideration | vs, best, how to choose | Framework, comparison |
| Decision | proof, case study, CTA | Trust + book call |
| Implementation | template, step-by-step | Tactical carousel/reel |

## Step 3 — Selection (15 min)

User picks 3–7 for `film-this-week`. Update `angle-library.md`:

- `status: selected` for this week
- `status: idea` for save-for-later
- Remove or mark archive for rejects

Prioritize by weighted score but allow user override for energy/timeliness (travel moment, timely news).

## Step 4 — Scripting (30–45 min)

For each selected idea: `/script [title]`

Order: **trials first** (film quick) → full reels → carousels

## Step 5 — Handoff to editor

Each script file should include:

- Spoken lines with timestamps optional
- `[VISUAL:]` directions
- `editor_notes`: music, pacing, captions, b-roll
- `length_target`

Deliverable: folder of `scripts/YYYY-MM-DD-*.md` for the week.

## Step 6 — Post-publish (async)

After filming/publishing:

1. Update script `status: published`
2. Log performance in angle-library weekly batch table
3. Strong performers → consider [reels-to-ads-engine](../../docs/content-engine/repurposing/reels-to-ads-engine.md)

## Apify cadence (optional weekly)

- 1 scrape per week max unless launching new niche
- Use [creator-research](../../../../.claude/skills/creator-research/SKILL.md): `/scrape-help` → Apify UI → `/apify-capture` → `/remix`
- Always archive raw JSON outside repo
- Never paste full Apify dump into OS — distill only
