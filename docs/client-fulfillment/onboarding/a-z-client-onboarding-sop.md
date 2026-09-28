---
title: A-Z Client Onboarding SOP
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-27
review_cycle: monthly
source_document: ../waiz-os-archive/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Onboarding/Updated A-Z Onboarding Document.docx
artifact_type: sop
---

# A-Z Client Onboarding SOP

## Purpose

Work inside the stages in the [Client Onboarding Blueprint](client-onboarding-blueprint.md). Each step exists for a clear handoff reason — so the next person can do their job without chase-downs or rework.

These steps are not a second stage list. Where a step sits:

| Blueprint stage | Steps in this SOP |
|-----------------|-------------------|
| Client Activated | Step 1 opens the stage. Steps 2 and 3 are its two statuses. Either can finish first. |
| Awaiting Kickoff | Steps 4 and 5, same session. Together they are the exit. |
| In Build | The build that follows Step 5. Step 6 is the two QA statuses. |
| Launch | Step 7. Launch Form sets Launch Gate to Approved — Schedule Ads. |
| Account Live | Ads are scheduled. Not this SOP. |

## Scope

Closer, CSM, tech/ops, media buying, and fulfillment from payment through launch.

## Trigger

New client payment confirmed; Closer submits the New Client Form.

## Inputs

- New Client Form
- Onboarding Form
- Kickoff Form
- Tech QA Form
- Marketing QA Form
- Launch Form

## Outputs

- CSM fully briefed for the OB call
- Client equipped and OB call booked
- Account buildable without further client chase
- Ops / media buying working from full project clarity
- Setup owners accountable for completed work
- Client trained, expectations set, account live with correct status
- [Client Launch Kit](sop-client-launch-kit.md) PDF + Drive swipe pack delivered on the Launch Call

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow product compliance guardrails when applicable ([RM](../reverse-mortgage-dna/rm-compliance-guardrails.md) / [DSCR](../dscr-dna/dscr-compliance-guardrails.md)).
- No stage moves until every part of its exit is true. One status finishing does not move the client.
- After Kickoff, ops and media buying should not need to ask CSM or the client for missing setup facts.

## Operating Content

### Core principles

1. **Gated workflow** — a stage moves only when every part of its exit is true. Two statuses in the same stage can finish in either order.
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

**Owner:** Automations (welcome assets) + CSM (book the call).

**Stage:** Stays **Client Activated**. Booking the call is one status. It does not move the client. The Onboarding Form is the other status, and it may already be in.

---

### Step 3 — Onboarding Form (OB Form)

**Gate:** Client submits the Onboarding Form.

**Why this step exists**

Collect the **deep client-side detail** required to build the account — business/legal facts, markets, assets, access paths, and anything else that creates clarity before the live call. This is the client’s structured dump of “who we are and what you need from us.”

**Owner:** Client (submit). CSM (chases). Tech may start gated work that only needs form data (e.g. A2P when EIN is present).

**Stage:** Stays **Client Activated** until the call is also booked. The form arriving first does not move the client. When both statuses are done, the client is **Awaiting Kickoff**.

---

### Step 4 — Kickoff Call (booked as the OB Call)

**Gate:** Live kickoff call completed; remaining collectibles confirmed on
the call. This is the meeting booked through the OB Call field in ClickUp.

**Why this step exists**

1. **Software setup + access** — get the client set up where needed and obtain ad account / page (and related) access for Waiz.
2. **Finish collection** — confirm and fill every remaining gap so we do not chase the client later for build-critical info.
3. **Mini strategy session** — plan the account at a high level and demonstrate that the work is custom to them — not a generic template dump.

**Owner:** CSM (lead). Client (access + decisions).

**Stage:** This call and the Kickoff Form are one exit from **Awaiting Kickoff**, in the same session. The call alone does not move the client.

---

### Step 5 — Kickoff Form

**Gate:** CSM submits the Kickoff Form.

**Why this step exists**

This is the **complete project brief for ops and media buying**. It must contain every last critical fact needed to understand and set up the account.

Goal: after Kickoff, the build team goes to work with **no reason** to ping Client Success or the client for missing information. Full clarity of account setup lives here.

**Owner:** CSM (form). Ops / media buying (consume and build).

**Stage:** Submitting this form, with the call held and the launch date set, moves the client to **In Build**.

**What follows (not a separate form gate):** Tech and media buying execute setup from the Kickoff packet (CRM, phone, funnel, bot, ads, pixel, tracker, etc.). See [New Client Campaign Setup SOP](../media-buying/new-client-campaign-setup-sop.md) for the ads launch frame.

---

### Step 6 — QA

**Gate:** Assigned owners submit QA for their portion of setup.

**Why this step exists**

Hold each setup owner **responsible for their own work**. They walk their checklist, confirm it is done, and catch misses before the client sees anything.

If something was forgotten, accountability stays with the person who owned that build — not a vague “someone should have caught it.”

**Owner:** VA (Tech QA). Media Buyer (Marketing QA).

**Stage:** These are the two statuses on **In Build**. Either can finish
first. The CSM moves the client to **Launch** when both are Complete.

---

### Step 7 — Launch Call + Launch Form

**Gate:** The client is in **Launch**. Its Launch Gate is Call Pending,
Revisions Required, or Approved — Schedule Ads. The Launch Form is what
sets Approved — Schedule Ads. It is not its own stage.

**Why this step exists**

**Launch Call**

1. **Show the work** — walk the client through what was built and get final approval.
2. **Coach / train** — teach them how to operate inside the system so they can get the best results.
3. **Set hard expectations** — frame timelines, early-phase reality, and roles clearly to reduce churn from surprise or impatience.

Run the call off the **[Client Launch Kit](sop-client-launch-kit.md)** — branded PDF + living Drive folder. The kit is a required output of this step. Generate it in **Mr. Waiz → Client Roster → Kit** (prefilled from the client file, versioned, posted to Slack); the Launch checklist flags when no kit exists. Agenda, shareability gate, and Drive pack live in that SOP.

**Launch Form**

The CSM submits it when the call has been held and nothing is left open.
That sets Launch Gate to **Approved — Schedule Ads**. It is the media
buyer's cue. It does not make the account live.

Do not submit it while revisions are open. The person who makes a revision does not submit it.

**Owner:** CSM (Launch Call, Launch Kit, and Launch Form). Media Buyer schedules the ads after the form is in.

**Unlocks:** **Account Live** when the ads are scheduled. Then the post-launch CS cadence ([Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md), [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md)).

---

### Flow (summary)

```text
Client Activated
  statuses: OB call booked · Onboarding Form filled (either order)
Awaiting Kickoff
  exit: kickoff call + Kickoff Form + launch date (same session)
In Build
  statuses: Tech QA · Marketing QA (Pending / Complete; either order)
Launch
  gate: Call Pending · Revisions Required · Approved — Schedule Ads
Account Live
  ads scheduled
```

## Related Docs

- [Client Launch Kit SOP](sop-client-launch-kit.md)
- [Client Success Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md)
- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [New Client Campaign Setup SOP](../media-buying/new-client-campaign-setup-sop.md)
- [Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md)
- [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md)
