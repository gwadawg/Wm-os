---
title: RM Borrower Objections — Unified Reference
domain: client-fulfillment
owner: founder
status: active
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: reference
---

# RM Borrower Objections — Unified Reference

## Purpose

Single canonical reference for **borrower** (B2C) objections across SMS/iMessage, AI bot, nurture drips, and call-center handoff. Consolidates scattered guidance from ICP intelligence, call scripts, and doctrine.

## Scope

Client fulfillment only — homeowners inquiring about a reverse mortgage / HECM. Not Waiz B2B sales to loan officers.

## Owner

Founder (compliance-sensitive). Client Success maintains channel examples.

## Trigger

Any copy or conversation design that handles borrower pushback: bot training, drip variants, call-center scripts, ad nurture.

## Inputs

- [Intelligence ICP RM](intelligence-icp-rm.md) — Section 7
- [Call Center Appointment-Setting Script](../call-center/script-appointment-setting-call.md) — Objection section
- [RM Compliance Guardrails](rm-compliance-guardrails.md)
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)

## Outputs

Channel-appropriate response patterns with compliance flags.

## Quality Bar

- No financial or tax advice — defer to LO and qualified professionals
- No guaranteed outcomes
- Bot/assistant: book appointments only; product education at high level
- Say **retired homeowners**, not age in copy
- Flag HUMAN REVIEW when citing benefits (SS/Medicare), fees, or inheritance outcomes

---

## How to use this doc

| Channel | Your job | Depth |
|---------|----------|-------|
| **AI bot (SMS)** | Acknowledge, educate lightly, move to booking | High-level; never underwrite |
| **iMessage drip** | Preempt in nurture; myth-bust in value touches | Outcome-first; product name when needed |
| **Call center** | Keep conversation alive; hand off to LO | Front-desk version only |
| **LO call** | Full product answer | LO's job — not covered here |

