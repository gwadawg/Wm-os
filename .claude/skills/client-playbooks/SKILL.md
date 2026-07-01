---
name: client-playbooks
description: >
  Index and maintain client playbooks, SOPs, and course material in Waiz Media OS — catalog
  sync, methodology pools, placement rules, shareability enforcement. Never link internal
  fulfillment processes in lo-course playbooks or course material. Use for catalog sync,
  checking what exists, or placement questions. To **create** a new playbook, use
  client-playbook-creator instead. Triggers: sync playbooks, playbook catalog, methodology
  pools, where does playbook go.
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
| Shareability | [shareability-boundaries.md](../../docs/client-fulfillment/shareability-boundaries.md) · [SHAREABILITY-CHECKLIST.md](../../docs/client-fulfillment/client-playbooks/SHAREABILITY-CHECKLIST.md) |
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
| `canonical` | `client-marketing/`, `client-sales/`, `media-buying/`, `client-success/`, `onboarding/` | Source of truth |
| `course-material` | `course-material/` | Client education — link to canonical |
| `client-instance` | `client-marketing/clients/` | Per-client delta only |

## Required frontmatter

```yaml
artifact_type: playbook
shareability: lo-course           # lo-course | paying-client | internal-fulfillment
audience: [client]
content_layer: canonical          # canonical | course-material | client-instance
product: reverse-mortgage
delivery_group: lead-nurture
methodology_sources:
  - docs/acquisition/sales/objection-handling-hub.md
canonical_parent: ...             # course-material wrappers only — point to *framework*
portal_url:                       # optional client portal link
client_delivery: true             # include docs outside client-fulfillment/
```

**Prospect LO course:** only link docs with `shareability: lo-course` in lesson bodies.

## No internal process links (hard rule)

When editing or recommending links for **`lo-course`** docs (frameworks, course material, generic LO playbooks):

**Never link Waiz internal fulfillment or DFY execution** in the main lesson body, banner, checklist, or "Go deeper" tables.

| Do not link | Examples |
|-------------|----------|
| CRM / bot / infra | `crm-architecture/`, `how-wm-ai-bot-works.md` |
| Onboarding runbooks | `onboarding/a-z*` |
| Media buying ops | `media-buying/` SOPs |
| Client success internals | `client-success/` constraint SOPs |
| Execution copy | `*-drip-campaign.md`, `rm-imessage-intent-drip*` |
| Waiz application playbooks | `playbook-*.md` without `-framework` (e.g. `playbook-lead-nurture.md`) |
| Engine maps | `fulfillment-lead-lifecycle.md` |

**Allowlist:** [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md) → section **LO course — `lo-course` only**.

**Frontmatter:** `methodology_sources` and `canonical_parent` on `lo-course` docs must point to **`lo-course`** paths only — not internal SOPs or application playbooks.

**If user asks to link internal docs into course material:** refuse in the main body; offer a gated *Waiz DFY clients only* appendix or route to [client-playbook-creator](../client-playbook-creator/SKILL.md) split workflow.

Full doctrine: [shareability-boundaries.md](../../docs/client-fulfillment/shareability-boundaries.md) · Audit: [SHAREABILITY-CHECKLIST.md](../../docs/client-fulfillment/client-playbooks/SHAREABILITY-CHECKLIST.md)

## Workflow

1. For **new playbooks**, use [client-playbook-creator](../client-playbook-creator/SKILL.md).
2. Read [README](../../docs/client-fulfillment/client-playbooks/README.md) and [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md).
3. Methodology scan — `catalog.yaml` → `methodology_pools`. Link existing; do not rewrite.
4. Before recommending course links, verify target `shareability` in catalog (or infer from path).
5. Run `python scripts/sync-client-playbooks.py` after changes.

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
