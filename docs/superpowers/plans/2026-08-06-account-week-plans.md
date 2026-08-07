# Account Week Plans Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship weekly account work plans in Mr. Waiz — plan + multi-task storage, founder approve every plan, person/day assignment, complete + optional report + optional action-log promote, client and week review lists — without building role day dashboards.

**Architecture:** Two Supabase tables (`account_week_plans`, `account_plan_tasks`). Domain rules live in `src/lib/account-week-plans.ts`. REST under `/api/account-week-plans` and `/api/account-plan-tasks`. UI: intake form, founder approval queue, week list, client history; Mon KPI embeds the form. Existing `meeting_commitments` stays installed; Mon/Thu swap priority to week plans without dual-write. Wm-os owns the SOP wording update.

**Tech Stack:** Next.js App Router, Supabase Postgres, existing `getAuthContext` / permissions, React client components, `node:test` + `tsx`.

**Spec:** [docs/superpowers/specs/2026-08-06-account-week-plans-design.md](../specs/2026-08-06-account-week-plans-design.md)

**Repos:**
- Schema / API / UI → Mr. Waiz repo root (this workspace:
  `call-center-reporting-template - Copy`)
- SOP + this plan → Wm-os (`docs/`)

When shell commands below say `MRWAIZ`, use:
```bash
cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
```

When they say `WMOS`, use:
```bash
cd "/Users/gwadawg/Desktop/Repos/Wm-os"
```

---

## File map

| File | Responsibility |
|------|----------------|
| `supabase/migrations/add_account_week_plans.sql` | DDL + indexes |
| `supabase/schema.sql` | Mirror DDL so schema dump stays truth |
| `src/lib/account-week-plans.ts` | Types, transitions, active-work filter, week helpers, soft-duplicate |
| `src/lib/account-week-plans.test.ts` | Unit tests for rules |
| `src/app/api/account-week-plans/route.ts` | GET list + POST create plan (with tasks) |
| `src/app/api/account-week-plans/[id]/route.ts` | GET one, PATCH plan fields / approve / reject |
| `src/app/api/account-week-plans/assignees/route.ts` | Lightweight profiles list for assignee picker |
| `src/app/api/account-plan-tasks/[id]/route.ts` | PATCH task fields / done / cancel + optional promote |
| `src/components/AccountWeekPlanForm.tsx` | Create/edit intake |
| `src/components/AccountWeekPlanApprovalQueue.tsx` | Founder pending queue |
| `src/components/AccountWeekPlansWeekList.tsx` | This/last week review + execute done |
| `src/components/AccountWeekPlansClientHistory.tsx` | Per-client history |
| `src/components/AccountWeekPlansHub.tsx` | Shell with tabs: Week / Approve / New |
| `src/components/TeamMeetings.tsx` | Mount week-plan panel on Mon/Thu (alongside or replacing commitments panel for mon/thu) |
| `src/lib/nav.ts`, `src/components/DashboardView.tsx`, `src/lib/permissions.ts` | View `account_work` + permission inheritance |
| Wm-os `docs/operations/people/kpi-review-meeting-sop.md` | Point at account week plans |

---

### Task 1: Migration — `account_week_plans` + `account_plan_tasks`

**Files:**
- Create: `supabase/migrations/add_account_week_plans.sql`
- Modify: `supabase/schema.sql` (append same DDL at end)

- [ ] **Step 1: Write migration SQL**

