---
title: Client Fulfillment Prompts
domain: prompts
owner: operations
status: active
last_updated: 2026-05-21
review_cycle: monthly
---

# Client Fulfillment Prompts

Reusable AI prompts for RM creatives, follow-up copy, and fulfillment workflows.

## Required context (load before any prompt)

1. [Fulfillment Operating System](../../client-fulfillment/fulfillment-operating-system.md)
2. Product compliance guardrails:
   - **RM:** [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md)
   - **DSCR:** [DSCR Compliance Guardrails](../../client-fulfillment/dscr-dna/dscr-compliance-guardrails.md)
3. Product pod (load before task-specific docs):
   - **RM:** [Reverse Mortgage DNA](../../client-fulfillment/reverse-mortgage-dna/README.md)
   - **DSCR:** [DSCR DNA](../../client-fulfillment/dscr-dna/README.md)
4. Task-specific SOP or playbook from [client-fulfillment](../../client-fulfillment/README.md)

## Prompts

| Prompt | Status | Purpose |
|--------|--------|---------|
| RM follow-up copy | **Active** | SMS/iMessage variants per [intent drip](../../client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md) + lifecycle stage — [prompt](rm-followup-copy-prompt.md) |
| RM creative draft | **Planned** | Generate ad copy/images per [angle library](../../client-fulfillment/media-buying/ad-copy-angle-library-rm.md) + [AI image SOP](../../client-fulfillment/media-buying/ai-rm-ad-image-creation-sop.md) |

Add `rm-creative-draft-prompt.md` when founder supplies tone rules and GHL field names.

## Related

- [Prompts index](../README.md)