**LO mindset before objections:** [LO D2C Sales Foundations](../client-sales/playbook-lo-d2c-sales-foundations-rm.md) · [Nurture Framework §2 — Limiting beliefs](../client-marketing/playbook-nurture-framework.md#2-limiting-beliefs-to-break). **Install beliefs first:** [RM Conceptual Beliefs Playbook](../client-sales/playbook-rm-conceptual-beliefs.md) — check Pain, Doubt, Cost, etc. before pitching. **Name deferral patterns:** [Prospect Fallacies Framework](../../acquisition/sales/prospect-fallacies-framework.md) — if-when and sunk cost map to unchecked beliefs (rep-side labels; don't lecture borrowers). **This doc:** word tracks when pushback still surfaces — diagnose which belief gap was missed on the playbook worksheet.

Always run [RM Compliance Guardrails](rm-compliance-guardrails.md) before deploying any response.

---

## Top 15 borrower objections

### 1. "The bank will take my house."

| | |
|--|--|
| **Fear** | Loss of home and security |
| **Truth anchor** | Borrower remains owner; loan is non-recourse; must meet occupancy and property obligations |
| **Marketing frame** | You remain the owner. As long as you live there and meet basic responsibilities, the home stays yours. |
| **Bot/SMS** | I hear that concern a lot — you stay the owner. {{user.first_name}} can walk you through exactly how that works on a quick call. Would [time] work? |
| **Call center** | That's exactly what {{LO NAME}} explains on the call — I'm just the assistant getting you on their calendar. |
| **Compliance** | PASS — no guarantees; HUMAN REVIEW if implying zero risk |

### 2. "My kids will inherit debt."

| | |
|--|--|
| **Fear** | Being a burden; guilt about legacy |
| **Truth anchor** | Non-recourse; heirs never personally liable; equity or sale repays loan |
| **Marketing frame** | Your children are never personally responsible. The loan is repaid from the home's value — not from their pockets. |
| **Bot/SMS** | Great question — your family isn't on the hook personally. {{user.first_name}} can explain how that works for your situation. Want to grab [time]? |
| **Compliance** | PASS |

### 3. "Will this affect my Social Security or Medicare?"

| | |
|--|--|
| **Fear** | Loss of essential benefits |
| **Truth anchor** | Proceeds generally not counted as income for SS/Medicare; **not tax advice** |
| **Marketing frame** | The money received is generally not considered income and does not impact Social Security or Medicare. |
| **Bot/SMS** | That's a common question — generally it doesn't count as income for those programs, but {{user.first_name}} can confirm how it applies to you. Worth a quick call? |
| **Compliance** | **HUMAN REVIEW** — benefits language is sensitive; never state as universal tax/benefit advice |

### 4. "I've heard horror stories."

| | |
|--|--|
| **Fear** | Distrust; fear of scams |
| **Truth anchor** | Old unregulated programs vs today's federally insured HECM |
| **Marketing frame** | Most horror stories come from older programs. Today's version is federally insured and heavily regulated. |
| **Bot/SMS** | Totally fair to be cautious. {{user.first_name}} specializes in this and can show you how today's program actually works — no pressure. [time]? |
| **Compliance** | PASS — don't disparage competitors by name |

### 5. "This sounds too good to be true."

| | |
|--|--|
| **Fear** | Hidden costs; skepticism |
| **Truth anchor** | Accessing built equity; costs disclosed upfront |
| **Marketing frame** | This isn't magic — it's accessing equity you've already built. We show you exactly how it works, including all costs. |
| **Bot/SMS** | I get it — it's smart to ask. {{user.first_name}} walks through the full picture, costs included, on the call. Would [time] work? |
| **Compliance** | PASS |

### 6. "Is this a scam?"

| | |
|--|--|
| **Fear** | Fraud; bad actors |
| **Truth anchor** | Verify LO identity; offer callback path |
| **Call center** | Totally hear you — there's a lot of bad calls out there. I'm [AGENT] from [LO]'s office at [COMPANY], and I can give you their direct line and website so you can call them back. Want me to text that to you? |
| **Bot/SMS** | I understand — lots of junk calls out there. I'm {{custom_values.setter_display_name}}, assistant for {{user.first_name}} at [COMPANY]. I can text you {{user.first_name}}'s direct info so you can verify. Still want to find a time to talk? |
| **Compliance** | PASS — offer verification; no pressure |

### 7. "I don't want more debt."

| | |
|--|--|
| **Fear** | Financial burden |
| **Truth anchor** | No required monthly mortgage payments on the loan |
| **Marketing frame** | No required monthly payments. Instead of money going out every month, money can come in or payments can stop. |
| **Bot/SMS** | A lot of people feel that way — it's different from a regular loan. {{user.first_name}} can explain how the payments work on your home. Quick call at [time]? |
| **Compliance** | PASS — still must meet property charges (taxes, insurance, maintenance) |

### 8. "What if I live a long time?"

| | |
|--|--|
| **Fear** | Running out of equity |
| **Truth anchor** | Non-recourse; can't owe more than home value at sale |
| **Marketing frame** | You can never owe more than your home is worth, and you can never be forced to leave as long as you meet basic requirements. |
| **Bot/SMS** | Good question — that's built into how the program works. {{user.first_name}} can walk you through it for your home. [time]? |
| **Compliance** | HUMAN REVIEW — ensure "never forced to leave" is qualified (occupancy, taxes, insurance) |

### 9. "I want to leave my home to my kids."

| | |
|--|--|
| **Fear** | Legacy loss |
| **Truth anchor** | Heirs can keep home (pay off loan) or sell; remaining equity to heirs |
| **Marketing frame** | Your heirs can keep the home by paying off the loan balance, or sell it. Any remaining equity goes to them. |
| **Bot/SMS** | Legacy is a big part of the conversation — {{user.first_name}} can show you how that works for your family. Worth [time]? |
| **Compliance** | PASS |

### 10. "The fees are too high."

| | |
|--|--|
| **Fear** | Being taken advantage of |
| **Truth anchor** | Regulated, disclosed fees |
| **Marketing frame** | All fees are regulated and disclosed upfront. We walk you through every cost — no surprises. |
| **Bot/SMS** | Fair concern — {{user.first_name}} breaks down every cost on the call so you can decide with full info. [time]? |
| **Compliance** | PASS — don't quote specific fee amounts unless LO-approved |

### 11. "I need to think about it."

| | |
|--|--|
| **Fear** | Decision paralysis; overwhelm |
| **Marketing frame** | You should think about it. Our consultation is purely educational — so when you do decide, you're thinking with clarity, not confusion. |
| **Bot/SMS** | Of course — no rush. If it helps, {{user.first_name}} can answer questions on a no-pressure call whenever you're ready. Want me to hold [time]? |
| **Call center** | Totally fair — bad timing or still gathering info? Schedule callback. |
| **Compliance** | PASS — no false urgency |

### 12. "Just send me information by email."

| | |
|--|--|
| **Fear** | Avoiding sales conversation |
| **Call center** | Of course — {{LO}} can send something directly. Best email is [EMAIL] — that good? [Pivot back to brief qual + appointment if possible] |
| **Bot/SMS** | Happy to — {{user.first_name}} can send info from their office. What's the best email? And so they send the right stuff — what were you hoping to use the funds for? |
| **Compliance** | PASS — don't promise specific rates or amounts by text |

### 13. "Where did you get my number?"

| | |
|--|--|
| **Fear** | Privacy; unsolicited contact |
| **Call center** | You came in through one of our inquiry forms / [LEAD SOURCE]. I've got your info as [NAME] looking at [USE OF FUNDS] — does that ring a bell? |
| **Bot/SMS** | You filled out a form about [home equity / use of funds] — that's how {{user.first_name}}'s team got your info. Does that sound familiar? |
| **Compliance** | PASS — stay factual, not defensive |

### 14. "I'm not interested right now."

| | |
|--|--|
| **Fear** | Bad timing; situation changed |
| **Call center** | Totally fair — can I ask what changed? Last time we heard from you, you were looking into [USE OF FUNDS]. Bad timing → schedule callback. Resolved → polite close. |
| **Bot/SMS** | No problem at all. If anything changes, just reply here and we can find a time with {{user.first_name}}. |
| **Compliance** | PASS — respect opt-out / STOP if applicable |

### 15. "My spouse / kid handles this — talk to them."

| | |
|--|--|
| **Fear** | Wrong decision-maker on the line |
| **Call center** | Oh, got it — what's the best way to reach them? I'd love to get them on a quick call with {{LO}} directly. |
| **Bot/SMS** | Got it — who should {{user.first_name}} connect with? I can make sure the right person gets the invite. |
| **Compliance** | PASS — don't treat as a hard no |

---

## Objection → drip / lifecycle mapping

| Lifecycle stage | Where objections surface | Primary docs |
|-----------------|-------------------------|--------------|
| Stage 3 — CRM / first contact | Scam, where did you get my number, send info | Bot works + call script |
| Stage 4 — Booking | Not interested, need to think | Call script + bot |
| Stage 5 — Pre-appointment | All product objections | Appointment follow-up value touches |
| Stage 6 — Long-term nurture | Myth-bust, legacy, fees | Intent drip Days 3–7 |

---

## Related

- [Intelligence ICP RM](intelligence-icp-rm.md) — full persona and VOC
- [Doctrine Reverse Mortgage](doctrine-reverse-mortgage.md) — stigma and product framing
- [RM iMessage Intent Drip](../client-marketing/rm-imessage-intent-drip-7day.md) — operational nurture copy
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md) — bot scope limits
- [RM Fulfillment Agent](../reverse-mortgage-agent/README.md) — Claude Project deploy kit
