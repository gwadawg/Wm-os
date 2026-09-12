---
title: 10-Day DSCR Self-Serve CRM Drip — LO First Person
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-11
review_cycle: monthly
artifact_type: script
product: dscr
shareability: paying-client
related_docs:
  - docs/client-fulfillment/dscr-dna/playbook-dscr-self-serve-lead-nurture.md
  - docs/client-fulfillment/dscr-dna/intelligence-icp-dscr.md
  - docs/client-fulfillment/dscr-dna/dscr-compliance-guardrails.md
  - docs/client-fulfillment/dscr-dna/dscr-nurture-and-booking-laura.md
  - docs/client-fulfillment/dscr-dna/dscr-objection-handling-guide.md
---

# 10-Day DSCR Self-Serve CRM Drip — LO First Person

> **DRAFT — REFINANCE ONLY · NUMBER-FREE · LO FIRST PERSON.** For DSCR clients who **do not** use the Waiz call center. The loan officer is the sender. Paste into the client's own CRM. Do **not** run this alongside [Laura](dscr-nurture-and-booking-laura.md).

## Purpose

Turn opted-in DSCR refinance leads into a reply and a booked call with the loan officer — by sounding like the LO actually wrote it, teaching one useful thing per day, and never reading like a template or a bot.

## Scope

| In | Out |
|----|-----|
| Days 1–10, new form / ad leads who have not replied or booked | Waiz call-center / Laura / CloseBot |
| LO first-person SMS (primary) + optional email | Post-consult, no-show, appointment reminders |
| Client's own CRM (GHL, Follow Up Boss, Lofty, etc.) | Purchase, primary residence, RM voice |
| Universal copy — one sequence for all DSCR refi leads | Per-persona branching, invented rates / LTV / day-counts |

## Who this is for

The lead is an **investor who already owns a rental**. They came in from an ad or form. They are not talking to Waiz setters. The next conversation is with the LO.

## Trigger

Lead submits the form (or is imported as a new DSCR lead) → no reply and no booking after the first human/speed-to-lead touch (if the client even has one) → Day 1 fires.

If the client has no speed-to-lead text, Day 1 **is** the first touch. Send it as soon as the lead lands, inside quiet hours.

## Inputs

| Token | Meaning | Typical CRM field |
|-------|---------|-------------------|
| `{{contact.first_name}}` | Lead first name | Contact first name |
| `{{custom_values.lo_first_name}}` | LO first name — **required** | Custom value, or GHL `{{user.first_name}}` if the assigned user is the LO |
| `{{custom_values.booking_link}}` | LO calendar | Custom value |
| `{{custom_values.company_name}}` | Brokerage / shop name | Custom value |
| `{{custom_values.lo_phone}}` | LO direct line (email sign-off) | Custom value |

**From the LO's own number:** after Day 1, drop the name intro. The phone already says who it is.

**From a company / CRM number:** keep `{{custom_values.lo_first_name}}` in the Day 1 opener and sign a few later texts so they know it is not "the team."

## Outputs

| Event | Action |
|-------|--------|
| Any inbound reply | Kill the drip. LO (or their VA) answers and books. |
| Call booked | Kill the drip. Reminders only — not this sequence. |
| STOP / unsubscribe | Kill immediately. Honor it. |
| Day 10, no reply | Stop. Optional monthly check-in later — not written here. |

## Quality bar

- Sounds like a person who does this for a living, not a sequence.
- Peer-to-operator. Name **DSCR**. Refinance of a rental they already own.
- One idea per day. Not every text asks for a booking.
- No "just checking in," "circling back," "bumping this," "are my texts coming through," "I'll close your file," "last chance."
- No invented numbers. No guarantees. "May qualify." Tax / entity questions → their CPA.
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) on every send.

## Voice (read this before you edit a line)

Write like the LO sat down with their phone. Investors smell stock copy.

| Do | Don't |
|----|-------|
| Short. Specific. A little dry. | Feature checklists, emoji stacks, "Hope you're doing well" |
| Vary the open. Some days skip the first name. | Same opener every day ("Hey {{contact.first_name}}, just wanted to…") |
| Teach one thing, then ask one question — or don't ask | Pitch + calendar link on every touch |
| Admit the rate trade (Day 7) | "Best rates," "guaranteed approval," "fast close" |
| Composite stories, first name only | Fake funded stats, cities, or "I just closed $X" |
| Leave a sentence a little uneven | Perfectly parallel three-bullet emails |