```sql
-- Spec: Wm-os docs/superpowers/specs/2026-08-06-account-week-plans-design.md

CREATE TABLE IF NOT EXISTS account_week_plans (
  id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id           uuid NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
  week_start          date NOT NULL,
  why                 text NOT NULL DEFAULT '',
  severity            text,
  status              text NOT NULL DEFAULT 'pending',
  success_signal      text,
  origin_meeting_id   uuid REFERENCES team_meeting_instances(id) ON DELETE SET NULL,
  approved_by         uuid REFERENCES auth.users(id) ON DELETE SET NULL,
  approved_at         timestamptz,
  founder_note        text,
  created_by          uuid REFERENCES auth.users(id) ON DELETE SET NULL,
  created_at          timestamptz NOT NULL DEFAULT now(),
  updated_at          timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT account_week_plans_severity_check CHECK (
    severity IS NULL OR severity IN ('911', 'below', 'watch')
  ),
  CONSTRAINT account_week_plans_status_check CHECK (
    status IN ('pending', 'approved', 'rejected')
  )
);

CREATE INDEX IF NOT EXISTS account_week_plans_client_week_idx
  ON account_week_plans (client_id, week_start DESC);

CREATE INDEX IF NOT EXISTS account_week_plans_status_idx
  ON account_week_plans (status);

CREATE INDEX IF NOT EXISTS account_week_plans_week_status_idx
  ON account_week_plans (week_start, status);

CREATE INDEX IF NOT EXISTS account_week_plans_origin_meeting_idx
  ON account_week_plans (origin_meeting_id)
  WHERE origin_meeting_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS account_week_plans_pending_idx
  ON account_week_plans (status)
  WHERE status = 'pending';

CREATE TABLE IF NOT EXISTS account_plan_tasks (
  id                     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  plan_id                uuid NOT NULL REFERENCES account_week_plans(id) ON DELETE CASCADE,
  client_id              uuid NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
  title                  text NOT NULL,
  notes                  text,
  tactic_tag             text,
  assignee_user_id       uuid REFERENCES auth.users(id) ON DELETE SET NULL,
  scheduled_for          date,
  status                 text NOT NULL DEFAULT 'open',
  completion_report      text,
  completed_at           timestamptz,
  completed_by           uuid REFERENCES auth.users(id) ON DELETE SET NULL,
  client_action_log_id   uuid REFERENCES client_action_logs(id) ON DELETE SET NULL,
  sort_order             int NOT NULL DEFAULT 0,
  created_at             timestamptz NOT NULL DEFAULT now(),
  updated_at             timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT account_plan_tasks_status_check CHECK (
    status IN ('open', 'done', 'cancelled')
  )
);

CREATE INDEX IF NOT EXISTS account_plan_tasks_assignee_day_idx
  ON account_plan_tasks (assignee_user_id, scheduled_for);

CREATE INDEX IF NOT EXISTS account_plan_tasks_client_created_idx
  ON account_plan_tasks (client_id, created_at DESC);

CREATE INDEX IF NOT EXISTS account_plan_tasks_plan_sort_idx
  ON account_plan_tasks (plan_id, sort_order);

CREATE INDEX IF NOT EXISTS account_plan_tasks_status_idx
  ON account_plan_tasks (status);

CREATE INDEX IF NOT EXISTS account_plan_tasks_open_assignee_day_idx
  ON account_plan_tasks (assignee_user_id, scheduled_for)
  WHERE status = 'open';
```

- [ ] **Step 2: Mirror into `schema.sql`**

Append the same DDL after the `meeting_commitments` block so local full-schema stay in sync.

- [ ] **Step 3: Apply migration**

Apply via the project’s usual Supabase path (SQL editor / CLI). Confirm both tables exist:

```sql
select tablename from pg_tables
where schemaname = 'public'
  and tablename in ('account_week_plans', 'account_plan_tasks');
```

Expected: two rows.

- [ ] **Step 4: Commit (Mr. Waiz)**

```bash
MRWAIZ
git add supabase/migrations/add_account_week_plans.sql supabase/schema.sql
git commit -m "$(cat <<'EOF'
Add account_week_plans and account_plan_tasks tables.

EOF
)"
```

---

### Task 2: Lib — types and rules

**Files:**
- Create: `src/lib/account-week-plans.ts`
- Create: `src/lib/account-week-plans.test.ts`

- [ ] **Step 1: Write failing tests**

