---
title: GHL Pipeline And Disposition Reference
domain: acquisition
owner: operations
status: draft
last_updated: 2026-06-10
smart_lists_version: 2.0
review_cycle: monthly
artifact_type: reference
---

# GHL Pipeline And Disposition Reference

## Purpose

Single source of truth for the **Waiz acquisition GHL pipeline**: stage names, what each stage means, who owns it, the tags and custom fields that control automations, lead grading, and the setter smart lists. Closes the open question in the [Power Dialer SOP](sop-power-dialer-new-leads.md) ("document full GHL pipeline stage list in one disposition reference").

Automation build specs live in [GHL Automation Workflows](ghl-automation-workflows.md). Automated message copy sources from [Setter Lead Messaging](setter-lead-messaging.md) and the [Demo Appointment Confirmation Script](script-demo-appointment-confirmation.md).

## Scope

- Waiz **B2B acquisition** sub-account only (reverse mortgage LO prospects). Not client fulfillment CRMs — see [CRM Infrastructure](../../client-fulfillment/crm-architecture/crm-infrastructure.md).
- One pipeline board. Stages track **where a lead sits**; **smart lists** (Contacts tab) are the setter/closer **work queues**. Tags control **what automation is running**. Never use stage alone to infer automation state.

## Owner

Operations owns this reference. Setter executes dispositions daily; escalate naming conflicts to ops once, then update here.

## Trigger

- Setter or closer needs the correct stage/disposition after any touch.
- Ops is building or editing GHL workflows, tags, fields, or smart lists.
- Auditing pipeline hygiene (EOD "pipeline cleared" per [EOD Report SOP](eod-report-sop-setters-closers.md)).

---

## Smart list quick reference

**Start every shift in Contacts → Smart Lists, not Opportunities.** Clear **DQ-1** every day — it reloads overnight. The board is for stage moves and EOD hygiene only.

| List | Who | Purpose | Clear by |
|------|-----|---------|----------|
| **DQ-1** Clear Today | Setter | All outbound: New Lead, Engaged, Quality, No-Shows | EOD (zero rows, or every row snoozed) |
| **DQ-2** Confirmations | Setter | Intro Booked + Demo Booked due in 48h | P3 block |
| **DQ-3** Scheduled | Setter | `conditional-followup` promises due today | EOD |
| **SL-C1** Demos Next 48 Hours | Closer | Morning prep on demo days | — |
| **SL-C2** Negotiating | Closer | Active deals | Daily |
| **SL-C3** Gabriel Tasks Due | Closer | Handoffs + pricing replies | Daily |

**Setter pin order:** DQ-1 → DQ-2 → DQ-3

Watchshift and P1 intro calls stay interrupt-driven (not a list). Full filter specs below. Build path: **Contacts → Smart Lists → Create → Advanced Filters**.

### How DQ-1 reloads (no manual reset)

GHL smart lists are filter-based — there is no native daily reset. DQ-1 simulates one with two fields:

| Mechanism | Field | Behavior |
|-----------|-------|----------|
| **Worked today** | Last Human Touch | WF-FIELDS sets to today on outbound call/SMS → lead drops out of DQ-1 for the rest of the day |
| **Snoozed** | Next Work Date | Setter sets to tomorrow or a future date → lead stays out until that date |
| **Reload next day** | (automatic) | Leads still in actionable stages whose Last Human Touch is before today and Next Work Date is empty or ≤ today reappear in DQ-1 |

**Setter rule:** Touch = out today. Snooze = Next Work Date. Booked intros/demos move to DQ-2 (not in DQ-1).

---

## Prerequisites audit (run before building lists)

Complete this checklist in GHL before creating smart lists. If any item fails, fix it first — lists will stay empty or wrong without these.

### Pipeline stages

Confirm the acquisition pipeline has these **exact** stage names (smart list filters are case-sensitive):

