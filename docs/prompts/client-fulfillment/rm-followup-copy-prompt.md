---
title: RM Follow-Up Copy Prompt
domain: prompts
owner: client-success
status: active
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: prompt
---

# RM Follow-Up Copy Prompt

Paste-ready user prompt for the **RM Fulfillment Assistant** Claude Project (or repo skill) when drafting SMS/iMessage nurture variants.

Companion to [RM iMessage Intent Drip](../client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md) and [10-Day RM Drip Campaign (Email + SMS)](../client-fulfillment/client-marketing/10-day-rm-drip-campaign.md). For Claude Project setup see [chatbot-deploy/README.md](../client-fulfillment/reverse-mortgage-agent/chatbot-deploy/README.md).

## Required context (load before any prompt)

1. [RM Compliance Guardrails](../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md)
2. [RM iMessage Intent Drip (7-Day)](../client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md)
3. [RM Borrower Objections](../client-fulfillment/reverse-mortgage-dna/rm-borrower-objections.md)

## User prompt template

```text
Task: Draft RM follow-up copy

Channel: [iMessage SMS / bot reply / email]
Lifecycle stage: [Stage 3 first contact / Stage 5 pre-appointment / Stage 6 long-term nurture]
Intent segment: [remove_mortgage_payment / pay_off_debt / access_cash / none]
Day or touch #: [e.g. Day 3, confirmation, 24h reminder]

Goal: [elicit reply / book appointment / remind only / handle objection]

Objection or angle (if any): [e.g. "Is this a scam?" / new equity angle / Carol story variant]

Client context (optional):
- LO first name: [{{user.first_name}} or name]
- Setter display name: [Laura or custom]
- State: [if geo-specific]

Constraints:
- Match tone of rm-imessage-intent-drip-7day (LO assistant, outcome-first)
- Run compliance check inline
- Do not invent dollar amounts or client-specific proof
- Appointment broadcasts: zero question marks if reminder-only

Output: [1 variant / 3 variants / table comparing segments]
```

## Example (fast path)

```text
Task: Draft RM follow-up copy
Channel: iMessage SMS
Lifecycle stage: Stage 6 long-term nurture
Intent segment: remove_mortgage_payment
Day or touch #: Day 3
Goal: elicit reply
Objection or angle: new angle — rising property tax stress, same tone as drip doc
Output: 1 variant + compliance check
```

## Related

- [Client fulfillment prompts README](README.md)
- [RM Fulfillment Agent deploy kit](../client-fulfillment/reverse-mortgage-agent/chatbot-deploy/README.md)
