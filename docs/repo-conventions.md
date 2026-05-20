---
title: Repository Conventions
domain: company
owner: operations
status: draft
last_updated: 2026-05-20
review_cycle: quarterly
source_document: source-docs/waiz-drive-export/Waiz Media OS/CONVENTIONS.md.docx
artifact_type: reference
---

# Repository Conventions

## Purpose

Repo naming and documentation conventions from Drive export.

## Scope

GitHub OS maintenance.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **operations**.

## When To Use

Use per source document and related operating docs.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).

## Metrics

- See [KPIs](../../kpis/README.md) as metrics are formalized.

## Operating Content

## # CONVENTIONS.md -- Waiz Media System Conventions
> This file defines how every document and folder in this system is named, organized, and maintained. It applies to humans and Claude Code equally. No exceptions.

## ---
## ## PART 1: FOLDER RULES
#of top-level folders use the pattern `XX | Folder Name`. Subfolders have no numbers.

## ```
## 00 | Company DNA/
## 01 | Acquisition/
## 02 | Fulfillment/
## 03 | Operations/
## 04 | Intelligence/
## Resources & References/
## ```
## ### Each top-level folder contains
## - An `Archive/` subfolder -- old documents go here, never to the trash
## - Functional subfolders where relevant (no numbers on subfolders)
## - Documents that belong directly to that folder's domain
## ### Where things live
## | Answers a question about... | Put it in... |
## |--------------------------------------------|-----------------------------|
| Who Waiz Media is, what we believe, how we sound | `00 | Company DNA` |

## | How we get clients; sales, ads, offer, ICP | `01 | Acquisition` |
## | How we serve clients; media, CRM, setters, onboarding | `02 | Fulfillment` |
## | How the company runs; team, tools, HR, processes | `03 | Operations` |
| What we know about the market; voice of customer, case studies | `04 | Intelligence` |

## | External frameworks; not Waiz-authored | `Resources & References` |
## ### Top-level folder subfolder map
## ```
## 01 | Acquisition/
## ├── Sales/
## *   ├── Scripts, Frameworks, Guides, Playbooks
## ℜ── Marketing/
## ℜ── Archive/
## 02 | Fulfillment/
## ├── Media Buying/
## ├── CRM Architecture/
## ℜ── Call Center/
## ├── Onboarding/
## ℜ── Archive/
## 03 | Operations/
## ├── Ops/
## ├── Client Success/
## ℜ── HR People/
## ℜ── Archive/
## Archive/
## ```
## ---
## ## PART 2: DOCUMENT NAMING FORMULA
Every document in this system follows this exact formula:

## ```
## [Type] -- [Descriptive Name] -- [Month Year]
## ```
## ### Examples
## ```
## Doctrine -- Identity Core -- April 2026
## Framework -- Sales Discovery (Hell, Bridges, Heaven, Fuel) -- March 2026
## Script -- Intro Call -- April 2026
## Guide -- Objection Handling -- April 2026
## SOP -- Meta Ads Campaign Setup -- January 2026
## Overview -- Offer -- April 2026
## Intelligence -- Sales Intelligence Bible -- April 2026
## Playbook -- 8-Week Client Timeline -- March 2026
## ```
## ### Rules
- Type comes first -- always. This is how Claude filters before reading.

- Name should answer: "what is in this file?" -- not "what section does it belong to?"

- Month Year is the date the document was first created or last majorly revised.

- WAIZ prefixes (e.g. `WM |`) are not needed -- everything in this system is Waiz Media.

## ---
## ## PART 3: DOCUMENT TYPES
These are the eight approved document types. If a new document doesn't fit one of these, question whether it needs to exist.

| Type | What it is | Claude reads it as | Example use |

|-------------|--------------------------------------------------|-------------------------------------|--------------------------------------|

| SOP | Step-by-step execution instructions. Repeatable process. | Follow these steps in order. | Meta ad campaign setup, onboarding a new client |

| Script | Word-for-word dialogue for calls or videos. | Use this language. | Intro call script, ad voiceover script |

