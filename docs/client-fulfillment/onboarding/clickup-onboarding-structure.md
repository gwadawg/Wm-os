---
title: Onboarding ClickUp Structure
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-27
review_cycle: monthly
artifact_type: sop
audience:
  - team
content_layer: canonical
shareability: internal-fulfillment
depends_on:
  - docs/client-fulfillment/onboarding/client-onboarding-blueprint.md
---

# Onboarding ClickUp Structure

## Purpose

How a client sits on the Client Onboarding list. Stage names, statuses,
and the moment a client moves are defined only in the
[Client Onboarding Blueprint](client-onboarding-blueprint.md).
This doc implements that model. It does not redefine a blueprint stage,
status field, or gate.

ClickUp owns stage for now. Forms and the Launch Kit stay in Mr. Waiz.

**List:** [Client Onboarding](https://app.clickup.com/9013498820/v/li/1400260000001901)
in Client Hub. The legacy list `Onboarding` is the old process. Do not mix them.

**Template:** [_TEMPLATE — {Client} — Onboarding](https://app.clickup.com/t/17tgxqyad8m).
Duplicate the parent with its subtasks for each new client.

## Scope

The parent task, its fields, and its subtasks. The work inside a step
(what the welcome contains, what each QA checks, the Launch Kit) stays in
the [A-Z Client Onboarding SOP](a-z-client-onboarding-sop.md) and the
child SOPs.

## Design rules

1. One parent task per client. Default assignee is the CSM.
2. Stage is one dropdown on the parent. No stage subtasks.
3. Each blueprint status or gate is one field on the parent. A field is
   empty until the client is in the stage that owns it.
4. Template depth is parent, then four build subtasks. One level only.
   A revision subtask is added later, only while Launch Gate is
   Revisions Required.
5. Checklists are the work inside a subtask. A checklist item does not
   move the stage and does not copy a parent field.
6. Blocked is a flag. It is not a stage. The client stays where they are.
7. Submit the form first. Update the matching field in the same sitting.
8. Native task status tracks whether work is active or complete. It does
   not track the onboarding stage.
9. A subtask enters an owner's queue only when its open rule is true.
10. The stage board shows parent tasks only. Do not drag cards to change
    stage; make the transition from inside the parent task.
11. The four template subtask names are fixed system identifiers. Do not
    rename them; views and future automations depend on the exact names.

## Native task statuses

Use the same simple ClickUp statuses on parents and subtasks:

```text
To Do
In Progress
On Hold
Complete
Canceled
```

The parent becomes In Progress when onboarding starts. It stays open
through Launch. After ads are scheduled, set the stage to Account Live,
complete the post-launch handoff, then mark the parent Complete.

Use On Hold when the entire client onboarding is paused. Keep the current
Onboarding Stage so the team knows where work stopped, and add the reason
in a task comment. Use Canceled only when onboarding will not resume.

A subtask starts as To Do and unassigned. Assign it when its open rule is
true. The owner moves it to In Progress when work begins and Complete when
its own done-definition is met.

Blocked and On Hold are different. Blocked marks one work lane that cannot
move while other lanes may continue. On Hold pauses the entire parent.

Do not replace these statuses with the five onboarding stages. Subtasks
share the list's native statuses, and an A2P task cannot meaningfully be
“Awaiting Kickoff” or “Account Live.”

## Parent fields

**Name:** `{Client Name} — Onboarding`

| Field | Type | Values | What it is |
|-------|------|--------|------------|
| Onboarding Stage | Dropdown | The five values below | The client's one position |
| OB Call | Dropdown | Not booked / Booked | Status on Client Activated. Booked alone does not move the stage. |
| OB Call date | Date | Calendar date | When the booked onboarding/kickoff call is. Not a status. |
| Onboarding Form | Dropdown | Not filled / Filled | The other status on Client Activated. Filled alone does not move the stage. |
| Tech QA | Dropdown | Pending / Complete | Status on In Build. Set to Pending when the stage opens. |
| Marketing QA | Dropdown | Pending / Complete | Status on In Build. Set to Pending when the stage opens. |
| Launch Gate | Dropdown | Call Pending / Revisions Required / Approved — Schedule Ads | The decision controlling launch. Set to Call Pending when the stage opens. Empty before that. |
| Launch Call date | Date | From the kickoff session | When the launch call is. Not a status. |
| Blocked | Dropdown | No / Yes | Flag on the parent or the lane task. Not a stage. |
| Blocked reason | Text | Only if Blocked = Yes | |
| Product | Dropdown | RM / DSCR | |
| Mr. Waiz | URL | Client record | |

### Stage values

```text
1 — Client Activated
2 — Awaiting Kickoff
3 — In Build
4 — Launch
5 — Account Live
```

Those five values are the only options on Onboarding Stage.

### Fields that do not exist

- **OB Call = Held.** Once both Client Activated statuses are done, leave
  OB Call and Onboarding Form alone. The kickoff session is the exit from
  Awaiting Kickoff. The move to In Build is the record that it happened.
- **A Launch Call dropdown.** Call Pending / Revisions Required /
  Approved — Schedule Ads is the Launch Gate. Launch Call date is the when.
- **Baton, Work package, or a QA field on a subtask.** The parent assignee
  is the CSM. The subtask assignee is the lane owner. The subtask name is
  the work. A second copy of a parent status will drift.

## Build subtasks

```text
{Client} — Onboarding          ← parent (CSM)
├── A2P                        ← assign to VA when open
├── Tech Buildout              ← assign to VA when open
├── Funnel                     ← assign to Media Buyer when open
└── Media Buying               ← assign to Media Buyer when open
```

Tech subtasks stay with Christian until a dedicated VA is named.

A subtask exists when the work has its own start gate, a long wait, or
its own done-definition. A call or a form does not get a task.

| Subtask | Assignee | Opens when | Done when |
|---------|----------|------------|-----------|
| A2P | VA | Onboarding Form = Filled, and EIN is present. The client may still be Client Activated or Awaiting Kickoff. | A2P cleared |
| Tech Buildout | VA | Stage becomes In Build | Its GHL, phone, and Closebot checklist is complete |
| Funnel | Media Buyer | Stage becomes In Build | Funnel is live |
| Media Buying | Media Buyer | Stage becomes In Build | Ad access is in and ads are ready |

A2P may still be open after the other three start. Opening A2P does not
move the stage.

Each subtask closes on its own work. The parent QA fields are bundle
gates: Tech QA covers A2P plus Tech Buildout; Marketing QA covers Funnel
plus Media Buying. A completed subtask must not stay in someone's queue
while it waits on another subtask.

**Checklists**

- **A2P:** EIN ready, filed, cleared.
- **Tech Buildout:** GHL, phone, Closebot.
- **Funnel:** Funnel live.
- **Media Buying:** Ad access, ads ready.

Subtask fields are Blocked and Blocked reason only.

| Form | Covers | Sets on the parent |
|------|--------|-------------------|
| Tech QA | A2P cleared and Tech Buildout done | Tech QA = Complete |
| Marketing QA | Funnel and Media Buying done | Marketing QA = Complete |
| Kickoff Form | The kickoff session | Stage → In Build. Launch Call date set. |
| Launch Form | Launch, with nothing left open | Launch Gate = Approved — Schedule Ads. Stage stays Launch. |

### Revision subtask

Do not put this on the template. Create it only when Launch Gate =
Revisions Required.

```text
Revision — {short what}
```

Assignee is whoever makes the change. Close it when the change is done.
The CSM then submits the Launch Form and sets Launch Gate =
Approved — Schedule Ads. The person who made the change does not set
that gate.

## How a client moves

One row is one sitting. Do not update a status field before its stage.

| When this is true | Who | Stage | Also set |
|-------------------|-----|-------|----------|
| New Client Form is in. Task created. | CSM | 1 — Client Activated | Native status = In Progress. OB Call = Not booked. Onboarding Form = Not filled. Tech QA, Marketing QA, and Launch Gate stay empty. |
| OB call is booked. Form is still out. | CSM | Stays 1 — Client Activated | OB Call = Booked. OB Call date set. |
| Form is in. Call is still unbooked. | CSM | Stays 1 — Client Activated | Onboarding Form = Filled. Open A2P if EIN is present. |
| OB Call = Booked and Onboarding Form = Filled | CSM | 2 — Awaiting Kickoff | Leave both fields as they are. |
| Kickoff call held, Kickoff Form in, and launch date set. Same session. | CSM | 3 — In Build | Launch Call date set. Tech QA = Pending. Marketing QA = Pending. Assign Tech Buildout, Funnel, and Media Buying. |
| Tech QA form is in | VA | Stays 3 — In Build | Tech QA = Complete |
| Marketing QA form is in | Media Buyer | Stays 3 — In Build | Marketing QA = Complete |
| Tech QA = Complete and Marketing QA = Complete | CSM | 4 — Launch | Launch Gate = Call Pending |
| Launch call held, and the client wants changes | CSM | Stays 4 — Launch | Launch Gate = Revisions Required. Open one revision subtask. Do not submit the Launch Form. |
| Launch Form is in. Nothing is open. | CSM | Stays 4 — Launch | Launch Gate = Approved — Schedule Ads |
| Ads are scheduled | CSM | 5 — Account Live | Complete the post-launch handoff, then mark the parent Complete. The Launch Form does not do this. |

Either Client Activated status can finish first. Either QA can finish
first. One of them finishing does not move the stage.

If the Kickoff Form is not in, the stage stays Awaiting Kickoff.
A2P may already be open. That is not an exception to this gate.

### Stage changes

Use the board to read the portfolio. Hide subtasks from it. Do not drag a
card between stage columns: a drag changes only Onboarding Stage and can
skip the required dates, QA defaults, assignments, and status updates.

Make the stage change inside the parent task using the transition row
above. Automate those bundled updates later if the volume warrants it.

### Automation contract

Automations act on the parent fields and transition rules in this doc.
They do not infer stage from checklist completion or a subtask name.

- Create or update each client by Mr. Waiz client ID so a retry cannot
  create a duplicate parent.
- Treat each stage transition as one bundle: stage, default status fields,
  assignments, dates, and notifications update together.
- A form submission updates its matching parent field. It does not update
  Account Live.
- Subtask completion does not set a QA field. The submitted QA form is the
  proof that sets Pending to Complete.
- Both QAs Complete may notify the CSM or move the client to Launch only
  when Launch Call date is present.
- Launch Form submission sets Launch Gate to Approved — Schedule Ads.
  Only confirmation that ads are scheduled moves the stage to Account Live.
- Moving to On Hold sets the next review date, then stops all other stage
  and due-date automations until the CSM returns the parent to In Progress.
- Start with notifications for a new automation. Promote it to an automatic
  field or stage update after the team has verified the trigger.

### Blocked

| Situation | Block | Continue |
|-----------|-------|----------|
| Ad access missing | Media Buying | Funnel, Tech Buildout, A2P |
| A2P waiting on a clear | A2P, and any SMS step that needs it | The rest of Tech Buildout |
| Kickoff packet is thin, or the client has gone quiet | Only the subtask that needs the missing input | Everything else |

## Views

| View | Filter | For |
|------|--------|-----|
| Onboarding — Board | Parent tasks only; native status is open; group by Onboarding Stage | CSM portfolio |
| My work | Assignee = me, open | Daily work |
| Build — Tech | Subtask name is A2P or Tech Buildout, open | VA |
| Build — Marketing | Subtask name is Funnel or Media Buying, open | Media Buyer |
| Form still out | Stage = Client Activated, Onboarding Form = Not filled | CSM chase |
| Call still unbooked | Stage = Client Activated, OB Call = Not booked | CSM |
| Ready for Launch | Stage = In Build, Tech QA = Complete, Marketing QA = Complete | CSM stage-move queue |
| Prepare to launch | Stage = Launch, Launch Gate = Call Pending | CSM, before the call |
| Ready to schedule | Stage = Launch, Launch Gate = Approved — Schedule Ads | Media Buyer |
| Blocked | Blocked = Yes | Escalation |
| On hold | Native status = On Hold | Exception review |

The board groups by stage. Do not add a view that turns a status into
a board column.

## Dates and due dates

- **Parent due date:** the next date the CSM must look at or act on the
  client. It is a rolling control date, not the promised completion date.
- **Subtask due date:** the committed completion date for that work package.
- **OB Call date:** the scheduled onboarding/kickoff meeting.
- **Launch Call date:** the scheduled client launch meeting.

Do not add a separate Next Action Date. The native due date powers ClickUp
Home, My Work, reminders, and overdue views. A second date would duplicate
the same operating signal.

### Parent due-date rules

| Event | Parent due date becomes |
|-------|-------------------------|
| Parent created | Initial CSM response deadline |
| Stage = Client Activated and either requirement is incomplete | Next CSM follow-up for the incomplete requirement, not the date the client is expected to reply |
| Stage → Awaiting Kickoff | OB Call date |
| Stage → In Build | Next CSM build-review checkpoint |
| Stage → Launch; Launch Gate = Call Pending | Launch Call date |
| Launch Gate → Revisions Required | Next CSM revision-review checkpoint |
| Launch Gate → Approved — Schedule Ads | Scheduling-confirmation deadline |
| Stage → Account Live | Post-launch handoff deadline |
| Native status → On Hold | Next date the CSM must review the hold |
| Native status → Complete or Canceled | Clear the due date |

Every active or On Hold parent has a due date. An overdue parent means a
CSM follow-up or checkpoint was missed; it does not mean the client missed
an overall onboarding deadline.

Automations may set the due date only on the events above. They must not
continually recalculate it or overwrite a later manual exception. Automatic
changes do not need a comment. A manual extension gets one short comment
with the reason.

Use stage-entry timestamps and Account Live date for onboarding-duration
reporting. Do not calculate duration or SLA performance from the rolling
parent due date. Full SLA intervals can be configured later without
changing this structure.

## New client

When the New Client Form lands:

1. Duplicate the template parent with its four subtasks.
2. Rename to `{Client} — Onboarding`.
3. Assignee = CSM. Product and Mr. Waiz URL filled.
4. Stage = `1 — Client Activated`.
5. Native status = In Progress.
6. OB Call = Not booked. Onboarding Form = Not filled.
7. Tech QA, Marketing QA, and Launch Gate left empty.
8. Leave all four subtasks To Do and unassigned. Assign each one only when
   its open rule is true.

## Out of scope

- Mr. Waiz `onboarding_stage` and any sync
- Full SLA targets and automated escalations
- A task or subtask per form
- ClickUp forms in place of Mr. Waiz forms
- A checkbox that says the ClickUp field was updated

## Freeze criteria

This doc is ready to freeze when:

1. The parent and the four build subtasks match the tree above.
2. Parent fields match the blueprint statuses, and no field copies a stage.
3. Tech QA and Marketing QA are the only QA fields, and they live on the parent.
4. Launch Gate is one field: Call Pending / Revisions Required /
   Approved — Schedule Ads.
5. The form and the matching field update happen in the same sitting.
6. Native status, assignment, due-date, and handoff rules are configured.

## Related

- [Client Onboarding Blueprint](client-onboarding-blueprint.md)
- [A-Z Client Onboarding SOP](a-z-client-onboarding-sop.md)
- [Client Launch Kit SOP](sop-client-launch-kit.md)
- [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md)
