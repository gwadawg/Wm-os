---
title: Automations
domain: automations
owner: operations
status: active
last_updated: 2026-05-17
review_cycle: monthly
---

# Automations

Automation specs, system maps, CRM flows, bot logic, and tool handoffs.

## Where automation specs live today

Most CRM, bot, and workflow specs are already canonical under **client fulfillment** (not in this folder yet):

| Topic | Canonical path |
|-------|----------------|
| CRM infrastructure | [crm-infrastructure.md](../client-fulfillment/crm-architecture/crm-infrastructure.md) |
| WM AI Bot | [how-wm-ai-bot-works.md](../client-fulfillment/crm-architecture/how-wm-ai-bot-works.md) |
| Claimed tag | [how-claimed-tag-works.md](../client-fulfillment/crm-architecture/how-claimed-tag-works.md) |
| Fulfillment OS (links) | [fulfillment-operating-system.md](../client-fulfillment/fulfillment-operating-system.md) |

When you add a **new** automation spec (Zapier, n8n, GHL workflow, internal bot), prefer `docs/automations/<subsystem>/` and link from the relevant domain README. Move or summarize existing CRM docs here only after duplicate check ([duplicate-resolutions.md](../_inventory/duplicate-resolutions.md)).

## Source Inventory Snapshot

- No standalone files classified only under `automations/` yet.

## Open Gaps

- [ ] Assign domain owner for `automations/` top-level.
- [ ] Inventory which fulfillment CRM docs should stay in `crm-architecture/` vs move here.
- [ ] Add related KPIs and prompts under [kpis/](../kpis/README.md) and [prompts/](../prompts/README.md) when automations go live.
