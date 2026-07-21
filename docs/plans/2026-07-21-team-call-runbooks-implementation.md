# Team Call Runbooks Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to
> implement this plan task-by-task.

**Goal:** Ship v1 Team Meetings in Mr. Waiz — recurring Q3 cadence
instances with live checklists, disposition + recording URL, and a
linked `team_calls` archive row.

**Architecture:** Seeded `team_meeting_templates` generate
`team_meeting_instances` on a rolling 14-day window in
`America/Sao_Paulo`. Host opens a runbook, checks items, submits
disposition; API completes the instance and creates a `team_calls` row.
Cadence copy stays in Wm-os; Mr. Waiz owns schedule + execution.

**Tech Stack:** Next.js App Router, Supabase Postgres, existing
`src/lib/time.ts` (`CALL_CENTER_TIMEZONE` / `zonedWallTimeToUtc`),
`node:test` + `tsx`, dashboard nav via `src/lib/nav.ts`.

**Spec:** [2026-07-21-team-call-runbooks-design.md](./2026-07-21-team-call-runbooks-design.md)

**Repos:** Implementation lands in
`call-center-reporting-template` (Mr. Waiz). This plan file lives in
Wm-os next to the design.

---

### Task 1: Migration — templates + instances

**Files:**

- Create:
  `call-center-reporting-template/supabase/migrations/add_team_meeting_runbooks.sql`
- Modify: `call-center-reporting-template/supabase/schema.sql`
  (append same DDL for canonical rollup)

**Step 1: Write migration SQL**

```sql
-- Team meeting runbooks: recurring templates + scheduled instances.
-- Spec: Wm-os docs/plans/2026-07-21-team-call-runbooks-design.md

CREATE TABLE IF NOT EXISTS team_meeting_templates (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug            text NOT NULL UNIQUE,
  title           text NOT NULL,
  theme           text NOT NULL DEFAULT '',
  call_type       text NOT NULL,
  weekdays        int[] NOT NULL DEFAULT '{}',
  -- empty weekdays = Mon–Fri (1..5); else ISO weekday 1=Mon .. 7=Sun
  default_time    time NOT NULL,
  duration_min    int NOT NULL DEFAULT 30,
  host_role       text NOT NULL,
  attendee_roles  text[] NOT NULL DEFAULT '{}',
  agenda_md       text NOT NULL DEFAULT '',
  checklist       jsonb NOT NULL DEFAULT '[]'::jsonb,
  disposition     jsonb NOT NULL DEFAULT '[]'::jsonb,
  active          boolean NOT NULL DEFAULT true,
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT team_meeting_templates_call_type_check CHECK (
    call_type IN (
      'coaching', 'training', 'team_meeting', 'team_review',
      'interview', 'role_play', '1on1', 'sales_review', 'other'
    )
  ),
  CONSTRAINT team_meeting_templates_host_role_check CHECK (
    host_role IN ('ccm', 'client_success', 'ceo', 'shared')
  )
);

CREATE TABLE IF NOT EXISTS team_meeting_instances (
  id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  template_id       uuid NOT NULL
    REFERENCES team_meeting_templates(id) ON DELETE CASCADE,
  scheduled_at      timestamptz NOT NULL,
  status            text NOT NULL DEFAULT 'scheduled',
  host_agent_id     uuid REFERENCES agents(id) ON DELETE SET NULL,
  checklist_state   jsonb NOT NULL DEFAULT '{}'::jsonb,
  responses         jsonb NOT NULL DEFAULT '{}'::jsonb,
  recording_url     text,
  notes             text,
  team_call_id      uuid REFERENCES team_calls(id) ON DELETE SET NULL,
  completed_at      timestamptz,
  completed_by      uuid REFERENCES auth.users(id) ON DELETE SET NULL,
  created_at        timestamptz NOT NULL DEFAULT now(),
  updated_at        timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT team_meeting_instances_status_check CHECK (
    status IN (
      'scheduled', 'in_progress', 'completed', 'skipped', 'cancelled'
    )
  ),
  CONSTRAINT team_meeting_instances_unique_slot
    UNIQUE (template_id, scheduled_at)
);

CREATE INDEX IF NOT EXISTS team_meeting_instances_scheduled_at_idx
  ON team_meeting_instances (scheduled_at);
CREATE INDEX IF NOT EXISTS team_meeting_instances_status_idx
  ON team_meeting_instances (status);
```

**Step 2: Apply locally / document for prod**

Run against the project’s usual Supabase migration path (SQL editor or
CLI). Confirm tables exist.

**Step 3: Commit**

```bash
git add supabase/migrations/add_team_meeting_runbooks.sql supabase/schema.sql
git commit -m "Add team meeting templates and instances tables."
```

---

### Task 2: Lib — seed templates + types + validation

**Files:**

- Create: `src/lib/team-meetings.ts`
- Create: `src/lib/team-meetings.test.ts`

