---
title: A-Z Client Onboarding SOP
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-04
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Onboarding/Updated A-Z Onboarding Document.docx
artifact_type: sop
---

# A-Z Client Onboarding SOP

## Purpose

Gated client onboarding from close through go-live. Each step exists for a clear handoff reason — so the next person (or system) can do their job without confusion, chase-downs, or rework.

## Scope

Closer, CSM, tech/ops, media buying, and fulfillment from payment through launch.

## Trigger

New client payment confirmed; Closer submits the New Client Form.

## Inputs

- New Client Form
- Onboarding Form
- Kickoff Form
- QA Form
- Launch Form

## Outputs

- CSM fully briefed for the OB call
- Client equipped and OB call booked
- Account buildable without further client chase
- Ops / media buying working from full project clarity
- Setup owners accountable for completed work
- Client trained, expectations set, account live with correct status

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow product compliance guardrails when applicable ([RM](../reverse-mortgage-dna/rm-compliance-guardrails.md) / [DSCR](../dscr-dna/dscr-compliance-guardrails.md)).
- No stage starts until its gate is complete.
- After Kickoff, ops and media buying should not need to ask CSM or the client for missing setup facts.

## Operating Content

### Core principles

1. **Gated workflow** — each step only starts when the prior gate is done.
2. **Handoff clarity** — every form and call exists to transfer complete context to the next role.
3. **No chase after Kickoff** — client-facing collection ends at Kickoff; build runs from a complete packet.
4. **Ownership at QA** — whoever built a piece confirms it; missed items stay on that owner.

**System of record (activation):** Mr. Waiz (Supabase `clients`) holds the master client record. ClickUp Client Hub is the task layer. Make.com orchestrates — call Mr. Waiz **before** GHL contact creation and Slack setup. Do not manually add every new close in Mr. Waiz Client Roster (that tab is for corrections / missing fields).

---

### Step 1 — New Client Form

**Gate:** Closer submits the New Client Form after payment / agreement.

**Why this step exists**

1. **Activate the system** — fire automations that create the client record, tasks, Slack channels, and notifications so onboarding actually starts.
2. **Brief Client Success** — capture everything CSM needs to walk into the onboarding call already understanding the project (offer, deal context, who the client is, what was sold). CSM should not hop on cold or confused.

**Owner:** Closer (form). Automations (Mr. Waiz → GHL → Slack → ClickUp).

**Unlocks:** Step 2 outreach and CSM prep.

---

### Step 2 — Outreach

**Gate:** Welcome / outreach sequence runs; CSM engages to book the OB call.

**Why this step exists**

1. **Equip the client** — give them everything they need (forms, access links, Slack/Skool, reminders) so they can move without friction.
2. **Show we are on it** — immediate, organized contact signals that delivery has started.
3. **Schedule the OB call** — lock the next live milestone so the timeline does not stall.

**Owner:** Automations (welcome assets) + CSM (call / book).

**Unlocks:** Client path to Step 3; calendar for Step 4.

---

### Step 3 — Onboarding Form (OB Form)

**Gate:** Client submits the Onboarding Form.

**Why this step exists**

Collect the **deep client-side detail** required to build the account — business/legal facts, markets, assets, access paths, and anything else that creates clarity before the live call. This is the client’s structured dump of “who we are and what you need from us.”

**Owner:** Client (submit). Automations (notify, Drive, task update). Tech may start gated work that only needs form data (e.g. A2P when EIN is present).

**Unlocks:** Step 4 with enough raw material to run a useful OB call.

---

### Step 4 — Onboarding Call (OB Call)

**Gate:** Live OB call completed; remaining collectibles confirmed on the call.

**Why this step exists**

1. **Software setup + access** — get the client set up where needed and obtain ad account / page (and related) access for Waiz.
2. **Finish collection** — confirm and fill every remaining gap so we do not chase the client later for build-critical info.
3. **Mini strategy session** — plan the account at a high level and demonstrate that the work is custom to them — not a generic template dump.

**Owner:** CSM (lead). Client (access + decisions).

**Unlocks:** Step 5 Kickoff packet can be completed with confidence.

---

### Step 5 — Kickoff Form

**Gate:** CSM submits the Kickoff Form.

**Why this step exists**

This is the **complete project brief for ops and media buying**. It must contain every last critical fact needed to understand and set up the account.

Goal: after Kickoff, the build team goes to work with **no reason** to ping Client Success or the client for missing information. Full clarity of account setup lives here.

**Owner:** CSM (form). Ops / media buying (consume and build).

**What follows (not a separate form gate):** Tech and media buying execute setup from the Kickoff packet (CRM, phone, funnel, bot, ads, pixel, tracker, etc.). See [New Client Campaign Setup SOP](../media-buying/new-client-campaign-setup-sop.md) for the ads launch frame.

**Unlocks:** Build → Step 6 QA when implementation is done.

---

### Step 6 — QA

**Gate:** Assigned owners submit QA for their portion of setup.

**Why this step exists**

Hold each setup owner **responsible for their own work**. They walk their checklist, confirm it is done, and catch misses before the client sees anything.

If something was forgotten, accountability stays with the person who owned that build — not a vague “someone should have caught it.”

**Owner:** Whoever built each piece (tech, media buying, etc.).

**Unlocks:** Step 7 Launch Call / Launch Form.

---

### Step 7 — Launch Call + Launch Form

**Gate:** Launch Call complete; Launch Form submitted when the account is ready / scheduled to go live.

**Why this step exists**

**Launch Call**

1. **Show the work** — walk the client through what was built and get final approval.
2. **Coach / train** — teach them how to operate inside the system so they can get the best results.
3. **Set hard expectations** — frame timelines, early-phase reality, and roles clearly to reduce churn from surprise or impatience.

**Launch Form**

Submitted after everything is done and go-live is scheduled. Final triple-check of the work, then activate automations and set account status correctly so the company treats the client as live.

**Owner:** CSM (Launch Call). Fulfillment / assigned owner (Launch Form).

**Unlocks:** Live account; post-launch CS cadence ([Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md), [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md)).

---

### Flow (summary)

```text
New Client Form
  → Outreach (equip + book OB)
  → OB Form (deep client data)
  → OB Call (access + finish collection + mini strat)
  → Kickoff Form (full ops/MB packet → build)
  → QA (owner accountability)
  → Launch Call + Launch Form (approve, train, expect, go live)
```

## Related Docs

- [Client Success Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md)
- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [New Client Campaign Setup SOP](../media-buying/new-client-campaign-setup-sop.md)
- [Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md)
- [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md)