**Banned filler:** touching base, following up, circling back, looping back, wanted to reach out, hope this helps, exciting opportunity, as a reminder, per my last.

## Cadence

One SMS per day, lead-local **8am–7pm**. Optional email the same morning on the days marked below — same idea, a bit more room. Do not send two SMS in one day.

| Day | Theme | Belief you are moving | Channel | Ask |
|-----|-------|------------------------|---------|-----|
| 1 | I'm the LO. What are you actually trying to do? | "Who is this / is this a bot?" | SMS + email | Reply with the situation |
| 2 | The property qualifies itself | "They'll want my tax returns" | SMS | Soft — rents + current loan |
| 3 | Write-offs are not the file | "My DTI killed conventional" | SMS + email | Which blocker they hit |
| 4 | Sitting equity is inventory | "Leaving it there is prudent" | SMS | None — just the idea |
| 5 | The bank's box is not the only box | "I already got told no" | SMS | Have they been turned down |
| 6 | Dana (composite) | "People like me don't get these" | SMS + email | Reply if it sounds familiar |
| 7 | The rate is the trade, not the point | "DSCR is too expensive" | SMS | 15 min on *their* numbers |
| 8 | What the call actually is | "This will be a sales pitch" | SMS + email | Calendar or a reply time |
| 9 | Hard-money was never the plan | "I'll deal with the balloon later" | SMS | Is that the situation |
| 10 | Door stays open | Silence ≠ no | SMS + email | Reply whenever |

---

# The sequence

## Day 1 — Open like a person

**Theme:** You came through. I'm the one who would look at this. What's going on?

### SMS — send when the lead lands (or +1–2 hrs if they already got a thank-you)

```
{{contact.first_name}} — {{custom_values.lo_first_name}} here. You came through looking at a DSCR refinance on a rental.

I do these. We look at the property's rent, not your tax returns.

What's the actual situation — trying to pull equity, get off a short-term note, or just see if the numbers work?

Txt STOP to opt out
```

**If the SMS is already coming from the LO's cell, use this instead:**

```
{{contact.first_name}} — saw you came through on a DSCR refi. I look at these on the rent, not the tax returns.

What are you trying to do with the property — cash out, clean up the current loan, or just see if it even works?

Txt STOP to opt out
```

### Email — same day, morning if SMS already went

**Subject:** you came through on a DSCR refi
**Alt:** {{contact.first_name}} — {{custom_values.lo_first_name}} here

---

{{contact.first_name}} —

You came through looking at a DSCR refinance. That's me. I work with investors who already own the rental and want a better position on it — cash out, a cleaner long-term loan, or an exit off something short-term.

I don't need your tax returns to start the conversation. I need a rough sense of the rent and what you owe.

What's going on with the property? Reply here, or grab a time if that's easier: {{custom_values.booking_link}}

{{custom_values.lo_first_name}}
{{custom_values.company_name}}
{{custom_values.lo_phone}}

---

**Compliance check:** PASS — lead source acknowledged; refinance / investment; STOP on first SMS; no numbers or guarantees.

---

## Day 2 — How this actually works

**Theme:** Conventional underwrites you. DSCR underwrites the rental.

### SMS

```
Most lenders are still underwriting you — W-2s, returns, DTI.

DSCR flips that. The rental has to cover its own payment. That's the file.

If you've been told your income docs are the problem, they're usually looking at the wrong thing.

Want me to run yours? I just need rough rents and the current loan.
```

**Compliance check:** PASS — mechanism only; "want me to run" is not an approval.

---

## Day 3 — Write-offs are not a character flaw

**Theme:** Tax strategy that makes you look broke on paper is normal in this world.

### SMS

```
{{contact.first_name}} — this is the one I hear the most.

Self-employed. Returns look terrible on purpose. Conventional says the DTI doesn't work.

That's a tax-return problem, not a property problem. DSCR doesn't use the returns to qualify.

Was that the blocker on your side, or was it something else — property count, a balloon, credit?
```

### Email

**Subject:** your tax returns are not the property
**Alt:** the DTI conversation is usually the wrong one

---

{{contact.first_name}} —

A lot of investors I talk to are good operators and bad conventional borrowers. Not because the rental is weak. Because they run write-offs like they're supposed to, and the bank reads that as "broke."

DSCR doesn't care about that story. It cares whether the rent covers the payment on that door.

I'm not telling you to change how you file. That's your CPA. I'm telling you the qualification basis is different, so the thing that killed the last refi may not matter here.

If that was your situation, just say so. I'll tell you what I need to look at it.

