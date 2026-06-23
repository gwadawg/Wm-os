---
title: RM iMessage Intent Drip (7-Day)
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-19
review_cycle: monthly
artifact_type: script
source_document: internal — conversation + rm-text-drip-2025.md evolution
---

# RM iMessage Intent Drip (7-Day)

## Purpose

Nurture reverse mortgage form leads who have not booked a call with the **loan officer (LO)**. Messages are sent as the LO's assistant (e.g. Laura) via iMessage. Goal: elicit a reply so the AI booking agent can take over.

## Scope

- Three intent-based segments (Days 1–7)
- Shared soft breakup (Day 7) and universal tail (Day 8+)
- GHL workflow build; per-client snapshot with custom values
- Does **not** replace speed-to-lead AI/bot in the first 0–5 minutes

## Owner

Client Success (Laura Moco). LO approves client-specific story names and compliance-sensitive lines.

## Trigger

- Lead submits form with intent field populated
- Lead has **not** replied and has **not** booked
- Lead is routed into correct segment automation at Day 1

## Inputs

- `form_intent` from form (see routing below)
- Contact: first name, state, estimated home value (Segment 3)
- Assigned LO user: `{{user.first_name}}`
- Setter display name: `{{custom_values.setter_display_name}}`

## Outputs

- Reply → remove from all drip workflows → AI/Closebot books with LO
- Day 7 → merge into long-term nurture workflow (Day 8+)

## Quality Bar

- Identity: **LO's assistant**, not company/brand as sender
- Copy: **outcome-first** (eliminate payment, clear debt, access cash) — name **HECM** or **reverse mortgage** only when mechanics or objection-handling require it; not every touch
- Product: reverse-specific mechanics when needed (HECM line growth, non-recourse, no required monthly mortgage payment on the loan) — not generic "equity options"
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md): no tax advice in SMS; no guaranteed outcomes; say *retired homeowners* not age in copy
- Stories (Carol, Ruth, Tom): LO-approved or labeled composite internally

## GHL routing

| Segment | `form_intent` values | % (reference) |
|---------|----------------------|---------------|
| 1 — Remove mortgage payment | `remove_mortgage_payment` | ~43% |
| 2 — Pay debt off | `pay_off_debt` | ~29% |
| 3 — Cash out / strategic | `tax_free_cash_out` or `cash_out` | ~27% |

**Rules**

1. Route by intent at Day 1.
2. At Day 7, all segments end → single long-term nurture workflow.
3. **Any inbound reply** → exit drip → AI responder books with LO.
4. After appointment booked → AI off; appointment reminders only (not this nurture).

## Merge fields (snapshot)

| Token | Use |
|-------|-----|
| `{{contact.first_name}}` | Lead first name |
| `{{contact.state}}` | State normalization |
| `{{contact.estimated_home_value}}` | Segment 3 only |
| `{{user.first_name}}` | Assigned LO first name |
| `{{custom_values.setter_display_name}}` | Assistant name (e.g. Laura) |

**Opener pattern:** `Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into…`

Use gender-neutral framing if needed: `{{user.first_name}} asked me to reach out` (no pronoun).

## Cadence note (recommended)

Default below is **~14 touches in 7 days**. For iMessage to retired homeowners, consider **9–10 touches**: Day 1 = 2 messages (drop evening ping); Days 2–6 = 1–2/day; keep Day 7 breakup.

## Outcome-first language (use vs avoid)

| Avoid | Use |
|-------|-----|
| "reverse mortgage" in every message | lead with the **outcome** they asked for; **one** program-name mention per segment when structure or objection-handling needs it |
| equity options (vague) | **eliminate monthly payment**, **clear debt**, **access cash from home** |
| access your equity (generic) | home equity proceeds — **no required monthly mortgage payment** on the loan |
| line of credit (generic) | **HECM line of credit** — unused portion **grows over time** |
| tax-free cash | tax questions → `{{user.first_name}}` on the call |

---

## Segment 1 — Remove mortgage payment

**Archetype:** Financially squeezed · validation + rightful access

### Day 1

**+4 hrs**

```
Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into getting rid of your monthly mortgage payment.

What pushed you to look now — the payment itself, or freeing up cash each month?
```