```ts
import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import {
  canCompleteTask,
  canTransitionPlan,
  filterActiveWorkTasks,
  isAccountPlanTaskStatus,
  isAccountWeekPlanStatus,
  softDuplicatePlanWarn,
  weekStartMondayContaining,
} from './account-week-plans';

describe('account-week-plans', () => {
  it('weekStartMondayContaining returns Monday for mid-week and Sunday', () => {
    // 2026-08-06 is Thursday America/Sao_Paulo-safe if you pass that calendar ymd
    assert.equal(weekStartMondayContaining('2026-08-06'), '2026-08-03');
    assert.equal(weekStartMondayContaining('2026-08-09'), '2026-08-03'); // Sun
    assert.equal(weekStartMondayContaining('2026-08-03'), '2026-08-03');
  });

  it('plan transitions: pending → approved|rejected only', () => {
    assert.equal(canTransitionPlan('pending', 'approved').ok, true);
    assert.equal(canTransitionPlan('pending', 'rejected').ok, true);
    assert.equal(canTransitionPlan('approved', 'rejected').ok, false);
    assert.equal(canTransitionPlan('rejected', 'approved').ok, false);
  });

  it('canCompleteTask requires approved plan and open task', () => {
    assert.equal(canCompleteTask({ planStatus: 'approved', taskStatus: 'open' }).ok, true);
    assert.equal(canCompleteTask({ planStatus: 'pending', taskStatus: 'open' }).ok, false);
    assert.equal(canCompleteTask({ planStatus: 'approved', taskStatus: 'done' }).ok, false);
  });

  it('filterActiveWorkTasks requires approved plan + open status', () => {
    const rows = [
      {
        id: '1',
        plan_status: 'approved' as const,
        status: 'open' as const,
        assignee_user_id: 'u1',
        scheduled_for: '2026-08-05',
      },
      {
        id: '2',
        plan_status: 'pending' as const,
        status: 'open' as const,
        assignee_user_id: 'u1',
        scheduled_for: '2026-08-05',
      },
      {
        id: '3',
        plan_status: 'approved' as const,
        status: 'done' as const,
        assignee_user_id: 'u1',
        scheduled_for: '2026-08-05',
      },
    ];
    const active = filterActiveWorkTasks(rows, {
      assigneeUserId: 'u1',
      scheduledFor: '2026-08-05',
    });
    assert.equal(active.length, 1);
    assert.equal(active[0].id, '1');
  });

  it('softDuplicatePlanWarn flags non-rejected same client+week', () => {
    const warn = softDuplicatePlanWarn(
      [
        {
          client_id: 'c1',
          week_start: '2026-08-03',
          status: 'pending',
        },
      ],
      'c1',
      '2026-08-03',
    );
    assert.equal(warn, true);
  });

  it('status type guards', () => {
    assert.equal(isAccountWeekPlanStatus('pending'), true);
    assert.equal(isAccountWeekPlanStatus('draft'), false);
    assert.equal(isAccountPlanTaskStatus('open'), true);
    assert.equal(isAccountPlanTaskStatus('active'), false);
  });
});
```

- [ ] **Step 2: Run tests — expect FAIL**

```bash
MRWAIZ
npx tsx --test src/lib/account-week-plans.test.ts
```

Expected: module not found / export errors.

- [ ] **Step 3: Implement lib**

