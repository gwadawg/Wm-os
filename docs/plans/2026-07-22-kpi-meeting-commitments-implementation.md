# KPI Meeting Commitments Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to
> implement this plan task-by-task.

**Goal:** Ship structured meeting commitments in Mr. Waiz Team Meetings —
Mon/Thu capture, Ops Needs Founder approval, durable
`meeting_commitments` storage, manual ClickUp URL paste — and update
Wm-os SOP/agenda copy to match.

**Architecture:** One thin `meeting_commitments` table linked to
`team_meeting_instances`. Team Meetings UI mounts a Commitments panel
(Mon/Thu) or Needs Founder panel (Ops). Status transitions enforced in
`src/lib/meeting-commitments.ts`. ClickUp stays manual. Wm-os owns
cadence copy; Mr. Waiz owns schema + UI + API.

**Tech Stack:** Next.js App Router, Supabase Postgres, existing Team
Meetings auth (`team_meetings` permission), `node:test` + `tsx`.

**Spec:** [docs/superpowers/specs/2026-07-22-kpi-meeting-commitments-design.md](../superpowers/specs/2026-07-22-kpi-meeting-commitments-design.md)

**Repos:** Schema/API/UI in `call-center-reporting-template` (Mr. Waiz);
SOP + cross-links in Wm-os. This plan file lives in Wm-os.

---

### Task 1: Migration — `meeting_commitments`

**Files:**

- Create: `call-center-reporting-template/supabase/migrations/add_meeting_commitments.sql`
- Modify: `call-center-reporting-template/supabase/schema.sql` (append same DDL)

**Step 1: Write migration SQL**

Create `meeting_commitments` with fields from the spec:

- FKs: `client_id` → `clients`, meeting ids → `team_meeting_instances`
  with `ON DELETE SET NULL` for meeting FKs
- Check constraints for `severity`, `constraint_type`, `owner_role`,
  `status`
- Indexes: `(status, needs_founder)`, `(client_id, created_at desc)`,
  `origin_meeting_id`, `due_date`

**Step 2: Apply locally / document apply for prod**

Run migration against the project’s usual Supabase path (or note apply
steps in the PR). Mirror DDL into `schema.sql`.

**Step 3: Commit (Mr. Waiz)**

```bash
git add supabase/migrations/add_meeting_commitments.sql supabase/schema.sql
git commit -m "$(cat <<'EOF'
Add meeting_commitments table for KPI/Ops structured plans.

EOF
)"
```

---

### Task 2: Lib — types, transitions, filters

**Files:**

- Create: `call-center-reporting-template/src/lib/meeting-commitments.ts`
- Create: `call-center-reporting-template/src/lib/meeting-commitments.test.ts`

**Step 1: Implement types + transition matrix**

Export:

- Status union and `canTransition(from, to, { needsFounder })`
- Rules from spec: founder actions only when `needs_founder`;
  `proposed` → `in_progress` only when `!needs_founder`; founder path
  must `approve` before `in_progress`
- `filterNeedsFounder(rows)` — `needs_founder && status in proposed|needs_clarification`
- `filterOpenForWeek(rows, weekStartYmd, weekEndYmd)` — exclude
  landed/rejected/cancelled; week by `due_date` or `created_at` in
  `America/Sao_Paulo` (match existing `CALL_CENTER_TIMEZONE`)
- `softDuplicateWarn(rows, clientId, constraintLabel, weekBounds)`

**Step 2: Unit tests**

Cover transition matrix edge cases, Needs Founder filter, open-week
filter, duplicate soft-check.

**Step 3: Run tests**

```bash
cd "call-center-reporting-template - Copy"
npx tsx --test src/lib/meeting-commitments.test.ts
```

**Step 4: Commit (Mr. Waiz)**

```bash
git add src/lib/meeting-commitments.ts src/lib/meeting-commitments.test.ts
git commit -m "$(cat <<'EOF'
Add meeting commitment status transitions and week filters.

EOF
)"
```

---

### Task 3: API — CRUD + status actions

**Files:**

- Create: `call-center-reporting-template/src/app/api/meeting-commitments/route.ts`
- Create: `call-center-reporting-template/src/app/api/meeting-commitments/[id]/route.ts`

**Step 1: List + create (`GET` / `POST` on collection)**

- `requirePermission(ctx, 'team_meetings')`
- `GET` query params: `meeting_id` (history for instance), `view=needs_founder|open_week`, optional `from`/`to`
- `POST` body: fields from spec; set `origin_meeting_id` /
  `last_touched_meeting_id`; validate `founder_ask` when
  `needs_founder`

**Step 2: Patch + status (`PATCH` on item)**

- Field updates (plan, why, clickup_url, etc.) for owning roles
- Status action payload: `{ status, founder_note?, check_note?, meeting_id? }`
- Enforce `canTransition`; on approve set `approved_in_meeting_id`
- Always refresh `last_touched_meeting_id` when `meeting_id` provided