{{custom_values.lo_first_name}}

---

**Compliance check:** PASS — no tax advice; CPA routed; no "you qualify."

---

## Day 4 — Idle equity (no ask)

**Theme:** Sitting equity is not automatically the smart play.

### SMS

```
One thing I keep seeing.

Investors leave a paid-down rental alone because it feels responsible. Meanwhile that equity is just sitting there. It's inventory.

You don't have to sell the door to use it. A DSCR cash-out is how a lot of people fund the next one — still qualifying on the rent.

Not asking you to do anything today. Just flagging it in case that's the real reason you came through.
```

**Compliance check:** PASS — identity / strategy; no amount promised; no CTA pressure.

---

## Day 5 — The bank's box

**Theme:** "Conventional already said no" is not the end of the file.

### SMS

```
If a conventional shop already told you no — too many financed properties, DTI, write-offs — that was their box.

DSCR is a different one. Each rental stands on its own income. There's generally no conventional-style property-count ceiling.

Have you already been turned down on this one, or are you looking before you hit that wall?
```

**Compliance check:** PASS — "generally" on the cap; no guarantee the next lender says yes.

---

## Day 6 — Dana (composite)

**Theme:** Someone in a familiar spot. Not a testimonial with fake numbers.

### SMS

```
This reminded me of Dana — composite, but the situation is one I see a lot.

Self-employed. Three rentals. Bank wouldn't do a cash-out because the returns looked like a mess.

We ran it as DSCR. The question became "does the property's rent cover the new payment," not "does this person look good on paper."

Not promising that's you. If it sounds close, tell me what your rents are and I'll tell you if a call is even worth it.
```

### Email

**Subject:** the file that looked dead on paper
**Alt:** this may sound familiar

---

{{contact.first_name}} —

I'll use a composite so I'm not putting a real client in an email.

Dana is self-employed. Writes everything off. Three rentals. Conventional wouldn't cash-out refinance because the personal file looked weak.

The rental income was never the problem. The underwrite was.

On a DSCR refinance the property is the file. Rent versus the payment. That's the conversation I have all week.

If any of that is in the neighborhood of your situation, reply and tell me which part. I'll tell you whether it's worth 15 minutes or whether you should leave it alone.

{{custom_values.lo_first_name}}

---

**Compliance check:** PASS — labeled composite; no funded stats; "may" / "if it's worth it"; HUMAN REVIEW if a client swaps in a real story (needs approval + no invented results).

---

## Day 7 — Be honest about the rate

**Theme:** The rate is often higher. That's the trade. Compare it to sitting equity or a balloon — not to a conventional they can't get.

### SMS

```
I'll be straight, {{contact.first_name}}.

DSCR rates are often higher than a conventional investment refi. That's the cost of qualifying on the property instead of your income.

The question I actually run is not "is the rate pretty." It's what it's costing you to leave the equity sitting, or to stay on a note that was never meant to be permanent.

If you want that version on your property, I can do it in 15 minutes. No application to start.
```

**Compliance check:** PASS — pratfall on rate; no quoted rate; no close-by date; "often" / no guarantee.

---

## Day 8 — What the call is

**Theme:** Lower the activation energy. This is a numbers look, not a pitch.

### SMS

```
If we talk it's pretty simple.

You tell me the rents, what you owe, what you're trying to do. I tell you whether the property may even be in range and what the tradeoffs look like.

15 minutes. No application to have the conversation.

Here's a calendar if that's easier: {{custom_values.booking_link}}
Or reply with a time that actually works for you this week.
```

### Email

**Subject:** what a call with me actually is
**Alt:** 15 minutes, your numbers, no application

---

{{contact.first_name}} —

I don't need a full package to talk.

Bring rough rents, the current loan, and what you're trying to do — pull capital, get off a short-term note, or just see if a DSCR refinance is even a fit. I'll walk the property with you and tell you if it may qualify, subject to underwriting. If it doesn't look like a fit, I'll say that too.

That's the whole call.

{{custom_values.booking_link}}

{{custom_values.lo_first_name}}
{{custom_values.lo_phone}}

---

**Compliance check:** PASS — "may qualify," "subject to underwriting"; no promised outcome.

---

## Day 9 — The note that was never supposed to stay

**Theme:** Hard-money / bridge / balloon — real urgency without a fake deadline.

### SMS