- [ ] New Lead
- [ ] Engaged
- [ ] Setter Quality Lead
- [ ] Intro Booked
- [ ] Intro No Show
- [ ] Demo Booked
- [ ] Demo No Show
- [ ] Negotiating
- [ ] Warm Nurture
- [ ] Cold Nurture
- [ ] Closed (Won / Lost sub-statuses)

If a live label differs from this doc, rename in GHL **or** update the filter specs here — they must match.

### Contact custom fields

Create under **Settings → Custom Fields → Contact** if missing:

- [ ] **Lead Grade** — dropdown: A / B / C / Junk
- [ ] **Lead Source** — dropdown: Meta / LinkedIn / Referral / Other
- [ ] **Last Human Touch** — date
- [ ] **Next Appointment Date** — date
- [ ] **Next Work Date** — date
- [ ] **Next Follow-Up Date** — date
- [ ] **Post-Demo Objection** — dropdown: Price / Timing / Trust / Partner-Spouse / Thinking / Other

### Tags

Confirm these tags exist (create on first use if GHL auto-creates):

- [ ] `stop-all-nurture`
- [ ] `conditional-followup`
- [ ] `human-active`
- [ ] `src-meta`
- [ ] `nurture:new-lead`, `nurture:appt-reminders`, `nurture:no-show`, `nurture:post-demo`, `nurture:warm`, `nurture:cold`

### Workflow field stamping (powers DQ-1, DQ-2)

