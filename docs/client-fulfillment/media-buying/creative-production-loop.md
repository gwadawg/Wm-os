---
title: Creative Production Loop (research → make → Drive → Mr. Waiz → OS swipe)
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-09-07
review_cycle: quarterly
artifact_type: playbook
---

# Creative Production Loop

**One-sentence job:** Research → make stills or video → save the file on Google Drive → register it in Mr. Waiz (full extraction) → distill a short swipe into Wm-os only if it wins (or the founder says so).

**Drive stores the file; Mr. Waiz stores what the agent reads.**

This page is the **umbrella**. Product SOPs (RM studio, DSCR script playbook, Arcads in wm-creative, compliance, naming) stay the how-to. Do not copy them here.

## How this fits existing folders

| Path | Role | Do not treat as |
|------|------|-----------------|
| This page | Sequence for every still and video (client ads + Waiz Instagram) | A fourth media system |
| [ad-development-workflow.md](ad-development-workflow.md) + [creative-studio/](creative-studio/README.md) | RM **client video**: concept → script → Arcads handoff | The file vault |
| **wm-creative** (sibling repo) | Arcads UGC/b-roll, gpt-image-2 statics, session `outputs/` | Product DNA SOT |
| [dscr-video-script-playbook.md](../dscr-dna/dscr-video-script-playbook.md) | DSCR **client video** scripts → wm-creative | RM studio |
| [ai-rm-ad-image-creation-sop.md](ai-rm-ad-image-creation-sop.md) | RM stills via Ideogram (legacy/Custom GPT path) | Required when generating in Cursor with GPT Image 2 |
| [dscr-static-image-generator-project.md](../dscr-dna/dscr-static-image-generator-project.md) | DSCR stills via Ideogram → Mr. Waiz block | GPT Image 2 (different tool) |
| [content-engine](../../content-engine/README.md) + [LANE-BOUNDARIES.md](../../content-engine/LANE-BOUNDARIES.md) | Voice, KB, scripts for personal / business / client | Where PNG/MP4 live |
| Mr. Waiz `ad_library` | **Agent source of truth** for owned ads | A file to download |
| Mr. Waiz `acquisition_ad_library` | Paid **Waiz** acquisition ads | A third library |
| Google Drive | Human file vault | Agent input / pixels |
| [creative-research/](creative-research/README.md) | Distilled swipes + catalogs | A dump of binaries |
| [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md) | When a winner becomes an OS swipe | Daily KPI tables in git |

## Scope

**In:** Client Meta ads (RM, DSCR, other products) and Waiz company Instagram / business creatives. Same loop for stills and video.

**Out:** Rewriting Arcads API docs, compliance gates, naming rules, Ideogram prompt packs, or Mr. Waiz schema.

## Trigger

You need a new still or video, or you are researching other posts / our winners before making one.

## Tools

| Need | Use |
|------|-----|
| Lane (voice / CTA) | [LANE-BOUNDARIES.md](../../content-engine/LANE-BOUNDARIES.md) — do not rewrite it |
| Watch a **new** post (not in Mr. Waiz) | `/watch` on a **public URL** or a file the human already has locally. Not for owned library ads |
| Stills in Cursor | GPT Image 2 skill (`~/.cursor/skills/gpt-image-2`; key in `~/.config/gpt-image-2/.env`). **Not** Cursor native image gen |
| Instagram **carousel** (any lane) | [carousel-production.md](../../content-engine/carousel-production.md) — HTML type cards at 1080×1350. **Not** GPT Image 2 / Ideogram |
| RM video | [ad-development-workflow.md](ad-development-workflow.md) / `rm-creative-studio` → **wm-creative** Arcads |
| DSCR video | [dscr-video-script-playbook.md](../dscr-dna/dscr-video-script-playbook.md) → **wm-creative** Arcads |
| DSCR Ideogram stills | [dscr-static-image-generator-project.md](../dscr-dna/dscr-static-image-generator-project.md) |
| Name + register | [ad-naming-convention.md](ad-naming-convention.md) + ad-naming skill (live `ad_library` lookup) |
| Winner → OS | knowledge-capture + [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md) |

Do not open `drive_url`, fetch Drive, download thumbnails, or cache stills so the agent can “see” the library. The row already has the extraction — **if that extraction is thin, ask; do not invent.**

