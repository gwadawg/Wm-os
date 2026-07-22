# KPI Review Meeting SOP Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to
> implement this plan task-by-task.

**Goal:** Ship a positions-only Mon/Thu KPI Review Meeting SOP and linked
Under-KPI Diagnosis Ladder in Wm-os, publish both to the Mr. Waiz Resource
Library, and lightly wire Open SOP links into existing Team Meetings runbooks
without adding new form fields.

**Architecture:** Wm-os owns canonical cadence copy. Mr. Waiz Resource Library
mirrors the two SOPs for in-app reading. Team Meetings keeps lean checklists;
`library_slugs` on seeds drive UI links by template slug (no DB migration).
Meeting note format lives in the SOP for existing summary/follow_ups until the
form is refined later. Expect Mr. Waiz agenda/checklist copy to iterate as the
team learns; update Wm-os when the format stabilizes.

**Tech Stack:** Markdown SOPs (waiz-business-os), library-doc-transfer /
`import-library-doc.mjs`, Next.js Team Meetings UI, `node:test` + `tsx`.

**Spec:** [docs/superpowers/specs/2026-07-21-kpi-review-meeting-sop-design.md](../superpowers/specs/2026-07-21-kpi-review-meeting-sop-design.md)

**Repos:** Docs in Wm-os; library + runbook wiring in
`call-center-reporting-template` (Mr. Waiz).

---

### Task 1: Author KPI Review Meeting SOP (Wm-os)

**Files:**

- Create: `docs/operations/people/kpi-review-meeting-sop.md`
- Modify: `docs/operations/people/README.md` (link under Team Meetings)

**Step 1: Create the meeting SOP**

Frontmatter:

```yaml
---
title: KPI Review Meeting SOP
slug: kpi-review-meeting-sop
domain: operations
owner: client-success
status: draft
last_updated: 2026-07-21
review_cycle: monthly
artifact_type: sop
related_docs:
  - docs/operations/people/under-kpi-diagnosis-ladder.md
  - docs/operations/people/client-success-daily-os.md
  - docs/kpis/client-diagnostic-playbook-runnable.md
  - docs/client-fulfillment/client-success/constraint-troubleshooting-sop.md
---
```

Body requirements (positions only — no personal names):

1. Purpose / Scope / Owner / Trigger / Inputs / Outputs / Quality bar / Metrics
2. Role ownership table (Client Success, Media Buyer, Call Center Manager, Founder)
3. **Section A — Monday Week Plan** (~25m): rules, R/Y/G scan, per-red fork, OB glance, In/Out
4. **Section B — Thursday Commitment Check** (~25m): open commitments only, land/block/miss, Fri Q&A remind, In/Out
5. Note / action-plan line format for meeting summary/follow_ups
6. Link to Under-KPI Diagnosis Ladder (relative path)
7. Map existing form checklist keys (do not invent new keys)

Commitment line format:

```
[Client] · [911|Below] · Why: [one sentence] · Constraint: [system|quality / label] · Plan: [role] will [action] by [date] · Success: [signal]
```

**Step 2: Link from people hub**

In `docs/operations/people/README.md`, replace the “Cadence/SOP copy is placeholder” sentence with a link to `kpi-review-meeting-sop.md` (and the ladder once Task 2 exists).

**Step 3: Commit (Wm-os)**

```bash
git add docs/operations/people/kpi-review-meeting-sop.md docs/operations/people/README.md
git commit -m "$(cat <<'EOF'
Add KPI Review Meeting SOP for Mon Week Plan and Thu Commitment Check.

Positions-only cadence with action-plan note format; form fields deferred.
EOF
)"
```

---

### Task 2: Author Under-KPI Diagnosis Ladder (Wm-os)

**Files:**

- Create: `docs/operations/people/under-kpi-diagnosis-ladder.md`
- Modify: `docs/operations/people/kpi-review-meeting-sop.md` (ensure mutual links)
- Modify: `docs/operations/people/README.md` if ladder not yet listed

**Step 1: Create the ladder doc**

Frontmatter: `slug: under-kpi-diagnosis-ladder`, `artifact_type: sop` (or `checklist`), `owner: client-success`, `status: draft`, `related_docs` pointing at meeting SOP + diagnostic playbook + constraint troubleshooting.

