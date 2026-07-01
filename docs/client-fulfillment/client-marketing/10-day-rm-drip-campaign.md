---
title: 10-Day RM Drip Campaign (Email + SMS) — Meta Leads
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-06-23
review_cycle: monthly
source_document: internal — conversation + rm-imessage-intent-drip-7day.md evolution
artifact_type: script
---

# 10-Day RM Drip Campaign (Email + SMS) — Meta Leads

## Purpose

Nurture **Meta instant-form** reverse mortgage leads who have not replied or booked with the **loan officer (LO)**. Combines educational email depth with conversational SMS/iMessage to elicit a reply so the AI booking agent can take over.

**Strategic layer:** [Lead Nurture Playbook](playbook-lead-nurture.md) — pillars, rules, quality bar. This doc is **execution** (copy + GHL).

Extends into **long-term nurture** (Days 11–90) for leads who complete the 10-day arc without booking.

## Scope

- Days 1–10: primary email + SMS sequence (Meta lead source)
- Days 11–30: Phase 2 long-term nurture (education rotation)
- Days 31–90: Phase 3 maintenance nurture (light touch)
- GHL workflow build; per-client snapshot with custom values
- Does **not** replace speed-to-lead AI/bot in the first 0–5 minutes
- Does **not** replace [RM iMessage Intent Drip (7-Day)](rm-imessage-intent-drip-7day.md) for intent-segmented SMS-only paths — use this doc when **email + SMS** is required or Meta is the lead source

## Owner

Client Success (Laura Moco). LO approves client-specific story names and compliance-sensitive lines.

## Trigger

- Lead submits Meta instant form
- Lead has **not** replied and has **not** booked
- Lead enters workflow at Day 1 (+4 hrs after form submit, after speed-to-lead bot)

## Inputs

- `form_intent` from form (optional — see intent routing)
- Contact: first name, state, estimated home value (when available)
- Assigned LO user: `{{user.first_name}}`
- Setter display name: `{{custom_values.setter_display_name}}`
- Lead source tag: `meta`

## Outputs

- Reply → remove from all drip workflows → AI/Closebot books with LO
- Day 10 complete, no reply → merge into Phase 2 (Days 11–30)
- Day 30 complete, no reply → merge into Phase 3 (Days 31–90)
- Any reply at any phase → exit → AI books

## Quality Bar

- Identity: **LO's assistant**, not company/brand as sender
- Copy: **outcome-first** — name **HECM** or **reverse mortgage** only when mechanics or objection-handling require it
- Product: reverse-specific mechanics when needed (HECM line growth, non-recourse, no required monthly mortgage payment on the loan)
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md): no tax advice in SMS; no guaranteed outcomes; say *retired homeowners* not age in copy
- Stories (Carol, Ruth, Tom): LO-approved or labeled composite internally
- Meta-specific: acknowledge form source; address scam/FB misinformation on Day 8

## GHL routing

| Segment | `form_intent` values | Use |
|---------|----------------------|-----|
| 1 — Remove mortgage payment | `remove_mortgage_payment` | Day 1 opener + Day 4 story swap |
| 2 — Pay debt off | `pay_off_debt` | Day 1 opener + Day 6 emphasis |
| 3 — Cash out / strategic | `tax_free_cash_out` or `cash_out` | Day 1 opener + Day 7 value line |
| Universal | none / unknown | Default copy below |

**Rules**

1. Route intent-specific lines at Day 1, 4, 6, 7 where bracketed.
2. **Any inbound reply** → exit all phases → AI responder books with LO.
3. After appointment booked → AI off; appointment reminders only (not this nurture).
4. Day 10 → Phase 2 if no reply. Day 30 → Phase 3 if no reply.

## Merge fields (snapshot)

| Token | Use |
|-------|-----|
| `{{contact.first_name}}` | Lead first name |
| `{{contact.state}}` | State normalization |
| `{{contact.estimated_home_value}}` | Segment 3 / Day 7 only |
| `{{user.first_name}}` | Assigned LO first name |
| `{{custom_values.setter_display_name}}` | Assistant name (e.g. Laura) |