- [ ] **WF-03A / WF-03B** set **Next Appointment Date** on booking and on reschedule — see [WF-FIELDS](ghl-automation-workflows.md#wf-fields--custom-field-stamping)
- [ ] **WF-FIELDS** updates **Last Human Touch** on every outbound setter call/SMS — powers DQ-1 exit/reload
- [ ] **WF-04** moves New Lead → Engaged on reply and adds `human-active`

### Smoke test (5 min)

1. New lead or Engaged contact appears in **DQ-1**.
2. Outbound call → **Last Human Touch** updates → contact drops out of DQ-1 same day.
3. Book test intro → **Next Appointment Date** populates → contact appears in **DQ-2** (not DQ-1).
4. Set **Next Work Date** = +3 days on a test contact → stays out of DQ-1 until that date.
5. Delete test contact.

---

## Pipeline stages (10 active + Closed)

| # | Stage | Owner | Definition (a lead is here when…) | Setter action |
|---|-------|-------|------------------------------------|---------------|
| 1 | **New Lead** | Automation → Setter | Meta form in; no reply yet; nothing booked | Power dialer P5 when block opens ([Power Dialer SOP](sop-power-dialer-new-leads.md)) |
| 2 | **Engaged** | Setter | Replied to SMS/email OR setter had a live conversation; new-lead drip OFF | Reply within watchshift window; steer to book |
| 3 | **Setter Quality Lead** | Setter | Strong fit, responsive, **not booked yet** (existing confirmed GHL label) | Hotlist — daily touch per [EOD hotlist rules](eod-report-sop-setters-closers.md#hotlist-setter) |
| 4 | **Intro Booked** | Setter | Intro on setter calendar | Call ASAP — slot is a placeholder ([No Shows SOP](no-shows-maximizing-show-rates-setter-levers.md#the-intro-call-reality)) |
| 5 | **Intro No Show** | Automation + Setter | Missed intro; appointment status marked no-show | Live P6 protocol same day; recovery workflow runs in parallel |
| 6 | **Demo Booked** | Setter | Demo on closer calendar | P3 confirms + pre-call videos ([Demo Confirmation Script](script-demo-appointment-confirmation.md)) |
| 7 | **Demo No Show** | Automation + Setter | Missed demo | Same as intro no-show; closer notified |
| 8 | **Negotiating** | Closer | Post-demo, active deal in motion (replaces "Hot (High Intent)") | Setter assists only when tasked |
| 9 | **Warm Nurture** | Automation | Post-demo unconverted, or timing objection; automated email running | **No manual setter SMS** unless they reply (see two-channel rule below) |
| 10 | **Cold Nurture** | Automation | 30+ days inactive in Warm, or no-show recovery failed | Email-only long-term sequence; no dialing |
| — | **Closed** | — | Won / Lost / Boot Camp / bad data | Remove all nurture tags on entry |

### Closed sub-dispositions

Use the opportunity status + a tag, not extra stages:

| Outcome | Status | Tag |
|---------|--------|-----|
| DFY client signed | Won | — |
| Boot Camp purchased | Won | `boot-camp-route` |
| Routed to Boot Camp offer, undecided | Lost (reopen on purchase) | `boot-camp-route` |
| Opt-out / hostile / junk / wrong number | Lost | `bad-data` if applicable |

### Stage migration map (from the old board)

| Old stage | New stage |
|-----------|-----------|
| Lead In | New Lead |
| Contacted (Nurturing) | delete — pre-reply leads stay in New Lead (drip handles them); post-reply = Engaged |
| Contact Responded | Engaged (rename) |
| Setter Followup (Quality) | Setter Quality Lead |
| Intro Booked / Intro No Show | unchanged |
| Demo Booked / Demo No Show | unchanged |
| Hot (High Intent) | Negotiating |
| Warm (Interested/Timing) | Warm Nurture |
| Cold (Longterm, 90+ days) | Cold Nurture |
| Aged | delete — use Cold Nurture or Closed Lost |
| Conditional Followup | delete — use tag `conditional-followup` + GHL task with date |

LinkedIn outbound prospects who already booked enter directly at **Intro Booked** or **Demo Booked** — they do not pass through New Lead or the Meta drip.

---

## Tags (automation control layer)

Tags — not stages — decide what sends. **A lead must never carry two `nurture:*` tags at once.**

| Tag | Set by | Meaning |
|-----|--------|---------|
| `src-meta` | Existing intake sequences | Meta/FB form lead — only source eligible for the new-lead drip |
| `nurture:new-lead` | WF-02 | New-lead SMS drip active |
| `nurture:appt-reminders` | WF-03A (intro) / WF-03B (demo) | Appointment reminder sequence active |
| `nurture:no-show` | WF-06/07 | No-show recovery sequence active |
| `nurture:post-demo` | WF-08 | Objection-tailored post-demo emails active |
| `nurture:warm` | WF-08 | Broad warm email track active |
| `nurture:cold` | WF-09 | Long-term cold emails active |
| `human-active` | WF-04 reply handler, or setter manually | A human owns this conversation — **all automated sends skip**. Setter adds it before any manual text to a Warm/Cold lead; auto-removed after 48h of no activity |
| `stop-all-nurture` | Setter/ops manually | Hard kill switch — no workflow may send anything |
| `boot-camp-route` | Setter/closer | Not DFY fit; Boot Camp offer presented per [Money Model](../../company/overview-money-model-april-26.md) |
| `conditional-followup` | Setter | Lead asked for contact at a specific future date — set **Next Follow-Up Date** + GHL task; pauses SMS workflows; surfaces on DQ-3 when due |
| `retrigger-noshow-recovery` | Ops (one-time) | Bulk migration trigger for the no-show backlog |

**Global send rule (built into every workflow):** if `human-active` OR `stop-all-nurture` is present, skip the send. On entering any nurture workflow, remove all other `nurture:*` tags first.

---

## Custom fields

| Field | Type | Values | Updated by |
|-------|------|--------|------------|
| **Lead Grade** | Dropdown | A / B / C / Junk | Setter, on every connect |
| **Lead Source** | Dropdown | Meta / LinkedIn / Referral / Other | Existing intake sequences (Meta) or manual |
| **Last Human Touch** | Date | — | WF-FIELDS on outbound setter call/SMS; powers DQ-1 exit and daily reload |
| **Post-Demo Objection** | Dropdown | Price / Timing / Trust / Partner-Spouse / Thinking / Other | Closer post-call form; branches WF-08 emails |
| **Next Appointment Date** | Date | — | WF-03A/B on appointment created; powers DQ-2 |
| **Next Work Date** | Date | — | Setter, when snoozing a lead out of DQ-1 until a future date |
| **Next Follow-Up Date** | Date | — | Setter, when applying `conditional-followup`; powers DQ-3 |

### Next Work Date rules (DQ-1 snooze)

Setter sets **Next Work Date** to remove a lead from today's queue without closing them. Distinct from **Next Follow-Up Date** (prospect promise → DQ-3).

| Situation | Next Work Date | Also set |
|-----------|----------------|----------|
| "Call me tomorrow" | Tomorrow | GHL task |
| "Call me after the 15th" | That date | `conditional-followup` tag + Next Follow-Up Date (DQ-3) |
| Attempted today, retry in 2 days | +2 days | Note |
| Couldn't reach today, defer | Tomorrow | GHL task + note |
| Booked intro/demo | Clear (empty) | Stage → Intro/Demo Booked (moves to DQ-2) |
| Lost / Boot Camp / Junk | Clear | Stage → Closed |

**Board filtering note:** the Opportunities view cannot filter by contact tags or contact fields. If the setter wants Grade visible/filterable on the pipeline board, mirror **Lead Grade only** as an *opportunity* custom field (single-select), synced by workflow via Update Opportunity. Do not mirror `nurture:*` tags — nobody filters the board by those.

### Lead Grade rules (setter sets on every connect)

| Grade | Definition | Treatment |
|-------|------------|-----------|
| **A** | FUN-qualified, budget path plausible, responsive, demo-ready | Call today; hotlist |
| **B** | Interested but timing/authority gap, or recovered no-show signal | Touch this week |
| **C** | Cold reply history, long silence, post-demo "not now" | Automation nurtures; no dialing priority |
| **Junk** | Wrong number, spam, not a reverse LO, hostile opt-out | Closed Lost + note; never re-enter nurture |

FUN criteria: [Intro Call Qualification Framework](intro-call-qualification-framework.md). Not-DFY-fit routing: [Disqualifying and Financial Qualification](disqualifying-financial-qualification.md) — Boot Camp, never dropped without an offer.

---

## Smart lists (setter + closer daily views)

Smart lists live in the **Contacts tab** (Contacts → Smart Lists), not Opportunities. Work each list **top to bottom, no cherry-picking**.

Build path: Contacts → Smart Lists → Create → Advanced Filters → filters below (AND logic) → columns + sort → Save → pin per [quick reference](#smart-list-quick-reference).

### Setter lists (daily queue model)

#### DQ-1 — Clear Today (primary outbound queue)

One list for all outbound work. Cleared daily; reloads overnight via Last Human Touch + Next Work Date filters.

| Setting | Value |
|---------|-------|
| **Name** | DQ-1 — Clear Today |
| **Stage includes** | New Lead, Engaged, Setter Quality Lead, Intro No Show, Demo No Show |
| **Stage excludes** | Intro Booked, Demo Booked, Negotiating, Warm Nurture, Cold Nurture, Closed |
| **Last Human Touch** | is empty OR is **before today** |
| **Next Work Date** | is empty OR is **today or earlier** |
| **Tag excludes** | `stop-all-nurture` |
| **Sort** | Last Human Touch — **oldest first** |
| **Columns** | Name, Phone, Stage, Lead Grade, Last Human Touch, Next Work Date, Created |
| **Maps to** | P5 dial blocks, P6 no-shows, EOD outbound sweep |

**Within-list priority (setter discipline — GHL sort is oldest Last Human Touch first):**

1. Fresh New Lead (Created today) — speed-to-lead
2. Engaged / `human-active` replies — respond first
3. A-grade (Lead Grade = A)
4. Everything else top to bottom

**EOD pass/fail:** DQ-1 is **empty**, OR every remaining row has Next Work Date ≥ tomorrow + GHL task + note. Fail = actionable lead with no touch today and no Next Work Date.

#### DQ-2 — Confirmations

Calendar-driven work — separate from DQ-1. Booked intros/demos do not appear in the outbound queue.

| Setting | Value |
|---------|-------|
| **Name** | DQ-2 — Confirmations |
| **Filters** | Stage include (**Intro Booked, Demo Booked**) AND Next Appointment Date is **within next 2 days** |
| **Sort** | Next Appointment Date — **soonest first** |
| **Columns** | Name, Phone, Stage, Next Appointment Date |
| **Maps to** | P3 confirms ([Demo Confirmation Script](script-demo-appointment-confirmation.md)) |

Depends on WF-03A/B stamping **Next Appointment Date** on booking and reschedule.

#### DQ-3 — Scheduled

Prospect promises — separate from Next Work Date (internal snooze).

| Setting | Value |
|---------|-------|
| **Name** | DQ-3 — Scheduled |
| **Filters** | Tag = `conditional-followup` AND Next Follow-Up Date is **today or earlier** (include empty to catch tagging mistakes) |
| **Sort** | Next Follow-Up Date — **oldest first** |
| **Columns** | Name, Phone, Stage, Next Follow-Up Date, Lead Grade |
| **Maps to** | EOD — "call me after the 15th" promises; nothing overdue past same day |

### Closer lists (Gabriel)

#### SL-C1 — Demos Next 48 Hours

| Setting | Value |
|---------|-------|
| Filters | Same as **DQ-2** — Stage include (**Intro Booked, Demo Booked**) AND Next Appointment Date **within next 2 days** |
| Sort | Next Appointment Date — **soonest first** |
| Columns | Name, Phone, Stage, Next Appointment Date, Lead Grade, Post-Demo Objection |
| Maps to | Morning prep on demo days |

#### SL-C2 — Negotiating (active deals)

| Setting | Value |
|---------|-------|
| Filters | Stage = **Negotiating** |
| Sort | Last Activity — **oldest first** |
| Columns | Name, Phone, Post-Demo Objection, Last Activity |
| Maps to | Daily deal follow-up |

#### SL-C3 — Gabriel Tasks Due

| Setting | Value |
|---------|-------|
| Filters | Tasks assigned to Gabriel AND due **today or overdue** |
| Sort | Due date — **oldest first** |
| Columns | Name, Phone, Task title, Due date, Stage |
| Maps to | Setter handoffs, pricing/policy replies, LinkedIn forwards |

### Daily rhythm

| When | List |
|------|------|
| Start of shift | Open **DQ-1** — see today's outbound workload |
| Continuous (interrupts) | Watchshift alerts + P1 intro calls |
| P3 block | **DQ-2** — top to bottom |
| P5 + P6 outbound | **DQ-1** — top to bottom until empty or snoozed |
| EOD | **DQ-1** cleared or snoozed + **DQ-3** zero overdue + Opportunities board scan |

**Closer daily:** SL-C2 + SL-C3 every day; SL-C1 on demo days.

### Opportunities board — use vs. avoid

**Use the board for:** stage moves after every touch, EOD pipeline cleared orphan scan, funnel orientation.

**Do not use the board for:** finding outbound work (**DQ-1**), confirmations (**DQ-2**), or scheduled promises (**DQ-3**).

### Week-one validation (pilot)

| Signal | Likely cause | Fix |
|--------|--------------|-----|
| DQ-1 never empties | Last Human Touch not updating on attempts | Enable WF-FIELDS |
| DQ-2 empty but demos on calendar | WF-03A/B not stamping Next Appointment Date | Verify WF-FIELDS + reschedule path |
| Leads stuck in DQ-1 overnight wrongly | Next Work Date not set when deferring | Train snooze workflow |
| Same lead every day, no progress | Touch updates Last Human Touch but no stage advance | Review disposition — book, nurture, or close |
| DQ-3 has empty Next Follow-Up Date rows | `conditional-followup` without date | Fix disposition |

**Setter briefing:** "Clear DQ-1 every day. Touch = out today. Snooze = Next Work Date. Booked = DQ-2."

### Appendix — superseded SL-1 through SL-7 (v1.0)

Replaced by the daily queue model (v2.0) on 2026-06-10. Do **not** build these if starting fresh — use DQ-1, DQ-2, DQ-3 only.

| Old list | Absorbed into |
|----------|---------------|
| SL-1 Speed-to-Lead | DQ-1 (New Lead + not touched today) |
| SL-2 Call First (A-grade) | DQ-1 (A-grade priority within list) |
| SL-3 Confirmations Due | DQ-2 |
| SL-4 Stale Responders | DQ-1 (Last Human Touch before today) |
| SL-5 Scheduled Follow-Ups | DQ-3 |
| SL-6 Power Dialer Queue | DQ-1 (all New Lead ages) |
| SL-7 No-Shows This Week | DQ-1 (Intro/Demo No Show stages) |

---

## Two-channel rule (prevents over-texting)

1. Leads in **Warm Nurture** or **Cold Nurture** get automated email only. If the setter needs to text one manually, add `human-active` first — this pauses the email cadence for 48 hours.
2. A reply on **any** channel fires the reply handler (WF-04): all `nurture:*` tags removed, `human-active` added, stage → Engaged (if pre-demo), setter notified via watchshift.
3. No lead re-enters the new-lead drip (WF-02) after a reply — re-engagement runs through [WF-05 Stale Engaged Recovery](ghl-automation-workflows.md#wf-05--stale-engaged-recovery) (2 touches max), then manual.

---

## Disposition quick table (after every touch)

Supersedes scattered stage references; consistent with [EOD disposition rules](eod-report-sop-setters-closers.md#setter-disposition-rules).

| Outcome | Stage | Tags / fields |
|---------|-------|---------------|
| Spoke, strong, not booked | Setter Quality Lead | Grade A/B + note + task |
| Replied to drip, conversation open | Engaged | `human-active` (auto via WF-04) |
| Intro booked | Intro Booked | WF-03A takes over reminders |
| Demo booked | Demo Booked | WF-03B takes over; closer notes |
| No-show (intro or demo) | Intro/Demo No Show | WF-06/07 auto-runs; run live P6 protocol too |
| Post-demo, deal active | Negotiating | Closer owns |
| Post-demo, unconverted | Warm Nurture | Post-Demo Objection field set via closer form → WF-08 |
| Not DFY fit | Closed (or Boot Camp pending) | `boot-camp-route` per [Money Model](../../company/overview-money-model-april-26.md) |
| Bad data / junk | Closed Lost | Grade = Junk |
| Asked for specific future date | current stage | `conditional-followup` + Next Follow-Up Date + GHL task (DQ-3) |
| Snooze out of today's queue | current stage | Next Work Date = future + GHL task + note |
| Attempted today, retry later | current stage | Last Human Touch = today (auto); optional Next Work Date if not tomorrow |

---

## Related docs

- [GHL Automation Workflows](ghl-automation-workflows.md) — build specs for all 9 workflows
- [Setter Daily Checklist](setter-daily-checklist.md) — priority stack
- [Power Dialer New Leads SOP](sop-power-dialer-new-leads.md) — P5 dialing
- [EOD Report SOP](eod-report-sop-setters-closers.md) — pipeline-cleared standard
- [No Shows And Maximizing Show Rates](no-shows-maximizing-show-rates-setter-levers.md) — live no-show protocol
- [Money Model And Offer Architecture](../../company/overview-money-model-april-26.md) — routing rules

## Open Questions

- [ ] Confirm final dropdown values for Post-Demo Objection with closer (match post-call form).
- [ ] Confirm 48h `human-active` auto-expiry is acceptable or should be 72h.
