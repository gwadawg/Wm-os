---
title: Client Fulfillment — Course Material
domain: client-fulfillment
owner: community-education
status: active
last_updated: 2026-07-01
review_cycle: quarterly
---

# Client Fulfillment — Course Material

Client-facing **education and training** — how we teach loan officers. **Do not treat as the ops source of truth** when a canonical SOP or playbook exists elsewhere.

**Hub:** [Client Playbooks](../client-playbooks/README.md) · **Index:** [catalog.md](../client-playbooks/catalog.md) (auto-sync: `python scripts/sync-client-playbooks.py`)

## Docs in this folder

| Doc | Status | Canonical source |
|-----|--------|------------------|
| [Lead Nurture — Course Material](lead-nurture-playbook.md) | `draft` | [Lead Nurture Playbook](../client-marketing/playbook-lead-nurture.md) |
| [Setting Up Facebook Lead Form](sop-setting-up-facebook-lead-form.md) | `draft` | — |

## Rule

If the same workflow exists in `media-buying/`, `client-marketing/`, or `onboarding/`, **link to that doc** — do not maintain two versions.

## Create new course material

1. Write or confirm the **canonical** playbook/SOP first (usually `client-marketing/` or `media-buying/`).
2. Add a **course material** doc here: intro, why it matters, checkpoints, links to canonical steps.
3. Set frontmatter: `content_layer: course-material`, `canonical_parent:`, `audience: [client]`.
4. Run `python scripts/sync-client-playbooks.py`.

Template: [client-playbook-template.md](../../templates/client-playbook-template.md) · Skill: [client-playbooks](../../.claude/skills/client-playbooks/SKILL.md)

## Related

- [Client Playbooks](../client-playbooks/README.md)
- [Fulfillment Operating System](../fulfillment-operating-system.md)
