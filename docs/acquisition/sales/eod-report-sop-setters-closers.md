---
title: EOD Report SOP (Setters And Closers)
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-29
review_cycle: weekly
source_document: source-docs/waiz-drive-export/Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Sales Admin Work/EOD Report SOP (Setters & Closers).docx
artifact_type: sop
---

# EOD Report SOP (Setters And Closers)

## Purpose

Standardize **end-of-day (EOD)** reporting so leadership has accurate activity, pipeline state, and coaching signals — without reps leaving CRM or admin half-done.

## Scope

- **Setters:** [Setter Daily Checklist](setter-daily-checklist.md) EOD block — this doc is the field-by-field standard.
- **Closers:** Demo metrics, pipeline hygiene, and roll-up (below).

## Owner

| Role | Owner |
|------|--------|
| Setter EOD | **setter** — see [domain owners](../../_inventory/domain-owners.md) |
| Closer EOD | **closer** / sales leadership |

## Trigger

Submit the EOD form when the setter/closer **wraps for the day** — no fixed clock-out time. Non-negotiable every working day.

## Inputs

- GHL pipeline, tasks, call/SMS history, KPI tracker
- Notes from today’s intros, dialer, watchshift, confirmations

## Outputs

- EOD form posted to the sales Slack channel (e.g. `#eods-salesteam`)
- CRM reflects today’s work (pipeline cleared, dispositions correct)

---

## Setter EOD

### Why it matters

- Coaching and feedback from real call detail  
- Marketing/product signals from objections and misaligned expectations  
- Proof admin and CRM hygiene happened (not just activity theater)  
- Self-review habit — short daily roll-up

### Admin (complete before submit)

Answer **yes** on the form only if true. Mirrors the [daily checklist](setter-daily-checklist.md#end-of-day-when-you-wrap).

| Task | Standard |
|------|----------|
| **Setter KPI tracker** | Filled for the day (dials, outcomes, etc.) |
| **Pipeline cleared** | No active lead without a **pipeline stage**, accurate disposition context, or **GHL task** (assigned to self or Gabriel) |
| **Dispositions correct** | Every lead you **spoke with** today is reflected in CRM — see [disposition rules](#setter-disposition-rules) |
| **GHL tasks** | Your open tasks current; anything waiting on Gabriel is assigned to Gabriel with context |
| **Hotlist** | See [Hotlist](#hotlist-setter) |
| **Notes** | No “called only” records — calls/SMS threads have notes per [Setter Lead Messaging](setter-lead-messaging.md) |

**Not required:** Routine “audit the next 3–4 days and mark bookings FREE” unless ops assigns a one-off calendar cleanup. Speed-to-lead on **new** bookings is [Watchshift](sop-watchshift.md) / P1, not a standing EOD calendar audit.

### Hotlist (setter)

Leads you flagged today as **high intent** (e.g. pipeline stage **Setter quality lead**, strong intro, waiting on a reply). Before EOD:

- Touch each hotlist lead (call, value SMS, or task), **or**
- Create/update a GHL task with the next step and date.

Do not leave hotlist names only in your head or Slack.

### Setter disposition rules

After every intro, dialer connect, or substantive SMS:

| Outcome | CRM |
|---------|-----|
| Strong pre-demo, not booked yet | Stage: **Setter quality lead** + note |
| Demo with closer booked | Correct booked stage + notes for Gabriel |
| Intro booked on setter calendar | Stage reflects intro slot |
| Not DFY fit | Boot Camp route or lost per [Disqualifying and Financial Qualification](disqualifying-financial-qualification.md) |
| No-show | No-show stage + protocol per [No Shows SOP](no-shows-maximizing-show-rates-setter-levers.md) |
| Junk / wrong number / spam | Lost (or bad lead) + brief note |
| Stuck on call-book with no movement | Move stage or task — nothing idle in limbo |

If unsure of stage name, match existing GHL pipeline labels; escalate naming to ops once.

### Metrics (form fields)

Report honestly with brief context (not bare numbers).

| Field | Report |
|-------|--------|
| Total dials made | Count + block context if useful |
| Total conversations | Count; note connect rate if you track it |
| Booked demos (from outbound) | Count + timing (e.g. 2 tomorrow, 1 next week) |
| Calls confirmed | Demos you confirmed for closer (P3 work) |

### Self grades (1–10)

Energy, focus, biology (food, water, sleep, movement). Short note if any score is low and why.

### Roll-up (required detail)

List **every** intro and meaningful outbound touch today:

**Bad:** `INTRO 1 - good call`

**Good:**

```text
INTRO 1 - [Name] - Booked demo tomorrow 2pm. FUN yes. Motivator: referral well dry. Notes in GHL.
INTRO 2 - [Name] - No-show. Ran protocol, moved to no-show stage, SMS sent.
OUTBOUND 3 - [Name] - Setter quality lead. Burned by prior agency. Gabriel tagged on Slack for pricing question.
```

### Objections / assets question

Flag patterns for pre-call assets or script updates (e.g. repeated “what’s the price on intro?”). Link ideas to [Pre-Call Objection Videos](../marketing/pre-call-objection-videos.md) when relevant.

**Bad:** `None`

**Good:** `3 intros asked price before qualify — suggest pre-call asset or intro framing tweak.`

---

## Closer EOD

### Admin

- Closer KPI tracker complete  
- New clients: new-client form + Slack  
- Pipeline: no-shows staged correctly; demos and follow-ups current  
- Hot list completed  
- Post-demo call forms filled  
- Calendar: unqualified/low-quality future bookings marked FREE (closer-owned hygiene)

### Metrics

Total calls connected, demos scheduled today, demos showed, clients closed, cash collected, UF cash %.

### Roll-up

Per demo: name, outcome, next step, notable objection. Include projection check (“on track for month?”) with brief math if not.

### Objections / assets

Same standard as setter — feed marketing and script improvements.

---

## Form and Slack

- Submit via the **HighLevel EOD form** (team snapshot / automation as implemented).  
- Submissions should post to the dedicated Slack channel (e.g. `#eods-salesteam`) via native GHL Slack integration or make.com — see implementation notes in source export if rebuilding.

## Enforcement (non-negotiable)

| Miss | Action |
|------|--------|
| 1st | Warning |
| 2nd | Final warning; no commission that day |
| 3rd | Off the team |

EOD is a standard, not optional when reps push back on change.

## Quality bar

- Management can coach from roll-ups without pulling recordings first.  
- Pipeline in GHL matches what the rep claims in EOD.  
- Setter EOD aligns with [Setter Daily Checklist](setter-daily-checklist.md) every day.

## Related Docs

- [Setter Daily Checklist](setter-daily-checklist.md)
- [Setter Lead Messaging](setter-lead-messaging.md) — notes + SMS
- [Watchshift SOP](sop-watchshift.md)
- [Power Dialer New Leads SOP](sop-power-dialer-new-leads.md)
- [No Shows and Maximizing Show Rates](no-shows-maximizing-show-rates-setter-levers.md)
- [Money Model And Offer Architecture](../../company/overview-money-model-april-26.md)
- [Identity Core](../../company/doctrine-identity-core-april-26.md)
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md)
- [Pre-Call Objection Videos](../marketing/pre-call-objection-videos.md)

## Open Questions

- [ ] Confirm live EOD form URL / field IDs match this SOP after next GHL publish.
- [ ] Setter KPI tracker location (sheet name or GHL report).
- [ ] Human review: `status: draft` → `active` when Pedro signs off.
