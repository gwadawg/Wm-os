---
name: editor-project-creator
description: EditorProjectcreator — structures call recordings into personal-brand editor projects (PROJECT.md + clip briefs) and pushes approved clips to ClickUp. Use when the user says EditorProjectcreator, "new editor project", "new repurpose project", "structure this call for the editor", Fathom URL, call transcript, "/new-repurpose-project", "/push-clip", or "/archive-project". Enforces WIP limits and storage rules in lifecycle.md.
disable-model-invocation: true
---

# EditorProjectcreator

Turn coaching/demo calls into editor-ready clip projects. **Personal lane only**
(@gabeegoertzen). Wm-os holds structure; ClickUp holds production.

## Before any task

1. Read [lifecycle.md](../../../docs/content-engine/personal/projects/lifecycle.md) — storage layers, WIP limits
2. Read [projects/README.md](../../../docs/content-engine/personal/projects/README.md)
3. Read [templates.md](templates.md)
4. Load `personal-brand-dna.md` + `format-library.md` (`call-clip-edit`)
5. For ClickUp handoff: [clickup-personal-brand-pipeline.md](../../../docs/content-engine/clickup-personal-brand-pipeline.md)

**Gates:**

- No ClickUp push until Gabe approves clip structure (`status: approved`)
- Max **2 active projects** — stop `/new-repurpose-project` if index is full unless Gabe overrides
- No duplicate project for same Fathom URL / Supabase call UUID

## Commands

### `/new-repurpose-project [source]`

**Trigger phrases:** "EditorProjectcreator", "new editor project", "new repurpose
project", "structure this call", "clip this call for the editor"

**Source** (priority order):

1. Fathom share URL — fetch/skim transcript
2. Supabase call UUID — pull via [knowledge-capture](../knowledge-capture/SKILL.md) + [call-intelligence-bridge](../../../docs/operations/call-intelligence-bridge.md)
3. User-pasted transcript + optional timestamps

**Steps:**

1. **Spot-check** — build timestamp table: Use / Skip / Optional cold open.
   Skip sales pitch, pricing, rapport, internal ops unless user says otherwise.
2. **Propose main clips** (phase 1 only) — 90s–3min anchors. Queue shorts in
   PROJECT.md phase-2 table; do **not** create `01a` files yet.
3. **Slug** — `kebab-case` + date hint, e.g. `second-voicing-june-2026`
4. **Scaffold** (templates in [templates.md](templates.md)):
   ```
   docs/content-engine/personal/projects/[slug]/
   ├── PROJECT.md
   └── clips/
       └── 01-anchor-[topic].md    ← full detail for clip 01 only
   ```
   Clips 02+ appear in PROJECT.md table; create clip files when that clip becomes current.
5. **Clip 01 body** — fixed section order: Hook → Thesis → Source segments →
   Cut list REMOVE → Key lines → Caption angle → Phase 2 shorts table → Editor notes
6. **Update** Active projects table in `projects/README.md`
7. **Return** — slug, clip count, clip 01 path, review ask

Do **not** push to ClickUp in this command.

### `/push-clip [clip-path]`

**Trigger phrases:** "push clip to editor", "push to ClickUp", after structure approval

**Use for:** `call-clip-edit` clip briefs under `personal/projects/*/clips/`.
For beat-timed filmed scripts → [content-engine `/push-clickup`](../content-engine/SKILL.md).

**Prerequisites:**

- Clip `status` is `approved` or Gabe explicitly says push despite `in-review`
- `clickup_task_id` empty (or user wants a new task)

**Ask Gabe each time:**

- Editor assignee — `clickup_resolve_assignees` (no default)
- Due date (optional)
- Starting status: `Ready to Edit` (default for call clips) or `Scripting`
- Raw footage URL (optional — Fathom link often sufficient)

**Steps:**

1. Load clip brief + parent `PROJECT.md`; confirm `production_format: call-clip-edit`
2. Count **main clips** in PROJECT.md phase 1 table
3. Build `markdown_description` (call-clip variant):
   Hook → Thesis → Source segments table → Cut list REMOVE → Key lines →
   Editor notes → Links (Fathom, OS clip path, footage URL)
4. **Single video** (1 main in project, or no project context):
   - `clickup_create_task` on list `901327607346` — standalone task
   - **Zero subtasks** — full direction on this task
5. **Multi-clip project** (2+ mains in PROJECT.md):
   - Create parent `PROJECT — [title]` on list if `PROJECT.md` has no ClickUp link yet
     (description: OS path, Fathom, publish sequence only — no clip edit directions)
   - `clickup_create_task` with `parent` = parent task ID — **one subtask = this clip**
   - Full clip brief in **subtask** description (not split across subtasks)
6. Set `name`, `status`, `custom_fields`, `due_date`, `assignees` on the task
   that owns the clip (standalone or subtask)
7. Write `clickup_task_id` + task URL into clip frontmatter; set `status: scripted`
8. Return task URL (and parent URL if multi-clip)

**Never** create workflow subtasks (Assembly, Captions, Export ratios, Sound mix,
Final export). One video = one task or one clip-subtask.

### `/add-clip [project-slug]`

Add the next main clip file when Gabe moves to clip 02+. Copy clip 01 pattern;
update PROJECT.md status column. Do not create splinter (`01a`) files until parent
main is `published`.

### `/archive-project [slug]`

**Trigger:** All mains published, project killed, or Gabe says archive.

1. Follow [lifecycle.md](../../../docs/content-engine/personal/projects/lifecycle.md) completion workflow
2. Set PROJECT.md `status: completed` or `archived`
3. Move row Active → Completed in `projects/README.md`
4. Offer optional KB distill (`project:[slug]:clip-id` source) — default skip
5. Do not delete project folder

## Storage rules (summary)

| Layer | System | OS stores |
|-------|--------|-----------|
| Raw | Supabase / Fathom | Links + timestamps only — never full transcript |
| Structure | `personal/projects/` | PROJECT.md + **current** clip brief only |
| Production | ClickUp | Status, assignee, assets — not duplicated in OS |
| Reusable KB | hook/angle libraries | Optional distill **after publish** only |
| Publish log | `wm-content-archive/published/` | Post metadata — not git |

Full rules: [lifecycle.md](../../../docs/content-engine/personal/projects/lifecycle.md)

## Quality bar

- **One tactic per main clip** — splittable frameworks, not whole-call dumps
- **Reframe for audience** — speak to camera as "if you're an LO/setter…", not
  "on our call with [name]…"
- **Preserve timestamps** — every segment links Fathom with `?timestamp=` seconds
- **Skip by default** — pricing, affiliate pitch, bootcamp close, sports rapport
- **Phase 2 deferred** — no splinter files until parent main is published
- `production_format: call-clip-edit` on all call-derived clips
- Never store full transcripts in Wm-os — cite `supabase:call:{uuid}` or Fathom URL
- Do not auto-append angle-library on project create — distill only after publish if asked
- Do not create `personal/scripts/` for call-clip-edit unless reshooting filmed

## Related

- [content-engine](../content-engine/SKILL.md) — `/script`, `/push-clickup` for filmed content
- [knowledge-capture](../knowledge-capture/SKILL.md) — transcript pull + KB distillation
- [projects index](../../../docs/content-engine/personal/projects/README.md)
- [lifecycle](../../../docs/content-engine/personal/projects/lifecycle.md) — WIP limits, archive, anti-flood rules
- Examples: `second-voicing-june-2026`, `robert-moore-demo-may-2025`
