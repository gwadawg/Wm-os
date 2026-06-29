---
title: RM iMessage Appointment Follow-Up
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-06-19
review_cycle: monthly
artifact_type: script
source_document: internal — rm-imessage-intent-drip-7day.md + dscr-nurture-and-booking-laura.md + fulfillment-lead-lifecycle Stage 5
---

# RM iMessage Appointment Follow-Up

## Purpose

**Remind** first-time bookers of their appointment — with **one optional value note** before the call. Broadcast only. No conversation, no questions, no reply prompts.

## Scope

- Booking confirmation (intent-segmented, short)
- One optional **value** touch (appointments booked 48+ hours out)
- Three **reminders**: 24 hours, 4 hours, 30 minutes before the call
- No-show acknowledgment (2 touches — rebook via call center, not SMS)
- GHL workflow; per-client snapshot with custom values

## Owner

Client Success (Laura Moco). LO approves value lines.

## Trigger

- First **booked appointment** on the LO calendar
- Routed by `form_intent` (same as [intent drip](rm-imessage-intent-drip-7day.md))
- **No-show disposition** → Phase 4 acknowledgment + call center rebook task

## Copy rules

Appointment follow-up is **reminder + value only**. Every message is a statement.

| Rule | Example |
|------|---------|
| **Zero question marks** | Never end with `?` — no "still good?", "any questions?", "ready?" |
| **One job per text** | Confirm **or** value **or** remind — not all three in one message |
| **Reminders = date, time, who calls** | No re-pitching the outcome in every ping |
| **Value = one useful fact** | Prep tip, what the call is, or one reassurance — not a mini sales letter |
| **No reply prompts** | No Y/R, no "just reply," no "let me know" |

If a lead texts back → call center or LO handles per ops SOP. This workflow does **not** auto-respond.

## GHL routing

| Segment | `form_intent` values |
|---------|----------------------|
| 1 — Remove mortgage payment | `remove_mortgage_payment` |
| 2 — Pay debt off | `pay_off_debt` |
| 3 — Cash out / strategic | `tax_free_cash_out` or `cash_out` |

**Rules**

1. **Appointment booked** → exit pre-booking nurture → AI off → enter this workflow.
2. Value touch: **+24 hr after booking**, only if appointment is **48+ hours out**.
3. Reminders: **24 hr**, **4 hr**, **30 min** before `{{appointment.time}}` (lead local time).
4. **No-show** → Phase 4 → call center rebook task.
5. **Rebook after no-show** → if `second_booking` flag → [Second-Booking Follow-Up](rm-imessage-second-booking-followup.md); else restart this workflow.
6. **Reschedule** (same booking attempt, new slot) → [Reschedule follow-up](#reschedule-same-booking-new-time) — not second booking.
7. **Show** disposition → exit workflow.

## Merge fields

| Token | Use |
|-------|-----|
| `{{contact.first_name}}` | Lead first name |
| `{{user.first_name}}` | LO first name |
| `{{custom_values.setter_display_name}}` | Assistant name |
| `{{appointment.date}}` | Booked date |
| `{{appointment.time}}` | Booked time |

---

## Touch 1 — Confirmation (instant)

Date, time, who calls. One outcome line max.

### Segment 1 — Remove mortgage payment

```
{{contact.first_name}}, you're booked with {{user.first_name}} on {{appointment.date}} at {{appointment.time}}. He'll call this number to walk through eliminating your monthly mortgage payment.
```

### Segment 2 — Pay debt off

```
{{contact.first_name}}, you're booked with {{user.first_name}} on {{appointment.date}} at {{appointment.time}}. He'll call this number to go over clearing debt with your home equity.
```

### Segment 3 — Cash out / strategic

```
{{contact.first_name}}, you're booked with {{user.first_name}} on {{appointment.date}} at {{appointment.time}}. He'll call this number to walk through your cash-out options.
```

---

## Touch 2 — Value (optional)

**When:** +24 hr after booking, only if appointment is **48+ hours out**.  
**Skip** if same-day or next-day booking.

### Segment 1

```
{{contact.first_name}} — your call with {{user.first_name}} is about 20 minutes. No application on the call. He'll have what you submitted and run numbers for your home.
```

### Segment 2

```
{{contact.first_name}} — your call with {{user.first_name}} is about 20 minutes. No application on the call. He'll walk through how proceeds could clear debt without adding a required monthly mortgage payment.
```

### Segment 3

```
{{contact.first_name}} — your call with {{user.first_name}} is about 20 minutes. No application on the call. He'll compare lump sum, line of credit, and monthly draw options for your home.
```

---

## Touch 3 — Reminder, 24 hours before

All segments — same copy.

```
{{contact.first_name}}, reminder: {{user.first_name}} tomorrow at {{appointment.time}}. He'll call this number.
```

---

## Touch 4 — Reminder, 4 hours before

```
{{contact.first_name}}, {{user.first_name}} calls today at {{appointment.time}} on this number.
```

---

## Touch 5 — Reminder, 30 minutes before

```
{{contact.first_name}}, {{user.first_name}} calls in about 30 minutes at {{appointment.time}}.
```

---

## Reschedule (same booking, new time)

When the lead **moves** an existing appointment — not a no-show rebook.

| | Reschedule | No-show rebook |
|---|------------|----------------|
| **What happened** | Proactive move before or after a missed slot, same intent to meet | Missed the call; new appointment created |
| **Who does it** | Call center or LO updates GHL calendar | Call center outbound after no-show disposition |
| **`second_booking` tag** | No | Yes |
| **SMS** | One confirm + reminders only | Second-booking drip (or first-booking if first rebook) |

**Trigger:** Appointment `date` / `time` updated in GHL while contact remains **Booked** (calendar reschedule event — not Cancel + new book).

**GHL rules**

1. **Cancel** all pending messages tied to the **old** slot.
2. Send **one** reschedule confirmation (instant) — below.
3. **Restart reminders** for the **new** slot only.
4. Do **not** re-send the value touch.
5. Do **not** increment `appointment_booking_count` or add `second_booking`.
6. Reminder cadence stays on the **current track** (first-booking 24/4/30 or second-booking 24/1).

**Reschedule confirmation (all segments — broad)**

```
{{contact.first_name}}, your call with {{user.first_name}} is now {{appointment.date}} at {{appointment.time}}. He'll call this number.
```

Then schedule Touch 3–5 from this doc (first track) or Touch 3–4 from [second-booking follow-up](rm-imessage-second-booking-followup.md) if already on that track.

**Operational note:** Rescheduling is **not** done over SMS. If a lead texts asking to move the call, call center or LO updates the calendar — this workflow fires on the update.

---

**Trigger:** No-show disposition in GHL.

Rebooking is **call center outbound** — not SMS.

### +10 minutes after no-show

```
{{contact.first_name}}, {{user.first_name}} tried to connect at {{appointment.time}} and missed you. Someone from the team will call to reschedule.
```

### +24 hours after no-show

```
{{contact.first_name}}, {{user.first_name}} is still available when timing works. The team may follow up by phone.
```

---

## Related docs

- [RM iMessage Second-Booking Follow-Up](rm-imessage-second-booking-followup.md) — rebook / second appointment
- [RM iMessage Intent Drip (7-Day)](rm-imessage-intent-drip-7day.md) — pre-booking nurture
- [How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)
- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Open questions

- [ ] Per-client LO approval of value lines
- [ ] Skip 24-hr reminder for same-day bookings
- [ ] Team Google Doc publish after LO review
