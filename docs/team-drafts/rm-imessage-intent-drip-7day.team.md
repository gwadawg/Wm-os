---
team_title: "RM iMessage Intent Drip (7-Day)"
team_role: client_success
source_repo_path: "docs/client-fulfillment/client-marketing/rm-imessage-intent-drip-7day.md"
approved: true
draft_updated: 2026-05-28
---

<!-- Edit below. Publish uses Google Doc template (Objection Categories styles). -->

**WAIZ MEDIA**

**RM iMessage Intent Drip (7-Day)**

Intent-based iMessage nurture for reverse mortgage leads — sent as the LO's assistant until they reply (then AI books).

*Client Success  |  Internal Use Only  |  May 2026*

# 1. Overview

Nurture reverse mortgage form leads who have not booked a call with the loan officer (LO). Messages are sent as the LO's assistant (e.g. Laura) via iMessage. Goal: elicit a reply so the AI booking agent can take over.

> **📌 NORTH STAR**
>
> Nurture reverse mortgage form leads who have not booked a call with the loan officer (LO).

- Who: Client-Success
- When: - Lead submits form with intent field populated - Lead has not replied and has not booked - Lead is routed into correct segment automation at Day 1
**Before You Start**

- Lead submits form with intent field populated
- Lead has not replied and has not booked
- Lead is routed into correct segment automation at Day 1
- Three intent-based segments (Days 1–7)
- Shared soft breakup (Day 7) and universal tail (Day 8+)
- GHL workflow build; per-client snapshot with custom values
- Does not replace speed-to-lead AI/bot in the first 0–5 minutes
- form_intent from form (see routing below)
- Contact: first name, state, estimated home value (Segment 3)
- Assigned LO user: {{user.first_name}}
- Setter display name: {{custom_values.setter_display_name}}
# How To Do It

## Owner

Client Success (Laura Moco). LO approves client-specific story names and compliance-sensitive lines.

## Outputs

- Reply → remove from all drip workflows → AI/Closebot books with LO
- Day 7 → merge into long-term nurture workflow (Day 8+)
## Ghl Routing

| Segment | form_intent values | % (reference) |
| --- | --- | --- |
| 1 — Remove mortgage payment | remove_mortgage_payment | ~43% |
| 2 — Pay debt off | pay_off_debt | ~29% |
| 3 — Cash out / strategic | tax_free_cash_out or cash_out | ~27% |

**Rules**

1. Route by intent at Day 1.
1. At Day 7, all segments end → single long-term nurture workflow.
1. Any inbound reply → exit drip → AI responder books with LO.
1. After appointment booked → AI off; appointment reminders only (not this nurture).
## Merge Fields

| Token | Use |
| --- | --- |
| {{contact.first_name}} | Lead first name |
| {{contact.state}} | State normalization |
| {{contact.estimated_home_value}} | Segment 3 only |
| {{user.first_name}} | Assigned LO first name |
| {{custom_values.setter_display_name}} | Assistant name (e.g. Laura) |

**Opener pattern:**

Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into…

Use gender-neutral framing if needed: {{user.first_name}} asked me to reach out (no pronoun).

## Cadence Note

Default below is ~14 touches in 7 days. For iMessage to retired homeowners, consider 9–10 touches: Day 1 = 2 messages (drop evening ping); Days 2–6 = 1–2/day; keep Day 7 breakup.

## Reverse-only Language

| Avoid | Use |
| --- | --- |
| equity options | reverse mortgage / HECM program |
| access your equity | convert home equity — no required monthly mortgage payment on the reverse loan |
| line of credit | HECM line of credit — unused portion grows over time |
| tax-free cash | tax questions → {{user.first_name}} on the call |

## Segment 1 — Remove Mortgage Payment

**Archetype:**

Financially squeezed · validation + rightful access

**Day 1**

**+4 hrs**

```

Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into getting rid of your monthly mortgage payment.

What pushed you to look now — the payment itself, or freeing up cash each month?

```

