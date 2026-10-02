---
title: Call Center — Call Flow
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-10-01
review_cycle: monthly
artifact_type: doctrine
---

# Call Center — Call Flow

## Purpose

Decide what the rep is trying to do on every connected call, and which path they take.

## Scope

Every fulfillment call, every offer. Scripts fill in the words. This page is the order of decisions.

## The outcome

Get the client into as many real conversations as possible with the leads generated for them.

A conversation is either a **live transfer** that connects, or a **booked appointment** the lead has actually committed to. Both count. Live transfer is the one to reach for first, because the conversation happens on this call.

## Before the rep dials

Pre-qualification runs in automation on the back end. The rep does not re-qualify the lead to decide whether they are allowed to book.

On the call, the rep may book anyone who is **interested**.

## Decision order

1. **Are they interested?**
   - No: end the call without a booking.
   - Yes: continue.
2. **Does the client file say this client is approved for live transfer, and is right now inside the loan officer's working hours?**
   - Yes: ask if they are free to talk to the loan officer right now.
   - No: go to booking. Do not attempt a live transfer.
3. **Can they talk right now?**
   - Yes: attempt the live transfer.
   - Any reason they cannot talk right now: go to booking.
4. **Did the live transfer connect?**
   - Yes: the conversation is delivered. Stop.
   - No: go to booking.

Booking rules for step 2–4 when the path is an appointment: [Booking rules](booking-rules.md).

## What the rep is selling

The appointment, or the transfer. The rep follows the show-rate rules on the booking path so the lead arrives. See [Show rate on the call](show-rate.md).

## How the call is run

This page is the decision order. The stages the rep moves through to get there are in the [call framework](call-framework.md).

## Related

- [Call framework](call-framework.md)
- [Representation](representation.md)
- [Booking rules](booking-rules.md)
- [Show rate on the call](show-rate.md)
- [Call center hub](README.md)
