# EditorProjectcreator Templates

Copy structure exactly. Replace bracketed placeholders.

## PROJECT.md frontmatter

```yaml
---
title: "PROJECT — [Call Title] ([Month Year])"
domain: content-engine
owner: founder
status: active
last_updated: YYYY-MM-DD
review_cycle: weekly
artifact_type: project
---
```

## PROJECT.md body

```markdown
# PROJECT — [Short Title]

**Lane:** personal (@gabeegoertzen)
**Strategy:** **Phase 1 — [N] main clips** (one at a time, structure first). **Phase 2 — shorts** deferred until a main performs.

## Workflow

| Phase | What | Rule |
|-------|------|------|
| **1 — Main clips** | [N] anchors below | One clip at a time: thesis → structure → Gabe approves → edit → publish |
| **2 — Shorts** | Splinters from mains | **Not until** that main is published |

**Gate:** No edit until structure is signed off per clip.

**Source:** [One-line description]

## Source

| Field | Value |
|-------|-------|
| Call | [Title] |
| Date | YYYY-MM-DD |
| Duration | ~[N] min |
| Recording | [Fathom URL] |
| Participants | [Names] |
| ClickUp project task | *(create when clip 01 structure approved)* |

## Spot-check — what to use vs skip

| Timestamp | Content | Verdict |
|-----------|---------|---------|
| 0:00–X:XX | [Segment] | **Skip** — [reason] |
| **X:XX–Y:YY** | [Coaching moment] | **Clip 01** — [topic] |

## Content thesis

[2–4 sentences: what Gabe teaches, reframed for public audience]

**Reframe for audience:** [How to speak on camera — not "on our call with…"]

## Production notes (all clips)

- **Source footage:** Fathom — [talking head / screen share mix]
- **Production format:** `call-clip-edit`
- **Captions:** Full burn-in required
- **Skip:** [rapport, pricing, etc.]

## Phase 1 — Main clips (active)

| # | Title | Length | Fathom | Brief | Status |
|---|-------|--------|--------|-------|--------|
| **01** | [Title](clips/01-anchor-[slug].md) | ~[M:SS] | [link](url?timestamp=SECS) | [one line] | **in review** ← current |
| **02** | [Title](clips/02-anchor-[slug].md) | ~[M:SS] | [link](url?timestamp=SECS) | [one line] | queued |

## Phase 2 — Shorts (deferred)

| ID | Idea | Parent |
|----|------|--------|
| 01a | [Short idea] | 01 |

## Publish sequence

| Order | Main | When |
|-------|------|------|
| 1 | **01** — [title] | After structure approved + edited |

## ClickUp

Parent project task + one task per main — create via `/push-clip` after clip structure sign-off.

## Related outputs

| Asset | Path | Note |
|-------|------|------|
| Clip 01 script | *(pending approval)* | — |
```

## Clip brief frontmatter

```yaml
---
clip_id: "01"
clip_type: anchor
parent_clip: null
project: [project-slug]
title: "[Clip title for ClickUp]"
format: reel
lane: personal
pillar: [from content-pillars.md]
production_format: call-clip-edit
discoverability: both
length_target: 150s
status: in-review
source:
  type: call
  recording: [fathom base url]
  timestamp_start: "MM:SS"
  timestamp_end: "MM:SS"
clickup_task_id:
os_script_path:
splinters: []
---
```

## Clip brief body (anchor — phase 1)

```markdown
# 01 — Anchor: [Short Title]

## Hook (on-screen + open line)

**Text overlay:** `[5–8 words]`

**Reframed open (caption or VO intro if needed):**
> [One sentence — audience pain or contrarian frame]

## Thesis

[One clip, one tactic — 2–3 sentences]

## Source segments (use in order)

| Order | Fathom | Topic | Cut notes |
|-------|--------|-------|-----------|
| 0 *(optional)* | [MM:SS](url?timestamp=SECS)–MM:SS | [Cold open] | [trim notes] |
| 1 | [MM:SS](url?timestamp=SECS)–MM:SS | [Core segment] | **Strong open candidate** |

## Cut list — REMOVE

- [Interjection / repetition / bleed into next clip]
- [Names to genericize if reframing for public]

## Key lines to preserve

- "[Verbatim quote worth keeping]"
- "[Verbatim quote]"

## Caption angle

**IG caption draft:**
\`\`\`
[Hook line]

[Body — 3–5 short paragraphs]

[CTA — save/share]

#hashtags
\`\`\`

## Phase 2 — Shorts (deferred)

| ID | Idea |
|----|------|
| 01a | [Short from this clip] |

## Editor notes

- Open with hook text in first 2s
- Jump cuts on pauses; no b-roll required (call footage)
- Captions: full burn-in; bold **[key terms]**
- End on [specific beat] — hard cut
- Export 9:16; optional 1:1 crop for feed

## Full script

→ *(pending structure approval)*
```

## ClickUp task description (call-clip-edit)

**Single video:** one standalone task — full brief below, **zero subtasks**.

**Multi-clip project:** one **subtask per clip** under parent `PROJECT — [title]`.
Parent holds OS link + publish sequence only; clip brief goes on the subtask.

Use when running `/push-clip`:

```markdown
## Hook
[From clip brief]

## Thesis
[From clip brief]

## Source segments (edit in this order)
| Order | Link | Topic | Cut notes |
|-------|------|-------|-----------|
| 1 | [Fathom](url?timestamp=SECS) | ... | ... |

## Cut list — REMOVE
- ...

## Key lines to preserve
- "..."

## Editor notes
- ...

## Links
- OS clip: docs/content-engine/personal/projects/[slug]/clips/[file].md
- Recording: [Fathom URL]
- Raw footage: [optional Drive/Frame.io]
```

## Fathom timestamp helper

Convert `MM:SS` → seconds for `?timestamp=`:

- `11:10` → `670` (`11*60 + 10`)
- Link format: `https://fathom.video/share/{id}?timestamp={seconds}`
