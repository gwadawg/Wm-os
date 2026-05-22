# Team Doc Translation Standards

Visual layout: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)  
Live reference: [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

## North star callout

Replace plain "At a glance" bullets with one **📌 NORTH STAR** table row:

- Who + when + outcome in 1–2 sentences max.

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

## Do not publish

- YAML, `source_document`, Open Questions, SPINE/inventory links
- Dollar pricing (escalate to Gabriel)
- ASCII `====` / `----` dividers