```ts
/**
 * Account week plans — plan + task domain rules.
 * Spec: Wm-os docs/superpowers/specs/2026-08-06-account-week-plans-design.md
 */

import { CALL_CENTER_TIMEZONE } from '@/lib/time';
import { addDaysToYmd } from '@/lib/team-meetings';

export type AccountWeekPlanStatus = 'pending' | 'approved' | 'rejected';
export type AccountPlanTaskStatus = 'open' | 'done' | 'cancelled';
export type AccountWeekPlanSeverity = '911' | 'below' | 'watch';

export type AccountWeekPlan = {
  id: string;
  client_id: string;
  week_start: string;
  why: string;
  severity: AccountWeekPlanSeverity | null;
  status: AccountWeekPlanStatus;
  success_signal: string | null;
  origin_meeting_id: string | null;
  approved_by: string | null;
  approved_at: string | null;
  founder_note: string | null;
  created_by: string | null;
  created_at: string;
  updated_at: string;
  client_name?: string | null;
  tasks?: AccountPlanTask[];
};

export type AccountPlanTask = {
  id: string;
  plan_id: string;
  client_id: string;
  title: string;
  notes: string | null;
  tactic_tag: string | null;
  assignee_user_id: string | null;
  scheduled_for: string | null;
  status: AccountPlanTaskStatus;
  completion_report: string | null;
  completed_at: string | null;
  completed_by: string | null;
  client_action_log_id: string | null;
  sort_order: number;
  created_at: string;
  updated_at: string;
};

export const ACCOUNT_WEEK_PLAN_STATUSES: AccountWeekPlanStatus[] = [
  'pending',
  'approved',
  'rejected',
];

export const ACCOUNT_PLAN_TASK_STATUSES: AccountPlanTaskStatus[] = [
  'open',
  'done',
  'cancelled',
];

export function isAccountWeekPlanStatus(v: unknown): v is AccountWeekPlanStatus {
  return typeof v === 'string' && (ACCOUNT_WEEK_PLAN_STATUSES as string[]).includes(v);
}

export function isAccountPlanTaskStatus(v: unknown): v is AccountPlanTaskStatus {
  return typeof v === 'string' && (ACCOUNT_PLAN_TASK_STATUSES as string[]).includes(v);
}

/** Monday of the calendar week containing `ymd` (America/Sao_Paulo weekday). */
export function weekStartMondayContaining(ymd: string): string {
  const [y, m, d] = ymd.split('-').map(Number);
  const probe = new Date(Date.UTC(y, m - 1, d, 15, 0, 0));
  const weekday = new Intl.DateTimeFormat('en-US', {
    timeZone: CALL_CENTER_TIMEZONE,
    weekday: 'short',
  }).format(probe);
  const map: Record<string, number> = {
    Mon: 0,
    Tue: 1,
    Wed: 2,
    Thu: 3,
    Fri: 4,
    Sat: 5,
    Sun: 6,
  };
  const offset = map[weekday] ?? 0;
  return addDaysToYmd(ymd, -offset);
}

export function canTransitionPlan(
  from: AccountWeekPlanStatus,
  to: AccountWeekPlanStatus,
): { ok: true } | { ok: false; error: string } {
  if (from === to) return { ok: false, error: `Already ${from}` };
  if (from === 'pending' && (to === 'approved' || to === 'rejected')) {
    return { ok: true };
  }
  return {
    ok: false,
    error: `Cannot move plan from ${from} to ${to}`,
  };
}

export function canCompleteTask(opts: {
  planStatus: AccountWeekPlanStatus;
  taskStatus: AccountPlanTaskStatus;
}): { ok: true } | { ok: false; error: string } {
  if (opts.planStatus !== 'approved') {
    return { ok: false, error: 'Plan must be approved before completing tasks' };
  }
  if (opts.taskStatus !== 'open') {
    return { ok: false, error: `Task is ${opts.taskStatus}, not open` };
  }
  return { ok: true };
}

/** Future dashboard: open tasks on approved plans for person/day. */
export function filterActiveWorkTasks<
  T extends {
    plan_status: AccountWeekPlanStatus;
    status: AccountPlanTaskStatus;
    assignee_user_id: string | null;
    scheduled_for: string | null;
  },
>(
  rows: T[],
  filters?: { assigneeUserId?: string; scheduledFor?: string },
): T[] {
  return rows.filter(r => {
    if (r.plan_status !== 'approved') return false;
    if (r.status !== 'open') return false;
    if (filters?.assigneeUserId && r.assignee_user_id !== filters.assigneeUserId) {
      return false;
    }
    if (filters?.scheduledFor && r.scheduled_for !== filters.scheduledFor) {
      return false;
    }
    return true;
  });
}

export function softDuplicatePlanWarn<
  T extends { client_id: string; week_start: string; status: AccountWeekPlanStatus },
>(rows: T[], clientId: string, weekStart: string): boolean {
  return rows.some(
    r =>
      r.client_id === clientId &&
      r.week_start === weekStart &&
      r.status !== 'rejected',
  );
}

export function weekPlanModeForTemplateSlug(
  slug: string,
): 'intake' | 'review' | null {
  if (slug === 'mon-kpi-week-plan') return 'intake';
  if (slug === 'thu-kpi-commitment-check') return 'review';
  return null;
}
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
MRWAIZ
npx tsx --test src/lib/account-week-plans.test.ts
```

Expected: all tests pass. If Sunday case fails due to TZ, adjust test ymd to a known Sao Paulo Sunday and re-run.

- [ ] **Step 5: Commit (Mr. Waiz)**