**+6 hrs**

```

A lot of retired homeowners in {{contact.state}} still send a forward mortgage payment every month — even with strong equity. With a reverse mortgage, many use proceeds to pay that loan off, then there's no required monthly mortgage payment on the reverse itself. Sound like what you're after?

```

**+18 hrs**

(optional — omit for lighter cadence)

```

{{user.first_name}} can walk through what that would look like for your home — usually about 20 minutes. Want me to find a time?

```

**Day 2**

**+5 hrs**

```

{{contact.first_name}} — still here. Still looking to eliminate that mortgage payment, or did something change?

```

**+7 hrs**

```

Carol had sent the same mortgage payment for 18 years. {{user.first_name}} set up a reverse mortgage that paid off her existing loan — she hasn't had a required monthly mortgage payment on it since. Want the short version?

```

**+18 hrs**

```

Mornings or afternoons better?

```

**Day 3**

**+6 hrs**

```

One thing people miss: you're not trading one payment for another. On a reverse mortgage there's no required monthly mortgage payment — you still keep title and stay in the home. Had you heard that?

```

**+24 hrs**

```

No pressure — this week or next better to compare notes?

```

**Day 4**

**+6 hrs**

```

{{contact.first_name}} — TV and neighbors say a lot of wrong things about reverse mortgages. What's been holding you back from a quick call with {{user.first_name}}?

```

**+24 hrs**

```

Just a conversation — no application, no commitment. Worth 20 minutes to see if a reverse mortgage fits your home?

```

**Day 5**

**+6 hrs**

```

You stay on title. The home stays yours. You're still responsible for taxes and insurance — but no required monthly mortgage payment on the reverse. Did you know that?

```

**+24 hrs**

```

Reply "ready" and I'll get you on {{user.first_name}}'s calendar.

```

**Day 6**

**+24 hrs**

```

Honest question: is that mortgage payment still taking up too much headspace in retirement, or are you mostly getting by?

```

**Day 7 — Soft breakup**

```

{{contact.first_name}} — I don't want to crowd your messages if the timing's off. I'll step back — just reply when you want to pick this back up.

```

## Segment 2 — Pay Debt Off

**Archetype:**

Security-seeker · empathy, no shame

**Day 1**

**+4 hrs**

```

Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking at using a reverse mortgage to clear debt.

Is it mostly one bill, or the overall stack?

```

**+6 hrs**

```

A lot of folks did everything right — and still carried debt into retirement. A reverse mortgage can pay off that debt with proceeds — and there's no required monthly mortgage payment on the reverse loan itself. Does that match what you're hoping for?

```

**+18 hrs**

```

Happy to set up a no-pressure chat with {{user.first_name}} — what does your week look like?

```

**Day 2**

**+5 hrs**

```

{{contact.first_name}} — still thinking about you. Still aiming to get that debt cleared, or has the priority shifted?

```

**+7 hrs**

```

Ruth used reverse mortgage proceeds to pay off balances she'd carried for years — without adding a new required monthly mortgage payment on the reverse. {{user.first_name}} can explain how the numbers work for your home. Want to hear more?

```

**+18 hrs**

```

This week or next — which's lighter for you?

```

**Day 3**

**+6 hrs**

```

Straight question: what have you heard about reverse mortgages that made you nervous?

```

**+24 hrs**

```

I'm here when you're ready. What day should I aim for?

```

**Day 4**

**+6 hrs**

```

Unlike a HELOC, a HECM reverse mortgage doesn't require monthly mortgage payments on the loan — and the unused line of credit can actually grow over time. Had you looked at it that way before?

```

**+24 hrs**

```

Just a conversation with {{user.first_name}} — no decisions. Worth 20 minutes?

```

**Day 5**

**+6 hrs**

```

Biggest worry we hear: kids and the house. It's a non-recourse loan — you or heirs don't owe more than the home's value when it's due, and heirs keep any equity left after payoff. Want {{user.first_name}} to walk through how that works for you?

```

