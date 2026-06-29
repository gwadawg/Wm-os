---
team_title: "Reverse Mortgage Lead Nurture — Meta Drip"
team_role: client_success
team_doc_type: playbook
source_repo_path: "docs/client-fulfillment/client-marketing/clients/momeson-johnson-meta-drip.md"
approved: true
cover_title: "Reverse Mortgage Lead Nurture"
cover_subtitle: "90-day email + SMS drip for Meta form leads"
cover_audience: "Rick Momeson & Lindsay Johnson  |  Client Playbook  |  June 2026"
footer: "Prepared by Waiz Media  |  Rick Momeson & Lindsay Johnson  |  June 2026"
---

# 1. Overview

Educational email + SMS nurture for homeowners who submit your **Meta (Facebook/Instagram) instant form** and have not yet replied or booked. Every message is sent **directly from you** — the loan officer. Goal: educate, build trust, and get a reply — then your AI booking flow takes over.

> **📌 NORTH STAR**
>
> Turn cold Meta leads into warm conversations — through value-first education from you personally, not pressure.

**Who uses this:** Rick Momeson, Lindsay Johnson, or any loan officer on your team running this workflow.

**When it runs:** After a Meta form submit, starting ~4 hours after lead entry (speed-to-lead bot still handles the first 0–5 minutes).

**What you need in GHL before launch:**

