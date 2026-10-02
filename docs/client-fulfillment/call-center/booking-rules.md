---
title: Call Center — Booking Rules
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-10-01
review_cycle: monthly
artifact_type: doctrine
---

# Call Center — Booking Rules

## Purpose

Set how a rep puts an appointment on the calendar once the [call flow](call-flow.md) has landed on booking.

## Scope

The booking moment on the live call. Reminder texts after the booking are the next layer, listed in the [call center hub](README.md).

## Where the appointment lives

The rep books in the **Waiz subaccount**, on the **number Waiz hosts for that client**.

The appointment is the lead's call with the client. Follow-up messages about that appointment go out as the client's assistant, because Waiz booked it on Waiz's number.

## How soon

Book the soonest time the lead will commit to. The further out the appointment, the lower the chance they show.

Push for an earlier time. If they cannot do soon, take the best time that works for them.

## What counts as a time

Lock a time only when the lead is sure that time works.

"Try me then and see if I'm around" is not a booking. Do not set it.

Before the time is locked, the rep weighs out the soft time, then asks whether anything would stop them from being there. That surfaces the real conflict while the time can still be moved. The mechanic is in [call framework stage 6](call-framework.md#6-find-time-or-transfer); the finished wording is a script decision.

A callback the lead offers you is an open slot they have already agreed to. Book the client into it instead of calling back yourself.

## Related

- [Call framework](call-framework.md)
- [Call flow](call-flow.md)
- [Show rate on the call](show-rate.md)
- [Dial cadence](dial-cadence.md)
- [Call center hub](README.md)