**Step 1: Write failing tests**

```ts
import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  TEAM_MEETING_SEED,
  validateCompletePayload,
  weekdaysForTemplate,
} from './team-meetings';

describe('team-meetings', () => {
  it('seeds five active series', () => {
    assert.equal(TEAM_MEETING_SEED.length, 5);
  });

  it('daily training expands to Mon–Fri', () => {
    assert.deepEqual(weekdaysForTemplate({ weekdays: [] }), [1, 2, 3, 4, 5]);
  });

  it('rejects complete without recording unless skipped', () => {
    const r = validateCompletePayload({
      status: 'completed',
      checklist: [{ key: 'a', required: true }],
      checklist_state: { a: true },
      responses: { summary: 'ok', participants_present: 'team' },
      recording_url: '',
    });
    assert.equal(r.ok, false);
  });
});
```

**Step 2: Run test — expect FAIL**

```bash
npx tsx --test src/lib/team-meetings.test.ts
```

**Step 3: Implement `team-meetings.ts`**

Include:

- `TEAM_MEETING_SEED` — five templates with São Paulo wall times:
  - `daily-setter-training` — `09:00`, 20m, weekdays `[]`, host `ccm`,
    `call_type: training`
  - `mon-kpi-week-plan` — `10:00`, 25m, `[1]`, host `client_success`
  - `mon-ops-planning` — `10:30`, 60m, `[1]`, host `ceo`
  - `thu-kpi-commitment-check` — `10:00`, 25m, `[4]`, host `client_success`
  - `fri-exec-qa` — `16:00`, 40m, `[5]`, host `ceo`, `call_type: team_review`
- Checklist keys from design (placeholder labels OK for v1)
- Shared disposition field defs
- `weekdaysForTemplate`, `validateCompletePayload`,
  `validateProgressPayload`
- Types: `TeamMeetingTemplate`, `TeamMeetingInstance`, status union

Use `CALL_CENTER_TIMEZONE` from `./time` for docs/comments; do not hardcode
`America/New_York`.

**Step 4: Re-run tests — expect PASS**

**Step 5: Commit**

```bash
git commit -m "Add team meeting seed templates and validation."
```

---

### Task 3: Lib — instance generator (São Paulo)

**Files:**

- Modify: `src/lib/team-meetings.ts`
- Modify: `src/lib/team-meetings.test.ts`

**Step 1: Test generator**

```ts
it('schedules mon KPI only on Mondays in Sao Paulo', () => {
  // Fixed: week containing 2026-07-20 (Mon) .. 2026-07-26
  const slots = plannedSlotsForRange(
    TEAM_MEETING_SEED.find(t => t.slug === 'mon-kpi-week-plan')!,
    '2026-07-20',
    '2026-07-26',
    'America/Sao_Paulo',
  );
  assert.equal(slots.length, 1);
  // 10:00 BRT = 13:00 UTC (Jul is UTC-3)
  assert.equal(slots[0].toISOString(), '2026-07-20T13:00:00.000Z');
});
```

**Step 2: Implement `plannedSlotsForRange`**

For each calendar day in range (inclusive), if ISO weekday is in
`weekdaysForTemplate(t)`, call:

```ts
zonedWallTimeToUtc(y, m, d, hour, minute, 0, CALL_CENTER_TIMEZONE)
```

Parse `default_time` as `HH:MM:SS` / `HH:MM`.

**Step 3: Tests pass → commit**

```bash
git commit -m "Generate team meeting slots in America/Sao_Paulo."
```

---

### Task 4: API — list / ensure / get / patch / complete

**Files:**

- Create: `src/app/api/team-meetings/route.ts`
- Create: `src/app/api/team-meetings/[id]/route.ts`

**Auth:** `getAuthContext` + `requirePermission(ctx, 'team_meetings')`
for read/progress. Complete/skip: same permission (lead seats + admin);
mirror `call_library` manage for destructive cancel later if needed.

**GET `/api/team-meetings`**

Query: `from`, `to` (ISO dates). Flow:

1. Ensure seed templates upserted by `slug` (idempotent).
2. Compute planned slots for range; insert missing instances
   (`ON CONFLICT DO NOTHING` via unique).
3. Return instances joined with template fields
   (`slug`, `title`, `theme`, `host_role`, `checklist`, `agenda_md`,
   `duration_min`).

**GET `/api/team-meetings/[id]`** — single instance + template.

**PATCH `/api/team-meetings/[id]`** — body:
`{ checklist_state?, responses?, notes?, status?: 'in_progress' }`.
If status was `scheduled` and checklist/responses touched → set
`in_progress`. Reject if already `completed` / `cancelled`.

**POST `/api/team-meetings/[id]/complete`** (or PATCH with
`action: 'complete' | 'skip'`):

