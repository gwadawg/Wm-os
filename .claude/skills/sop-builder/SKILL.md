---
name: sop-builder
description: >
  Build, brainstorm, and store Waiz Media SOPs and operational documents correctly in the OS.
  Use when the user wants to: document a business process, create an SOP, capture a workflow,
  brainstorm how a process should work, or define who owns and executes a repeatable task.
  Also use when the user says "help me build a SOP", "document this process", "how should we
  handle X", or "let's build out the process for". For **client playbooks** for paying LO
  clients, use client-playbook-creator instead.
---

# Waiz SOP Builder

Turn founder knowledge and messy process ideas into clean, correctly stored operational documents in the Waiz Media OS.

This skill handles two modes:
- **Brainstorm mode**: You have a rough idea or verbal process — work through it conversationally to extract all the steps, rules, and context.
- **Build mode**: You have enough information — produce the structured artifact immediately and place it in the right location.

---

## Step 1: Identify Mode

Read the user's input. If they have a clear, detailed process to document → go to Build Mode.
If they have a rough idea, a vague description, or need help thinking it through → go to Brainstorm Mode.

When in doubt, start with one discovery question to get oriented.

---

## Step 2: Brainstorm Mode — Discovery Questions

Ask ONE question at a time. Do not list multiple questions at once.

Use this discovery sequence (skip questions already answered):

1. **What is the process?** — Describe it in one sentence. What happens, who does it, and what does it produce?
2. **What triggers it?** — What event, schedule, or condition starts this process?
3. **Who owns it?** — Which role is accountable for executing and maintaining this?
4. **What are the inputs?** — What does the person need before they can start? (access, data, prior step, tool)
5. **What are the steps?** — Walk me through it from start to finish. Don't worry about structure — just talk through it.
6. **What does done look like?** — What is the output or definition of done?
7. **What goes wrong?** — What are the common failure modes, edge cases, or escalation triggers?
8. **What does good look like?** — How would you know this process was executed correctly?

After answers are gathered, confirm: "Here's what I'm going to build: [doc type] — [title] — stored at [path]. Does that look right?"

---

## Prospect video assets (do not duplicate)

If the SOP involves **sending nurture videos to LO prospects** before calls, link [pre-call-objection-videos.md](../../docs/acquisition/marketing/pre-call-objection-videos.md) and [manifest](../../docs/acquisition/marketing/pre-call-objection-videos-manifest.yaml) — do not create a second video registry. Skill: [pre-call-objection-videos](../pre-call-objection-videos/SKILL.md).

---

## Step 3: Determine Document Type

Use the Waiz document type taxonomy to pick the right type:

| Type | When to use | Example |
|------|-------------|---------|
| **SOP** | Step-by-step repeatable execution process | Campaign setup, client onboarding, billing report |
| **Playbook** | Strategic execution plan over a time period or campaign | 8-week client timeline, launch strategy |
| **Script** | Word-for-word language for calls or videos | Intro call script, objection handling language |
| **Framework** | Repeatable decision or analysis model | Lead qualification, sales discovery |
| **Guide** | Non-linear reference for a complex task | Troubleshooting ads, objection handling reference |
| **Doctrine** | Core beliefs, principles, immutable positions | Identity, brand voice, compliance rules |
| **Overview** | Summary/orientation for a system or concept | Offer overview, CRM map |
| **Intelligence** | Market data, ICP insights, customer patterns | Sales intelligence bible, ICP profile |

If the process is sequential and repeatable → SOP is almost always right.

---

## Step 4: Map to Domain and Folder

Use this map to determine the correct destination path in `docs/`:

| Domain | Folder | What lives here |
|--------|--------|----------------|
| Sales — scripts, calls, qualification | `docs/acquisition/sales/` | Call scripts, qualification frameworks, objection handling |
| Outbound — LinkedIn, prospecting | `docs/acquisition/outbound/` | Outreach SOPs, copy angles, sequences |
| Marketing — ads, email, copy | `docs/acquisition/marketing/` | Ad playbooks, email frameworks, copy SOPs |
| Media buying — Meta, campaigns | `docs/client-fulfillment/media-buying/` | Campaign setup SOPs, optimization rules, QA |
| Client success — retention, reporting | `docs/client-fulfillment/client-success/` | Post-launch SOPs, reset calls, KPI checks |
| Onboarding — client or team | `docs/client-fulfillment/onboarding/` | A-Z onboarding SOPs, launch comms |
| Client training — Skool, education | `docs/client-fulfillment/course-material/` | Training wrappers; link to canonical SOPs |
| Per-client deliverables | `docs/client-fulfillment/client-marketing/clients/` | Client-specific deltas only |
| CRM / automation | `docs/client-fulfillment/crm-architecture/` | CRM flows, bot logic, tag logic |
| Hiring / HR | `docs/operations/hiring/` | Assessment SOPs, onboarding bootcamps, scorecards |
| Team / people | `docs/operations/people/` | Role expectations, bonus tiers, task lists |
| Systems / ops | `docs/operations/systems/` | Internal tools, reporting SOPs, priority systems |
| Company knowledge | `docs/company/` | Doctrine, identity, brand, money model |

If a doc doesn't clearly fit one folder, prefer the domain the primary executor works in.

---

## Step 5: Apply File Naming Convention

Pattern: `[type-keyword]-[descriptive-name].md`

Examples:
- `sop-client-reset-call.md`
- `playbook-month-1-ad-account.md`
- `script-intro-call.md`
- `framework-lead-qualification.md`
- `guide-meta-ads-troubleshooting.md`
- `sop-eod-report-setters.md`

Rules:
- Lowercase, hyphenated, no spaces
- Start with the document type keyword
- Name answers: "what is in this file?"
- Do not add dates to filenames unless the doc is time-specific (e.g., scripts that change by season)

---

## Step 6: Draft the Document

Use the SOP template for repeatable processes. Pull from `TEMPLATES.md` in waiz-business-os for the correct template per doc type.

**SOP Template (default):**

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
[Why this process exists — one to two sentences.]

## Scope
[What is included. What is excluded.]

## Owner
[Role accountable for execution and maintenance.]

## Trigger
[What starts this process — event, schedule, or condition.]

## Inputs
- [What the executor needs before starting]

## Outputs
- [What exists after completion — definition of done]

## Tools
- [Tools, software, or systems used]

## Process
1. [Step]
2. [Step]
3. [Step]

## Decision Rules
- If [condition], then [action].

## Quality Bar
- [What correct execution looks like]

## Escalation
[When and how to escalate — to whom, via what channel.]

## Metrics
- [How to measure this process is working]

## Related Docs
- [Link to related SOP or reference]

## Open Questions
- [Anything unresolved or needing owner confirmation]
```

---

## Step 7: OS Scan — Dedup and Cross-Link

Before writing the file, scan the OS to avoid duplicating existing knowledge and to surface links that belong in the new doc.

### 7a — Duplicate check

1. Check `docs/_inventory/duplicate-resolutions.md` for prior resolutions on this topic.
2. Search `docs/` for files with similar names, topics, or keywords from the process being documented.
3. If a file already covers this exact process → update it instead of creating a new one.
4. If a file partially overlaps → note the overlap and scope the new doc to avoid it.

State the finding before proceeding: "No existing doc covers this. Creating `[path]`." or "Related doc found at `[path]` — updating it instead of creating a new file."

### 7b — Cross-link scan

For every step or section in the new doc, ask: **does this reference a process, rule, or concept already documented elsewhere in the OS?**

Search `docs/` for:
- Any SOP, playbook, script, or guide the new process depends on as a prerequisite or handoff
- Any doc that defines a term, rule, or standard referenced in the new doc
- Any adjacent doc a reader would logically need after completing this process

**Cross-linking rules:**

- If a step involves a process fully documented elsewhere → do NOT re-write it. Replace the step with: `→ See [Doc Title](relative/path/to/doc.md)` and a one-line summary of what it covers.
- If a section references a standard or rule already in another doc → add a `→ See` reference instead of repeating the rule.
- If a process is only partially covered elsewhere → write the delta (what's new/different) and link to the base doc for the shared parts.
- Always use relative paths for internal links (e.g., `../../acquisition/sales/script-intro-call.md`).

**Populate the `Related Docs` section** with every doc surfaced in this scan, organized as:

```markdown
## Related Docs