**+24 hrs**

```

Still happy to talk. Reply with a day that works.

```

**Day 6**

**+24 hrs**

```

{{contact.first_name}} — are you worrying about money more than you're enjoying retirement? Just trying to understand where you're at.

```

**Day 7 — Soft breakup**

```

{{contact.first_name}} — I'll stop reaching out for now. Reply anytime and we'll pick it up — no hard feelings.

```

## Segment 3 — Cash Out / Strategic

**Archetype:**

Strategic / legacy · peer tone, numbers + optionality

**Day 1**

**+4 hrs**

```

Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you were looking into a reverse mortgage for cash from your home.

Are you leaning toward a lump sum upfront, a HECM line of credit you draw when you need it, or still deciding?

```

**+6 hrs**

```

With about {{contact.estimated_home_value}} in value, there's often a meaningful amount available — lump sum, monthly draws, line of credit, or a mix. No required monthly mortgage payment on the reverse, and you don't have to sell. Worth a quick run-through with {{user.first_name}}?

```

**+18 hrs**

```

What does your week look like for a 20-minute walkthrough of how you could structure the reverse?

```

**Day 2**

**+5 hrs**

```

{{contact.first_name}} — still exploring a reverse mortgage, or did timing shift?

```

**+7 hrs**

```

Tom set up a HECM line of credit at 64 and didn't draw for two years. The unused portion kept growing. When the market dipped, he drew from it instead of selling investments at a loss. That's the piece most people don't compare to a HELOC. Interesting to you?

```

**+18 hrs**

```

Mornings or afternoons better?

```

**Day 3**

**+6 hrs**

```

On a HECM reverse mortgage, the unused line of credit grows over time — so setting it up earlier can mean more available later. Does that change how you're thinking about timing?

```

**+24 hrs**

```

Happy to go through specifics with {{user.first_name}}. What does the rest of your week look like?

```

**Day 4**

**+6 hrs**

```

{{user.first_name}} usually walks through four structures: lump sum, fixed monthly draws (tenure or term), line of credit, or a combination. Which would fit your plan best?

```

**+24 hrs**

```

No commitment — just numbers with {{user.first_name}}. Worth 20 minutes?

```

**Day 5**

**+6 hrs**

```

A lot of people ask how reverse proceeds affect taxes. That's one for {{user.first_name}} on a call — along with which disbursement makes sense for you. Have you gotten that far in your research?

```

**+24 hrs**

```

Still here when you want to run the numbers. What day works?

```

**Day 6**

**+24 hrs**

```

{{contact.first_name}} — comparing reverse mortgage structures actively, or still early research?

```

**Day 7 — Soft breakup**

```

{{contact.first_name}} — I'll pause for now. Reply whenever you want to revisit the reverse mortgage numbers with {{user.first_name}}.

```

## Day 8+ — Universal Nurture Tail

**+2 days after Day 7**

```

{{contact.first_name}} — still here. A lot can change in a week. If you want {{user.first_name}} to walk through what a reverse mortgage could look like for your home, just reply.

```

## Done Right Looks Like

- Identity: LO's assistant, not company/brand as sender
- RM Compliance Guardrails: no tax advice in SMS; no guaranteed outcomes; say retired homeowners not age in copy
- Stories (Carol, Ruth, Tom): LO-approved or labeled composite internally
## When To Get Help

Questions, pricing, or exceptions → escalate to Gabriel (Client-Success team).

## Related Procedures

- [How The WM AI Bot Works](https://docs.google.com/document/d/1UDe_xi89VXYIKEtTBkKD8nTsSi2I1Zfk3I07RgoZMXI/edit)
- RM Text Drip 2025 (legacy longer-cycle SMS — repo)
- RM Lead Nurture Drip Sequence (repo)
> **📌 REMEMBER**
>
> If this doc conflicts with what you heard elsewhere, follow this doc and tell Gabriel.


<div align="center">

*Waiz Media | Internal Document | Confidential*

</div>