**+6 hrs**

```
A lot of retired homeowners in {{contact.state}} still send a forward mortgage payment every month — even with strong equity. Many use proceeds to pay that loan off — then there's no required monthly mortgage payment going forward. Sound like what you're after?
```

**+18 hrs** *(optional — omit for lighter cadence)*

```
{{user.first_name}} can walk through what that would look like for your home — usually about 20 minutes. Want me to find a time?
```

### Day 2

**+5 hrs**

```
{{contact.first_name}} — still here. Still looking to eliminate that mortgage payment, or did something change?
```

**+7 hrs**

```
Carol had sent the same mortgage payment for 18 years. {{user.first_name}} helped her use home equity to pay off the existing loan — she hasn't had a required monthly mortgage payment since. Want the short version?
```

**+18 hrs**

```
Mornings or afternoons better?
```

### Day 3

**+6 hrs**

```
One thing people miss: you're not trading one payment for another. There's no required monthly mortgage payment — you still keep title and stay in the home. Had you heard that?
```

**+24 hrs**

```
No pressure — this week or next better to compare notes?
```

### Day 4

**+6 hrs**

```
{{contact.first_name}} — a lot of what people hear about this isn't accurate. What's been holding you back from a quick call with {{user.first_name}}?
```

**+24 hrs**

```
Just a conversation — no application, no commitment. Worth 20 minutes to see if eliminating that payment makes sense for your home?
```

### Day 5

**+6 hrs**

```
You stay on title. The home stays yours. You're still responsible for taxes and insurance — but no required monthly mortgage payment on the loan. Did you know that?
```

**+24 hrs**

```
Reply "ready" and I'll get you on {{user.first_name}}'s calendar.
```

### Day 6

**+24 hrs**

```
Honest question: is that mortgage payment still taking up too much headspace in retirement, or are you mostly getting by?
```

### Day 7 — Soft breakup

```
{{contact.first_name}} — I don't want to crowd your messages if the timing's off. I'll step back — just reply when you want to pick this back up.
```

---

## Segment 2 — Pay debt off

**Archetype:** Security-seeker · empathy, no shame

### Day 1

**+4 hrs**

```
Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking at using home equity to clear debt.

Is it mostly one bill, or the overall stack?
```

**+6 hrs**

```
A lot of folks did everything right — and still carried debt into retirement. Proceeds from your home can pay off that debt — and there's no required monthly mortgage payment on the loan itself. Does that match what you're hoping for?
```

**+18 hrs**

```
Happy to set up a no-pressure chat with {{user.first_name}} — what does your week look like?
```

### Day 2

**+5 hrs**

```
{{contact.first_name}} — still thinking about you. Still aiming to get that debt cleared, or has the priority shifted?
```

**+7 hrs**

```
Ruth used proceeds from her home to pay off balances she'd carried for years — without adding a new required monthly mortgage payment. {{user.first_name}} can explain how the numbers work for your home. Want to hear more?
```

**+18 hrs**

```
This week or next — which's lighter for you?
```

### Day 3

**+6 hrs**

```
Straight question: what have you heard that made you nervous about using your home equity this way?
```

**+24 hrs**

```
I'm here when you're ready. What day should I aim for?
```

### Day 4

**+6 hrs**

```
Unlike a HELOC, a HECM line of credit doesn't require monthly mortgage payments — and the unused portion can actually grow over time. Had you looked at it that way before?
```

**+24 hrs**

```
Just a conversation with {{user.first_name}} — no decisions. Worth 20 minutes?
```

### Day 5

**+6 hrs**

```
Biggest worry we hear: kids and the house. It's a non-recourse loan — you or heirs don't owe more than the home's value when it's due, and heirs keep any equity left after payoff. Want {{user.first_name}} to walk through how that works for you?
```

**+24 hrs**

```
Still happy to talk. Reply with a day that works.
```

### Day 6

**+24 hrs**

```
{{contact.first_name}} — are you worrying about money more than you're enjoying retirement? Just trying to understand where you're at.
```

### Day 7 — Soft breakup

