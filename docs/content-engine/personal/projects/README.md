---
title: Personal Content — Repurpose Projects
domain: content-engine
owner: founder
status: active
last_updated: 2026-06-24
review_cycle: quarterly
artifact_type: index
---

# Personal Content — Repurpose Projects

**Purpose:** Group call-derived (or long-form) content into a **master project**
with anchor posts + splinter shorts. Wm-os holds **distilled clip structure**
only; ClickUp holds production; Supabase/Fathom holds raw calls.

**Storage rules:** [lifecycle.md](lifecycle.md) — creation gates, WIP limits,
archive workflow. Read before opening a new project.

## When to create a project

- Sales/demo call with dense coaching moments (Gabe educating, not pitching)
- Podcast or interview with splittable frameworks
- Long-form recording planned as anchor + shorts series

## Folder structure

```
projects/[slug]/
├── PROJECT.md          Master index, source, publish sequence
└── clips/
    ├── 01-anchor-[slug].md
    ├── 01a-short-[slug].md
    └── ...
```

## Clip ID convention

| ID | Phase | Type | Typical length |
|----|-------|------|----------------|
| `01`, `02`, … | **1** | Main clip | 90s–3min |
| `01a`, `01b`, … | **2** | Short (from main) | 30–60s — **after main is published** |

## Workflow

Run [EditorProjectcreator skill](../../../../.claude/skills/editor-project-creator/SKILL.md):

1. **`/new-repurpose-project`** — Fathom URL or transcript → spot-check → `PROJECT.md` + clip 01 brief
2. **Approve** — Gabe signs off clip structure (`status: approved`)
3. **`/push-clip`** — ClickUp task per approved clip (zero subtasks if 1 main; one subtask per clip if multi-clip project)
4. **Phase 2** — shorts from published mains only (`/add-clip` for next main when ready)

## Clip brief frontmatter

```yaml
---
clip_id: 01
clip_type: anchor | splinter
parent_clip: null | 01
project: robert-moore-demo-may-2025
title:
format: reel
lane: personal
pillar:
length_target: 180s | 45s
status: in-review | approved | scripted | filmed | published
source:
  type: call
  recording: [fathom url]
  timestamp_start:
  timestamp_end:
clickup_task_id:
os_script_path:
---
```

## WIP limit

**Max 2 active projects.** Before `/new-repurpose-project`, check the table
below. Finish, kill, or `/archive-project` one first. See [lifecycle.md](lifecycle.md).

## Active projects

| Project | Source | Main clips | Status |
|---------|--------|------------|--------|
| [robert-moore-demo-may-2025](robert-moore-demo-may-2025/PROJECT.md) | Robert Moore demo, May 2025 | 6 (01 in review) | phase 1 |
| [second-voicing-june-2026](second-voicing-june-2026/PROJECT.md) | Pedro coaching — second voice, Jun 2026 | 2 (01 ready to edit) | phase 1 |
| [laura-cs-coaching-june-2026](laura-cs-coaching-june-2026/PROJECT.md) | CS coaching w/ Laura — retention framing, Jun 2026 | 10 (01 in review) | phase 1 |

## Completed projects

| Project | Source | Outcome | Archived |
|---------|--------|---------|----------|
| *(none yet)* | — | — | — |

## Related

- [lifecycle.md](lifecycle.md) — storage layers, lazy files, archive, KB distill
- [EditorProjectcreator skill](../../../../.claude/skills/editor-project-creator/SKILL.md) — `/new-repurpose-project`, `/push-clip`, `/archive-project`
- [ClickUp personal brand pipeline](../clickup-personal-brand-pipeline.md)
- [Call intelligence bridge](../../operations/call-intelligence-bridge.md)
- [Scripts output folder](../scripts/README.md)