### Prerequisites (read before this SOP)
- [Doc Title](relative/path.md) — one-line description of what it covers

### Handoffs (what happens after this SOP)
- [Doc Title](relative/path.md) — one-line description

### Reference (used during execution)
- [Doc Title](relative/path.md) — one-line description
```

Use only the categories that apply. Skip empty categories.

### 7c — Methodology scan (client + team playbooks)

1. Read [catalog.yaml](../../docs/client-fulfillment/client-playbooks/catalog.yaml) → `methodology_pools`.
2. For each technique, framework, or rule in the new doc, check whether it already exists in the OS (pools, acquisition, company, skills).
3. Populate `methodology_sources:` in frontmatter with paths to reused techniques.
4. If a **reusable technique is new** (not in any pool or linked doc), ask verbatim:

> I used **[technique]** in this playbook, but it is not in the knowledge base yet. Should I update **[candidate doc(s)]**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)

Follow [client-playbooks](../client-playbooks/SKILL.md) for full rules.

---

## Step 8: Write the File

Write the completed document to the correct path. Use `status: draft` unless the user confirms it is ready for team use.

Set `last_updated` to today's date.

For **client-facing playbooks**, use [client-playbook-creator](../client-playbook-creator/SKILL.md) — not this skill.

---

## Step 9: Sync catalog (client-facing docs only)

If the user created client-facing docs via [client-playbook-creator](../client-playbook-creator/SKILL.md), catalog sync is handled there. For other client-facing SOPs tagged `client_delivery: true`:

1. Run `python scripts/sync-client-playbooks.py` from repo root.
2. Confirm the entry appears in [catalog.md](../../docs/client-fulfillment/client-playbooks/catalog.md).

---

## Step 10: Summary and Next Steps

After creating the file, return:

**Created:** `[file path]`
**Type:** [doc type]
**Owner:** [role]
**Status:** draft

**Gaps flagged** (if any):
- Missing: [field or decision]
- Assumption made: [what you assumed]

**Suggested next docs** (if relevant):
- [Related SOP or template that would complete this workflow]

---

## Step 11: Publish Offer

After writing the file, ask verbatim:

> This SOP is in the repo (`status: draft`). When you're ready to approve it for the team, I can publish a team-friendly version to Google Drive. Do you want to do that now, or save it for later? (publish now / save for later)

If publish now: use the [team-doc-translate](../team-doc-translate/SKILL.md) skill first, then [team-doc-publish](../team-doc-publish/SKILL.md).

---

## Operating Rules

- One question at a time in Brainstorm Mode.
- Never create a duplicate — check first, update when possible.
- Always state the destination path before writing.
- Use `status: draft` by default. Only `status: active` when user approves.
- GitHub `docs/` is the source of truth. Google Drive is downstream.
- Flag missing owner, trigger, quality bar, or escalation path as open questions — do not invent them.
- Keep language operational: direct, concrete, executable. No filler.
- **Never repeat documented content.** If a step, rule, or standard already exists in another doc, link to it — do not restate it. The new doc should only contain what is genuinely new.
- **Always use relative paths for internal links.** Links must work from the file's location in the repo.
- **Cross-link before you write.** Run the OS scan (Step 7b) before drafting the Process section so links are built in from the start, not added as an afterthought.

## Related Skills

| Skill | When |
|-------|------|
| [waiz-business-os](../waiz-business-os/SKILL.md) | Broader OS work, repo structure, migration |
| [client-playbook-creator](../client-playbook-creator/SKILL.md) | Create/rebuild client playbooks |
| [client-playbooks](../client-playbooks/SKILL.md) | Catalog sync, methodology pools |
| [team-doc-translate](../team-doc-translate/SKILL.md) | Convert repo SOP into branded team copy |
| [team-doc-publish](../team-doc-publish/SKILL.md) | One-way publish to Google Drive |
| [brainstorming](../brainstorming/SKILL.md) | Deep product/system design exploration |
| [senior-prompt-engineer](../senior-prompt-engineer/SKILL.md) | Building prompt assets under `docs/prompts/` |
