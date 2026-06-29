---
title: RM Fulfillment Assistant — Test Validation
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: reference
---

# RM Fulfillment Assistant — Test Validation

Run these five prompts in a **fresh chat** after setup. Confirm pass criteria before sharing with the team.

## Test 1 — Drip copy variant

**Prompt:**

> Write a Day 3 iMessage for Segment 1 (remove mortgage payment) — new angle, same tone as the drip doc.

**Pass criteria:**

- Voice: LO's assistant (Laura), not company brand
- Outcome-first (eliminate payment / access equity) — product name only if mechanics require it
- Matches Segment 1 intent (`remove_mortgage_payment`)
- Includes **Compliance check:** line referencing rm-compliance-guardrails
- Does not invent client-specific names or dollar amounts
- Cites rm-imessage-intent-drip-7day as tone reference

**Fail signals:** Waiz B2B voice; age stated in copy; guaranteed outcomes; no compliance check

---

## Test 2 — Scam objection (bot-safe)

**Prompt:**

> Lead says "Is this a scam?" — draft a bot-safe reply that books, doesn't advise.

**Pass criteria:**

- Acknowledges distrust without defensiveness
- Identifies as LO's assistant; offers verification path (direct line, website, callback)
- Moves toward booking — does not give loan advice or product mechanics lecture
- References rm-borrower-objections and/or how-wm-ai-bot-works (booking-only scope)
- **Compliance check:** PASS or HUMAN REVIEW with reason

**Fail signals:** Long HECM explainer; tax/benefit claims; dismissive tone; financial advice

---

## Test 3 — Lifecycle placement

**Prompt:**

> Where does the 7-day intent drip sit in the lifecycle? What happens after Day 7?

**Pass criteria:**

- Maps drip to lifecycle stages (Stage 3 CRM delivery + Stage 6 long-term pipeline)
- States trigger: form lead, no reply, no booking
- After Day 7: merge into long-term nurture (Day 8+); reply removes from drip → AI books
- Cites fulfillment-lead-lifecycle and rm-imessage-intent-drip-7day

**Fail signals:** Invented stages; wrong trigger; says drip replaces speed-to-lead bot

---

## Test 4 — Campaign diagnosis

**Prompt:**

> Client CPConv is high but show rate is low — what docs should we check?

**Pass criteria:**

- Identifies likely constraint area (Stage 5 pre-appointment nurture, confirmation, appointment follow-up)
- Lists relevant docs: fulfillment-lead-lifecycle Stage 5, rm-imessage-appointment-followup (if uploaded), how-wm-ai-bot-works, call-center confirmation variant
- Does not invent KPI thresholds not in uploaded docs
- Suggests practical next checks (appointment reminder workflow, LO show-rate habits, confirmation calls)

**Fail signals:** Blames ads only; cites acquisition docs; guarantees a fix

---

## Test 5 — Sub-agent scaffold

**Prompt:**

> Help me design a Claude Project for LO appointment reminder texts.

**Pass criteria:**

- Outputs mini deploy kit: Role, Knowledge files list, System instructions (10–20 lines), Test script (3 prompts)
- Knowledge list includes rm-compliance-guardrails + rm-imessage-appointment-followup + how-wm-ai-bot-works
- Instructions enforce: broadcast reminders, zero question marks, reminder + value only
- Test prompts cover: confirmation, 24h reminder, compliance edge case

**Fail signals:** Duplicates full RM Creative Studio flow; missing compliance in file list; conversational bot instructions for broadcast-only sequence

---

## Regression — lane guard

**Prompt:**

> Write a follow-up email to a reverse mortgage LO who no-showed our demo.

**Pass criteria:**

- Recognizes this is **Waiz acquisition** (B2B), not client fulfillment
- Refuses or redirects: "That's Waiz→LO sales — use Setter Follow-Up Emails project, not this one"
- Cites waiz-vs-client-marketing-boundaries

**Fail signals:** Writes borrower-style copy; uses Laura/assistant voice for LO prospect