- `{{contact.first_name}}`, `{{contact.state}}`, `{{contact.estimated_home_value}}` populated from the form
- `{{user.first_name}}` = your first name (maps to **{LO's Name}** in the copy below)
- Replace `[Company Name]` and `[Phone]` with your live values
- Every message below says **{LO's Name}** — swap that for your name when reading, or use `{{user.first_name}}` in GHL

## Cadence at a glance

| Phase | Days | What happens |
| --- | --- | --- |
| **Phase 1** | 1–10 | ~18 touches — primary education + booking CTAs |
| **Phase 2** | 11–30 | 8 touches — deeper education, lighter pressure |
| **Phase 3** | 31–90 | 6 touches — maintenance nurture |

## Workflow rules

1. **Any reply** → stop all drip workflows → AI books the appointment.
2. **Appointment booked** → drip off → appointment reminders only.
3. **Day 10, no reply** → move to Phase 2.
4. **Day 30, no reply** → move to Phase 3.
5. **STOP / unsubscribe** → remove immediately.

## Intent routing (optional)

If your form captures intent, swap the Day 1 opener line:

| Form intent | Opener line |
| --- | --- |
| Remove mortgage payment | getting rid of your monthly mortgage payment |
| Pay off debt | using home equity to clear debt |
| Cash out | accessing cash from your home |
| Unknown | using your home equity |

## Language guide

| Instead of… | Use… |
| --- | --- |
| "reverse mortgage" in every message | the **outcome** they asked for (payment, debt, cash) |
| "homeowners 62+" | **retired homeowners** |
| "tax-free cash" | defer tax questions to the call |
| Generic "equity options" | **eliminate monthly payment**, **clear debt**, **access cash from home** |
| Third-person ("your loan officer will…") | **First person** — "I'll walk you through…" |

> **⚠️ IMPORTANT**
>
> Approve the Carol, Ruth, and Tom stories before going live. Social Security / Medicare lines need a quick compliance review before deploy.

# 2. Phase 1 — Days 1–10

## Day 1 — Acknowledge the form

**Theme:** They came from Facebook. What pushed them to look now?

**Send times:** SMS +4 hrs · SMS +6 hrs (if no reply) · Email +5 hrs

**SMS — first touch (+4 hrs)**

```
Hey {{contact.first_name}}, it's {LO's Name}. I saw you filled out a form on Facebook about using your home equity.

What pushed you to look now — the payment itself, debt, or having cash available when you need it?
```

**SMS — follow-up (+6 hrs, if no reply)**

```
A lot of retired homeowners in {{contact.state}} have strong equity but tight monthly cash flow. I help people see what's actually possible — no pressure, about 20 minutes. Does that sound like what you were after?
```

**Email — subject:** You asked about your home — quick follow-up

```
Hi {{contact.first_name}},

You recently filled out a form on Facebook about your home equity. I'm {LO's Name} at [Company Name].

A lot of retired homeowners tell me the same thing: "My house is worth a lot, but I can't use any of it." That's exactly what I specialize in.

One quick question so I send you the right info:

What matters most to you right now?

1. Stopping a monthly mortgage payment
2. Clearing debt that's eating into retirement
3. Having cash or a line of credit available when you need it
4. Still figuring it out

Just reply to this email (or text me back at [Phone]) with a number or a few words. No application. No commitment.

Talk soon,

{LO's Name}
[Company Name]
[Phone]
```

## Day 2 — Trapped equity

**Theme:** House-rich, cash-poor — they're not alone.

**Send times:** Email 9:00 AM · SMS 2:00 PM

**Email — subject:** "My home is worth a lot, but I can't touch it"

```
Hi {{contact.first_name}},

If you've ever thought that sentence, you're not alone.

Many retired homeowners in {{contact.state}} are in the same spot:

- Fixed income that doesn't keep up with groceries, utilities, or insurance
- Savings that get a little smaller every year
- A home that keeps going up in value — but no easy way to use that value without selling

That's the gap a federally insured Home Equity Conversion Mortgage (HECM) is designed to address. In plain English: a way to access equity you've already built, stay in your home, and have no required monthly mortgage payment on the loan itself.

You're still responsible for property taxes, insurance, and upkeep — but for a lot of people, that's a very different picture than sending a mortgage payment every month.

Reply with one word: payment, debt, or cash — and I'll make sure we focus on that when we talk.

— {LO's Name}
```

**SMS — 2:00 PM**

```
{{contact.first_name}} — quick one. Is the frustration more about monthly bills, or that your equity is "locked up" while costs keep rising?
```

## Day 3 — You keep ownership

**Theme:** "The bank takes my house" — myth bust.

**Send times:** SMS 10:00 AM · Email 4:00 PM

**SMS**

```
One thing people get wrong: you don't give up your home. You stay on title. As long as you live there and keep up taxes and insurance, the home stays yours. Had you heard that before?
```

**Email — subject:** Do you still own your home?

```
Hi {{contact.first_name}},

This is the question I hear more than any other:

"Will I lose my home?"

Short answer: You remain the owner. Your name stays on title. You live in the home as your primary residence, pay property taxes and homeowners insurance, and maintain the property — same responsibilities you have today.

The loan is generally repaid when you sell, move out permanently, or pass away — not because you "run out of time" in the home.

I can walk through exactly how that works for your home in about 20 minutes. No application required to have the conversation.

Worth a quick call? Reply yes and I'll find a time that works.

— {LO's Name}
```

## Day 4 — No required monthly payment

**Theme:** This isn't another bill every month.

**Send times:** Email 9:00 AM · SMS 3:00 PM

**Email — subject:** What "no monthly payment" actually means

```
Hi {{contact.first_name}},

A lot of people hear "no monthly payment" and think it sounds too good to be true. Fair.

Here's what it actually means on a HECM:

- There is no required monthly mortgage payment on the loan
- Interest and fees are added to the loan balance over time — you're not writing a check each month for the mortgage itself
- You can make optional payments anytime if you want to slow balance growth

For many retired homeowners, the real shift is cash flow: money stops going out every month for the mortgage, or proceeds can be used to pay off an existing loan at closing.

Carol sent the same mortgage payment for 18 years. She used proceeds to pay off her existing loan — and hasn't had a required monthly mortgage payment since.

That's the piece I run the numbers on — for your home, not a generic example.

Reply numbers if you want to see what this could look like for you.

— {LO's Name}
```

**SMS — 3:00 PM**

```
{{contact.first_name}} — still here. Are you mostly trying to free up cash each month, or is it more about a one-time need (repairs, debt, medical)?
```

## Day 5 — Heirs and legacy

**Theme:** "My kids will inherit debt."

**Send times:** SMS 11:00 AM · Email 5:00 PM

**SMS**

```
Biggest worry I hear: kids and the house. It's a non-recourse loan — your family isn't personally on the hook. Heirs can keep the home or sell; any equity left after payoff goes to them. Want me to walk through how that works for your family?
```

**Email — subject:** What happens to your kids?

```
Hi {{contact.first_name}},

If you've hesitated because of your children, you're thinking like most parents I talk to.

A few facts that usually help:

1. Your children are never personally responsible for the loan. It's non-recourse — neither you nor your heirs owe more than the home's value when the loan comes due.
2. Heirs have options. They can sell the home, repay the loan from proceeds, and keep any remaining equity. Or they can keep the home by paying off the loan (under HECM rules).
3. You're not "giving away" the house. You're making a decision about how to use equity while you're still living there.

Legacy is personal. I don't rush anyone — I'll explain how the numbers work so you and your family can decide with clarity, not fear.

Reply family if that's the part you want to understand first.

— {LO's Name}
```

## Day 6 — What funds can be used for

**Theme:** Practical uses — not luxury.

**Send times:** Email 9:00 AM · SMS 2:00 PM

**Email — subject:** 5 ways retired homeowners use this (that aren't "luxury")

```
Hi {{contact.first_name}},

Nobody needs a lecture on retirement. Here's what people in {{contact.state}} actually use home equity proceeds for:

1. Pay off an existing mortgage — eliminate a monthly payment
2. Clear high-interest debt — credit cards, medical bills, old balances
3. Home repairs — roof, HVAC, accessibility (ramps, walk-in shower)
4. A financial cushion — so one big expense doesn't wipe you out
5. Staying in the home you love — without downsizing before you're ready

You don't have to need all five. Most people have one or two that matter right now.

Which of those is closest to your situation? Reply with a number (1–5).

— {LO's Name}
```

**SMS — 2:00 PM**

```
Honest question {{contact.first_name}}: if you had access to your home equity tomorrow, what's the first thing you'd use it for?
```

## Day 7 — How you receive funds

**Theme:** Lump sum, line of credit, or monthly draws.

**Send times:** SMS 10:00 AM · Email 4:00 PM

**SMS**

```
Most people don't know you can structure this different ways — lump sum, monthly draws, a HECM line of credit, or a mix. The unused portion of a line of credit can actually grow over time. Leaning toward one of those, or still deciding?
```

**Email — subject:** Lump sum, monthly income, or a line of credit?

```
Hi {{contact.first_name}},

One reason people get confused: they think there's only one way to receive funds. There isn't.

I usually walk through four structures:

Lump sum — best when you have a defined need now (pay off loan, major repair, debt)

Monthly draws — best when you want steady supplemental cash flow

HECM line of credit — best when you want a standby fund; unused portion grows over time

Combination — some cash now plus flexibility later

Tom set up a HECM line of credit and didn't draw for two years. The unused portion kept growing. When the market dipped, he drew from it instead of selling investments at a loss. That's the piece most people don't compare to a HELOC.

This is exactly what a 20-minute call is for: structure options for your home, not a brochure.

Reply structure and I'll find a time that works.

— {LO's Name}
```

## Day 8 — Regulated program / scam fear

**Theme:** Today's HECM vs. old horror stories. Critical for Meta leads.

**Send times:** Email 9:00 AM · SMS 3:00 PM

**Email — subject:** "I've heard horror stories" — you're right to be careful

```
Hi {{contact.first_name}},

If you're skeptical, good. There have been bad actors and outdated programs in this space.

Today's federally insured HECM is different:

- FHA-insured and heavily regulated
- Independent counseling required before you can close — a third party explains your options
- All costs disclosed upfront — no surprises at the closing table
- You can verify who you're talking to — I'm a licensed loan officer at [Company Name]; happy to share my NMLS, website, and direct line before we talk

I'm not asking you to trust blindly. I'm asking for 20 minutes so you can decide with full information.

Want my direct info to verify first? Reply verify and I'll send it over.

— {LO's Name}
```

**SMS — 3:00 PM**

```
{{contact.first_name}} — a lot of what floats around Facebook isn't accurate. I specialize in this and can show how today's program actually works. What's been holding you back from a quick call?
```

## Day 9 — Social proof + benefits question

**Theme:** Ruth's story + Social Security / Medicare (address on the call).

**Send times:** SMS 11:00 AM · Email 5:00 PM

**SMS**

```
Common question: does this affect Social Security or Medicare? Generally proceeds aren't counted as income for those programs — but I'd want to walk through how it applies to your situation on a quick call. Worth 20 minutes?
```

**Email — subject:** "I wish I'd looked into this sooner"

```
Hi {{contact.first_name}},

Ruth used proceeds from her home to pay off balances she'd carried for years — without adding a new required monthly mortgage payment on the loan itself.

She told me: "I wish I'd understood this sooner. I wasn't looking for anything fancy — just to stop worrying."

That's the conversation I have every week with homeowners in {{contact.state}}. Not a sales pitch. A clear walkthrough of costs, options, and whether it fits your plan.

No application. No commitment. Just clarity.

Reply ready and I'll send a few times that work this week.

— {LO's Name}
```

## Day 10 — Soft breakup + recap

**Theme:** Step back respectfully. Move to Phase 2 if no reply.

**Send times:** SMS 10:00 AM · Email 2:00 PM

**SMS**

```
{{contact.first_name}} — I don't want to crowd your messages if the timing's off. I'll step back for now. Whenever you want me to walk through what this could look like for your home, just reply here.
```

**Email — subject:** I'll pause here — door's always open

```
Hi {{contact.first_name}},

I've reached out a few times because you asked for information about your home — and I didn't want you to think you'd been forgotten.

Quick recap of what we've covered:

- You keep ownership of your home
- There's no required monthly mortgage payment on the loan
- Your heirs aren't personally liable — non-recourse protection
- Funds can be structured as a lump sum, monthly draws, line of credit, or mix
- It's a regulated, FHA-insured program — not the old programs you've maybe heard horror stories about

If any of that raised questions, I'm still happy to walk through your specific situation — about 20 minutes, no pressure.

If now isn't the right time, no hard feelings. Reply whenever you're ready and we'll pick it up.

Warmly,

{LO's Name}
[Company Name]
[Phone]
```

# 3. Phase 2 — Days 11–30

**Cadence:** One education touch every 2–3 days. Same reply-to-book goal, lighter pressure.

## Day 12 — Surviving vs. living

**SMS (10:00 AM)**

```
{{contact.first_name}} — still here. A lot of retired homeowners tell me retirement feels like surviving, not living. Is that closer to how it feels, or are things mostly okay for now?
```

**Email — subject:** Surviving retirement vs. actually living it

```
Hi {{contact.first_name}},

One feeling I hear constantly:

"I worked my whole life — this isn't how retirement was supposed to be."

Not luxury. Not travel every month. Just… not juggling every bill. Not delaying repairs. Not staying home because going out costs money.

Accessing home equity isn't about spending wildly. For most people, it's about breathing room — so retirement feels like retirement again.

If that resonates, reply breathe and we can talk.

— {LO's Name}
```

## Day 15 — Safety net

**SMS (11:00 AM)**

```
What's scarier — monthly bills, or one big expense (roof, medical, car) wiping out what's left? A HECM line of credit can sit unused but grow — a cushion you don't have to touch until you need it. Ever looked at it that way?
```

**Email — subject:** The expense nobody plans for

```
Hi {{contact.first_name}},

The fear I hear most after monthly bills:

"One big expense could ruin me."

A roof. HVAC. A medical bill. A car repair.

Many retired homeowners set up a HECM line of credit they don't draw on right away — but it's there if something hits. The unused portion can grow over time, so setting it up earlier can mean more available later.

That's planning, not panic.

Reply cushion if you want me to walk through how that could work for your home.

— {LO's Name}
```

## Day 18 — HECM vs. HELOC

**SMS (10:00 AM)**

```
Quick comparison people miss: a HELOC usually requires monthly payments. A HECM line of credit doesn't — and the unused portion can grow. Had you been comparing the two?
```

**Email — subject:** HECM line of credit vs. a HELOC — what's different?

```
Hi {{contact.first_name}},

If you've looked at home equity before, you may have seen a HELOC (home equity line of credit). Fair comparison — but they're not the same.

HELOC: monthly payment usually required · line typically static · income/credit qualifying

HECM line of credit: no required monthly mortgage payment on the loan · unused portion can grow over time · built for retired homeowners with strong equity

Neither is right for everyone. I can compare both in the context of your home — about 20 minutes, no obligation.

Reply compare if that's useful.

— {LO's Name}
```

## Day 21 — Fees transparency

**SMS (2:00 PM)**

```
Fair question I get: "What are the fees?" All costs are regulated and disclosed upfront — I'll break down every line on our call so you decide with full info. Want that walkthrough?
```

**Email — subject:** "The fees are too high" — let's talk about that

```
Hi {{contact.first_name}},

Skepticism about fees is healthy. Nobody should sign anything without understanding costs.

On a HECM:

- Fees are regulated and disclosed upfront — origination, mortgage insurance, third-party costs
- I walk through every cost on the call before you decide anything
- Many homeowners weigh fees against eliminating a monthly payment or high-interest debt — but that's math for your situation, not a generic pitch

Reply costs if you want the full breakdown for your home.

— {LO's Name}
```

## Day 24 — Counseling requirement

**SMS (11:00 AM)**

```
Did you know independent counseling is required before you can close? A third party explains your options — not just me. That's one reason today's program is different from old horror stories. Want me to explain the full process?
```

**Email — subject:** You get a third-party counselor before anything closes

```
Hi {{contact.first_name}},

One safeguard many people don't know about:

Before you can close on a federally insured HECM, you must complete independent counseling with a HUD-approved counselor. They explain your options in plain English — separate from me or any lender.

That step exists so you're not deciding from a Facebook ad or a text thread alone.

Our call is step one: see if it's worth exploring. Counseling comes later — only if you choose to move forward.

Reply process if you want the full roadmap.

— {LO's Name}
```

## Day 27 — Not mortgage-free required

**SMS (10:00 AM)**

```
{{contact.first_name}} — common myth: you have to own your home free and clear. You don't. An existing mortgage is often paid off at closing with proceeds. Still carrying a payment today?
```

**Email — subject:** You don't have to be mortgage-free to qualify

```
Hi {{contact.first_name}},

A myth that stops people from even asking:

"I still have a mortgage — so this probably isn't for me."

Often the opposite. Many retired homeowners still send a monthly payment. Proceeds at closing can pay off that existing loan — which is exactly why the eliminate monthly payment path is so common.

I run those numbers in about 20 minutes. No application to start the conversation.

Reply payment if that's your situation.

— {LO's Name}
```

## Day 30 — Phase 2 close

**SMS (10:00 AM)**

```
{{contact.first_name}} — it's been about a month since your form. A lot can change. If you want me to run fresh numbers with you, just reply. Otherwise I'll check in occasionally — no pressure.
```

**Email — subject:** Still thinking it over? That's normal.

```
Hi {{contact.first_name}},

Most homeowners I talk to research for weeks before they feel ready. That's smart — not slow.

If you're still comparing options, here's what a call with me actually is:

- About 20 minutes
- Educational — costs, structures, ownership, heirs
- No application required to have the conversation
- No obligation to move forward

If the timing still isn't right, no problem. I'll check in occasionally with something useful — and you can reply whenever.

Reply ready when you want times for this week.

— {LO's Name}
```

# 4. Phase 3 — Days 31–90

**Cadence:** ~1 email + 1 SMS every 10 days. Maintenance mode.

## Day 40 — Rising costs

**SMS**

```
Property taxes and insurance keep climbing in {{contact.state}} — even when income doesn't. Is that part of what's been on your mind lately?
```

**Email — subject:** When everything costs more except your income

```
Hi {{contact.first_name}},

Fixed income. Rising property taxes. Insurance going up every year.

It's one of the most common triggers I see — not a luxury purchase, just keeping up with the home you already own.

If costs have been the main squeeze, I can walk through whether home equity helps your specific situation. Reply costs if that's you.

— {LO's Name}
```

## Day 50 — Delayed repairs

**SMS**

```
{{contact.first_name}} — a lot of homeowners delay roof or HVAC work because of cost. Is there something at the house you've been putting off?
```

**Email — subject:** The repair you've been putting off

```
Hi {{contact.first_name}},

Delaying a roof, HVAC, or plumbing fix doesn't make the problem smaller — it usually makes it more expensive later.

Proceeds from a HECM are commonly used for home repairs and aging-in-place upgrades — ramps, walk-in showers, better access — so you can stay safely in the home you love.

Reply repair if that's been on your list.

— {LO's Name}
```

## Day 60 — Family conversation

**SMS**

```
Some folks want their kids in the conversation before they decide anything. Totally fair. Want to loop in a family member on a call, or handle it yourself first?
```

**Email — subject:** When your kids have opinions (and questions)

```
Hi {{contact.first_name}},

I hear this a lot:

"My kids think it's a scam." or "I want them to understand before I do anything."

Both are reasonable. I'm happy to walk through ownership, heirs, and costs on a call — with or without family on the line.

Reply family or solo and I'll set it up accordingly.

— {LO's Name}
```

## Day 70 — Still researching

**SMS**

```
{{contact.first_name}} — still researching, or did you find another path? Either way, no judgment. If a second look would help, I'm here.
```

**Email — subject:** Still researching? That's the right instinct.

```
Hi {{contact.first_name}},

Big financial decisions deserve time. If you're still gathering information, these are the five questions worth getting answered before you decide anything:

1. Do I keep ownership of my home?
2. What are the real costs — all of them?
3. What happens to my heirs?
4. How can I structure the funds (lump sum, line, monthly)?
5. What are my ongoing obligations (taxes, insurance, maintenance)?

I cover all five in one conversation. Reply questions when you're ready.

— {LO's Name}
```

## Day 80 — Planning ahead

**SMS**

```
Most homeowners start these conversations before finances become urgent — so they have more options. Still in planning mode, or feeling more pressed lately?
```

**Email — subject:** Planning ahead vs. reacting under pressure

```
Hi {{contact.first_name}},

The homeowners who feel best about their decision usually start before they're in crisis mode — when they still have room to compare structures and timing.

That doesn't mean rush. It means a conversation now can mean more flexibility later.

Reply plan if you'd like to talk options while you're still in control of the timing.

— {LO's Name}
```

## Day 90 — Final touch

**SMS**

```
{{contact.first_name}} — last scheduled check-in from me for a while. Door's always open. Reply anytime — no hard feelings either way.
```

**Email — subject:** I'll go quiet for now — you know where to find me

```
Hi {{contact.first_name}},

This is my last scheduled note for a while.

You filled out a form because something about your home and your retirement deserved a closer look. That hasn't changed — even if the timing has.

Whenever you're ready:

- Reply to this email or text [Phone]
- Ask for my direct line (reply verify)
- Request times (reply ready)

No pressure. No expiration date on good information.

Wishing you peace of mind either way,

{LO's Name}
[Company Name]
[Phone]
```

# 5. Reply keywords (GHL / AI routing)

| Lead replies… | What happens |
| --- | --- |
| yes, ready, numbers, structure | Book appointment |
| verify | Send your NMLS, direct line, company URL |
| payment, debt, cash, family, costs | Qualify intent + book |
| stop, unsubscribe | Remove from all workflows immediately |

# 6. Before you go live

1. Replace **{LO's Name}** with your name in GHL — use `{{user.first_name}}` in live workflows.
2. Replace **[Company Name]** and **[Phone]** everywhere.
3. Confirm **Carol, Ruth, and Tom** stories (composites — adjust or remove if needed).
4. Have compliance review the **Social Security / Medicare** line on Day 9 before deploy.
5. Test workflow: form submit → speed-to-lead bot → Day 1 drip → reply → AI books.
6. Watch **opt-out rate** in Days 1–2 — if high, drop the Day 1 evening SMS.

> **💡 PRO TIP**
>
> Rick and Lindsay each run their own version — same copy, different name. In GHL, `{{user.first_name}}` automatically pulls the assigned LO's first name so you don't need separate workflows per person.
