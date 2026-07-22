---
title: KPI Review Meeting SOP Design
domain: operations
owner: client-success
status: draft
last_updated: 2026-07-21
review_cycle: monthly
artifact_type: overview
related_docs:
  - docs/plans/2026-07-21-team-call-runbooks-design.md
  - docs/plans/2026-07-13-team-restructure-design.md
  - docs/plans/2026-07-15-role-clarity-lane-map.md
  - docs/operations/people/client-success-daily-os.md
  - docs/kpis/client-diagnostic-playbook-runnable.md
  - docs/client-fulfillment/client-success/constraint-troubleshooting-sop.md
---

# KPI Review Meeting SOP Design

## Purpose

Define the company standard for Mon/Thu KPI review so the team can open a lean
Team Meetings runbook and a linked Resource Library SOP — without flooding the
form — and leave every under-KPI account with an action plan plus a documented
explanation of what went wrong.

## Scope

### In (this design)

- One **KPI Review Meeting SOP** with two sections: Monday Week Plan and
  Thursday Commitment Check (positions only; no personal names).
- One linked **Under-KPI Diagnosis Ladder** (system vs quality, basic data
  checklist, solve cadence).
- Publish both into Mr. Waiz Resource Library with `related_docs` backlinks.
- Light Team Meetings wiring: replace Mon/Thu PLACEHOLDER `agenda_md`, add
  “Open SOP” / “Diagnosis ladder” links. Checklist keys stay stable.
- Note-line format defined in the SOP for use in existing meeting
  summary / follow_ups (form fields not redesigned this pass).

### Out (this design)

- New disposition fields or structured commitment / RYG board objects.
- SOPs for other meeting series (setter weekly, daily training, ops planning,
  Fri Exec Q&A).
- Rewriting the Client Health grader, KPI bands, or full diagnostic rulebook.
- Team Google Drive publish (optional later after `status: active`).

## Locked decisions

| Topic | Choice |
|-------|--------|
| Audience | Company standard — **positions only** (Client Success, Media Buyer, Call Center Manager, Founder, Ops) |
| Host | Client Success for Mon and Thu |
| Success bar | Every red leaves Mon with **action plan + short “what went wrong” explanation**; Thu verifies land / adjust |
| Notes storage (near-term) | Existing meeting disposition notes; SOP defines copy-paste line format; **no new form fields this pass** |
| Doc packaging | Two linked docs; Mon + Thu are **two sections of the meeting SOP** |
| Delivery | Approach 2 — docs + library + light runbook links |
| Numbers source of truth | Mr. Waiz live grading + reporting `docs/KPIS.md` (do not copy tier tables into the SOP) |

## Architecture

```
Wm-os (canonical markdown)
  kpi-review-meeting-sop.md
  under-kpi-diagnosis-ladder.md
        │
        ▼ import
Mr. Waiz Resource Library  (/library/{slug})
        ▲
        │ Open SOP links
Team Meetings runbook (checklist + agenda only)
  mon-kpi-week-plan
  thu-kpi-commitment-check
```

### Artifact paths

| Artifact | Path / slug |
|----------|-------------|
| Meeting SOP (Wm-os) | `docs/operations/people/kpi-review-meeting-sop.md` |
| Ladder (Wm-os) | `docs/operations/people/under-kpi-diagnosis-ladder.md` |
| Library slug — meeting | `kpi-review-meeting-sop` |
| Library slug — ladder | `under-kpi-diagnosis-ladder` |
| Runbook seeds | Mr. Waiz `src/lib/team-meetings.ts` (`mon-kpi-week-plan`, `thu-kpi-commitment-check`) |
| Runbook UI | Mr. Waiz `src/components/TeamMeetings.tsx` |

## Meeting SOP content (Section A + B)

### Role ownership (positions)

| Role | Owns in the room |
|------|------------------|
| Client Success | Host; R/Y/G rollup; client/LO risk; captures action plans + explanations into meeting notes |
| Media Buyer | Reds on CPL / CPQL / opt-in / lead quality |
| Call Center Manager | Reds on hand-raise/booking, show, dial coverage on under-KPI logos |
| Founder | Not required in-room; reviews notes later; 911 / DATA_HOLD / GHL approval |