```bash
git add src/lib/account-week-plans.ts src/lib/account-week-plans.test.ts
git commit -m "$(cat <<'EOF'
Add account week plan domain rules and unit tests.

EOF
)"
```

---

### Task 3: API — list + create plans

**Files:**
- Create: `src/app/api/account-week-plans/route.ts`

Auth pattern: use `requireAnyPermission(ctx, ['team_meetings', 'client_health'])` so CS + meetings seats can access; owner always passes.

- [ ] **Step 1: Implement GET + POST**

`GET` query params:

| Param | Behavior |
|-------|----------|
| `view=pending_approval` | `status=pending` ordered by `created_at` |
| `week_start=YYYY-MM-DD` | filter that week |
| `client_id=` | plans for client |
| `origin_meeting_id=` | plans for meeting history |
| `include_tasks=1` | nest tasks (default true for single-client / pending / week) |

Select plans; join client names via second query on `clients`. When including tasks, query `account_plan_tasks` where `plan_id in (...)`, order by `sort_order`, `created_at`.

`POST` body:

```ts
{
  client_id: string;
  why: string;
  week_start?: string; // default weekStartMondayContaining(todayYmdInCallCenterTz())
  severity?: '911' | 'below' | 'watch' | null;
  success_signal?: string | null;
  origin_meeting_id?: string | null;
  tasks: Array<{
    title: string;
    notes?: string | null;
    tactic_tag?: string | null;
    assignee_user_id?: string | null;
    scheduled_for?: string | null;
    sort_order?: number;
  }>;
}
```

Rules:
- `why` required non-empty after trim
- Create plan `status: 'pending'`, `created_by: ctx.userId`
- Insert tasks with denormalized `client_id`, `status: 'open'`
- Soft-duplicate: if another non-rejected plan exists for same client+week, still insert but set response header or body flag `duplicate_warning: true`
- Allow `tasks: []` on create (draft editing); founder approve path will reject empty open tasks later

Response: `{ plan, tasks, duplicate_warning?: boolean }`

- [ ] **Step 2: Smoke POST with curl or browser while logged in** (manual after server up)

- [ ] **Step 3: Commit**

```bash
git add src/app/api/account-week-plans/route.ts
git commit -m "$(cat <<'EOF'
Add account week plans list and create API.

EOF
)"
```

---

### Task 4: API — plan get / update / approve / reject

**Files:**
- Create: `src/app/api/account-week-plans/[id]/route.ts`

- [ ] **Step 1: Implement GET + PATCH**

`GET`: plan + tasks + `client_name`.

`PATCH` body variants:

**Field update (while pending):**
```json
{ "why": "...", "severity": "below", "success_signal": "...", "week_start": "2026-08-03" }
```
Only if current status is `pending`. Optionally replace tasks via:
```json
{ "tasks": [ { "title": "...", ... } ] }
```
When `tasks` is present, delete existing tasks for plan and re-insert (simplest v1), preserving only if all are still open — if any task is done, return 400 “cannot replace tasks after completion”.

**Approve / reject:**
```json
{ "status": "approved" }
{ "status": "rejected", "founder_note": "reason required" }
```

Rules:
- `canTransitionPlan` from lib
- Approve/reject: `ctx.isOwner === true` OR `hasPermission('ceo', …)` — mirror owner/ceo gate; if product has no ceo permission on a user, owner must do it. Use:

```ts
function canApprovePlans(ctx: AuthContext): boolean {
  if (ctx.isOwner) return true;
  return hasPermission('ceo', {
    isOwner: ctx.isOwner,
    allowedPermissions: ctx.allowedPermissions,
  });
}
```

Import `hasPermission` from `@/lib/permissions`.

On **approved**:
- Set `approved_by`, `approved_at = now()`
- Leave tasks `open`

On **rejected**:
- Require non-empty `founder_note`
- Bulk-update open tasks → `cancelled`, `updated_at = now()`

- [ ] **Step 2: Unit not required if lib covers transitions; manual smoke approve + confirm tasks cancelled on reject**

- [ ] **Step 3: Commit**

