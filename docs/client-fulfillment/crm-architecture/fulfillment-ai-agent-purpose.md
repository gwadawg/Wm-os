---
title: Fulfillment AI Agent — Purpose & Scope
domain: client-fulfillment
owner: operations
status: draft
last_updated: 2026-06-22
review_cycle: monthly
artifact_type: overview
---

# Fulfillment AI Agent — Purpose & Scope

> **Status: planning.** This doc describes *what the fulfillment AI agent is for* and the
> behavior boundaries it must respect. It intentionally does **not** contain the build
> (the agent is being rebuilt on CloseBot's Agent Node — see the build task in
> [Open questions](#open-questions)). Build mechanics get added here once it ships.

## Purpose

The fulfillment AI agent is the **conversational responder** for reverse mortgage client
delivery. Its single mission is to **confirm what a lead came in for and book them with the
loan officer (LO)**. It is not a salesperson, advisor, or underwriter.

It works hand-in-hand with two systems that already exist:

- The GoHighLevel **intent drip** that nurtures leads before they reply
  ([RM iMessage Intent Drip](../client-marketing/rm-imessage-intent-drip-7day.md)).
- The **appointment follow-up** workflow after a call is booked
  ([RM iMessage Appointment Follow-Up](../client-marketing/rm-imessage-appointment-followup.md)).

## Where it sits in the flow

The agent does **not** cold-start conversations and does **not** collect lead information.
The lead's details and objective are already captured on the form.

```
Form submitted (info + objective captured)
   -> GoHighLevel runs the intent drip (text follow-ups)
   -> Lead replies
   -> GHL drip STOPS, AI agent TAKES OVER
        -> confirm intent -> book call with LO -> reschedule/cancel if asked
   -> No reply, or reply then goes quiet
   -> Follow-up agent re-engages with intent
```

## What the agent does

1. **Confirm intent.** The lead arrives with a custom field (`form_intent`) recording exactly
   what they selected on the form. The agent cleanly confirms that objective back to them
   (e.g. "I saw you were looking to eliminate your monthly mortgage payment"), then moves
   toward booking. The three intents:

   | Intent (`form_intent`) | What they want |
   |------------------------|----------------|
   | `remove_mortgage_payment` | Eliminate the monthly mortgage payment |
   | `pay_off_debt` | Use home equity to clear debt |
   | `tax_free_cash_out` / `cash_out` | Access cash from the home |

2. **Book the call.** Get the lead onto the loan officer's calendar to discuss how we can
   help accomplish that objective with the programs available.

## The follow-up agent

When a lead **does not respond, or responds and then goes quiet**, the follow-up agent
re-engages. The purpose is **ghost recovery with intent** — referencing the objective the
lead came in for and steering back toward booking, using **different cadences depending on
how warm or cold the lead is** (rather than one rigid timeline that treats everyone the same).

It stops following up when the lead **books** or clearly says they are **not interested**.

## Reschedule & cancel

Unlike the legacy bot (which goes silent the moment an appointment is booked), the agent can
**reschedule or cancel** a booked appointment in-conversation, with the change reflected on
the calendar. A cancellation routes the lead back toward re-booking rather than dropping them.

## Behavior boundaries (non-negotiable)

- **Only discuss the lead's intention.** The agent never asks for the lead's name, situation,
  financials, or any scenario detail — that information is already captured from the form. The
  only thing it confirms is their intention.
- **No recommendations, no competitors, nothing outside its use.** The job is confirm intent
  → book.
- **If the lead asks what we serve / a product question,** the agent answers it **directly
  from its own knowledge base**, then circles back to focusing on booking the appointment.
- **Book appointments only** — no financial or tax advice, no underwriting, no quoting rates
  or terms. See [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md).
- **Voice:** the loan officer's assistant — warm, plain-spoken, outcome-first, never pushy.

## Related docs

- [How The WM AI Bot Works](how-wm-ai-bot-works.md) — current/legacy bot behavior (being superseded)
- [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md) — 6-stage engine
- [RM iMessage Intent Drip (7-Day)](../client-marketing/rm-imessage-intent-drip-7day.md) — pre-reply nurture
- [RM iMessage Appointment Follow-Up](../client-marketing/rm-imessage-appointment-followup.md) — post-booking reminders
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Open questions

- [ ] Build is in progress on CloseBot's Agent Node — see ClickUp task
  [Rebuild RM Fulfillment CloseBot on Agent Node](https://app.clickup.com/t/86aj68d9x). Add
  build mechanics + final follow-up cadences here once shipped.
- [ ] Confirm Cold follow-up cadence spacing and approved per-touch copy with client success.
