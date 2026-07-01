# Client Playbook Format

Gold-standard structure for client playbooks. **Reference implementations:**

- **Principles:** [playbook-nurture-framework.md](../client-marketing/playbook-nurture-framework.md) — flow-agnostic rules
- **Application:** [playbook-lead-nurture.md](../client-marketing/playbook-lead-nurture.md) — Waiz Meta stack (links to framework; no duplicate principles)

Use this doc when creating playbooks so future ones stay consistent.

---

## Default: single client playbook

**New client playbooks** should be **one file** unless the topic includes a **long standalone script** (full sales call, drip sequence, call-center script).

| In the playbook | Separate doc only when |
|-----------------|------------------------|
| North star, framework, decision rules | Full word-for-word call script (200+ lines) |
| Usable lines — questions, smoke screens, short pitch weaves | Drip/SMS copy libraries |
| Metrics, related links | GHL step-by-step build docs |

**Team/universal frameworks** → `docs/acquisition/sales/` (e.g. [conceptual-beliefs-framework.md](../../acquisition/sales/conceptual-beliefs-framework.md)). Product playbooks link and add product-specific lines.

**Do not create** by default: `{topic}-question-bank.md`, `{topic}-education.md`, or `course-material/` wrappers for the same topic.

---

## Three layers (lead nurture — legacy exception)

When a topic has both **universal principles** and a **Waiz-specific implementation**, split across docs — never maintain two copies of the same rules.

| Layer | Doc pattern | Contains | Example |
|-------|-------------|----------|---------|
| **Framework** | `playbook-{topic}-framework.md` | Why, mental models, universal rules, backlinks | `playbook-nurture-framework.md` |
| **Application** | `playbook-{topic}.md` | How Waiz runs one flow (GHL, phases, metrics) | `playbook-lead-nurture.md` (Meta stack) |
| **Execution** | `*-drip*.md`, `*-script.md`, `*-sop.md` | Copy, steps, word tracks | `10-day-rm-drip-campaign.md` |

**Course material** teaches from the **framework** first; Waiz DFY automation belongs in a **gated appendix** (`paying-client` only) — never in the prospect LO course body.

---

## Shareability (required)

Every playbook, course module, and execution doc must declare who may see it. Full doctrine: [shareability-boundaries.md](../shareability-boundaries.md).

| Tier | LO course (non-clients)? | Use for |
|------|--------------------------|---------|
| `lo-course` | **Yes** | Frameworks, generic LO skills, RM education |
| `paying-client` | **No** | Waiz application playbooks, client portal modules |
| `internal-fulfillment` | **No** | GHL builds, drip copy, bot specs, MB/onboarding SOPs |

**Frontmatter:**

```yaml
shareability: lo-course   # lo-course | paying-client | internal-fulfillment
```

**Defaults by layer:**

| Layer | Default |
|-------|---------|
| `playbook-*-framework.md` | `lo-course` |
| `playbook-*.md` (application) | `paying-client` |
| `course-material/` (prospect course) | `lo-course` |
| Drip copy, GHL steps, `crm-architecture/` | `internal-fulfillment` |

Before publishing course material, run [SHAREABILITY-CHECKLIST.md](SHAREABILITY-CHECKLIST.md).

---

## Overlap check (required before saving)

Before adding or expanding any playbook section, ask:

1. **Does this principle already exist** in a framework, doctrine, or methodology pool doc? → **Link**, don't rewrite.
2. **Does another playbook in the same `delivery_group` cover this?** → Grep [catalog.md](catalog.md) and consolidate.
3. **Is this Waiz-flow-specific or universal?** → Universal → framework; GHL/Meta/bot → application playbook.
4. **Would course material repeat canonical copy?** → One-line summary + link only.

**Flag overlaps to the owner** when building — propose merge, split, or link before duplicating content.

---

## Two layers (always)

| Layer | Folder | Contains |
|-------|--------|----------|
| **Canonical playbook** | `client-marketing/`, `client-sales/`, `media-buying/`, etc. | System, rules, frameworks, links to execution |
| **Course material** | `course-material/` | Client education only — why, mental model, checklist, links |

Never put full copy libraries or GHL step lists in both places.

---

## Canonical playbook sections (in order)

1. **Frontmatter** — see [template](../../templates/client-playbook-template.md)
2. **Title + North star** — one blockquote with the single outcome
3. **Purpose** — why this exists (1–2 sentences)
4. **Scope** — included / excluded table (link out excluded items)
5. **Owner** — role accountable
6. **Trigger** — when to use this playbook
7. **Inputs** — what's required before starting
8. **Outputs** — definition of done / exit conditions
9. **Core framework** — the "how to think" (pillars, stages, principles)
10. **System / process** — diagram + table linking to execution docs
11. **Decision rules** — if/then table
12. **Quality bar** — bullets + compliance link
13. **Metrics** — what to measure (link KPI doc if formal)
14. **Related docs** — split: Methodology | Execution | Course material
15. **Open questions** — unchecked items for owner

---

## Course material sections (in order)

1. **Frontmatter** — `content_layer: course-material`, `canonical_parent:` required
2. **Banner** — link to canonical playbook
3. **What you'll understand** — 3–5 bullets
4. **Concept / story** — teach the why (leaky bucket, framework summary)
5. **How Waiz runs it** — simple flow (text or diagram)
6. **Client checklist** — what the LO must do
7. **Go deeper** — table linking to canonical + execution docs
8. **Optional:** key stats or examples (brief)
9. **Related** — hub links

**Max length target:** 1–2 screens of teaching; no duplicated copy from execution docs.

---

## Frontmatter (canonical)

```yaml
shareability: lo-course          # lo-course | paying-client | internal-fulfillment
artifact_type: playbook
audience: [client, team]
content_layer: canonical
product: reverse-mortgage
delivery_group: lead-nurture
is_reference_playbook: true   # only on gold-standard examples
methodology_sources: [...]
delivery: [github, course-material, team-drive]
```

Course material frontmatter must include `shareability: lo-course` unless the module is **paying-client portal only**.

---

## Filename convention

`playbook-{topic}.md` in the workflow folder (e.g. `playbook-lead-nurture.md`).

Course material: keep descriptive name (`lead-nurture-playbook.md`) or `{topic}-course-material.md`.

---

## After creating

```bash
python scripts/sync-client-playbooks.py
```

Verify entry in [catalog.md](catalog.md).

---

## Related

- [Template](../../templates/client-playbook-template.md)
- [Client Playbooks README](README.md)
- [client-playbook-creator skill](../../.claude/skills/client-playbook-creator/SKILL.md)
- [client-playbooks skill](../../.claude/skills/client-playbooks/SKILL.md)
