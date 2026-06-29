---
title: RM iMessage Second-Booking Follow-Up
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-19
review_cycle: monthly
artifact_type: script
source_document: internal — rm-imessage-appointment-followup.md
---

# RM iMessage Second-Booking Follow-Up

## Purpose

**Remind** second-time bookers of their appointment — with **one value note** before the call. Shorter and **broad** (no intent segments). Broadcast only. No questions, no reply prompts.

## Scope

- Rebook confirmation (one line)
- One **value** touch (rotate A / B / C)
- Two **reminders**: 24 hours and 1 hour before the call
- **4 touches total** — they already received the full first-booking sequence

## Owner

Client Success (Laura Moco). LO approves value lines.

## Trigger

Second **booked appointment** after a **no-show** — flag via tag `second_booking`, `appointment_booking_count` ≥ 2, or prior **No-show** disposition when the next appointment is created.

**Not a second booking:** [Reschedule](rm-imessage-appointment-followup.md#reschedule-same-booking-new-time) (same attempt, new time) — no `second_booking` tag, no value touch repeat.

## Copy rules

Same as [first-booking follow-up](rm-imessage-appointment-followup.md#copy-rules):

- **Zero question marks**
- **Reminders = date, time, who calls** — nothing else
- **Value = one useful fact** — prep, reassurance, or what the call is
- **Broad language** — your home, your options, your situation — not payment/debt/cash-out segments
- **No reply prompts**

## GHL routing

1. **First booking** → [RM iMessage Appointment Follow-Up](rm-imessage-appointment-followup.md).
2. **Reschedule** (calendar update, same attempt) → [reschedule confirm + reminders only](rm-imessage-appointment-followup.md#reschedule-same-booking-new-time) — **not** this workflow.
3. **Second booking** after no-show (flag present) → this workflow; exit first-booking workflow.
4. Value touch: **+24 hr after rebook**, only if appointment is **36+ hours out**.
5. Reminders: **24 hr** and **1 hr** before `{{appointment.time}}`.
6. **Show** or **Cancel** → exit workflow.
7. Second no-show → [first-booking no-show acknowledgment](rm-imessage-appointment-followup.md#phase-4--no-show-acknowledgment) + call center task.

## Merge fields

| Token | Use |
|-------|-----|
| `{{contact.first_name}}` | Lead first name |
| `{{user.first_name}}` | LO first name |
| `{{appointment.date}}` | Booked date |
| `{{appointment.time}}` | Booked time |

---

## Touch 1 — Confirmation (instant)

```
{{contact.first_name}}, you're booked with {{user.first_name}} on {{appointment.date}} at {{appointment.time}}. He'll call this number.
```

---

## Touch 2 — Value (optional)

**When:** +24 hr after rebook, only if appointment is **36+ hours out**.  
Rotate one variant per rebook so repeat no-shows don't get the same line.

### Value A — Prep

```
{{contact.first_name}} — for your call on {{appointment.date}}, a rough home value and mortgage balance helps {{user.first_name}} run numbers faster. Ballpark is fine.
```

### Value B — What the call is

```
{{contact.first_name}} — your call with {{user.first_name}} is about 20 minutes. No application on the call. He'll walk through what using your home equity could look like for your situation.
```

### Value C — Stay in the home

```
{{contact.first_name}} — you stay on title and in the home. {{user.first_name}} will cover how that works on the call, including taxes and insurance.
```

**Skip Touch 2** when the appointment is within 36 hours.

---

## Touch 3 — Reminder, 24 hours before

```
{{contact.first_name}}, reminder: {{user.first_name}} tomorrow at {{appointment.time}}. He'll call this number.
```

---

## Touch 4 — Reminder, 1 hour before

```
{{contact.first_name}}, {{user.first_name}} calls in about an hour at {{appointment.time}}.
```

---

## What not to repeat

| First booking already sent | Second booking skips |
|----------------------------|----------------------|
| Intent-specific outcome pitch | Broad "your home" / "your situation" only |
| 24 hr + 4 hr + 30 min reminders | 24 hr + 1 hr only |
| Full confirmation with outcome line | One-line confirm (date, time, who calls) |

---

## Related docs

- [RM iMessage Appointment Follow-Up](rm-imessage-appointment-followup.md) — first booking
- [Call Center Appointment-Setting Script](../call-center/script-appointment-setting-call.md) — rebook outbound

## Open questions

- [ ] GHL tag/field name for second booking per snapshot
- [ ] Third+ booking: this workflow or manual-only
- [ ] Team Google Doc publish after LO review