Body:

1. Purpose: field guide after a red is named — not a second grader
2. Solve cadence (Mon → Tue–Wed ladder → Thu check)
3. Ladder steps 0–7 from the spec (data gate → escalate)
4. Basic data-accuracy checklist (5 bullets)
5. System vs quality definitions
6. Explicit: live numbers = Mr. Waiz; do not copy tier tables

**Step 2: Commit (Wm-os)**

```bash
git add docs/operations/people/under-kpi-diagnosis-ladder.md docs/operations/people/kpi-review-meeting-sop.md docs/operations/people/README.md
git commit -m "$(cat <<'EOF'
Add Under-KPI Diagnosis Ladder linked from the KPI Review Meeting SOP.

System-vs-quality field checklist with basic data gates; defers bands to the app.
EOF
)"
```

---

### Task 3: Point Daily OS pages at the new SOPs (link only)

**Files:**

- Modify: `docs/operations/people/client-success-daily-os.md`
- Modify: `docs/operations/people/call-center-manager-daily-os.md`
- Modify: `docs/operations/people/media-buyer-daily-os.md` (if Mon/Thu KPI mentioned)

**Step 1:** Find Mon/Thu KPI meeting sections; add one-line links to the meeting SOP and ladder. Do not paste agendas.

**Step 2: Commit (Wm-os)**

```bash
git add docs/operations/people/*daily-os.md
git commit -m "$(cat <<'EOF'
Link Daily OS Mon/Thu KPI sections to the meeting SOP and under-KPI ladder.
EOF
)"
```

---

### Task 4: Import both docs into Mr. Waiz Resource Library

**Files (Mr. Waiz repo):**

- Modify: `scripts/import-library-doc.mjs` — add `team-meetings-kpi` (or `client-success-kpi`) bundle
- Create via import: `content/library/operations/people/kpi-review-meeting-sop.md` (path per `outputSubdir`)
- Create via import: `content/library/operations/people/under-kpi-diagnosis-ladder.md`
- Modify: `content/library/manifest.json` (regenerated by script)
- Optionally: `RELATED_DOCS_OVERRIDES` for the two slugs

**Step 1: Add bundle config**

```js
"team-meetings-kpi": {
  entries: [
    {
      rel: "operations/people/kpi-review-meeting-sop.md",
      slug: "kpi-review-meeting-sop",
      sourceRoot: WMI_OS_DOCS, // same pattern as other bundles
    },
    {
      rel: "operations/people/under-kpi-diagnosis-ladder.md",
      slug: "under-kpi-diagnosis-ladder",
      sourceRoot: WMI_OS_DOCS,
    },
  ],
  department: "operations", // or client-success if enum allows
  outputSubdir: "operations/people",
  featuredSlug: "kpi-review-meeting-sop",
},
```

Match existing `sourceRoot` / Wm-os path resolution in the script (do not invent a new env pattern).

**Step 2: Dry run**

```bash
cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
node scripts/import-library-doc.mjs --bundle team-meetings-kpi --dry-run
```

Expected: lists both docs, no writes.

**Step 3: Import**

```bash
node scripts/import-library-doc.mjs --bundle team-meetings-kpi
```

Expected: files under `content/library/…` and manifest updated with both slugs and related_docs.

**Step 4: Verify**

```bash
npm run dev
# open /library/kpi-review-meeting-sop and /library/under-kpi-diagnosis-ladder
# confirm RelatedDocsPanel cross-links and draft banner if status: draft
```

**Step 5: Commit (Mr. Waiz)**

```bash
git add scripts/import-library-doc.mjs content/library/
git commit -m "$(cat <<'EOF'
Import KPI Review Meeting SOP and Under-KPI ladder into the Resource Library.
EOF
)"
```

---

### Task 5: Add `library_slugs` to meeting seeds + fill Mon/Thu agenda copy

**Files (Mr. Waiz):**

- Modify: `src/lib/team-meetings.ts`
- Modify: `src/lib/team-meetings.test.ts`

**Step 1: Extend seed type (no DB column)**

```ts
export type TeamMeetingSeed = {
  // ...existing fields
  /** Resource Library slugs opened from the runbook UI (not stored on template row). */
  library_slugs?: string[];
};
```