### Section A — Monday Week Plan (~25 min)

1. Rules (60s): one primary constraint per red; owners speak only on their reds; no creative debates.
2. R/Y/G scan from the app (Act now + Below KPI; exclude fresh launches unless flagged).
3. Per red (2–3 min): confirm north-star miss → system vs quality fork → action plan + one-sentence explanation.
4. OB glance for launches this week; close.

North star: RM/DSCR = CPConv; HE = hand-raise and/or show. Do not chase CPL alone when CPConv is healthy.

### Section B — Thursday Commitment Check (~25 min)

1. Open commitments only (no full book re-scan).
2. Each item: landed / blocked / missed → re-commit or escalate to Fri Q&A intake.
3. Remind Thu EOD questions for Fri Exec Q&A (decisions only — not KPI status).

### Note / action-plan line format

Paste into existing meeting summary or follow_ups until the form is refined:

```
[Client] · [911|Below] · Why: [one sentence] · Constraint: [system|quality / label] · Plan: [role] will [action] by [date] · Success: [signal]
```

### In / Out

**In:** reds with role owners, explanations, action plans, OB glance, Thu follow-through.  
**Out:** creative debates, Founder status theater, deep coaching, rewriting the grader.

### Form checklist keys (unchanged)

Mon: `ryg_scan_done`, `reds_have_owners`, `commitments_named`, `ob_glance`  
Thu: `commitments_checked`, `still_red_recommitted`, `fri_qa_reminded`

## Under-KPI Diagnosis Ladder

Separate library doc. Used async Tue–Wed (and when a red is named mid-week). Links from Mon runbook and from the meeting SOP.

### Solve cadence

1. Mon names the red + thin explanation + action plan.
2. Tue–Wed: owning role runs the ladder.
3. Thu: verify action landed; update note if diagnosis changed.

### Ladder steps

| Step | Check | Outcome |
|------|--------|---------|
| 0 | Data complete for W14? (spend, leads, booked, show/no-show dispositions) | No → system / DATA_HOLD — fix data first |
| 1 | Known webhook / GHL / attribution break? | Escalate Ops/Founder; no funnel thrash |
| 2 | External shock? | Observe 48–72h |
| 3 | App north star still Below/911? | If no, do not invent a red |
| 4 | First broken layer top→down: Ads → Landing → Call center → Show/LO | Primary constraint |
| 5 | System vs quality | System = tracking/disposition/spend; Quality = creative, targeting, setter execution, LO show |
| 6 | One lever + role owner + timebox | Link constraint troubleshooting SOP; success = band move |
| 7 | Escalate | 911 same day; DATA_HOLD immediate; GHL changes need Founder approval |

### Basic data checklist

- Ad spend present for the window
- Lead volume not obviously missing vs Meta/GHL
- Appointment outcomes dispositioned
- Booking agent / credit looks sane
- No phantom duplicate shows or spend double-count

Do **not** duplicate full KPI tier tables. Link existing diagnostic rulebook and troubleshooting SOP.

## Library + runbook wiring

1. Author both docs in Wm-os with frontmatter (`status: draft`, `artifact_type: sop`, positions-based owner fields, `related_docs`).
2. Import into Mr. Waiz library (bundle or in-app publish) with cross-links.
3. Update people README + Daily OS Mon/Thu sections with links only.
4. Fill Mon/Thu `agenda_md` from SOP In/Out; add `library_slugs` (or equivalent) on seeds; render Open SOP links in TeamMeetings UI.

## Quality bar

- Executable by Client Success without Founder in the room.
- Positions only; no personal names.
- Form checklist stays ≤4 items; depth lives in library SOPs.
- One primary constraint per red; system fork before quality levers.
- Every red has action plan + explanation line (even if action is “observe 48h”).

## Success metrics (process)

- % of Mon reds with a complete note line (why + plan + role + due).
- % of Thu open commitments dispositioned (landed / blocked / missed).
- Meeting stays ~25 minutes without agenda creep into diagnosis workshop.