```bash
git add src/app/api/account-week-plans/\[id\]/route.ts
git commit -m "$(cat <<'EOF'
Add account week plan approve, reject, and edit API.

EOF
)"
```

---

### Task 5: API — task patch / complete / optional promote

**Files:**
- Create: `src/app/api/account-plan-tasks/[id]/route.ts`

- [ ] **Step 1: Implement PATCH**

Load task + parent plan (`status` of plan).

Allowed field updates when plan is `pending` or `approved` and task is `open`:
- `title`, `notes`, `tactic_tag`, `assignee_user_id`, `scheduled_for`, `sort_order`

**Complete:**
```json
{
  "status": "done",
  "completion_report": "optional text",
  "log_as_account_change": false
}
```

Use `canCompleteTask`. On success:
- `status = done`, `completed_at = now()`, `completed_by = ctx.userId`, store report
- If `log_as_account_change === true`:
  - Insert `client_action_logs` with:
    - `client_id` = task.client_id
    - `title` = task.title
    - `change_description` = completion_report or notes
    - `hypothesis` = notes or null
    - `constraint_label` = tactic_tag
    - `status` = `'in_progress'` (existing open pipeline)
    - `change_date` = today (YYYY-MM-DD)
    - `created_by` = ctx.userId
  - Set `client_action_log_id` on task
  - Do **not** call the full baseline snapshot machinery unless already trivial — keep promote thin; user can refine on Client Success action log UI

**Cancel:**
```json
{ "status": "cancelled" }
```
Allowed when task is `open`. No approve requirement.

- [ ] **Step 2: Commit**

```bash
git add src/app/api/account-plan-tasks/\[id\]/route.ts
git commit -m "$(cat <<'EOF'
Add account plan task complete/cancel and optional action-log promote.

EOF
)"
```

---

### Task 6: API — assignee picker

**Files:**
- Create: `src/app/api/account-week-plans/assignees/route.ts`

`/api/users` is admin-only; team needs a lighter list.

- [ ] **Step 1: Implement GET**

```ts
// Permission: team_meetings | client_health
// Select from profiles: id, display/email via auth.admin if needed
// Prefer: profiles join — check which columns exist (name/email often on auth.users)
```

Implementation approach matching existing UserManager: use service `auth.admin.listUsers()` **only if** permission allows team meetings OR client_health, return `{ assignees: [{ id, email, name }] }` with name = `user_metadata.full_name` or email local-part. Cap to 200 users. Do not return allowed_permissions.

Alternatively if admin.listUsers is too heavy: `agents` where `user_id is not null` union profiles — prefer auth list for accuracy of login accounts.

- [ ] **Step 2: Commit**

```bash
git add src/app/api/account-week-plans/assignees/route.ts
git commit -m "$(cat <<'EOF'
Add lightweight assignee list for account week plan forms.

EOF
)"
```

---

### Task 7: Nav + permissions + hub shell

**Files:**
- Modify: `src/lib/nav.ts`
- Modify: `src/lib/permissions.ts`
- Modify: `src/components/DashboardView.tsx`
- Create: `src/components/AccountWeekPlansHub.tsx`

- [ ] **Step 1: Add view key**

In `nav.ts` `View` union add `"account_work"`.

In `NAV_ITEMS` (Team group, near team_meetings):

```ts
{ view: "account_work", label: "Account Work", group: "Team" },
```

- [ ] **Step 2: Permissions**

In `permissions.ts` inheritance (same pattern as `team_meetings`):

```ts
account_work: ["team_meetings", "client_health", "ops_overview", "ceo"],
```

Ensure owner unrestricted path still sees it. Grant inheritance so anyone with those perms sees the tab without new admin setup.

- [ ] **Step 3: Hub component**

`AccountWeekPlansHub.tsx` client component with three simple tabs:
1. **This week** → `AccountWeekPlansWeekList` (`week_start` current Monday; toggle last week)
2. **Approve** → `AccountWeekPlanApprovalQueue` (founder; others see read-only pending list or message)
3. **New plan** → `AccountWeekPlanForm`

Match existing dashboard panel styling (`text-slate-*`, dark panels used in TeamMeetings).

Wire in `DashboardView.tsx`:

```tsx
{view === "account_work" && <AccountWeekPlansHub />}
```