`templateRowFromSeed` must **not** pass `library_slugs` into the DB upsert.

**Step 2: Fill Mon KPI seed**

- Replace PLACEHOLDER `agenda_md` with lean In/Out from the SOP (positions only).
- Set `library_slugs: ['kpi-review-meeting-sop', 'under-kpi-diagnosis-ladder']`.
- Keep checklist keys: `ryg_scan_done`, `reds_have_owners`, `commitments_named`, `ob_glance`.
- Optionally sharpen checklist **labels** only (keys stable).

**Step 3: Fill Thu KPI seed**

- Replace PLACEHOLDER `agenda_md` with Commitment Check In/Out.
- Set `library_slugs: ['kpi-review-meeting-sop', 'under-kpi-diagnosis-ladder']`.
- Keep keys: `commitments_checked`, `still_red_recommitted`, `fri_qa_reminded`.

**Step 4: Helper for UI**

```ts
export function librarySlugsForTemplate(slug: string): string[] {
  return TEAM_MEETING_SEED.find(s => s.slug === slug)?.library_slugs ?? [];
}
```

**Step 5: Tests**

In `team-meetings.test.ts`:

- Assert Mon/Thu `agenda_md` does not include `PLACEHOLDER`.
- Assert `librarySlugsForTemplate('mon-kpi-week-plan')` includes both slugs.
- Assert checklist keys unchanged.

Run:

```bash
npx tsx --test src/lib/team-meetings.test.ts
```

Expected: PASS.

**Step 6: Commit (Mr. Waiz)**

```bash
git add src/lib/team-meetings.ts src/lib/team-meetings.test.ts
git commit -m "$(cat <<'EOF'
Fill Mon/Thu KPI runbook agendas and attach library SOP slugs on seeds.
EOF
)"
```

---

### Task 6: Render Open SOP links in TeamMeetings UI

**Files (Mr. Waiz):**

- Modify: `src/components/TeamMeetings.tsx`

**Step 1: Import helper**

```ts
import { librarySlugsForTemplate } from "@/lib/team-meetings";
```

**Step 2: Above the Live checklist section in `TeamMeetingRunbook`**

Render links when `librarySlugsForTemplate(row.template.slug)` is non-empty:

- Label map: `kpi-review-meeting-sop` → “Open meeting SOP”; `under-kpi-diagnosis-ladder` → “Diagnosis ladder”
- `href={`/library/${slug}`}` with `target="_blank"` `rel="noreferrer"`
- Style: text links consistent with existing slate UI — no new cards/form fields

**Step 3: Manual check**

Open `/dashboard?view=team_meetings`, open a Mon KPI instance, confirm links work. Confirm disposition fields unchanged.

**Step 4: Commit (Mr. Waiz)**

```bash
git add src/components/TeamMeetings.tsx
git commit -m "$(cat <<'EOF'
Link Team Meetings Mon/Thu runbooks to KPI Review library SOPs.
EOF
)"
```

---

### Task 7: Reseed templates so DB agenda_md updates

**Files:** none new — uses existing `ensureTemplatesSeeded` in `src/lib/team-meetings-db.ts`

**Step 1:** Hit Team Meetings in local/dev (or whatever path already calls seed upsert) so Mon/Thu `agenda_md` and checklist labels refresh from seeds.

**Step 2:** Confirm DB-backed instances show new agenda text (not PLACEHOLDER).

If upsert only runs on empty table, document the admin/reseed path already used for Team Meetings and run that instead — do not invent a new migration.

---

### Task 8: Final cross-check

**Step 1:** Spec checklist vs shipped artifacts

- [ ] Two Wm-os docs, positions only
- [ ] Mon + Thu as sections of meeting SOP
- [ ] Ladder separate with data checklist
- [ ] Library pages + related_docs
- [ ] Open SOP links on Mon/Thu runbooks
- [ ] No new disposition fields
- [ ] Checklist keys unchanged

**Step 2:** Note in people README or SOP: Mr. Waiz meeting format may iterate; sync Wm-os when stabilized.

---

## Out of scope (do not do in this plan)

- New meeting form fields for red-account notes
- Structured commitment / RYG board DB
- Other five meeting series SOPs
- Rewriting KPI grader or diagnostic rulebook
- Team Drive publish
