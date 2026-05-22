# Waiz Business OS Operating Framework

## Architecture Philosophy

Waiz Media's business OS should function as company infrastructure. The repository is the source of truth for how the company thinks, sells, fulfills, hires, improves, measures, and automates work.

Core principles:

- Single source of truth: each policy, process, metric, or playbook should live in one canonical place.
- Domain ownership: organize knowledge around operating domains, not around who wrote the document.
- Execution first: documentation should make work easier to perform, not merely describe it.
- AI-readable by default: use predictable headings, explicit metadata, stable names, and clear relationships.
- Progressive detail: put the operating overview first, then link to deeper SOPs, templates, examples, and references.
- Scalable before complex: design for repeatability and delegation without overbuilding.
- Continuous improvement: every system should expose gaps, metrics, review cadence, and owner accountability.

## Documentation Standards

Use these standards for every durable document:

```markdown
---
title: Clear Human Title
domain: sales | media-buying | client-success | operations | onboarding | automation | prompts | kpis | company
owner: Role or person
status: draft | active | deprecated
last_updated: YYYY-MM-DD
review_cycle: weekly | monthly | quarterly | as-needed
---
```

Required sections for most docs:

- Purpose: why this exists.
- Scope: what is included and excluded.
- Owner: who maintains it.
- When to use: triggers or scenarios.
- Inputs: what is needed before execution.
- Outputs: what should exist after completion.
- Process: ordered steps or decision rules.
- Quality bar: what good looks like.
- Metrics: how performance is measured.
- Related docs: links to adjacent sources of truth.

Writing rules:

- Use direct, concrete language.
- Prefer numbered steps for sequence and bullets for unordered requirements.
- Define acronyms and internal terms once.
- Keep examples close to the process they explain.
- Separate strategy, SOPs, checklists, and templates instead of mixing them in one long doc.
- Mark uncertain information as an assumption or open question.
- Avoid duplicating content. Link to the canonical source instead.

## Team-facing publish format (Google Drive)

Repo Markdown is the **source of truth**. When a SOP is approved for the team (`status: active`), publish a **scannable Google Doc** that matches the WM visual standard — do not paste raw repo Markdown into Drive.

| Layer | Where | Format |
|-------|--------|--------|
| Canonical | `docs/` | Structured Markdown (sections below) |
| Team-facing | Google Drive | WM branded layout via publish pipeline |

**Layout reference (match this look):**

- Live doc: [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)
- Written spec: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)
- Skills: [team-doc-translate](../team-doc-translate/SKILL.md) → [team-doc-publish](../team-doc-publish/SKILL.md)
- Publish SOP: [team-drive-publish.md](../../docs/operations/systems/team-drive-publish.md)

When authoring repo SOPs, write content that **translates cleanly** into that layout: short Overview bullets (become 📌 NORTH STAR callout), clear H2-worthy subsections, decision tables, and field-style labels (`What It Is`, `How to Handle It`) where helpful. Strip repo-only sections (`Open Questions`, migration notes) before publish.

## Naming Conventions

Use lowercase kebab-case for files and folders:

- Good: `sales/discovery-call-sop.md`
- Good: `media-buying/campaign-launch-checklist.md`
- Good: `client-success/onboarding-workflow.md`
- Avoid: `Final Sales SOP v3.md`
- Avoid: `Random Notes.md`

File naming patterns:

- SOPs: `[workflow]-sop.md`
- Checklists: `[workflow]-checklist.md`
- Playbooks: `[domain]-playbook.md`
- Templates: `[artifact]-template.md`
- KPI definitions: `[metric-name]-kpi.md`
- Automation specs: `[workflow]-automation-spec.md`
- Prompt assets: `[use-case]-prompt.md`
- Meeting docs: `[meeting-name]-meeting.md`
- Role docs: `[role-name]-scorecard.md`

Use stable names. Do not rename files casually once linked from other docs.

## Folder Structure Philosophy

Organize by operating domain first. A recommended top-level structure:

```text
company/
strategy/
operations/
sales/
media-buying/
client-success/
onboarding/
automations/
prompts/
kpis/
templates/
archive/
```

Folder rules:

- `company/`: mission, principles, org structure, decision logs, operating cadence.
- `strategy/`: positioning, offers, markets, growth strategy, annual or quarterly planning.
- `operations/`: internal systems, rhythms, admin processes, cross-functional SOPs.
- `sales/`: lead handling, qualification, discovery, proposals, closing, follow-up.
- `media-buying/`: account setup, campaign planning, launch, optimization, reporting, QA.
- `client-success/`: onboarding, communication, reporting, retention, escalation, renewals.
- `onboarding/`: employee, contractor, client, and role-specific onboarding systems.
- `automations/`: automation maps, specs, prompts, handoff rules, tool connections.
- `prompts/`: reusable prompts grouped by business function.
- `kpis/`: metric definitions, dashboards, reporting cadences, scorecards.
- `templates/`: reusable document, email, report, meeting, and planning templates.
- `archive/`: deprecated docs that should no longer guide current operations.

If the repo already has a different structure, follow the existing structure unless asked to redesign it. Propose migrations before moving many files.

## How Claude Should Interact With The Repo

Default workflow:

1. Inspect existing docs and folder patterns.
2. Identify the canonical source of truth.
3. Update the existing source when possible.
4. Create new files only for distinct concepts.
5. Add cross-links to related docs.
6. Flag duplicates, contradictions, and stale docs.
7. Leave a concise summary of what changed and what remains unresolved.

When receiving messy founder input:

1. Extract raw ideas without losing nuance.
2. Group ideas by domain, workflow, and decision.
3. Convert each group into the right artifact type: SOP, checklist, playbook, KPI, automation spec, prompt, or decision log.
4. Separate current process from desired future process.
5. Identify missing owners, triggers, inputs, outputs, metrics, and tools.

## Future SOP Structure

Every SOP should follow this structure unless a simpler checklist is clearly enough:

```markdown
---
title: [Workflow Name] SOP
domain: [domain]
owner: [role]
status: draft
last_updated: YYYY-MM-DD
review_cycle: monthly
---

# [Workflow Name] SOP

## Purpose
[Why this SOP exists.]

## Scope
[What this SOP covers and does not cover.]

## Owner
[Role accountable for maintenance and performance.]

## Trigger
[When this process starts.]

## Inputs
- [Input 1]
- [Input 2]

## Outputs
- [Output 1]
- [Output 2]

## Tools
- [Tool 1]
- [Tool 2]

## Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Decision Rules
- If [condition], then [action].

## Quality Bar
- [Standard 1]
- [Standard 2]

## Escalation
[When and how to escalate.]

## Metrics
- [KPI 1]
- [KPI 2]

## Related Docs
- [Related document](../path/example.md)

## Open Questions
- [Question 1]
```

After the SOP is active in the repo, the published team copy must follow [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md) (cover block, HEADING_1/2, callout tables, footer). Reference layout: [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit).
