---
name: client-playbook-creator
description: >
  Interviews, drafts, and stores new client playbooks in Waiz Media OS with correct layers
  (canonical, execution, course material), OS dedup, methodology linking, catalog sync, and
  optional knowledge-base updates. Use when the user wants to create, rebuild, or split a
  client playbook, client training module, or course material doc. Triggers: create client
  playbook, new playbook, rebuild playbook, playbook for clients, course material, split
  playbook, playbook-lead-nurture style, rm-ad-playbook refactor.
---

# Client Playbook Creator

Orchestrates **new client playbook creation** from idea → stored artifacts. For catalog rules and paths only, see [client-playbooks](../client-playbooks/SKILL.md). For internal team SOPs (non-client), use [sop-builder](../sop-builder/SKILL.md).

## Assets (read before building)

| Asset | Path |
|-------|------|
| Format spec | [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md) |
| Template | [client-playbook-template.md](../../docs/templates/client-playbook-template.md) |
| Reference playbook | [playbook-lead-nurture.md](../../docs/client-fulfillment/client-marketing/playbook-lead-nurture.md) |
| Catalog | [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) |
| Methodology pools | [catalog.yaml](../../docs/client-fulfillment/client-playbooks/catalog.yaml) |
| Discovery questions | [discovery-questions.md](discovery-questions.md) |
| Examples | [examples.md](examples.md) |

## Modes

| Mode | When |
|------|------|
| **Interview** | User has a topic but not enough detail — ask one question at a time ([discovery-questions.md](discovery-questions.md)) |
| **Build** | User gave topic + references + enough context — pre-flight, then write |
| **Split** | Existing monolith (e.g. `rm-ad-playbook.md`) → canonical + execution + optional course material |

Default to **Interview** unless the user pasted a full outline or said "just build it."

---

## Phase 0 — Intake (always)

Before writing, state:

```
Playbook: [title]
Layers: [canonical / + execution / + course material]
Path(s): [planned file paths]
Reference: [playbook-lead-nurture or other]
```

If paths or layers are unclear, start Interview mode.

---

## Phase 1 — OS pre-flight (before draft)

1. Read [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) — duplicate topic?
2. Check [duplicate-resolutions.md](../../docs/_inventory/duplicate-resolutions.md) if converting from Drive export
3. Grep `docs/client-fulfillment/` for similar filenames/topics
4. Read [catalog.yaml](../../docs/client-fulfillment/client-playbooks/catalog.yaml) → `methodology_pools` — what to link, not rewrite
5. Read [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md) + skim reference playbook

**Outcome:** "No duplicate — creating `[path]`" OR "Updating `[path]`" OR "Splitting `[path]` into …"

---

## Phase 2 — References (when user provides material)

Accept:

- Pasted notes or outline in chat
- Repo paths (`docs/…`, existing playbooks)
- `waiz-os-archive/waiz-drive-export/` `.docx` → [docx](../docx/SKILL.md)
- URLs (fetch if needed; do not store full transcripts in OS)

**Rules:**

- Extract **framework, rules, decisions** into canonical playbook
- Extract **long copy, scripts, checklists** into separate **execution** doc
- Extract **teaching narrative** into **course material** only
- Never paste 500+ lines into one file when layers apply

---

## Phase 3 — Layer decision

| Layer | Folder | Filename pattern | Contains |
|-------|--------|------------------|----------|
| Canonical | `client-marketing/`, `media-buying/`, `client-success/`, `onboarding/` | `playbook-{topic}.md` | North star, scope, framework, rules, metrics, links |
| Execution | Same domain folder | `{topic}-*.md`, `*-sop.md`, existing names | Copy libraries, GHL steps, scripts |
| Course material | `course-material/` | `{topic}-course-material.md` or descriptive | Why, checklist, links — no duplicate ops copy |
| Client instance | `client-marketing/clients/` | `{client-slug}-{topic}.md` | Delta only |

Confirm with user if execution doc is needed (any doc expected to exceed ~200 lines of copy/steps).

---

## Phase 4 — Write

1. Use [client-playbook-template.md](../../docs/templates/client-playbook-template.md) for canonical
2. Match section order in [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md)
3. Set frontmatter: `artifact_type: playbook`, `content_layer: canonical`, `audience`, `product`, `delivery_group`, `methodology_sources`
4. `status: draft` unless user approves `active`
5. Link compliance: [rm-compliance-guardrails.md](../../docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when client copy involved
6. Course material: `content_layer: course-material`, `canonical_parent:` → canonical path

---

## Phase 5 — Post-build (required)

1. Run from repo root:
   ```bash
   python scripts/sync-client-playbooks.py
   ```
2. Confirm new entries in [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md)
3. **Methodology ask** — if reusable technique is new, ask verbatim:

> I used **[technique]** in this playbook, but it is not in the knowledge base yet. Should I update **[candidate doc(s)]**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)

4. **Knowledge capture** — if references contained distillable value (frameworks, objections, hooks), offer [knowledge-capture](../knowledge-capture/SKILL.md) per [routing-table.md](../knowledge-capture/routing-table.md). **Never auto-update compliance docs.**
5. Return summary:

```
Created: [paths]
Layers: [canonical | execution | course material]
Status: draft
Linked methodology: [list]
Gaps / open questions: [list]
Catalog synced: yes
```

6. If `status: active` and team needs Drive copy → offer [team-doc-publish](../team-doc-publish/SKILL.md)

---

## Split mode (legacy monoliths)

For bloated playbooks (e.g. `rm-ad-playbook.md`):

1. Propose split: canonical strategy doc + keep execution content in place or new execution doc
2. Do **not** delete original until user approves — add "Superseded by" links or migrate in place
3. Follow same post-build sync + methodology ask

See [examples.md](examples.md).

---

## Operating rules

- **One interview question at a time** in Interview mode
- **Link, don't duplicate** — methodology lives in pools and linked docs
- **GitHub `docs/` is source of truth** — course material and Drive are downstream
- **Do not invent owners, metrics targets, or pricing** — use `[TO FILL]` or open questions
- Client playbooks ≠ Waiz acquisition docs — [waiz-vs-client-marketing-boundaries.md](../../docs/client-fulfillment/waiz-vs-client-marketing-boundaries.md)

## Related skills

| Skill | When |
|-------|------|
| [client-playbooks](../client-playbooks/SKILL.md) | Catalog, pools, placement reference |
| [sop-builder](../sop-builder/SKILL.md) | Internal team SOPs only |
| [waiz-business-os](../waiz-business-os/SKILL.md) | Repo structure, migration |
| [docx](../docx/SKILL.md) | Drive export `.docx` |
| [knowledge-capture](../knowledge-capture/SKILL.md) | Distill references into OS |
| [copywriting](../copywriting/SKILL.md) | Client-facing copy quality |
| [team-doc-publish](../team-doc-publish/SKILL.md) | Team Google Drive publish |
