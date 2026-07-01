---
title: "[Topic] Playbook"
domain: client-fulfillment
owner: client-success
status: draft
last_updated: YYYY-MM-DD
review_cycle: quarterly
shareability: lo-course   # lo-course | paying-client | internal-fulfillment
artifact_type: playbook
audience:
  - client
  - team
content_layer: canonical
product: reverse-mortgage
delivery_group: general
methodology_sources:
  - docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md
delivery:
  - github
  - course-material
  - team-drive
---

# [Topic] Playbook

> **North star:** [One sentence — the outcome this playbook exists to produce.]

## Purpose

[Why this playbook exists — strategic layer only. Execution copy lives in linked docs.]

## Scope

| Included | Excluded |
|----------|----------|
| [What this doc covers] | [What lives elsewhere — link to doc] |

## Owner

[Role accountable for maintaining and executing.]

## Trigger

Use this playbook when:

- [Event or condition]
- [Another trigger]

## Inputs

- [Required access, data, or prior setup]

## Outputs

- [Definition of done / exit conditions]

## [Core framework name]

[The mental model — pillars, stages, principles. Use tables where helpful.]

---

## [System name] (execution order)

[Optional mermaid diagram]

| Stage | Doc | Owner |
|-------|-----|-------|
| [Stage] | [Link to execution doc](path.md) | [Role] |

---

## Decision rules

| Condition | Action |
|-----------|--------|
| [If X] | [Then Y] |

## Quality bar

- [Standard]
- Compliance: [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Metrics

| Metric | Target direction | Notes |
|--------|------------------|-------|
| [Metric] | [Up/down/stable] | [Context] |

## Related docs

### Methodology (from OS)

| Doc | What we reuse |
|-----|----------------|
| [Doc](path.md) | [One line] |

### Execution (do not duplicate here)

| Doc | Role |
|-----|------|
| [Doc](path.md) | [Primary execution — copy, GHL, etc.] |

### Course material (client education)

| Doc | Role |
|-----|------|
| [Doc](../course-material/example.md) | Client-facing teaching layer |

## Open questions

- [ ] [Unresolved item for owner]

---

**Reference example:** [playbook-lead-nurture.md](../client-fulfillment/client-marketing/playbook-lead-nurture.md) · **Format spec:** [PLAYBOOK-FORMAT.md](../client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md)

**After saving:** `python scripts/sync-client-playbooks.py`

**Course material:** create thin wrapper in `course-material/` with `canonical_parent:` pointing here — see [PLAYBOOK-FORMAT.md](../client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md).