Import hub; add icon in view icons map if required by that file’s pattern.

- [ ] **Step 4: Commit**

```bash
git add src/lib/nav.ts src/lib/permissions.ts src/components/DashboardView.tsx \
  src/components/AccountWeekPlansHub.tsx
git commit -m "$(cat <<'EOF'
Add Account Work hub nav shell for week plans.

EOF
)"
```

---

### Task 8: Intake form UI

**Files:**
- Create: `src/components/AccountWeekPlanForm.tsx`

- [ ] **Step 1: Build form**

Props:

```ts
type Props = {
  originMeetingId?: string | null;
  defaultClientId?: string | null;
  onCreated?: (planId: string) => void;
};
```

Behavior:
- Load clients from existing lightweight clients API used elsewhere (`/api/clients` or roster endpoint used by MeetingCommitmentsPanel — copy that pattern)
- Load assignees from `/api/account-week-plans/assignees`
- Fields: client select, why textarea, severity select (optional empty), week_start date (default Monday), success_signal optional
- Tasks: array of rows — title (required per row if present), tag, assignee select, scheduled_for date, notes
- Add / remove task rows
- Submit → POST `/api/account-week-plans`
- Show `duplicate_warning` banner if returned
- On success call `onCreated` and clear form or toast

Keep UI compact; no card heap — follow TeamMeetings form controls.

- [ ] **Step 2: Commit**

```bash
git add src/components/AccountWeekPlanForm.tsx
git commit -m "$(cat <<'EOF'
Add account week plan intake form.

EOF
)"
```

---

### Task 9: Approval queue + week list + client history

**Files:**
- Create: `src/components/AccountWeekPlanApprovalQueue.tsx`
- Create: `src/components/AccountWeekPlansWeekList.tsx`
- Create: `src/components/AccountWeekPlansClientHistory.tsx`

- [ ] **Step 1: Approval queue**

- GET `view=pending_approval&include_tasks=1`
- Each row: client name, why, severity, task titles/assignees/days
- Buttons: Approve / Reject (reject expands note textarea required)
- PATCH `/api/account-week-plans/:id` with status
- Hide action buttons if current user is not owner/ceo; show “Waiting on founder”

- [ ] **Step 2: Week list / execute**

- GET `week_start=…&include_tasks=1`
- Toggle this week / last week (`addDaysToYmd(weekStart, -7)`)
- Expand plans with tasks; for approved open tasks: Done / Cancel
- Done modal: optional completion_report, checkbox “Log as account change”
- PATCH task endpoint
- Show done tasks with report snippet for review

- [ ] **Step 3: Client history**

Props: `{ clientId: string }`

- GET `client_id=&include_tasks=1` ordered week_start desc
- Expandable plan rows; show all task statuses, completion reports, link text if `client_action_log_id` set (“Logged as account change”)

Mount history on Client Health detail if a clear mount point exists (e.g. near intervention history). Search for `ClientInterventionHistory` usage and place adjacent:

```tsx
{clientId && <AccountWeekPlansClientHistory clientId={clientId} />}
```

If no clean detail surface without large refactor, mount only via hub filter “by client” dropdown in week list for v1 and skip deep CS tab embed.

- [ ] **Step 4: Commit**

```bash
git add src/components/AccountWeekPlanApprovalQueue.tsx \
  src/components/AccountWeekPlansWeekList.tsx \
  src/components/AccountWeekPlansClientHistory.tsx \
  # plus ClientHealthDetail or similar if mounted
git commit -m "$(cat <<'EOF'
Add week plan approval, week review, and client history UI.

EOF
)"
```

---

### Task 10: Embed in Team Meetings (Mon / Thu)

**Files:**
- Modify: `src/components/TeamMeetings.tsx`
- Modify: `src/lib/account-week-plans.ts` (already has `weekPlanModeForTemplateSlug`)

- [ ] **Step 1: Mount panels**

Near existing `MeetingCommitmentsPanel`:

```tsx
const weekPlanMode = weekPlanModeForTemplateSlug(row.template.slug);
// ...
{weekPlanMode === 'intake' && (
  <AccountWeekPlanForm originMeetingId={row.id} />
)}
{weekPlanMode === 'review' && (
  <AccountWeekPlansWeekList defaultWeekStart={/* Monday of meeting date or today */} />
)}
```