**Opener pattern:** `Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you filled out a form about…`

## Cadence summary

| Phase | Days | Touches | Channel mix |
|-------|------|---------|-------------|
| Primary | 1–10 | ~18 | 1 email + 1–2 SMS most days |
| Long-term A | 11–30 | 8 | 1 email + 1 SMS every 2–3 days |
| Long-term B | 31–90 | 6 | 1 email + 1 SMS every ~10 days |

## Outcome-first language (use vs avoid)

| Avoid | Use |
|-------|-----|
| "reverse mortgage" in every message | lead with the **outcome** they asked for |
| equity options (vague) | **eliminate monthly payment**, **clear debt**, **access cash from home** |
| access your equity (generic) | home equity proceeds — **no required monthly mortgage payment** on the loan |
| tax-free cash | tax questions → `{{user.first_name}}` on the call |
| homeowners 62+ | **retired homeowners** |

## Educational arc (Days 1–10)

| Day | Theme | Objection preempted |
|-----|--------|---------------------|
| 1 | Acknowledge Meta form + qualify | "Where did you get my info?" |
| 2 | House-rich, cash-poor | Trapped equity |
| 3 | You keep the home | "Bank takes my house" |
| 4 | No required monthly payment | "I don't want more debt" |
| 5 | Heirs & legacy | "Kids inherit debt" |
| 6 | What funds can be used for | "Is this right for me?" |
| 7 | Disbursement structures | Confusion / paralysis |
| 8 | Regulated program / scam fear | Horror stories |
| 9 | SS/Medicare + social proof | Benefits + "need to think" |
| 10 | Soft breakup + recap | Respect opt-out |

---

# Phase 1 — Days 1–10

## Day 1 — Acknowledge + qualify

**Theme:** You came from our Meta form. What pushed you to look now?

### SMS — +4 hrs after form submit

```
Hey {{contact.first_name}}, this is {{custom_values.setter_display_name}} — {{user.first_name}}'s assistant. He asked me to reach out because you filled out a form about [INTENT — see routing below].

What pushed you to look now — the payment itself, debt, or having cash available when you need it?
```

**Intent routing (Day 1 SMS):**

| Segment | `[INTENT]` line |
|---------|-----------------|
| `remove_mortgage_payment` | getting rid of your monthly mortgage payment |
| `pay_off_debt` | using home equity to clear debt |
| `cash_out` / `tax_free_cash_out` | accessing cash from your home |
| Universal | using your home equity |

### SMS — +6 hrs (if no reply)

```
A lot of retired homeowners in {{contact.state}} have strong equity but tight monthly cash flow. {{user.first_name}} helps people see what's actually possible — no pressure, about 20 minutes. Does that sound like what you were after?
```

### Email — +5 hrs

**Subject:** You asked about your home — quick follow-up

**Preview:** {{user.first_name}} asked me to reach out personally.

---

Hi {{contact.first_name}},

You recently filled out a form on Facebook about [INTENT — match routing table above]. I'm {{custom_values.setter_display_name}}, assistant to {{user.first_name}} at [COMPANY].

A lot of retired homeowners tell us the same thing: *"My house is worth a lot, but I can't use any of it."* That's exactly the conversation {{user.first_name}} specializes in.

**One quick question so we send you the right info:**

What matters most to you right now?

1. Stopping a monthly mortgage payment
2. Clearing debt that's eating into retirement
3. Having cash or a line of credit available when you need it
4. Still figuring it out

Just reply to this email (or text me back at [PHONE]) with a number or a few words. No application. No commitment.

Talk soon,

{{custom_values.setter_display_name}}
On behalf of {{user.first_name}}, [COMPANY]
[PHONE]

---

**Compliance check:** PASS — factual lead source; no amounts or guarantees.

---

## Day 2 — Trapped equity

**Theme:** Your equity isn't useless — here's why people feel stuck.

### Email — 9:00 AM

**Subject:** "My home is worth a lot, but I can't touch it"

---

Hi {{contact.first_name}},

If you've ever thought that sentence, you're not alone.

Many retired homeowners in {{contact.state}} are in the same spot:

- Fixed income that doesn't keep up with groceries, utilities, or insurance
- Savings that get a little smaller every year
- A home that keeps going up in value — but no easy way to use that value without selling

That's the gap a federally insured **Home Equity Conversion Mortgage (HECM)** is designed to address. In plain English: a way to access equity you've already built, **stay in your home**, and have **no required monthly mortgage payment** on the loan itself.

You're still responsible for property taxes, insurance, and upkeep — but for a lot of people, that's a very different picture than sending a mortgage payment every month.

**Reply with one word:** *payment*, *debt*, or *cash* — and I'll make sure {{user.first_name}} focuses on that on your call.

— {{custom_values.setter_display_name}}

---

### SMS — 2:00 PM

```
{{contact.first_name}} — quick one. Is the frustration more about monthly bills, or that your equity is "locked up" while costs keep rising?
```

**Compliance check:** PASS

---

## Day 3 — You keep ownership

**Theme:** Myth #1 — "The bank takes my house."

### SMS — 10:00 AM

```
One thing people get wrong: you don't give up your home. You stay on title. As long as you live there and keep up taxes and insurance, the home stays yours. Had you heard that before?
```

### Email — 4:00 PM

**Subject:** Do you still own your home?

---

Hi {{contact.first_name}},

This is the question we hear more than any other:

*"Will I lose my home?"*

**Short answer:** You remain the owner. Your name stays on title. You live in the home as your primary residence, pay property taxes and homeowners insurance, and maintain the property — same responsibilities you have today.

The loan is generally repaid when you sell, move out permanently, or pass away — not because you "run out of time" in the home.

{{user.first_name}} walks through exactly how that works for *your* home in about 20 minutes. No application required to have the conversation.

**Worth a quick call?** Reply *yes* and I'll find a time that works.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — qualified with taxes/insurance/occupancy obligations.

---

## Day 4 — No required monthly payment

**Theme:** This isn't "another bill every month."

### Email — 9:00 AM

**Subject:** What "no monthly payment" actually means

---

Hi {{contact.first_name}},

A lot of people hear "no monthly payment" and think it sounds too good to be true. Fair.

Here's what it actually means on a HECM:

- There is **no required monthly mortgage payment** on the loan
- Interest and fees are added to the loan balance over time — you're not writing a check each month for the mortgage itself
- You **can** make optional payments anytime if you want to slow balance growth

For many retired homeowners, the real shift is cash flow: money stops going *out* every month for the mortgage, or proceeds can be used to pay off an existing loan at closing.

**Segment 1 story (remove_mortgage_payment):** Carol sent the same mortgage payment for 18 years. She used proceeds to pay off her existing loan — and hasn't had a required monthly mortgage payment since.

That's the piece {{user.first_name}} runs the numbers on — for your home, not a generic example.

Reply *numbers* if you want to see what this could look like for you.

— {{custom_values.setter_display_name}}

---

### SMS — 3:00 PM

```
{{contact.first_name}} — still here. Are you mostly trying to free up cash each month, or is it more about a one-time need (repairs, debt, medical)?
```

**Compliance check:** PASS — Carol story = LO-approved composite; flag for client approval before deploy.

---

## Day 5 — Heirs & legacy

**Theme:** "My kids will inherit debt."

### SMS — 11:00 AM

```
Biggest worry we hear: kids and the house. It's a non-recourse loan — your family isn't personally on the hook. Heirs can keep the home or sell; any equity left after payoff goes to them. Want {{user.first_name}} to walk through how that works for your family?
```

### Email — 5:00 PM

**Subject:** What happens to your kids?

---

Hi {{contact.first_name}},

If you've hesitated because of your children, you're thinking like most parents we talk to.

A few facts that usually help:

1. **Your children are never personally responsible** for the loan. It's non-recourse — neither you nor your heirs owe more than the home's value when the loan comes due.
2. **Heirs have options.** They can sell the home, repay the loan from proceeds, and keep any remaining equity. Or they can keep the home by paying off the loan (under HECM rules).
3. **You're not "giving away" the house.** You're making a decision about how to use equity *while you're still living there.*

