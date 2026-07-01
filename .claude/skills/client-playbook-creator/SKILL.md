---
name: client-playbook-creator
description: >
  Interviews, drafts, and stores new client playbooks in Waiz Media OS with correct layers
  (canonical, execution, course material), OS dedup, methodology linking, catalog sync, and
  optional knowledge-base updates. Enforces shareability — never link internal fulfillment
  processes in lo-course frameworks or course material. Use when the user wants to create,
  rebuild, or split a client playbook, client training module, or course material doc.
  Triggers: create client playbook, new playbook, rebuild playbook, playbook for clients,
  course material, split playbook, playbook-lead-nurture style, rm-ad-playbook refactor.
---

# Client Playbook Creator

Orchestrates **new client playbook creation** from idea → stored artifacts. For catalog rules and paths only, see [client-playbooks](../client-playbooks/SKILL.md). For internal team SOPs (non-client), use [sop-builder](../sop-builder/SKILL.md).

## Assets (read before building)

| Asset | Path |
|-------|------|
| Format spec | [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md) |
| Template | [client-playbook-template.md](../../docs/templates/client-playbook-template.md) |
| Reference playbook | [playbook-nurture-framework.md](../../docs/client-fulfillment/client-marketing/playbook-nurture-framework.md) (principles) · [playbook-lead-nurture.md](../../docs/client-fulfillment/client-marketing/playbook-lead-nurture.md) (Waiz Meta application) |
| Catalog | [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) |
| Shareability | [shareability-boundaries.md](../../docs/client-fulfillment/shareability-boundaries.md) |
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
Path: [single client playbook path — or split only if long script]
Reference: [existing framework or playbook to link]
Product: [reverse-mortgage | dscr | general]
```

Default is **one client playbook file**. Only plan additional paths when the topic includes a **long standalone script** (full sales call, drip sequence, call-center script).

If scope is unclear, start Interview mode.

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

- **Default:** one client playbook with framework, decision rules, and **usable lines/questions inline**
- **Split to a separate doc only** when content is a **long script** reused on its own — full sales call scripts, drip/SMS copy libraries, call-center scripts, GHL step lists (~200+ lines of script-only copy)
- **Universal team frameworks** → `docs/acquisition/sales/` (or methodology pool) — product playbooks **link**, don't duplicate the universal model
- **Do not create** separate question banks, course-material wrappers, or execution docs for the same training topic unless the user explicitly asks
- Never paste 500+ lines of drip/script copy into a playbook when a dedicated script doc already exists or is needed

---

## Phase 3 — Layer decision

**Default (most client playbooks):**

| What | Where | Contains |
|------|-------|----------|
| **Client playbook** | `client-marketing/`, `client-sales/`, `media-buying/`, etc. | `playbook-{product}-{topic}.md` or `playbook-{topic}.md` — north star, framework, **inline lines**, decision rules, metrics, links |
| **Team framework** (when reusable across products) | `docs/acquisition/sales/` | Product-agnostic mental model — client playbook links here |

**Split to separate doc only when:**

| Type | Pattern | Example |
|------|---------|---------|
| Long sales script | `script-*.md`, `*-call-script.md` | `discovery-call-script-2026.md` |
| Drip / copy library | `*-drip*.md`, `*-script.md` | `10-day-rm-drip-campaign.md` |
| Call-center script | `call-center/script-*.md` | Appointment-setting script |

**Do not create by default:** `{topic}-question-bank.md`, `{topic}-education.md`, or `course-material/` wrappers for the same topic as the playbook.

**Legacy / exception — nurture stack only:** [playbook-nurture-framework.md](../../docs/client-fulfillment/client-marketing/playbook-nurture-framework.md) + [playbook-lead-nurture.md](../../docs/client-fulfillment/client-marketing/playbook-lead-nurture.md) + drip execution docs pre-date this rule; new topics follow single-playbook default.

| Layer | Folder | Filename pattern | When |
|-------|--------|------------------|------|
| Framework (team) | `docs/acquisition/sales/` | `*-framework.md` | Universal model for Waiz team + linked from product playbooks |
| Client playbook | `client-marketing/`, `client-sales/`, etc. | `playbook-{topic}.md` | **Default** — one file with inline lines |
| Long script | Same domain or `call-center/` | `script-*.md`, `*-drip*.md` | Only when script stands alone at length |
| Client instance | `client-marketing/clients/` | `{client-slug}-{topic}.md` | Per-client delta only |

Do **not** ask to split unless the draft exceeds ~200 lines of **script-only** copy that should live in its own referenced doc.

---

## Phase 3b — Shareability gate (required before write)

Read [shareability-boundaries.md](../../docs/client-fulfillment/shareability-boundaries.md).

1. Ask (if not clear): **Is this for prospect LO course, paying DFY clients, or Waiz team only?**
2. Set `shareability:` on every file you create.
3. **Prospect LO course material:** link only `lo-course` docs in sections 1–4; put Waiz DFY context in a labeled appendix or separate `paying-client` module.
4. Run [SHAREABILITY-CHECKLIST.md](../../docs/client-fulfillment/client-playbooks/SHAREABILITY-CHECKLIST.md) before marking course material `active`.

| If building… | Default shareability |
|--------------|---------------------|
| Framework / generic LO skill | `lo-course` |
| Waiz Meta stack, client portal | `paying-client` |
| GHL, drip copy, bot, MB SOP | `internal-fulfillment` |

**Forbidden in prospect course body:** links to `crm-architecture/`, `onboarding/a-z`, `media-buying/`, drip execution docs, bot specs.

---

## No internal process links (hard rule)

When `shareability` is **`lo-course`** (frameworks, generic LO playbooks, course material):

**Do not link to Waiz internal fulfillment or DFY execution.** Teach the framework in plain language; name the concept, not our build.

### Never link in `lo-course` doc body, banner, checklist, or "Go deeper"

| Blocked | Why |
|---------|-----|
| `docs/client-fulfillment/crm-architecture/` | Bot specs, tag architecture, infra |
| `docs/client-fulfillment/onboarding/a-z*` | Post-close team runbooks |
| `docs/client-fulfillment/media-buying/` | MB ops, campaign setup SOPs |
| `docs/client-fulfillment/client-success/` | Constraint diagnosis, internal CS |
| `*-drip-campaign.md`, `rm-imessage-intent-drip*` | Executable copy + GHL |
| `how-wm-ai-bot-works.md`, `fulfillment-lead-lifecycle.md` | Waiz engine internals |
| `playbook-*.md` **application** docs (non-`-framework`) | Waiz stack — use `paying-client` appendix instead |
| Any doc with `shareability: internal-fulfillment` or `paying-client` | See [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) → **LO course** section for allowlist |

### Allowed links for `lo-course`

- `playbook-{topic}-framework.md`
- Generic LO skills: dialing, BAMFAM, conceptual beliefs (when tagged `lo-course`)
- `reverse-mortgage-dna/` / `dscr-dna/` education and compliance guardrails
- `docs/acquisition/` when selling Waiz (not fulfillment ops)
- Other docs listed under **LO course — `lo-course` only** in [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md)

### Frontmatter and methodology

- `methodology_sources:` on `lo-course` docs — **only `lo-course` paths**. Do not cite internal SOPs or application playbooks as methodology parents.
- `canonical_parent:` on course material — **framework doc only**, never application or execution.

### If internal detail is needed

1. **Summarize in one sentence** without a link (*"Automation can handle speed-to-lead"*).
2. Or add a **gated appendix** titled *Waiz DFY clients only* linking `paying-client` docs — never `internal-fulfillment` in prospect exports.
3. **Application / execution docs** may link inward to each other — that is expected for team and paying-client tiers.

Before save, grep the draft for blocked path prefixes and remove or move links to an appendix.

---

## Phase 4 — Write

1. Use [client-playbook-template.md](../../docs/templates/client-playbook-template.md) for canonical
2. Match section order in [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md)
3. Set frontmatter: `artifact_type: playbook`, `content_layer: canonical`, `shareability`, `audience`, `product`, `delivery_group`, `methodology_sources`
4. `status: draft` unless user approves `active`
5. Link compliance: [rm-compliance-guardrails.md](../../docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when client copy involved
6. If a universal framework exists or applies → link from `docs/acquisition/sales/`; keep product-specific lines in the client playbook
7. **Inline usable lines** in the playbook (questions, smoke screens, short pitch weaves) — do not spin out question banks for the same topic
8. Course material: `content_layer: course-material`, `shareability: lo-course` (unless paying-client portal), `canonical_parent:` → **framework** path only
9. **Link audit before save** — for `lo-course` files, grep for blocked internal paths (see **No internal process links**); remove or move to gated appendix

---

## Phase 5 — Post-build (required)

1. **Link audit (lo-course only)** — grep new/changed files for blocked internal paths. If any found, remove from main body or move to gated appendix.
2. Run from repo root:
   ```bash
   python scripts/sync-client-playbooks.py
   ```
3. Confirm new entries in [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md)
4. **Methodology ask** — if reusable technique is new, ask verbatim:

> I used **[technique]** in this playbook, but it is not in the knowledge base yet. Should I update **[candidate doc(s)]**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)

4. **Knowledge capture** — if references contained distillable value (frameworks, objections, hooks), offer [knowledge-capture](../knowledge-capture/SKILL.md) per [routing-table.md](../knowledge-capture/routing-table.md). **Never auto-update compliance docs.**
5. Return summary:

```
Created: [path(s)]
Split: [none | long script at path]
Status: draft
Linked methodology: [list]
Gaps / open questions: [list]
Catalog synced: yes
Link audit (lo-course): [pass | N links moved to appendix]
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
- **Overlap check (required)** — before writing, grep [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) and related playbooks in the same `delivery_group`. If principles overlap an existing framework or playbook, **link or consolidate** — flag to the user before duplicating. See [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md#overlap-check-required-before-saving).
- **Framework vs application** — universal rules → `playbook-{topic}-framework.md`; Waiz GHL/bot/flow specifics → application playbook. Course material links frameworks only; never repeats canonical sections.
- **No internal process links** — `lo-course` docs must not link `internal-fulfillment` or `paying-client` paths in lesson bodies. Use [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) **LO course** section as link allowlist.
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