```
{{contact.first_name}} — I'll stop reaching out for now. Reply anytime and we'll pick it up — no hard feelings.
```

---

## Segment 3 — Cash out / strategic

**Archetype:** Strategic / legacy · peer tone, numbers + optionality

### Day 1

**+4 hrs**

```
Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into accessing cash from your home.

Are you leaning toward a lump sum upfront, a HECM line of credit you draw when you need it, or still deciding?
```

**+6 hrs**

```
With about {{contact.estimated_home_value}} in value, there's often a meaningful amount available — lump sum, monthly draws, line of credit, or a mix. No required monthly mortgage payment on the loan, and you don't have to sell. Worth a quick run-through with {{user.first_name}}?
```

**+18 hrs**

```
What does your week look like for a 20-minute walkthrough of how you could structure the funds?
```

### Day 2

**+5 hrs**

```
{{contact.first_name}} — still exploring your options, or did timing shift?
```

**+7 hrs**

```
Tom set up a HECM line of credit at 64 and didn't draw for two years. The unused portion kept growing. When the market dipped, he drew from it instead of selling investments at a loss. That's the piece most people don't compare to a HELOC. Interesting to you?
```

**+18 hrs**

```
Mornings or afternoons better?
```

### Day 3

**+6 hrs**

```
On a HECM line of credit, the unused portion grows over time — so setting it up earlier can mean more available later. Does that change how you're thinking about timing?
```

**+24 hrs**

```
Happy to go through specifics with {{user.first_name}}. What does the rest of your week look like?
```

### Day 4

**+6 hrs**

```
{{user.first_name}} usually walks through four ways to structure a reverse mortgage: lump sum, fixed monthly draws (tenure or term), line of credit, or a combination. Which would fit your plan best?
```

**+24 hrs**

```
No commitment — just numbers with {{user.first_name}}. Worth 20 minutes?
```

### Day 5

**+6 hrs**

```
A lot of people ask how proceeds affect taxes. That's one for {{user.first_name}} on a call — along with which disbursement makes sense for you. Have you gotten that far in your research?
```

**+24 hrs**

```
Still here when you want to run the numbers. What day works?
```

### Day 6

**+24 hrs**

```
{{contact.first_name}} — comparing draw structures actively, or still early research?
```

### Day 7 — Soft breakup

```
{{contact.first_name}} — I'll pause for now. Reply whenever you want to revisit the numbers with {{user.first_name}}.
```

---

## Day 8+ — Universal nurture tail

**+2 days after Day 7**

```
{{contact.first_name}} — still here. A lot can change in a week. If you want {{user.first_name}} to walk through what this could look like for your home, just reply.
```

---

## Metrics

- Reply rate by segment and by day
- Reply → book rate (post-AI handoff)
- Stop / opt-out rate (Day 1–2 spike = cadence too heavy)
- Messages to first reply

## Related docs

- [10-Day RM Drip Campaign (Email + SMS) — Meta Leads](10-day-rm-drip-campaign.md) — email + SMS path for Meta form leads; long-term nurture Days 11–90
- [RM iMessage Appointment Follow-Up](rm-imessage-appointment-followup.md) — post-booking confirmation, reminders, no-show re-engagement
- [RM iMessage Second-Booking Follow-Up](rm-imessage-second-booking-followup.md) — rebook / second appointment (broad, lighter cadence)
- [RM Text Drip 2025](rm-text-drip-2025.md) — legacy longer-cycle SMS
- [RM Lead Nurture Drip Sequence](rm-lead-nurture-drip-sequence.md)
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)
- [Intelligence RM Product](../reverse-mortgage-dna/intelligence-rm-product.md)
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Team Google Doc

Published copy: [RM iMessage Intent Drip (7-Day)](https://docs.google.com/document/d/1fqPy41ZZXKtQDHhKt7zVRC54NH1C_6ztJjNeNWA72l8/edit) (Waiz Team SOPs → 04 - Client Success). Repo is source of truth; re-publish with `python3 scripts/publish-team-doc.py docs/client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md`.

## Open questions

- [ ] Per-client approval of story names and state-specific disclaimers
- [ ] A/B lighter cadence (9-touch) vs full 14-touch in GHL
