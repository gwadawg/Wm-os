---
title: RM Text Drip 2025
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-05-21
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/RM _ Text drip 2025.docx
artifact_type: script
---

# RM Text Drip 2025

## Purpose

Canonical SMS drip sequences for RM leads in GHL.

## Scope

Post-opt-in text nurture; align with bot and claimed-tag flow.

## Trigger

CRM workflow build or sequence refresh.

## Inputs

- Lead stage
- Disposition
- Claimed status

## Outputs

- Configured GHL SMS workflows

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when applicable.

## Operating Content

Follow-Up SMS Sequence — Reverse Mortgage Leads

This document outlines a structured follow-up SMS sequence created to re-engage homeowners who submitted a form and didn't engage enough to book an appointment or  became unresponsive. Messages are delivered across multiple touchpoints and timeframes to maintain consistent communication without pressure, address common objections, and naturally reopen the conversation.

The primary goal is to ensure the messages do not feel automated, but instead sound as though they are being personally sent by a secretary or loan officer. This human tone is designed to increase trust and maximize response rates.

Once a prospect replies, our AI chatbot takes over to continue the conversation and attempt to book the next step. If the AI is unable to secure a response or complete the booking, a VA steps in to follow up and respond manually, ensuring no lead is left unattended.

1- After 5 minutes

Would love to set a call up with you and our loan officer sometime later to see if we have any programs that would make sense for you!

2- After 4 hours

No rush at all, {{contact.first_name}} — just checking in to see if you'd like help setting up a quick call with {{user.first_name}} to answer any questions.Happy to work around your schedule.

3- After 1 dayHaven't heard back from you since you reached out. {{user.first_name}} has been able to help homeowners in {{contact.state}} with removing their mortgage payments, or even taking cash out of their home without paying monthly. You up for a quick call?

4- After  1 day

{{contact.first_name}}, generally when i do not receive a response it is because you were told you didn't qualify. Just so you know, We're flexible with credit and income.

5- After 2 daysHey {{contact.first_name}}, I know life gets busy.But I didn’t want you to miss this... many people your age are using this program to:✅ Eliminate monthly mortgage payments✅ Tap into home equity without selling✅ Improve quality of life in retirementWant me to help schedule a time to talk?

6- After 4 daysHey {{contact.first_name}} just bumping this to the top of your inbox to make sure you saw this ^

7- After 2 daysAre my calls coming through? Goes straight to voicemail

8- After 7 days

No hard feelings if you're not interested... Just let me know! I know you sent in a form a while back, and don't want to leave you hanging there.

9 - After 7 days

Hey {{contact.first_name}} I'm just submitting my files from last week and came across yours. You still looking to take cashout of your equity without paying monthly? No hard feelings at all if not, I can put you as "completed" and make your day a whole lot easier just let me know

10 - After 6 days

If you are working with another lender it wouldn't hurt to get a second opinion. 9 times out of 10 we can beat them. Are you interested in getting a better deal?

11 - After 10 days

Something came up in the market... You still trying to take cash out of your home, or remove your mortgage payment?


## Related Docs

- [RM iMessage Intent Drip (7-Day)](rm-imessage-intent-drip-7day.md) — current intent-segmented iMessage nurture (team Google Doc)
- [10-Day RM Drip Campaign](10-day-rm-drip-campaign.md)
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)