**v1 policy:** Keep `MeetingCommitmentsPanel` mounted so existing flow doesn’t break until ops cut over — place **Account Work** section **above** commitments with heading “Account week plans (new)”. Soft-deprecate in SOP only; no drop of meeting_commitments API yet.

- [ ] **Step 2: Commit**

```bash
git add src/components/TeamMeetings.tsx
git commit -m "$(cat <<'EOF'
Embed account week plan form and review in Mon/Thu meetings.

EOF
)"
```

---

### Task 11: Wm-os SOP update

**Files:**
- Modify: `docs/operations/people/kpi-review-meeting-sop.md`
- Optionally: mirror library copy under Mr. Waiz `content/library/...` if that file is synched by library import — update both if present (check `content/library/operations/people/kpi-review-meeting-sop.md`)

- [ ] **Step 1: Update SOP language**

Replace “structured commitments” / ClickUp paste as primary path with:

- Monday: create **Account week plan** rows (why + tasks with person + day) in Mr. Waiz Account Work / Mon embed
- Founder approves **every** plan (approval queue) before work is active
- Thursday: week list — open vs done + completion reports
- Material changes: optional “Log as account change” on complete → existing CS action logs

Link design: `docs/superpowers/specs/2026-08-06-account-week-plans-design.md`

Keep checklist keys stable if Team Meetings seed still uses them (`commitments_named` can mean “plans logged”).

- [ ] **Step 2: Commit (Wm-os)**

```bash
WMOS
git add docs/operations/people/kpi-review-meeting-sop.md
# and content library path if edited in Mr. Waiz repo
git commit -m "$(cat <<'EOF'
Point KPI review SOP at account week plans workflow.

EOF
)"
```

---

### Task 12: End-to-end smoke checklist

- [ ] **Step 1: Run unit tests**

```bash
MRWAIZ
npx tsx --test src/lib/account-week-plans.test.ts
```

- [ ] **Step 2: Manual QA**

1. Create plan with 2 tasks assigned different people/days → status pending  
2. Non-founder cannot approve  
3. Founder approve → tasks completable  
4. Complete one with report; complete one with log_as_account_change=true → see action log id  
5. Reject a second plan → open tasks cancelled  
6. Client history shows both plans  
7. Week list this week shows executed work  
8. Mon meeting embed creates plan with `origin_meeting_id` set  
9. Dashboard query shape for later dashboards:

```sql
select t.*
from account_plan_tasks t
join account_week_plans p on p.id = t.plan_id
where p.status = 'approved'
  and t.status = 'open'
  and t.assignee_user_id = $1
  and t.scheduled_for = $2;
```

- [ ] **Step 3: Final commit** if only docs/UI polish remain

---

## Spec coverage self-check

| Spec requirement | Task |
|------------------|------|
| Tables + indexes | 1 |
| Minimal statuses + rules | 2 |
| Create plan + tasks anytime | 3, 8 |
| Founder approve every plan | 4, 9 |
| Person assignee + day | 3, 6, 8 |
| Free-text tags | 1, 3 |
| Complete + optional report | 5, 9 |
| Optional action log promote | 5, 9 |
| Client history | 9 |
| Week list | 9 |
| Mon/Thu embed | 10 |
| No ClickUp / no catalog / no day dashboards | All (out of scope) |
| Active-work query ready | 1 indexes + 2 filter + Task 12 SQL |
| SOP language | 11 |
| meeting_commitments not dual-written | 10 keeps both; new path preferred |

## Placeholder / type consistency review

- Plan statuses: only `pending | approved | rejected` across SQL, lib, API.
- Task statuses: only `open | done | cancelled`.
- No `draft` / `in_progress` / `active` task status.
- Permission helper name: `canApprovePlans` uses owner + `ceo` permission only.
- Table names: `account_week_plans`, `account_plan_tasks` only.

## Deferred (do not implement in this plan)

- Role command day playbook UI
- Tactic catalog
- Data migration from `meeting_commitments`
- ClickUp API
- Auto KPI outcome without action logs
