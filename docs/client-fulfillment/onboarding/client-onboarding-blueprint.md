---
title: Client Onboarding Blueprint
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-09-27
review_cycle: monthly
artifact_type: blueprint
audience:
  - team
content_layer: canonical
shareability: internal-fulfillment
client_delivery: true
---

# Client Onboarding Blueprint

Stage truth for client onboarding. SOPs, forms, and ClickUp use these
stage names, status fields, and the Launch Gate. Do not add a stage for
a status or gate value.

## Purpose

One position for every client, from payment confirmed through Account Live. After that: [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md).

## The rule

The **stage** is where the client is. A client is in one stage.

A **status** is a fact inside that stage. Statuses in the same stage can finish in either order. Flipping one status does not move the stage. The stage moves only when every part of its exit is true.

The **Launch Gate** is the decision controlling whether ads can be
scheduled. Changing it does not move the client to Account Live.

Say the stage with its statuses or Launch Gate when the stage has them.
A stage name alone is incomplete when more detail is listed below.

## Stages

| Stage | Owner | Status fields / gate | Leaves when |
|-------|-------|----------------------|-------------|
| 1 — Client Activated | CSM | OB call: Not booked / Booked. Onboarding form: Not filled / Filled. | Both are done |
| 2 — Awaiting Kickoff | CSM | None | Kickoff call held, Kickoff Form in, launch date set. Same session. |
| 3 — In Build | CSM moves the client. VA owns Tech. Media Buyer owns Marketing. | Tech QA: Pending / Complete. Marketing QA: Pending / Complete. | Both QAs are complete |
| 4 — Launch | Changes with the gate | Call Pending / Revisions Required / Approved — Schedule Ads | Ads are scheduled |
| 5 — Account Live | Hands to post-launch Client Success | None | Onboarding is over |

## What is true in each stage

### 1 — Client Activated

Payment is in. The closer has submitted the New Client Form. Welcome messages, the Onboarding Form, and access links have already gone out. That send is not a stage.

The CSM books the onboarding call. The client fills the Onboarding Form, and the CSM chases it. If the form comes back before the call is booked, the client stays here: form filled, call not booked.

### 2 — Awaiting Kickoff

The call is on the calendar and the Onboarding Form is in. Those two facts are not tracked again. The CSM holds the kickoff, submits the Kickoff Form in that same session, and sets the launch date.

### 3 — In Build

Kickoff is done and the launch date is set. Tech and Marketing build at the same time. The VA closes Tech with Tech QA. The media buyer closes Marketing with Marketing QA. One lane can finish while the other is still open. The CSM moves the client when both QAs are in.

### 4 — Launch

The build is done. Always say the gate with the stage.

| Launch Gate | Owner | What it means |
|-------------|-------|---------------|
| Call Pending | CSM | The call is on the calendar from kickoff and has not happened. The media buyer does not schedule. |
| Revisions Required | Whoever makes the change | The call happened and the client asked for changes. The CSM accepts the fix. The media buyer does not schedule. |
| Approved — Schedule Ads | Media Buyer | The call happened, nothing is open, and the CSM has submitted the Launch Form. That form is the cue to schedule. |

### 5 — Account Live

The ads are scheduled. Onboarding ends.

## How to say where a client is

- **Client Activated** — always add both statuses.
- **Awaiting Kickoff** — nothing to add.
- **In Build** — always add each QA.
- **Launch** — always add the Launch Gate.
- **Account Live** — nothing to add.

## Not a stage

| Fact | Where it lives |
|------|----------------|
| Welcome send | Happens as soon as the New Client Form is in. No owner, no stage. |
| OB call booked, or Onboarding Form filled | Statuses on Client Activated. Neither one moves the client alone. |
| Kickoff call and Kickoff Form | The exit from Awaiting Kickoff. Same session, not two stages. |
| Tech QA or Marketing QA | Statuses on In Build. Either can finish first. |
| Launch Form | The proof that Launch Gate is **Approved — Schedule Ads**. Not its own stage, and not Account Live. |
| Ads scheduled | Account Live. Not another Launch Gate value. |
| A blocked lane | A flag on that lane. The client stays In Build. |

Work inside a stage (what the welcome contains, when A2P can start, what each QA checks, the Launch Kit, what a revision changes) lives in the child SOPs. That work does not get a new stage.

## Related docs

- [A-Z Client Onboarding SOP](a-z-client-onboarding-sop.md) — work inside the stages
- [Client Launch Kit SOP](sop-client-launch-kit.md)
- [Onboarding ClickUp Structure](clickup-onboarding-structure.md)
- [Client Success Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md)
- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md)
