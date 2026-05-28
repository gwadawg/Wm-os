---
title: Call Center Live Transfer Warm Hand-off Script (Reverse Mortgage)
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-05-28
review_cycle: monthly
artifact_type: script
---

# Call Center Live Transfer Warm Hand-off Script (Reverse Mortgage)

## Purpose

Word-for-word language for the moment a fulfillment call-center agent transfers a qualified borrower live to the client loan officer. Covers the borrower-side hold, the LO-side announcement, the formal in-call introduction, and the graceful exit.

## Scope

Used **after** the agent has completed Stages 1–3 of the [Appointment-Setting Call Script](script-appointment-setting-call.md) and the borrower is qualified for transfer. Client-side B2C only — excludes acquisition (Waiz-selling) transfers, which live in [docs/acquisition/sales/](../../acquisition/sales/script-intro-call-basic.md).

## Owner

See [domain owners](../../_inventory/domain-owners.md): **client-success** (until a dedicated call-center lead is assigned).

## When To Use

- Qualified borrower is on the line, ready to be introduced to the LO.
- LO has been pre-confirmed available (Slack ping, internal signal, or known active hours).
- Borrower has not been over-interviewed — they have a story left to tell the LO.

## The One Job of This Hand-off

Make the LO feel like the borrower was **served to them on a silver platter** — already qualified, already introduced, already warm. The LO should hang up the call thinking *"this is awesome that I'm paying for this."* If the LO has to re-ask basic questions, the hand-off failed.

---

## Core Hand-off Principles (read before every shift)

1. **Hover in. Introduce by name + situation.** Do not connect two strangers and disappear. You stay on the line until both are talking.
2. **Spoon-feed the data.** Tell the LO who the borrower is, what they want, what they own, and what they owe — in 2 sentences — so the LO opens with insight, not interrogation.
3. **Talk to the LO like a friend, not like a customer.** Especially during dead-air while a slow LO walks to the desk. Loose tone. Real human. From founder: *"yo, if you hear the things these guys say in my meetings, you wouldn't even believe it — anyways…"*
4. **Speed kills bad transfers.** 5 seconds of silence on a transfer feels like forever to a borrower. Fill it or end it.
5. **No "give me one second" without a reason.** Anchor the hold: *"Let me grab [LO NAME] real quick — he's right at his desk."*
6. **Borderline lead? Confirm with the LO BEFORE the borrower hears you.** Use the parking-the-borrower line below. Don't waste an LO's appointment slot on a lead they can't fund.

---

## STAGE 1 — PARK THE BORROWER ON HOLD

> Awesome [BORROWER NAME], so what I'm going to do is put you on a brief hold and grab [LO NAME] real quick so I can introduce you guys directly — that way you don't have to repeat any of this. Sound good? Cool — hang tight for me, one moment.

📋 Rules:
- Always give the hold a **reason** ("grab [LO NAME]" / "make sure he's at his desk").
- Always tell the borrower **how long** ("brief hold" / "one moment").
- Always tell them **why** ("so you don't have to repeat anything").
- Mute or place on actual hold. Don't ever let the borrower hear you talk to the LO if there's any chance you'll have to disqualify.

---

## STAGE 2 — REACH THE LO (private line)

Two scenarios. Match the LO's style.

### Scenario A — Fast LO (Andy style: picks up in 2 seconds, ready to go)

> Hey [LO NAME] — got a borrower for you ready to go. Quick rundown: [NAME], looking for [AMOUNT] for [USE OF FUNDS]. Home's worth about [VALUE], owes [BALANCE]. Wants to hop on now — cool if I transfer?

📋 No small talk. Andy wants speed. Get to the data, get permission, transfer.

### Scenario B — Slow LO (Toby style: takes 40 seconds to get to the desk)

> Hey [LO NAME] — got a borrower on the other line ready to talk. So as you're walking to the desk, let me catch you up real quick…

Then fill the walk with the brief — talk like a friend, not a robot:

> So her name is [NAME], she came in on the inquiry form for tapping into her home equity. She's looking for about [AMOUNT] — she actually mentioned [USE OF FUNDS]. House is worth around [VALUE], she's got about [BALANCE] left on the mortgage. She sounded [VIBE — friendly / hurried / confused / motivated]. Couple things you might want to know — [ANY UNIQUE DETAIL: state, family situation, prior loan attempt, urgency reason].

When the LO is at the desk:

> Cool — you good to take her? I'm going to bring her on right now and introduce you.

📋 Per founder: this is where reps freeze. Don't. Treat the LO like a coworker. Loose, casual, conversational. "Yo, dude, you would not believe what this borrower just said." Build rapport with the LO across calls — they show up more eager next time.

### Scenario C — LO Not Available

> Hey [LO NAME] — got a hot one on the other line, you free? … No? Cool, I'll book her and shoot you the notes.

Then:
- Go back to borrower → fall back to the booking flow in [Appointment-Setting Script — Stage 4](script-appointment-setting-call.md#stage-4--transition-to-transfer-or-book).
- Send LO a Slack/notes summary so they're prepped for the appointment.

---

## STAGE 3 — THE FORMAL HOVER-IN INTRODUCTION

This is the **single most important moment of the hand-off**. Do not skip the introduction. Do not just connect the lines and drop.

### Bring Both Parties Back On

> [BORROWER NAME], you still there? … Awesome — sorry about the hold.

> [BORROWER NAME], this is [LO NAME] — they're the reverse mortgage specialist here at [COMPANY] and they're the one who's going to be helping you out today.

### Hand the Mic to the LO With a Briefing

> And [LO NAME] — so just so you've got the picture: [BORROWER NAME] is looking at [AMOUNT] for [USE OF FUNDS]. Home's around [VALUE], owes about [BALANCE]. They also mentioned [UNIQUE DETAIL — e.g., "they're in Michigan," "their daughter's helping with the paperwork," "they're looking to do this in the next 60 days"].

📋 Why this works (per founder): the LO can now **open the call with insight** — "Oh awesome, so you're looking at [AMOUNT] for [USE OF FUNDS] — let me ask about [SOMETHING SPECIFIC]" — instead of starting from zero. That makes the borrower feel known and the LO look sharp.

### Step Out

> All right, I'll let you two take it from here — [BORROWER NAME], you're in great hands. [LO NAME], I'll send the notes over.

Then drop off.

📋 Rules:
- Use both names again at the end. Borrower hears their name twice → trust signal.
- Mention the notes → reassures the LO you're not leaving them empty-handed.
- Do not linger or interject after this. The LO is now driving.

---

## STAGE 4 — POST-HAND-OFF (within 60 seconds of dropping off)

1. **Send LO the notes** in Slack / CRM (or whatever channel they prefer):
   - Borrower name + phone + email
   - Use of funds
   - Home value, mortgage balance, lien status if surfaced
   - Vibe / personality flags
   - Any objection raised on your call (so the LO isn't caught off-guard)
2. **Disposition in CRM**: "Live transferred — [LO NAME] — [TIME]"
3. **Add Live Transfer tag** in the dialer/CRM so the lead doesn't reappear in your queue.

📋 Per coaching call: tagging matters. Bernardo had a live-transferred borrower reappear in his dialer the next day because the tag missed. Verify the tag.

---

## VARIANT — Borderline Lead Confirmation Before Transfer

Use when you suspect the lead might not meet the LO's program (e.g., low home value, leased land, etc.), but you want the LO to decide.

### Park the borrower

(See Stage 1.)

### On the LO line (private)

> Hey [LO NAME] — got a borrower on the other line, but I wanted to flag her first before I bring her over. She's looking for [AMOUNT] for [USE OF FUNDS], house is worth around [VALUE], owes [BALANCE]. [FLAG: manufactured home? low value? etc.] Want me to transfer, or should I close it out and let her down easy?

### If LO says "pass"

Go back to the borrower:

> Hey [BORROWER NAME], thanks for hanging in there. So I talked with [LO NAME] and based on what you're looking at, this might not be the best fit for what they do — but I appreciate you walking me through everything. We'll get back to you if anything changes. Have a great rest of your day.

Then escalate to your manager so the lead gets reviewed properly (per Gabe: never silently disqualify).

### If LO says "go ahead anyway"

Run Stage 3 (Formal Hover-In Introduction) as normal.

---

## VARIANT — LO Wants You To Stay On The Call

Some LOs (especially newer client LOs or LOs trying out the call center for the first time) will ask the agent to stay on the line.

> Sure thing, [LO NAME] — I'll stay quiet on the line. If anything comes up, just say my name and I'll jump in.

Then mute. Take notes for the post-call brief. Do not interject unless the LO calls you by name.

📋 Use this sparingly. It signals to the LO that they don't fully trust the agent yet. Earn trust over reps so the LO is comfortable taking borrowers solo.

---

## ANTI-PATTERNS (do not do these)

| Anti-pattern | Why it fails |
|--------------|--------------|
| Cold transfer ("Connecting you now" + drop) | LO starts from zero. Borrower feels like a number. |
| Repeating qualification questions in front of the LO that you already asked | Wastes the LO's time. Spoon-feed the data instead. |
| Transferring a lead the LO can't fund | Burns the LO's calendar and trust. Confirm first if borderline. |
| Leaving silence on the LO line during the walk-to-desk | Awkward. Talk like a friend. Catch them up. |
| Calling the LO "sir" / overly professional | Founder's note: be human, not stiff. They're coworkers. |
| Ending the borrower hold with "okay, here he is" + no intro | Skips the most valuable line of the hand-off — the briefing. |
| Forgetting to send the notes after the transfer | LO works without context. Show rate / close rate drops. |

---

## QUALITY BAR

- **Borrower never repeats themselves** to the LO. The briefing covered it.
- **LO opens the call with insight**, not interrogation.
- **Hand-off completes in under 90 seconds** of total dead-air for the borrower.
- **Borderline leads are confirmed with the LO before transfer**, not surprise-dropped on them.
- **Notes hit the LO within 60 seconds** of drop-off.
- **Live Transfer tag** is applied in CRM so the lead doesn't recycle.
- **LO feels good** about taking the next transfer from this agent. (Soft metric: track LO push-back rate over time.)

---

## METRICS

- Live transfer rate (per LO client, per agent)
- LO "good lead" feedback rate (% of transfers the LO marks as quality)
- LO "bad lead" / push-back rate (target: trending down)
- Borrower hold time during transfer (target: < 30 seconds)
- Show rate / close rate downstream of live transfers vs. booked appointments

---

## Related Docs

### Prerequisites (read before this script)

- [Appointment-Setting Call Script](script-appointment-setting-call.md) — Stages 1–3 must be completed before this hand-off runs.
- [Call Center Script Boundary Rules](script-boundary-rules.md) — non-negotiable separation from acquisition transfers.
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md) — no guarantees, no advice, no age in copy.

### Handoffs (what happens after this script)

- LO runs the consultation / loan conversation — out of scope for the call center.
- CRM disposition + notes to LO.

### Reference (used during execution)

- [Call Center Script Factory SOP](sop-call-center-script-factory.md) — how this script gets improved.
- [Client Fulfillment — Call Center](README.md) — domain index.
- [Reverse Mortgage Doctrine](../reverse-mortgage-dna/doctrine-reverse-mortgage.md) — product context.

---

## Open Questions

- [ ] Confirm preferred LO notification channel per client (Slack DM vs. CRM note vs. text).
- [ ] Confirm Live Transfer tag name in each client's CRM (GHL workflows vary by LO).
- [ ] Decide whether to build a per-LO "transfer profile" doc (fast/slow, prefers small-talk, hates small-talk, etc.) — Andy / Toby / Jesse currently differ.
- [ ] Define the exact "borderline" threshold for the confirmation variant per LO.