| Playbook | Strategic execution plan for a specific length/outcome. | Follow this strategy. | 8-week client timeline, ad campaign strategy |

| Framework | Repeatable model for decision-or analysis. | Apply this model. | Sales discovery framework, lead stages framework |

| Guide | How-to for a non-linear task. Referenced, not followed step-by-step. | Use this for reference. | Objection handling, troubleshooting |

| Doctrine | Beliefs, principles, and immutable positions. Rarely changes. | This is who we are. | Identity core, objection categories doctrine |

| Overview | Summary document for a system, product, or concept. | Understand this first. | Offer overview, software stack map |

| Intelligence | Market data, patterns, customer insights. | Reference for decisions. | Sales intelligence bible, case studies, ICP profile |

## ### Picking the right type
## - Step-by-step process ? --> SOP
## - Perform a call or speech exactly ? --> Script
## - Strategic execution over time ? --> Playbook
## - Repeatable thinking model ? --> Framework
## - Reference for a non-linear task ? --> Guide
## - Core belief or position ? --> Doctrine
## - Summary or orientation document ? --> Overview
## - Market knowledge or data ? --> Intelligence
## ---
## ## PART 4: ARCHIVE RULES
**Never delete a document.** Ever.

When a document is outdated or superseded:

## 1. Move it to the `Archive/` folder inside its parent folder
## 2. No renaming required -- the date in the name tells the story
**When not to archive:** If a document is still being referenced by an active process, do not archive it yet -- update it in place instead.

## ---
## ## PART 5: CONTENT RULES
## ### Every document must
- Have a single clear purpose -- if it can't be stated in one sentence, it probably needs to be split

## - Answer a unique question not answered elsewhere
- Open with a single line stating what it is and who it is for

## ### No document may
## - Delete or layer over another document's content without archiving the old one
## - Live outside a designated folder -- no orphaned files at any root level
## - Contain pricing -- pricing lives on a separate sheet owned by Gabe
## ### Redundancy rule
If two documents answer the same question, one goes to Archive. Multiple documents covering the same topic mean Claude will never know which one to trust.

## ---
## ## PART 6: WHAT NEEDS A DATE VS. WHAT DOESN'T
## **Always include a date:**
## - Anything that changes over time: scripts, playbooks, SOPs, intelligence
## - Anything tied to a specific campaign or client segment
## **Dates are still included but less critical for:**
## - Doctrines (changes rarely)
## - Overviews for stable systems
## ---
## ## PART 7: CHEM-O FOR ANY NEW DOCUMENT
Before creating or saving any new file:

1. What question does this answer?

2. Does an existing document already answer it? (If yes -- update that one, don't create a new one)

## 3. What type is it? (reference Part 3)
## 4. Which folder does it belong in? (reference Part 1)
## 5. Is the name following the formula? (`[Type] -- [Name] -- [Month Year]`)
6. Is it standalone enough to be read without context from another doc?

## ---
## ## PART 8: KNOWN DOCUMENT COMMITMENTS
These documents are planned or exist in proto form and need to be built or normalized:

## | Document Needed | Type | Folder | Status |
|------------------------------------|---------|--------------------|-------------------------------------------|

| Objection Handling (consolidated) | Guide | 01 | Ac | Three overlapping docs exist -- need consolidation before GitHub transfer |

| Company at a Glance | Overview | 00 | Does not exist yet -- needed |

| ICP Profile | Intelligence | 01 or 04 | Exists as 'WM | ICP Document' -- needs renaming and moving |

| Money Model & Offer Architecture | Overview | 01 | Exists as 'WM | Money Model' -- needs renaming and moving |

## | Voice of Customer | Intelligence | 04 | Does not exist yet |
| Hook and Angle Library | Framework | 01 / Marketing | Does not exist yet |

## ---
## *CONVENTIONS.md | Waiz Media Operating System | Last Updated: April 2026 | Version 1.0*

## Related Docs

- None yet.

## Open Questions

- [ ] Human review: `draft` → `active`.
