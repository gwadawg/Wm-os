---
title: CCM Command Dashboard Design
domain: operations
owner: operations
status: draft
last_updated: 2026-07-17
review_cycle: monthly
artifact_type: overview
related_docs:
  - docs/operations/people/call-center-manager-daily-os.md
  - docs/operations/people/call-center-manager-role-scorecard.md
  - docs/plans/2026-07-15-role-clarity-lane-map.md
---

# CCM Command Dashboard Design

## Purpose

Give Pedro (CCM) one login home in Mr. Waiz that shows floor pace, week
Booking/Show health, under-KPI clients in his lane, and a read-only Daily OS
reminder — without inventing a second analytics product.

## Scope

- **In:** Team Dashboards → CCM Command composed board (v1)
- **Out (v1):** Interactive checklist, live idle/attendance, stack-bug queue,
  Mon/Thu commitment objects, other role boards (nav group only)

## Decisions

| Decision | Choice |
|----------|--------|
| Modes | One surface: situation + act + reminder; time-aware framing only |
| Data | Hybrid — existing pace/goals/health now; live status slots later |
| Nav | New **Team Dashboards** group; CCM first; future CS / MB siblings |
| Playbook | Read-only Daily OS day shape + priority stack |
| Access | CCM + leadership (owner; admin; ops_overview / client_health / ceo) |
| Landing | Linked roster `pay_type === ccm` → land on CCM Command |

## Page bands

1. **Situation** — Today dials/bookings vs goal sum; week dials/bookings;
   week show rate; under-KPI count; Mon/Thu reds-day banner
2. **Team at a glance** — Call-rep cards: dials vs daily goal, bookings,
   pace vs day elapsed; behind-first; deep link to Call Center Hub
3. **Under-KPI clients** — CCM lens only (booking / show / hand-raise /
   conversation — never CPL/CPQL); deep link to Client Success CCM lens
4. **Day Playbook** — Static blocks + priority stack from
   [CCM Daily OS](../operations/people/call-center-manager-daily-os.md);
   highlight current block; links to Schedule, Credit Queue, CCM EOD

## Data sources (Mr. Waiz)

- Agent events + goals + enriched bookings (floor / pace)
- Client health bundle + `ccmStatus` (under-KPI list)
- Static playbook config in app (sourced from Daily OS)

## Phase 2 hooks

- Live attendance / idle / wrong-account on agent cards
- Stack-bug queue + Mon/Thu named commitments shared with Laura

## Success

Pedro opens Mr. Waiz and immediately sees who is behind today, which logos
need dial focus, and what priority order to run — without hunting tabs.