Legacy is personal. {{user.first_name}} doesn't rush anyone — he explains how the numbers work so you and your family can decide with clarity, not fear.

Reply *family* if that's the part you want to understand first.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — HUMAN REVIEW if adding 95% appraisal payoff detail for a specific state/client.

---

## Day 6 — What funds can be used for

**Theme:** Practical uses — repairs, debt, cushion, staying put.

### Email — 9:00 AM

**Subject:** 5 ways retired homeowners use this (that aren't "luxury")

---

Hi {{contact.first_name}},

Nobody needs a lecture on retirement. Here's what people in {{contact.state}} actually use home equity proceeds for:

1. **Pay off an existing mortgage** — eliminate a monthly payment
2. **Clear high-interest debt** — credit cards, medical bills, old balances
3. **Home repairs** — roof, HVAC, accessibility (ramps, walk-in shower)
4. **A financial cushion** — so one big expense doesn't wipe you out
5. **Staying in the home you love** — without downsizing before you're ready

You don't have to need all five. Most people have one or two that matter right now.

**Which of those is closest to your situation?** Reply with a number (1–5) and I'll note it for {{user.first_name}}.

— {{custom_values.setter_display_name}}

---

### SMS — 2:00 PM

```
Honest question {{contact.first_name}}: if you had access to your home equity tomorrow, what's the first thing you'd use it for?
```

**Segment 2 emphasis (pay_off_debt):** Swap SMS to: `A lot of folks did everything right — and still carried debt into retirement. Proceeds can pay off that debt without adding a new required monthly mortgage payment on the loan. Does that match what you're hoping for?`

**Compliance check:** PASS

---

## Day 7 — How you receive funds

**Theme:** Lump sum vs. line of credit vs. monthly draws.

### SMS — 10:00 AM

```
Most people don't know you can structure this different ways — lump sum, monthly draws, a HECM line of credit, or a mix. The unused portion of a line of credit can actually grow over time. Leaning toward one of those, or still deciding?
```

### Email — 4:00 PM

**Subject:** Lump sum, monthly income, or a line of credit?

---

Hi {{contact.first_name}},

One reason people get confused: they think there's only one way to receive funds. There isn't.

{{user.first_name}} usually walks through **four structures**:

| Option | Best when… |
|--------|----------------|
| **Lump sum** | You have a defined need now (pay off loan, major repair, debt) |
| **Monthly draws** | You want steady supplemental cash flow |
| **HECM line of credit** | You want a standby fund — unused portion **grows over time** |
| **Combination** | You want some cash now + flexibility later |

**Segment 3 (cash_out):** With about {{contact.estimated_home_value}} in value, there's often meaningful room to work with — exact amounts depend on your situation, rates, and payoff needs.

**Tom story (cash_out / strategic):** Tom set up a HECM line of credit and didn't draw for two years. The unused portion kept growing. When the market dipped, he drew from it instead of selling investments at a loss. That's the piece most people don't compare to a HELOC.

This is exactly what a 20-minute call is for: structure options for *your* home, not a brochure.

Reply *structure* and I'll get you on {{user.first_name}}'s calendar.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — HUMAN REVIEW if inserting home value amounts; Tom story = LO-approved composite.

---

## Day 8 — Regulated program / scam fear

**Theme:** Today's HECM vs. old horror stories. Meta leads often need this.

### Email — 9:00 AM

**Subject:** "I've heard horror stories" — you're right to be careful

---

Hi {{contact.first_name}},

If you're skeptical, good. There *have* been bad actors and outdated programs in this space.

Today's federally insured **HECM** is different:

- **FHA-insured** and heavily regulated
- **Independent counseling required** before you can close — a third party explains your options
- **All costs disclosed upfront** — no surprises at the closing table
- **You verify who you're talking to** — {{user.first_name}} is a licensed loan officer at [COMPANY]; happy to share NMLS, website, and direct line before you book

We're not asking you to "trust us blindly." We're asking for 20 minutes so you can decide with full information.

**Want {{user.first_name}}'s direct info to verify first?** Reply *verify* and I'll text his details.

— {{custom_values.setter_display_name}}

---

### SMS — 3:00 PM

```
{{contact.first_name}} — a lot of what floats around Facebook isn't accurate. {{user.first_name}} specializes in this and can show how today's program actually works. What's been holding you back from a quick call?
```

**Compliance check:** PASS — verification path offered; no competitor disparagement.

---

## Day 9 — Benefits question + social proof

**Theme:** SS/Medicare (defer to LO) + relatable story + booking CTA.

### SMS — 11:00 AM

```
Common question: does this affect Social Security or Medicare? Generally proceeds aren't counted as income for those programs — but that's one for {{user.first_name}} on a call, along with what makes sense for your home. Worth 20 minutes?
```

### Email — 5:00 PM

**Subject:** "I wish I'd looked into this sooner"

---

Hi {{contact.first_name}},

Ruth used proceeds from her home to pay off balances she'd carried for years — **without adding a new required monthly mortgage payment** on the loan itself.

She told us: *"I wish I'd understood this sooner. I wasn't looking for anything fancy — just to stop worrying."*

That's the conversation {{user.first_name}} has every week with homeowners in {{contact.state}}. Not a sales pitch. A clear walkthrough of costs, options, and whether it fits your plan.

**No application. No commitment. Just clarity.**

Reply *ready* and I'll send a few times that work this week.

— {{custom_values.setter_display_name}}

---

**Compliance check:** HUMAN REVIEW — SS/Medicare language is sensitive; confirm with LO/compliance before deploy. Ruth = LO-approved composite.

---

## Day 10 — Soft breakup + recap

**Theme:** Step back respectfully; leave door open. Merge to Phase 2 if no reply.

### SMS — 10:00 AM

```
{{contact.first_name}} — I don't want to crowd your messages if the timing's off. I'll step back for now. Whenever you want {{user.first_name}} to walk through what this could look like for your home, just reply here.
```

### Email — 2:00 PM

**Subject:** I'll pause here — door's always open

---

Hi {{contact.first_name}},

I've reached out a few times because you asked for information about your home — and I didn't want you to think you'd been forgotten.

Quick recap of what we've covered:

- You **keep ownership** of your home
- There's **no required monthly mortgage payment** on the loan
- Your **heirs aren't personally liable** — non-recourse protection
- Funds can be structured as a **lump sum, monthly draws, line of credit, or mix**
- It's a **regulated, FHA-insured program** — not the old programs you've maybe heard horror stories about

If any of that raised questions, {{user.first_name}} is still happy to walk through your specific situation — about 20 minutes, no pressure.

If now isn't the right time, no hard feelings. Reply whenever you're ready and we'll pick it up.

Warmly,

{{custom_values.setter_display_name}}
[PHONE]

---

**Compliance check:** PASS

---

# Phase 2 — Days 11–30 (long-term nurture A)

**Cadence:** One education touch every 2–3 days. Rotate themes not covered deeply in Phase 1. Lighter pressure; same reply-to-book goal.

**GHL:** New workflow triggered at Day 10 completion with no reply and no booking.

---

## Day 12 — Surviving vs. living

### SMS — 10:00 AM

```
{{contact.first_name}} — still here. A lot of retired homeowners tell us retirement feels like surviving, not living. Is that closer to how it feels, or are things mostly okay for now?
```

### Email — Day 12, 2:00 PM

**Subject:** Surviving retirement vs. actually living it

---

Hi {{contact.first_name}},

One feeling we hear constantly:

*"I worked my whole life — this isn't how retirement was supposed to be."*

Not luxury. Not travel every month. Just… not juggling every bill. Not delaying repairs. Not staying home because going out costs money.

Accessing home equity isn't about spending wildly. For most people, it's about **breathing room** — so retirement feels like retirement again.

If that resonates, reply *breathe* and I'll note it for {{user.first_name}}.

— {{custom_values.setter_display_name}}

---

## Day 15 — Safety net / one big expense

### SMS — 11:00 AM

```
What's scarier — monthly bills, or one big expense (roof, medical, car) wiping out what's left? A HECM line of credit can sit unused but grow — a cushion you don't have to touch until you need it. Ever looked at it that way?
```

### Email — Day 15, 4:00 PM

**Subject:** The expense nobody plans for

---

Hi {{contact.first_name}},

The fear we hear most after monthly bills:

*"One big expense could ruin me."*

A roof. HVAC. A medical bill. A car repair.

Many retired homeowners set up a **HECM line of credit** they don't draw on right away — but it's there if something hits. The unused portion can grow over time, so setting it up earlier can mean more available later.

That's planning, not panic.

Reply *cushion* if you want {{user.first_name}} to walk through how that could work for your home.

— {{custom_values.setter_display_name}}

---

## Day 18 — HECM vs. HELOC

### SMS — 10:00 AM

```
Quick comparison people miss: a HELOC usually requires monthly payments. A HECM line of credit doesn't — and the unused portion can grow. Had you been comparing the two?
```

### Email — Day 18, 3:00 PM

**Subject:** HECM line of credit vs. a HELOC — what's different?

---

Hi {{contact.first_name}},

If you've looked at home equity before, you may have seen a **HELOC** (home equity line of credit). Fair comparison — but they're not the same.

| | HELOC | HECM line of credit |
|--|-------|---------------------|
| Monthly mortgage payment | Usually required | **Not required** on the loan |
| Unused line | Typically static | **Can grow over time** |
| Typical borrower | Income/credit qualifying | Retired homeowners with strong equity |

Neither is right for everyone. {{user.first_name}} can compare both in the context of *your* home — about 20 minutes, no obligation.

Reply *compare* if that's useful.

— {{custom_values.setter_display_name}}

---

## Day 21 — Fees transparency

### SMS — 2:00 PM

```
Fair question we get: "What are the fees?" All costs are regulated and disclosed upfront — {{user.first_name}} breaks down every line on the call so you decide with full info. Want that walkthrough?
```

### Email — Day 21, 5:00 PM

**Subject:** "The fees are too high" — let's talk about that

---

Hi {{contact.first_name}},

Skepticism about fees is healthy. Nobody should sign anything without understanding costs.

On a HECM:

- Fees are **regulated and disclosed upfront** — origination, mortgage insurance, third-party costs
- {{user.first_name}} walks through **every cost** on the call before you decide anything
- Many homeowners weigh fees against **eliminating a monthly payment** or **high-interest debt** — but that's math for your situation, not a generic pitch

Reply *costs* if you want the full breakdown for your home.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — do not quote specific fee amounts unless LO-approved.

---

## Day 24 — Counseling requirement (trust builder)

### SMS — 11:00 AM

```
Did you know independent counseling is required before you can close? A third party explains your options — not just us. That's one reason today's program is different from old horror stories. Want {{user.first_name}} to explain the full process?
```

### Email — Day 24, 4:00 PM

**Subject:** You get a third-party counselor before anything closes

---

Hi {{contact.first_name}},

One safeguard many people don't know about:

Before you can close on a federally insured HECM, you must complete **independent counseling** with a HUD-approved counselor. They explain your options in plain English — separate from {{user.first_name}} or any lender.

That step exists so you're not deciding from a Facebook ad or a text thread alone.

{{user.first_name}}'s call is step one: see if it's worth exploring. Counseling comes later — only if you choose to move forward.

Reply *process* if you want the full roadmap.

— {{custom_values.setter_display_name}}

---

## Day 27 — Not mortgage-free required

### SMS — 10:00 AM

```
{{contact.first_name}} — common myth: you have to own your home free and clear. You don't. An existing mortgage is often paid off at closing with proceeds. Still carrying a payment today?
```

### Email — Day 27, 2:00 PM

**Subject:** You don't have to be mortgage-free to qualify

---

Hi {{contact.first_name}},

A myth that stops people from even asking:

*"I still have a mortgage — so this probably isn't for me."*

Often the opposite. Many retired homeowners still send a monthly payment. Proceeds at closing can pay off that existing loan — which is exactly why the **eliminate monthly payment** path is so common.

{{user.first_name}} runs those numbers in about 20 minutes. No application to start the conversation.

Reply *payment* if that's your situation.

— {{custom_values.setter_display_name}}

---

## Day 30 — Phase 2 close + handoff to Phase 3

### SMS — 10:00 AM

```
{{contact.first_name}} — it's been about a month since your form. A lot can change. If you want {{user.first_name}} to run fresh numbers with you, just reply. Otherwise I'll check in occasionally — no pressure.
```

### Email — Day 30, 3:00 PM

**Subject:** Still thinking it over? That's normal.

---

Hi {{contact.first_name}},

Most homeowners we talk to research for weeks before they feel ready. That's smart — not slow.

If you're still comparing options, here's what a call with {{user.first_name}} actually is:

- About **20 minutes**
- **Educational** — costs, structures, ownership, heirs
- **No application** required to have the conversation
- **No obligation** to move forward

If the timing still isn't right, no problem. I'll check in occasionally with something useful — and you can reply whenever.

Reply *ready* when you want times for this week.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — merge to Phase 3 if no reply.

---

# Phase 3 — Days 31–90 (long-term nurture B)

**Cadence:** ~1 email + 1 SMS every 10 days. Maintenance mode — value-first, minimal repetition.

**GHL:** Trigger at Day 30 completion with no reply and no booking.

---

## Day 40 — Property tax / rising costs

### SMS

```
Property taxes and insurance keep climbing in {{contact.state}} — even when income doesn't. Is that part of what's been on your mind lately?
```

### Email

**Subject:** When everything costs more except your income

---

Hi {{contact.first_name}},

Fixed income. Rising property taxes. Insurance going up every year.

It's one of the most common triggers we see — not a luxury purchase, just keeping up with the home you already own.

If costs have been the main squeeze, {{user.first_name}} can walk through whether home equity helps your specific situation. Reply *costs* if that's you.

— {{custom_values.setter_display_name}}

---

## Day 50 — Delayed repairs

### SMS

```
{{contact.first_name}} — a lot of homeowners delay roof or HVAC work because of cost. Is there something at the house you've been putting off?
```

### Email

**Subject:** The repair you've been putting off

---

Hi {{contact.first_name}},

Delaying a roof, HVAC, or plumbing fix doesn't make the problem smaller — it usually makes it more expensive later.

Proceeds from a HECM are commonly used for **home repairs and aging-in-place upgrades** — ramps, walk-in showers, better access — so you can stay safely in the home you love.

Reply *repair* if that's been on your list.

— {{custom_values.setter_display_name}}

---

## Day 60 — Family conversation

### SMS

```
Some folks want their kids in the conversation before they decide anything. Totally fair. Want to loop in a family member on a call with {{user.first_name}}, or handle it yourself first?
```

### Email

**Subject:** When your kids have opinions (and questions)

---

Hi {{contact.first_name}},

We hear this a lot:

*"My kids think it's a scam."* or *"I want them to understand before I do anything."*

Both are reasonable. {{user.first_name}} is happy to walk through ownership, heirs, and costs on a call — with or without family on the line.

Reply *family* or *solo* and I'll set it up accordingly.

— {{custom_values.setter_display_name}}

---

## Day 70 — Second look / still researching

### SMS

```
{{contact.first_name}} — still researching, or did you find another path? Either way, no judgment. If a second look would help, {{user.first_name}} is here.
```

### Email

**Subject:** Still researching? That's the right instinct.

---

Hi {{contact.first_name}},

Big financial decisions deserve time. If you're still gathering information, these are the five questions worth getting answered before you decide anything:

1. Do I keep ownership of my home?
2. What are the real costs — all of them?
3. What happens to my heirs?
4. How can I structure the funds (lump sum, line, monthly)?
5. What are my ongoing obligations (taxes, insurance, maintenance)?

{{user.first_name}} covers all five in one conversation. Reply *questions* when you're ready.

— {{custom_values.setter_display_name}}

---

## Day 80 — Planning ahead (calm urgency)

### SMS

```
Most homeowners start these conversations before finances become urgent — so they have more options. Still in planning mode, or feeling more pressed lately?
```

### Email

**Subject:** Planning ahead vs. reacting under pressure

---

Hi {{contact.first_name}},

The homeowners who feel best about their decision usually start **before** they're in crisis mode — when they still have room to compare structures and timing.

That doesn't mean rush. It means a conversation now can mean more flexibility later.

Reply *plan* if you'd like to talk options while you're still in control of the timing.

— {{custom_values.setter_display_name}}

---

**Compliance check:** PASS — calm planning urgency only; no false scarcity.

---

## Day 90 — Final long-term touch

### SMS

```
{{contact.first_name}} — last scheduled check-in from me for a while. Door's always open. Reply anytime and we'll pick it up with {{user.first_name}} — no hard feelings either way.
```

### Email

**Subject:** I'll go quiet for now — you know where to find us

---

Hi {{contact.first_name}},

This is my last scheduled note for a while.

You filled out a form because something about your home and your retirement deserved a closer look. That hasn't changed — even if the timing has.

Whenever you're ready:

- Reply to this email or text [PHONE]
- Ask for {{user.first_name}}'s direct line (*verify*)
- Request times (*ready*)

No pressure. No expiration date on good information.

Wishing you peace of mind either way,

{{custom_values.setter_display_name}}
On behalf of {{user.first_name}}, [COMPANY]

---

**Compliance check:** PASS — after Day 90, move to quarterly re-engagement or manual recycle per client policy.

---

## Subject line A/B options

| Day | Option A | Option B | Option C |
|-----|----------|----------|----------|
| 1 | You asked about your home — quick follow-up | {{contact.first_name}}, following up from your form | {{user.first_name}} asked me to reach out |
| 3 | Do you still own your home? | The #1 question we get | "Will I lose my home?" — honest answer |
| 5 | What happens to your kids? | Your family isn't on the hook | Legacy question — quick clarity |
| 8 | "I've heard horror stories" | You're right to be careful | How today's program is different |
| 10 | I'll pause here — door's always open | Quick recap + no pressure | Whenever you're ready |
| 30 | Still thinking it over? That's normal. | No rush — here's what the call actually is | Ready when you are |

## Reply keywords (bot routing)

| Keyword | Intent for AI/bot |
|---------|-------------------|
| `yes`, `ready`, `numbers`, `structure` | Book appointment |
| `verify` | Send LO NMLS, direct line, company URL |
| `payment`, `debt`, `cash`, `family`, `costs` | Qualify + book |
| `stop`, `unsubscribe` | Opt out immediately |

## Metrics

- Reply rate by day and phase
- Reply → book rate (post-AI handoff)
- Stop / opt-out rate (Day 1–2 spike = cadence too heavy)
- Email open rate by subject theme
- Messages to first reply
- Phase 2 vs Phase 3 reply recovery rate

## Sequence-level compliance summary

| Area | Status |
|------|--------|
| No guaranteed outcomes | PASS |
| No tax advice in SMS | PASS (Day 9 → defer to LO) |
| SS/Medicare | **HUMAN REVIEW** before deploy |
| Age in copy | PASS ("retired homeowners") |
| Composite stories (Carol, Ruth, Tom) | **LO approval** before client deploy |
| Dollar amounts | PASS (merge field only; no invented figures) |
| High-pressure urgency | PASS |

## Related docs

- [RM iMessage Intent Drip (7-Day)](rm-imessage-intent-drip-7day.md) — intent-segmented SMS-only path
- [RM iMessage Appointment Follow-Up](rm-imessage-appointment-followup.md) — post-booking
- [RM iMessage Second-Booking Follow-Up](rm-imessage-second-booking-followup.md) — rebook
- [RM Text Drip 2025](rm-text-drip-2025.md) — legacy longer-cycle SMS
- [RM Lead Nurture Drip Sequence](rm-lead-nurture-drip-sequence.md) — Skool-origin extended nurture
- [RM Borrower Objections](../reverse-mortgage-dna/rm-borrower-objections.md)
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Open questions

- [ ] Per-client approval of story names and state-specific disclaimers
- [ ] A/B lighter cadence (email-only some days) for opt-out-sensitive lists
- [ ] Merge vs. replace [RM iMessage Intent Drip (7-Day)](rm-imessage-intent-drip-7day.md) when both email and SMS are live
- [ ] Post–Day 90 quarterly re-engagement workflow (not yet authored)