1. `validateCompletePayload`
2. Upsert `team_calls` row:
   - `title` = template title
   - `call_type` from template
   - `called_at` = `scheduled_at` (or `now()` if late complete)
   - `participants` from responses
   - `recording_url`, `summary` from responses
   - `tags` include `runbook`, template `slug`
3. Set instance `status`, `team_call_id`, `completed_at`, `completed_by`
4. Idempotent if already completed with `team_call_id`

**Step: Commit**

```bash
git commit -m "Add team-meetings API with ensure and complete."
```

---

### Task 5: Nav + permissions

**Files:**

- Modify: `src/lib/nav.ts` — add `"team_meetings"` to `View` union;
  NAV entry under group `"Team"`, label `"Team Meetings"`, near
  `call_library`
- Confirm `VIEW_PERMISSIONS` / `hasPermission` pick up the new view
  automatically from NAV
- If a SQL seed grants default perms to roles, add
  `supabase/migrations/nav_team_meetings_permission.sql` only if the
  repo already patterns role↔view grants (see `nav_hub_permissions.sql`)

**Commit:**

```bash
git commit -m "Add Team Meetings nav view."
```

---

### Task 6: UI — list + runbook

**Files:**

- Create: `src/components/TeamMeetings.tsx` (week list)
- Create: `src/components/TeamMeetingRunbook.tsx` (checklist + form)
- Modify: `src/components/DashboardView.tsx` — lazy import +
  `view === "team_meetings"` branch

**List behavior**

- On mount: `GET /api/team-meetings?from=&to=` for current week
  (São Paulo local dates via `getZonedParts` / local date helper)
- Group by day; status chips; Open sets selected instance id
- Filters: upcoming | in_progress | completed | skipped

**Runbook behavior**

- Header: title, theme, scheduled time (format in
  `CALL_CENTER_TIMEZONE`), status
- Checklist checkboxes → debounced PATCH
- Agenda: render `agenda_md` as pre-wrapped text (v1; no MD lib required)
- Disposition: recording URL, summary, participants, follow_ups;
  Complete / Skip buttons
- On success: toast/banner + refresh list; link to Call Library optional

Match existing Mr. Waiz ops styling (same buttons/inputs as
`CallLibrary` / EOD). Large checklist targets for mid-call use.

**Commit:**

```bash
git commit -m "Add Team Meetings list and runbook UI."
```

---

### Task 7: Today strip on CCM Command (lightweight)

**Files:**

- Modify: `src/components/team-dashboards/CcmCommandDashboard.tsx`
  (or sibling) — fetch today’s instances; show 1–3 rows with Open →
  `setView('team_meetings')` if parent exposes navigation, else link
  `?view=team_meetings`

If navigation prop is awkward in v1, skip deep-link and only show
read-only “Today’s meetings” with times/titles. Do not block on Ops
Overview strip — optional follow-up.

**Commit:**

```bash
git commit -m "Surface today's team meetings on CCM Command."
```

---

### Task 8: Seed agenda copy from Wm-os (minimal)

**Files:**

- Modify: `src/lib/team-meetings.ts` `agenda_md` strings — paste short
  In/Out from
  `Wm-os/docs/plans/2026-07-13-team-restructure-design.md` meeting rules
- Modify checklist labels to readable sentences (still same keys)

No separate content repo sync in v1 — constants are enough.

**Commit:**

```bash
git commit -m "Fill v1 team meeting agenda and checklist labels."
```

---

### Task 9: Docs touch-up

**Files (Wm-os):**

- Modify: `docs/operations/people/README.md` — link Team Meetings +
  design/impl plans
- Modify: design doc status note if needed (`status: draft` stays until
  you critique)

**Files (Mr. Waiz):**

- Modify: `docs/CALL-INTELLIGENCE.md` — note runbooks create
  `team_calls` with `runbook` tag (fix stale “UI not built” if still
  present)

**Commit each repo separately.**

---

### Task 10: Manual smoke checklist

1. Apply migration on target Supabase.
2. Open dashboard as admin → Team Meetings visible.
3. Week shows Mon KPI, Mon Ops, daily trainings, Thu KPI, Fri Q&A at
   São Paulo times.
4. Open daily training → check all items → paste fake recording URL →
   Complete.
5. Confirm `team_calls` row in Team Calls with tag `runbook` + slug.
6. Re-complete same instance → idempotent (no duplicate call).
7. Skip one instance with reason → status `skipped`, no recording
   required.

---

## Out of scope (do not build in this plan)

- Zoom auto-ingest
- Multi-attendee forms
- Commitment DB objects / Fri Q&A intake form
- Google Calendar sync
- Christian Tue/Wed tech blocks

## Execution handoff

After this plan is accepted:

1. **Subagent-Driven (this session)** — one task per subagent, review
   between tasks
2. **Parallel Session** — new session with executing-plans in the
   Mr. Waiz worktree

Which approach?