```
The other group I work with a lot: the bridge or hard-money loan that already did its job.

That note was never the long-term plan. A DSCR refinance is usually the exit — still on the rent, still without the tax-return process.

I can't promise we'll beat a maturity date. I can look at the timeline honestly.

Is that you, or is this more of a cash-out / idle-equity thing?
```

**Compliance check:** PASS — no guaranteed close date; refinance / exit framing only.

---

## Day 10 — Leave the door open

**Theme:** Respect the silence. Recap. Stay easy to answer.

### SMS

```
{{contact.first_name}} — I'll leave this here so I'm not filling up your phone.

You came through on a DSCR refinance. I can run the rental on its own rent and tell you if it's even worth doing.

If the timing's off, that's fine. Reply when you want the look. Or grab a time: {{custom_values.booking_link}}
```

### Email

**Subject:** I'll leave this with you
**Alt:** whenever you want the look

---

{{contact.first_name}} —

I've sent a few notes. I don't want to turn into noise.

Short version of what I can do: look at a rental you already own as a DSCR refinance. Qualification is the property's rent versus the payment — not your W-2 or tax returns. Useful if write-offs, a property-count ceiling, or a short-term note is in the way. The rate is often the trade for that access. I won't pretend otherwise.

If you want me to run yours, reply or use this: {{custom_values.booking_link}}

If now isn't the time, leave it. You know how to find me.

{{custom_values.lo_first_name}}
{{custom_values.company_name}}
{{custom_values.lo_phone}}

---

**Compliance check:** PASS — recap is factual; no scarcity; door open.

---

## Subject line options

| Day | A | B |
|-----|---|---|
| 1 | you came through on a DSCR refi | {{contact.first_name}} — {{custom_values.lo_first_name}} here |
| 3 | your tax returns are not the property | the DTI conversation is usually the wrong one |
| 6 | the file that looked dead on paper | this may sound familiar |
| 8 | what a call with me actually is | 15 minutes, your numbers, no application |
| 10 | I'll leave this with you | whenever you want the look |

## CRM install (keep it dumb)

1. Map the five tokens. If the CRM sends as the assigned user, `{{user.first_name}}` can replace `{{custom_values.lo_first_name}}`.
2. Day 1 = first SMS of the campaign → STOP language stays on that text.
3. Quiet hours: ~8am–7pm lead local. One SMS per day. Email optional, same idea, not a second ask.
4. Exit goals: inbound message, appointment created, STOP / unsub, deal moved to "working / application."
5. Human replies after they text back. This sequence has no bot.
6. Do **not** clone [Laura](dscr-nurture-and-booking-laura.md) into the same account. Pick one sender identity.
7. Do **not** enroll post-consult leads here — that is a different job ([design spec](../../superpowers/specs/2026-08-14-dscr-post-consult-nurture-drip-design.md)).
8. Swap Dana for a real funded story only with LO approval. No invented results.

TCPA / consent still applies. Opt-in must already be on the form. This copy does not create consent.

## Metrics

| Metric | What it tells you |
|--------|-------------------|
| Reply rate by day | Which belief actually landed |
| Day-1 reply rate | Opener / sender-ID problem if this is weak |
| Reply → booked | LO / VA follow-up after the drip did its job |
| Booked from Day 8 vs Day 10 | Whether the calendar link helps or just looks automated |
| STOP / unsub | Spike = too many touches or it still reads like a blast |

## Sequence-level compliance

| Rule | Status |
|------|--------|
| Business-purpose refinance / investment only | PASS |
| No invented rates, LTV, FICO, day-counts | PASS |
| No approval / close-date guarantees | PASS |
| Tax / entity → their CPA | PASS (Day 3) |
| Composite labeled; no fake proof | PASS — real stories need LO approval |
| STOP on first SMS | PASS |
| AI / assistant persona | Not used — LO is the sender |
| Counsel | **HUMAN REVIEW** before a client ships — [guardrails](dscr-compliance-guardrails.md) are draft; licensed-state list is per client |

## Related

- [DSCR Prospecting Playbook](playbook-dscr-self-serve-lead-nurture.md) — speed, cadence, BAMFAM; this file is Chapter 08
- [Intelligence ICP DSCR](intelligence-icp-dscr.md) — who they are; idle-equity and write-off ideas
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) — ship gate
- [Objection-Handling Guide](dscr-objection-handling-guide.md) — what the LO says live after they book
- [Nurture And Booking — Laura](dscr-nurture-and-booking-laura.md) — **do not use** when the client is self-serve
- RM analog (different product, assistant voice): [10-Day RM Drip](../client-marketing/10-day-rm-drip-campaign.md)
