# Client Playbook Format

Gold-standard structure for client playbooks. **Reference implementation:** [playbook-lead-nurture.md](../client-marketing/playbook-lead-nurture.md).

Use this doc when creating playbooks so future ones stay consistent.

---

## Two layers (always)

| Layer | Folder | Contains |
|-------|--------|----------|
| **Canonical playbook** | `client-marketing/`, `media-buying/`, etc. | System, rules, frameworks, links to execution |
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
artifact_type: playbook
audience: [client, team]
content_layer: canonical
product: reverse-mortgage
delivery_group: lead-nurture
is_reference_playbook: true   # only on gold-standard examples
methodology_sources: [...]
delivery: [github, course-material, team-drive]
```

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