## Incomplete rows (ask, don’t fabricate)

Mr. Waiz is only as good as the row. Older ads may have empty `summary`, missing tags, or no `visual_notes`.

**Enough to proceed without asking:** `summary` describes the message (hook / what it says / who it’s for), plus `product` and `ad_format` (or type). Tags and `visual_notes` help but are not required if the summary is specific.

**Stop and ask before generating, remixing, or writing a swipe** if any of these are true:

- `summary` is empty, a filename, or one vague line (“static”, “UGC”, “test”)
- `product` or `ad_format` / type is missing and the task depends on it
- The user named a specific ad and the row doesn’t match what they described
- KPIs are too thin to call it a winner, but the task is “make more of this winner”

Ask 1–3 concrete questions (what’s on screen, hook, format, who it’s for). Do **not** fill gaps from memory, a similar ad, or a swipe file. If they say “proceed anyway,” state the assumptions in one line, then continue.

## Process (stills and video)

1. **Lane** — Client ads vs Waiz Instagram/business vs personal. Follow [LANE-BOUNDARIES.md](../../content-engine/LANE-BOUNDARIES.md). One piece, one primary lane.

2. **Research**
   - **Owned ads (remix / winners):** query Mr. Waiz — `summary`, `visual_notes` if present, tags, `product`, `ad_format` / type, `status`, KPIs. Concept from that text. Do not open Drive. If the row is incomplete, follow **Incomplete rows** above — ask, don’t invent.
   - **Not in the library yet:** `/watch` or a pasted public URL (competitor post, Reel, etc.).

3. **Concept → generate**
   - **Carousel:** [carousel-production.md](../../content-engine/carousel-production.md) HTML kit → PNG. Do not generate slide art with GPT Image 2.
   - Other stills in Cursor: GPT Image 2. Write files to a **local path outside Wm-os git** (e.g. `~/Downloads/` or `/tmp/`). Never `docs/` or repo `assets/`.
   - Motion: RM → `rm-creative-studio` then **wm-creative** Arcads; DSCR → `dscr-video-script-playbook` then **wm-creative** Arcads; editors as needed. Not native Cursor video.

4. **Human saves the final file to Drive** (Meta / editors). **Log or update Mr. Waiz** with the same extraction habit: `summary`, tags, type/`ad_format`, plus `ad_name`, `status`, `product`, `visual_notes`, `drive_url` (humans use the URL; the agent does not fetch it).
   - Client Meta → `ad_library`
   - Paid Waiz acquisition → `acquisition_ad_library`
   - Organic Instagram with no spend → Drive + content-engine script; library row optional until there is paid performance

5. **Distill to Wm-os only** for winners or founder-approved learnings — short swipe in `creative-research/swipes/` (and catalogs on repeat). No KPI tables in git. See [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md).

## Where each thing lives

| Thing | Lives |
|-------|--------|
| PNG / MP4 / final file | Google Drive (humans) |
| What the ad says + KPIs over time | Mr. Waiz (`ad_library` or `acquisition_ad_library`) — **what the agent reads** |
| “Why it won” pattern | Wm-os swipe / catalog (git) |
| Script markdown (optional save) | `creative-studio/outputs/` — **markdown only** |

## Do not

- Put media in Wm-os git (PNG, MP4, frames). Git is already ignoring `*.mp4`; do not add a stills vault.
- Keep a second spreadsheet of performance (Mr. Waiz owns KPIs).
- Open `drive_url`, fetch Drive, thumbnails, or a local stills cache so the agent can see owned ads.
- Invent a hook, script, or visual from a thin or empty Mr. Waiz `summary`. Ask first.
- Fork product DNA into wm-creative (DNA stays in Wm-os; renders live in wm-creative).
- Duplicate naming, compliance, or winner-capture docs on this page.
- Use Higgsfield (retired) or route DSCR jobs through `rm-creative-studio`.
- Commit GPT Image 2 output (skill default `assets/gpt-image-2/` is gitignored if cwd is this repo — still prefer `~/Downloads/`).

## Related

- [Media buying README](README.md)
- [Content engine README](../../content-engine/README.md)
- [AGENTS.md](../../../AGENTS.md)
