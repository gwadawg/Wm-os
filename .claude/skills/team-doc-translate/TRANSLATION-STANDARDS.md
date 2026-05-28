# Team Doc Translation Standards

**Remake for humans, not translate for machines.** Repo markdown is input; the team doc is a redesigned operator manual.

Visual layout: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)  
Live reference: [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

## Human readability rules

| Repo artifact | Team doc output |
|---------------|-----------------|
| Markdown `\| table \|` | Real Google Doc table (navy header row) |
| `> quote` lines | **✉️ COPY & PASTE** shaded boxes (one message per box) |
| `---` separators | Omit |
| Long pipe bullets | Never — always a table or template box |
| Playbook sections | Each `##` → its own **H2** section (not one giant "How to do it") |
| `**Rule:**` lines | 💡/⚠️ callout or bold label |

## North star callout

- **NORTH STAR:** one sentence (purpose outcome only), max ~220 characters.
- **Who / When:** bullets directly under the shaded box in Overview — never inside NORTH STAR.
- Publish applies **navy/blue theme**, divider under cover, shaded callout box, navy table headers.

## Section mapping (repo → WM format)

| Repo section | WM format |
|--------------|-----------|
| Purpose | `HEADING_1` Overview + 11pt paragraphs |
| When To Use | Fold into NORTH STAR or Before You Start |
| Inputs / Tools | Label **Before You Start** + bullets |
| Process | `HEADING_1` How To Do It + `HEADING_2` subsections |
| Subsections in process | `HEADING_2` + optional labels (What It Is, How to Handle It) |
| Quality Bar | `HEADING_2` Done Right Looks Like + bullets |
| Escalation | `HEADING_2` When To Get Help |
| Related Docs | `HEADING_2` Related Procedures + links |

## Callout table labels (pick one)

| Label | When |
|-------|------|
| 📌 NORTH STAR | Single most important rule for this doc |
| ⚠️ IMPORTANT | Must-follow warning |
| 💡 PRO TIP | Tactic that improves results |
| 🚨 CRITICAL MISTAKE TO AVOID | High-cost error |
| ⚠️ WATCH FOR THIS | Easy to miss case |
| 📌 RULE / 📌 REMEMBER | Closing non-negotiable |

## Tables

Use when doc has:

- Categories/types (Category | What It Is | How to Handle)
- Steps (Step | What to Do)
- Quick reference at end (HEADING_2 + summary table)

## Footer

Always end with centered:

`Waiz Media | Internal Document | Confidential`

**One footer per doc.** No duplicate NORTH STAR callouts.

## Angle / script libraries

When the registry row has `team_doc_type: angle_library`:

- Follow [wm-team-angle-unit-template.md](../../docs/templates/wm-team-angle-unit-template.md) for every `## Angle N —` section.
- Run [wm-team-doc-review-checklist.md](../../docs/templates/wm-team-doc-review-checklist.md) Pass 2 before approve.

## Do not publish

- YAML, `source_document`, Open Questions, SPINE/inventory links
- Dollar pricing (escalate to Gabriel)
- ASCII `====` / `----` dividers
