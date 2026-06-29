---
title: RM Fulfillment Agent
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: overview
---

# RM Fulfillment Agent

Internal fulfillment assistant for reverse mortgage client delivery — copy, drips, bot behavior, objections, lifecycle, and sub-agent design.

**Not** a replacement for [RM Creative Studio](../media-buying/creative-studio/README.md) (video ad scripts). Use both:

| Project | Use when |
|---------|----------|
| **RM Fulfillment Assistant** (this agent) | SMS/iMessage drips, bot replies, objections, lifecycle, static ad angles, campaign diagnosis, designing other RM agents |
| **RM Creative Studio** | Gated 4-step video ad flow (concept → script → Higgsfield prompt) |

## Lane

**Client fulfillment only** — copy and systems for **borrowers** (retired homeowners). Not Waiz B2B sales to loan officers. See [Waiz vs client marketing boundaries](../waiz-vs-client-marketing-boundaries.md).

## Deploy

Claude Project setup: [chatbot-deploy/README.md](chatbot-deploy/README.md)

Repo skill (Cursor / Claude Code): [.claude/skills/rm-fulfillment-agent/SKILL.md](../../../.claude/skills/rm-fulfillment-agent/SKILL.md)

## Knowledge hierarchy

Load in this order:

1. [Reverse Mortgage DNA](../reverse-mortgage-dna/README.md) — compliance + doctrine + ICP
2. [Client marketing](../client-marketing/README.md) — playbooks + drip copy
3. [CRM architecture](../crm-architecture/README.md) — bot + GHL
4. [Fulfillment lead lifecycle](../fulfillment-lead-lifecycle.md) — 6-stage engine

## Related

- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [RM Creative Studio deploy kit](../media-buying/creative-studio/chatbot-deploy/README.md)
- [Client fulfillment prompts](../../prompts/client-fulfillment/README.md)
