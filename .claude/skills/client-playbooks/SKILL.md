---
name: client-playbooks
description: >
  Index and maintain client playbooks, SOPs, and course material in Waiz Media OS — catalog
  sync, methodology pools, placement rules. Use for catalog sync, checking what exists, or
  placement questions. To **create** a new playbook, use client-playbook-creator instead.
  Triggers: sync playbooks, playbook catalog, methodology pools, where does playbook go.
---

# Client Playbooks

Master system for **all client playbooks, SOPs, and training** — not tied to any single product or portal name.

| Asset | Path |
|-------|------|
| **Start here** | [client-playbooks/README.md](../../docs/client-fulfillment/client-playbooks/README.md) |
| Auto-index | [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) |
| Config | [catalog.yaml](../../docs/client-fulfillment/client-playbooks/catalog.yaml) |
| Template | [client-playbook-template.md](../../docs/templates/client-playbook-template.md) |
| Format spec | [PLAYBOOK-FORMAT.md](../../docs/client-fulfillment/client-playbooks/PLAYBOOK-FORMAT.md) |
| Reference example | [playbook-lead-nurture.md](../../docs/client-fulfillment/client-marketing/playbook-lead-nurture.md) |
| Sync | `python scripts/sync-client-playbooks.py` |

## When to use

- **Creating a new playbook** → use [client-playbook-creator](../client-playbook-creator/SKILL.md)
- Syncing or browsing the catalog
- Checking placement, methodology pools, or dedup before/after creation
- Adding course material wrappers (often via client-playbook-creator)

## Where files go

| Layer | Folder | Role |
|-------|--------|------|
| `canonical` | `client-marketing/`, `media-buying/`, `client-success/`, `onboarding/` | Source of truth |
| `course-material` | `course-material/` | Client education — link to canonical |
| `client-instance` | `client-marketing/clients/` | Per-client delta only |

## Required frontmatter

```yaml
artifact_type: playbook
audience: [client]
content_layer: canonical          # canonical | course-material | client-instance
product: reverse-mortgage
delivery_group: lead-nurture
methodology_sources:
  - docs/acquisition/sales/objection-handling-hub.md
canonical_parent: ...             # course-material wrappers only
portal_url:                       # optional client portal link
client_delivery: true             # include docs outside client-fulfillment/
```

## Workflow

1. For **new playbooks**, use [client-playbook-creator](../client-playbook-creator/SKILL.md).
2. Read [README](../../docs/client-fulfillment/client-playbooks/README.md) and [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md).
3. Methodology scan — `catalog.yaml` → `methodology_pools`. Link existing; do not rewrite.
4. Run `python scripts/sync-client-playbooks.py` after changes.

## Methodology propagation (required ask)

If a **reusable technique** is new (not in pools or linked docs):

> I used **[technique]** in this playbook, but it is not in the knowledge base yet. Should I update **[candidate doc(s)]**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)

## Related skills

| Skill | When |
|-------|------|
| [client-playbook-creator](../client-playbook-creator/SKILL.md) | **Create or rebuild** client playbooks (interview + build + sync) |
| [sop-builder](../sop-builder/SKILL.md) | Internal team SOPs (not client playbooks) |
| [waiz-business-os](../waiz-business-os/SKILL.md) | Repo structure |
| [knowledge-capture](../knowledge-capture/SKILL.md) | Distill calls into OS; may feed pools |
| [team-doc-publish](../team-doc-publish/SKILL.md) | Internal team Drive |
| [copywriting](../copywriting/SKILL.md) | Client copy |

## Related docs

- [Course material README](../../docs/client-fulfillment/course-material/README.md)
- [Fulfillment Operating System](../../docs/client-fulfillment/fulfillment-operating-system.md)
- [SOURCE-OF-TRUTH](../../docs/SOURCE-OF-TRUTH.md)
