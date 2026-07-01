---
title: LO Lead Dialing SOP — RM
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-07-02
review_cycle: monthly
artifact_type: sop
shareability: lo-course
audience:
  - client
content_layer: canonical
product: reverse-mortgage
delivery_group: lead-nurture
methodology_sources:
  - docs/client-fulfillment/client-marketing/playbook-nurture-framework.md
delivery:
  - github
  - course-material
  - team-drive
---

# LO Lead Dialing SOP — RM

> **Execution layer** for [Nurture Framework §3 — Cadence science](playbook-nurture-framework.md#3-cadence-science). Principles and BAMFAM: framework + [BAMFAM Playbook — RM](../client-sales/playbook-bamfam-rm.md).

## Purpose

Standardize how the **loan officer or in-house assistant** works fresh and follow-up lead dial blocks — call order, double-dial, voicemail + text, CRM notes, and handoff to BAMFAM when they can't talk now.

## Scope

- Client-side **B2C** borrower leads in the LO's CRM (Meta, referrals, sphere, reactivation lists).
- LO or assistant **self-serve** dialing — not a third-party call center script.

## Owner

Loan officer (accountable). Assistant/setter executes if the LO employs one.

## Trigger

- Scheduled dial block (daily recommended for fresh leads)
- Speed-to-lead: new form submit while motivation is high (same day priority)
- Callback due from prior touch or GHL task

## Inputs

- CRM access with lead queue or smart list (fresh → aged follow-ups)
- Active phone line(s) — **multiple lines** if primary is flagged spam ([Framework §2](playbook-nurture-framework.md#2-limiting-beliefs-to-break))
- [BAMFAM Playbook — RM](../client-sales/playbook-bamfam-rm.md) for no-time outcomes
- [RM Borrower Objections](../reverse-mortgage-dna/rm-borrower-objections.md) for live pushback
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Outputs

- Every touched lead has **notes**, **disposition**, and **next step** (or booked appointment)
- No lead leaves a dial block with "I called once" as the only record
- Hot replies handled same session or within the hour

---

## Queue priority

Work in this order within a dial block:

| Priority | Lead type |
|----------|-------------|
| 1 | **Fresh** — form submit today (or bot handoff "call now") |
| 2 | **Inbound reply** — text/email while sequence running |
| 3 | **Callback due** — GHL task or promised return time |
| 4 | **Unreached** — prior attempts, no connect |
| 5 | **Aged reactivation** — see [Framework §4](playbook-nurture-framework.md#4-aged-lead-reactivation) |

Do not cherry-pick only "easy" names. Work the list top to bottom.

---

## Per-lead process

1. **Review CRM** — form intent, source, prior touches, notes (30 seconds).
2. **Call first** — live attempt per [cadence](#call-cadence-default) below.
3. **On connect:**
   - Identify as **[LO NAME]'s office / assistant** in the first 10 seconds.
   - **[Save your number](playbook-nurture-framework.md#2-limiting-beliefs-to-break)** ask on first live conversation.
   - Goal: **live transfer to LO** if available, else **book on LO calendar** — [BAMFAM](../client-sales/playbook-bamfam-rm.md) if they can't talk now.
4. **On no connect:** double-dial → voicemail → text (same session when appropriate).
5. **Notes required** — motivators, objection, next step. A dial without notes is incomplete.
6. **Update CRM** — stage, disposition, next work date, or booked appointment **before** the next lead.

---

## Call cadence (default)

Front-load attempts while interest is highest — especially Days 1–3 on new Meta leads.

| Step | Action |
|------|--------|
| 1 | Live call |
| 2 | **Immediate second dial** if first rings out / no answer (many phones block first call, allow second) |
| 3 | Voicemail — who you are, why calling (they requested info), short callback ask (~20 sec) |
| 4 | Text immediately after voicemail if not recently texted — reference form/outcome, one clear ask |
| 5 | Repeat double-dial + VM + text **once more same day** (spacing: few hours apart) |
| 6 | **Next 2 days:** one call pass morning + one evening; text after second attempt if no connect |
| 7 | **Days 4–7:** one call + text per day if still unreached |
| 8 | After Day 7 with no connect → long-term nurture (automated drip + periodic manual re-touch per framework) |

📋 **Compliance:** Obey calling/texting laws and registry rules for your states and lead source. When in doubt, defer to your compliance officer and [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md).

### Voicemail pattern (RM)

> Hey [NAME], this is [ASSISTANT NAME] calling from [LO NAME]'s office. You had reached out about [INTENT — payment relief / equity / debt — match form]. [LO FIRST NAME] asked me to give you a quick call. I'll try you again — or text me back here if now's a good time.

---

## Texting rules

- **Call before cold text** on a lead you haven't spoken with.
- **No long objection threads** over SMS — acknowledge, offer a call, book.
- **Reply fast** when they text back mid-block — treat as Priority 2.
- **Outcome-first** language; assistant voice — short, one clear ask (match form intent; avoid product jargon on first touch).

---

## Multi-line and local presence

| Situation | Action |
|-----------|--------|
| Repeated no-answer on primary cell | Try published LO office line or alternate CRM line |
| High spam-flag risk on outbound | Local area code / caller ID tools if available |
| They say "I blocked you" | Apologize lightly; confirm best number; switch channel to email |

---

## Dispositions (minimum)

| Outcome | CRM action |
|---------|------------|
| Booked on LO calendar | Appointment set; confirmation + reminders on |
| Live transfer to LO | Note outcome; LO owns close |
| Qualified, not booked — callback | BAMFAM or explicit callback datetime + task |
| Not ready — nurture | Stay in drip; next dial date |
| Wrong number / bad data | Mark per CRM convention; do not keep dialing |
| Unsubscribe / STOP | Remove from all sequences immediately |

---

## Quality bar

- Sound **human** — not robodial monotone; match borrower energy.
- **Never** end a live call with "I'll call you later" without a hold — [BAMFAM Playbook](../client-sales/playbook-bamfam-rm.md).
- When speed-to-lead is automated, dial blocks **complement** the first touch — don't duplicate the same minute.

## Related docs

| Doc | Role |
|-----|------|
| [Nurture Framework §3](playbook-nurture-framework.md#3-cadence-science) | Cadence principles |
| [Nurture Framework §4](playbook-nurture-framework.md#4-aged-lead-reactivation) | Aged queue priority |
| [BAMFAM Playbook — RM](../client-sales/playbook-bamfam-rm.md) | Book next step on the phone |
| [Aged Lead Reactivation Script — RM](script-aged-lead-reactivation-rm.md) | Aged list word tracks |