**Step 3: Smoke via curl or script against local/dev** (optional if no local DB)

**Step 4: Commit (Mr. Waiz)**

```bash
git add src/app/api/meeting-commitments
git commit -m "$(cat <<'EOF'
Add meeting-commitments API for KPI and Ops workflows.

EOF
)"
```

---

### Task 4: UI — Commitments + Needs Founder panels

**Files:**

- Create: `call-center-reporting-template/src/components/MeetingCommitmentsPanel.tsx`
- Modify: `call-center-reporting-template/src/components/TeamMeetings.tsx`
- Modify: `call-center-reporting-template/src/lib/team-meetings.ts` (agenda copy + checklist labels)

**Step 1: Panel modes**

- `mode="edit"` — Mon KPI: add/edit rows
- `mode="check"` — Thu KPI: open week + landed/blocked/missed
- `mode="approve"` — Ops: Needs Founder queue + approve/reject/clarify;
  optional “Show full week plan” toggle

**Step 2: Mount in `TeamMeetingRunbook`**

By template slug:

- `mon-kpi-week-plan` → edit
- `thu-kpi-commitment-check` → check
- `mon-ops-planning` → approve

Load commitments for the instance / week when runbook opens. Soft-warn
on Mon complete if zero rows (do not hard-block).

**Step 3: Update seeds**

- Mon KPI agenda: replace paste note-line with “use Commitments panel”
- Update checklist label for `commitments_named` (Why lives on rows)
- Fill Ops `agenda_md` PLACEHOLDER with Needs Founder + OB/systems
  sections (keep existing checklist keys)
- Thu agenda: reference Commitments panel for open set

**Step 4: Commit (Mr. Waiz)**

```bash
git add src/components/MeetingCommitmentsPanel.tsx src/components/TeamMeetings.tsx src/lib/team-meetings.ts
git commit -m "$(cat <<'EOF'
Wire commitment panels into Mon/Thu KPI and Ops runbooks.

EOF
)"
```

---

### Task 5: Wm-os SOP + cross-links

**Files:**

- Modify: `docs/operations/people/kpi-review-meeting-sop.md`
- Modify: `docs/superpowers/specs/2026-07-21-kpi-review-meeting-sop-design.md`
- Modify: `docs/plans/2026-07-21-team-call-runbooks-design.md`
- Optionally: people Daily OS / README one-line pointers if they still
  say “paste note lines”

**Step 1: Meeting SOP**

Replace note-line paste instructions with structured Commitments panel
behavior (Mon create, Thu check, Ops Needs Founder). Keep checklist
keys. Link this design spec and keep ladder link.

**Step 2: Prior designs**

- KPI SOP design: note that form fields / structured commitments are
  specified in `2026-07-22-kpi-meeting-commitments-design.md`
- Team Call Runbooks: Phase 2 commitments → point to that design

**Step 3: Library re-import (Mr. Waiz)**

After SOP update, re-import `kpi-review-meeting-sop` via
`scripts/import-library-doc.mjs` / library-doc-transfer skill so
`/library/kpi-review-meeting-sop` matches.

**Step 4: Commit (Wm-os, then Mr. Waiz library if separate)**

```bash
# Wm-os
git add docs/operations/people/kpi-review-meeting-sop.md \
  docs/superpowers/specs/2026-07-21-kpi-review-meeting-sop-design.md \
  docs/plans/2026-07-21-team-call-runbooks-design.md
git commit -m "$(cat <<'EOF'
Point KPI meeting SOPs at structured meeting commitments.

EOF
)"
```

---

### Task 6: End-to-end verification

**Manual checklist:**

1. Open Mon KPI instance → add commitment with Needs Founder on →
   appears in Ops Needs Founder.
2. Ops Approve → status `approved`; `approved_in_meeting_id` set.
3. Paste `clickup_url` → `in_progress`.
4. Thu → mark `landed`; past Mon/Ops instances still show linked rows.
5. Seat-owned (`needs_founder=false`) can go `proposed` → `in_progress`
   without Ops.
6. Invalid transition returns clear error.
7. Empty Ops queue shows “Nothing needs founder.”

**Automated:** re-run `meeting-commitments.test.ts` (+ any Team Meetings
tests still green).

---

## Out of scope (do not implement in this plan)

- ClickUp API create
- Client Success deployed-changes merge
- Fri Exec Q&A structured form
- Auto-KPI number pull onto rows
- Multi-attendee concurrent editing

## Execution handoff

After this plan is approved, implement task-by-task in order (migration
→ lib/tests → API → UI → Wm-os SOP → verify). Do not start app code
until the design spec at
`docs/superpowers/specs/2026-07-22-kpi-meeting-commitments-design.md`
has been reviewed with no blocking changes.
