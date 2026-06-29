---
title: ClickUp — Personal Brand Pipeline
domain: content-engine
owner: founder
status: draft
last_updated: 2026-06-24
review_cycle: quarterly
artifact_type: playbook
---

# ClickUp — Personal Brand Pipeline

**Purpose:** Execution layer for @gabeegoertzen personal brand content. Wm-os
holds scripts and KB; ClickUp holds production tasks, editor handoffs, and
publish tracking.

**Trigger:** Gabe approves a script or says "create ClickUp project" / `/push-clickup`.

**Scope:** Personal lane only. Client fulfillment ads → [Ad Creative Pipeline](https://app.clickup.com/9013498820/v/l/li/901327426635).
Waiz business organic → future list (not built yet).

## System of record

| Layer | System | Contents |
|-------|--------|----------|
| Knowledge + scripts | Wm-os `docs/content-engine/personal/` | Voice, hooks, angles, dated scripts |
| Repurpose structure | Wm-os `personal/projects/` | PROJECT.md + clip briefs — [lifecycle](personal/projects/lifecycle.md) |
| Production + editor | ClickUp **Personal Brand Pipeline** | Status, assignee, asset links; subtasks = clips only in multi-clip projects |
| Published archive | `wm-content-archive/published/` (sibling, not git) | Post metadata after go-live |

## ClickUp location

| Item | Value |
|------|-------|
| Space | Creative (`90139913737`) |
| List | **Personal Brand Pipeline** |
| List ID | `901327607346` |
| List URL | https://app.clickup.com/9013498820/v/l/li/901327607346 |

### Template tasks (duplicate to start)

| Task | ID | URL |
|------|-----|-----|
| START HERE — Personal Brand Pipeline | `86aj46c9v` | https://app.clickup.com/t/86aj46c9v |
| [TEMPLATE] New Content — duplicate me | `86aj46cdn` | https://app.clickup.com/t/86aj46cdn |
| [EXAMPLE] Reel — beat-timed script | `86aj46cj0` | https://app.clickup.com/t/86aj46cj0 |

## Rule: one task = one video

Move work forward by changing **status** (board columns). Never create subtasks
for edit **directions** (captions, assembly, export, sound mix, etc.) — those
belong in the task **description** under `## Editor notes`.

### Single video (default)

One piece of content = **one ClickUp task, zero subtasks.**

| Source | ClickUp shape |
|--------|---------------|
| `/push-clickup` — one filmed script | Standalone task; full script + editor notes in description |
| `/push-clip` — one clip, or project with **1 main** only | Standalone task; full clip brief in description |

The editor owns the whole deliverable in that one task.

### Multi-clip project

When a repurpose project has **2+ main clips** (see `PROJECT.md` phase 1 table):

| Level | Task | Subtasks |
|-------|------|----------|
| **Parent** | `PROJECT — [call title]` | Container only — OS link, Fathom, publish sequence. **No edit directions.** |
| **Child** | — | **One subtask per video/clip** — each subtask description = full clip brief (hook, segments, cut list, editor notes) |

Push clip 01 → create parent (if missing) + subtask for clip 01. Push clip 02
later → add **one** new subtask under same parent. Never split one video across
multiple subtasks.

Phase 2 splinter shorts (after main published): same rule — **one subtask per
short video**, not per edit step.

### Never create these subtasks

Do not use subtasks for workflow steps:

- Assembly + rough cut
- Captions / subtitles
- Export ratios
- Sound mix
- Final export + upload
- Design slides / Write caption (carousel steps)

Put all of that in `## Editor notes` on the **single task** (or the **clip
subtask** in a multi-clip project).

## Statuses

Configure these as list statuses in ClickUp (replace defaults):

| Status | Owner | What happens |
|--------|-------|--------------|
| Backlog | Gabe | Idea captured; no script yet |
| Scripting | Gabe | Full script in Wm-os |
| Ready to Film | Gabe | Script approved; filming scheduled |
| Filming | Gabe | Raw footage capture |
| Ready to Edit | Editor | Footage uploaded |
| Editing | Editor | Cut, captions, assembly |
| In Review | Gabe | Proofing + comments |
| Revisions | Editor | Rework; bump `Revision #` |
| Approved | — | Signed off; ready to post |
| Published | — | Live on @gabeegoertzen |
| Killed | — | Trial/idea abandoned |

Trial concepts may enter at **Backlog** or **Ready to Film** with Format =
`trial-concept`.

### Approval loop

1. Editor moves to **In Review**.
2. Gabe reviews via Proofing + comments.
3. Changes → **Revisions** + increment `Revision #`.
4. Editor reworks → **In Review** again.
5. Clean → **Approved** → post → **Published**.

## Custom fields

ClickUp fields = **production execution only**. Ideation metadata (pillar,
discoverability, belief/story refs) stays in Wm-os `angle-library.md` and script
frontmatter — not duplicated as ClickUp fields.

Add these fields on the list in ClickUp UI:

| Field | Type | Values |
|-------|------|--------|
| Format | Dropdown | `reel`, `carousel`, `trial-concept` |
| Length Target | Dropdown | `15s`, `30s`, `60s` |
| Platform | Labels | `Instagram`, `TikTok`, `YouTube Shorts` |
| Script Date | Date | ISO date from script filename |
| OS Script Path | URL | Path to Wm-os script file |
| Source Idea | Short text | `angle-library` title (optional) |
| Revision # | Number | Default `0`; bump on Revisions |
| Raw Footage Link | URL | Drive / Frame.io |
| Final Asset Link | URL | Exported file |
| Publish Date | Date | When live |

## Views

Create in ClickUp after statuses and fields exist:

| View | Type | Filter / group |
|------|------|----------------|
| Pipeline | Board | Group by status (default) |
| Film This Week | List | Status ∈ Ready to Film, Filming; sort by due date |
| Editor Queue | List | Status ∈ Ready to Edit, Editing, Revisions |
| Needs My Review | List | Status = In Review |
| Publish Calendar | Calendar | Group by Publish Date |
| Trials | Table | Format = trial-concept |
| All Content | Table | All fields visible |

## Task description format

Parent task description = full script for the editor. Agents build this from
[`_templates.md`](_templates.md) / [`format-templates.md`](../../.claude/skills/content-engine/format-templates.md).

### Reel / trial

```markdown
## Hook
[spoken hook]

## Script (timed)
| Time | Visual | Line |
|------|--------|------|
| 0:00-0:03 | [VISUAL: ...] | [LINE: ...] |

## CTA
...

## Editor notes
- Captions: ...
- Music: ...
- Cut pace: ...

## Links
- OS script: [path]
- Raw footage: [url]
```

### Carousel

Replace beat table with slide blocks from carousel template (`slides` frontmatter).
Slide design, export, and caption direction → `## Editor notes` on the **one**
task (zero subtasks unless part of a multi-clip project parent).

## Field mapping (script → ClickUp)

When pushing via `/push-clickup`, map script frontmatter to custom fields:

| Script frontmatter | ClickUp field |
|--------------------|---------------|
| `format` | Format |
| `length_target` | Length Target |
| (user specifies) | Platform |
| `date` | Script Date |
| file path | OS Script Path |
| `source_idea` | Source Idea |
| — | Revision # → `0` on create |
| (user provides) | Raw Footage Link |
| — | Final Asset Link (empty until export) |
| — | Publish Date (empty until published) |

Belief/story refs and discoverability: include in task description if present in
script; do not create ClickUp fields for them.

## ClickUp ID registry

Agents use UUIDs for dropdown custom field values. **Backfill this section after
adding custom fields in ClickUp UI** — run `clickup_get_custom_fields` with
`list_id: 901327607346`.

```yaml
# Last synced: 2026-06-18 — custom_fields empty until added in ClickUp UI
list_id: "901327607346"
space_id: "90139913737"
list_url: "https://app.clickup.com/9013498820/v/l/li/901327607346"
template_tasks:
  start_here: "86aj46c9v"
  new_content: "86aj46cdn"
  example_reel: "86aj46cj0"
custom_fields: {}  # run clickup_get_custom_fields after UI setup
dropdown_options: {}  # map Format + Length Target option UUIDs after UI setup
```

**Re-sync:** After adding custom fields in ClickUp, ask an agent to run
`clickup_get_custom_fields` with `list_id: 901327607346` and update this block.

> `clickup_get_list` may error on this workspace (MCP schema mismatch). Use
> `clickup_get_custom_fields` + `clickup_filter_tasks` instead.

## Manual setup checklist

Complete in ClickUp UI (MCP cannot create statuses, fields, or views):

1. [ ] Open [Personal Brand Pipeline](https://app.clickup.com/9013498820/v/l/li/901327607346)
2. [ ] Replace default statuses with the 11 statuses above
3. [ ] Add 9 custom fields (table above)
4. [ ] Create 7 views
5. [ ] Pin Pipeline board as default view
6. [ ] Run agent `/push-clickup` test or ask agent to backfill ID registry

## Agent command

See [content-engine skill](../../.claude/skills/content-engine/SKILL.md) →
`/push-clickup`. Lane must be `personal`; business organic returns "not set up
yet".

## Related lists (do not use for new personal work)

| List | ID | Use |
|------|-----|-----|
| Factory | `901312805332` | **Frozen** — legacy mixed personal/business |
| Ad Creative Pipeline | `901327426635` | Client + Waiz **paid** ads |
| RM Library / WM Library | — | Launched ad inventory only |

## Related

- [INFRASTRUCTURE.md](INFRASTRUCTURE.md) — phases, script paths
- [LANE-BOUNDARIES.md](LANE-BOUNDARIES.md) — personal vs business
- [repurposing/reels-to-ads-engine.md](repurposing/reels-to-ads-engine.md) — organic → ads handoff
