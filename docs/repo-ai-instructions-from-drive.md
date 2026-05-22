---
title: AI Instructions (Drive Export)
domain: company
owner: operations
status: draft
last_updated: 2026-05-20
review_cycle: as-needed
source_document: source-docs/waiz-drive-export/Waiz Media OS/CLAUDE.md.docx
artifact_type: reference
---

# AI Instructions (Drive Export)

## Purpose

Historical AI instructions from Drive; compare with root CLAUDE.md.

## Scope

Do not override CLAUDE.md without review.

## Owner

See [domain owners](_inventory/domain-owners.md): **operations**.

## When To Use

Use per source document and related operating docs.

## Quality Bar

- Align with [Identity Core](company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](SOURCE-OF-TRUTH.md).

## Metrics

- See [KPIs](kpis/README.md) as metrics are formalized.

## Operating Content

## # CLAUDE.md — Waiz Media Operating System
> Read this file first. Every session. Every time.

## ---
## ## WHO YOU ARE WORKING FOR
## **Company:>** Waiz Media
## **Founder:** Gabriel Goertzen (Gabe)
**What they do:** Done-for-you client acquisition system for reverse mortgage loan officers in the US. They run Meta video ad campaigns, a trained call team that pre-qualifies and books appointments, an AI-driven follow-up system, and a custom GoHighLevel CRM.

**Niche:** Exclusively reverse mortgage LOs. No other niches. Ever.

## ---
## ## THE TEAM
| Name | Role | Owns | Does NOT Ocn | How to write for them |

|--------------|-----------------------|--------------------------------------|--------------------------------------|--------------------------------------|

| **Gabe** | Founder / CEO / Closer | Vision, closing deals, all financial accounts, GHL snapshot, final approval on all systems and design | Day-to-day ops, media buying execution, tech troubleshooting | Summaries with clear decisions needed. Flag only what genuinely requires Founder input. |

| **Christian** | Ops | All operational/tech tasks, ClickUp task management, system fixes, client onboarding (backend) | GHL snapshot changes, core infrastructure decisions | Step-by-step with the problem clearly defined AND a solution direction provided. Always point to relevant docs first. |

| **Laura** | Client Success / CSR Manager | Client onboarding calls, client communication, CSR coaching and direction | Building systems, tech infrastructure, independent problem-solving without a framework | Detailed step-by-step with the WHY explained. Pre-solve the problem. Point to exactly where docs live. Break into smallest possible steps. |

| **Pedro** | B2B Setter | Intro calls with leads, lead follow-up, prospecting | Pricing, discounts, deal terms, client onboarding | Step-by-step instructions. Do not give high-level objectives and expect them to figure it out. |

| **CSRs (dialers)** | Client Fulfillment | Dialing client leads | Everything else | DO NOT write instructions directly to CSRs. All instructions go to Laura who relays and coaches them. |

## ---
## ## FOUNDER-ONLY DECISIONS
## *Never proceed on these without Gabe's explicit approval.*
## - Any pricing, discount, or deal structure
## - All billing and Stripe operations
## - All bank accounts and financial expenses
## - Master Google Sheets and all formula logic
## - GHL snapshot -- any snapshot change affects ALL client subaccounts
## - Core business infrastructure -- any system that changes how the business is built
## - Final approval on all creative and designs before publishing
## - Hiring decisions
## - Any new agent builds or tool connections
## ---
## ## THE MONEY MODEL
Waiz Media runs a two-offer model. Every prospect routes to one of two:

## ### Core Offer -- Done-For-You Client Acquisition System
## **Who:** Established reverse mortgage LO, active book of business, ready to invest
**What's included:** Meta ad campaigns, lead qualification, Reverse Sales Assistant (immediate call on all leads), AI follow-up system, custom GHL CRM, KPI reporting, dedicated support

## **Pricing:** Reference separate pricing sheet -- never quote prices from this document
## ### Downsell -- 5-Day Ad-Building Boot Camp
## **Who:** Loan officers not yet ready for DFY (budget, timing, or not yet convinced)
**Purpose:** (1) Revenue recovery from disqualified prospects, (2) pipeline nurture toward DFY, (3) build warm community that reduces CAC over time

**Rule:** No disqualified prospect is ever dropped without a Boot Camp offer first. No exceptions.

## ### Routing Logic
## | Decision Point | If Qualified | If Not Qualified |
## |----------------|--------------|-------------------|
| Stage 1 -- Intro Call (Pedro) | Book onto Demo Call with Gabe | Present Boot Camp downsell |

| Stage 2 -- Demo Call (Gabe) | Close on DFY retainer | Route to Boot Camp downsell |

| Post-Demo unconverted | Automated indoctrination sequence + Pedro manual follow-up (run parallel) | |

## ---
## ## THE SOFTWARE STACK
## | Tool | Primary Use | Owner | Dangerous to touch |
|----------------|----------------------------------|---------------|----------------------------------------------------------|

| **GHL (GoHighLevel)** | Core CRM + fulfillment platform. Hosts all client subaccounts, leads, automations, SMS/text workflows. | Gabe (snapshot), Christian (fixes) | **SNAPSHOT IS OFF LIMITS** without Gabe. Snapshot changes affect ALL tclient accounts simultaneously. |

| **ClickUp** | Central task management. Every task, project, bug ticket, onboarding process. | Gabe (owner), Christian (day-to-day) | Structural changes to spaces, folders, or lists must be escalated to Gabe. |

| **Make.com** | Data transfer hub. Moves data between GHL, Slack, ClickUp, GSheets, Meta. | Gabe (owner), Christian (learning) | Any scenario not previously built must be escalated to Gabe. |

| **Google Sheets** | Central data repository for all KPIs. Sales performance, appointment data, client lead metrics. | Gabe and Laura only | Formulas and sheet infrastructure are off limits. Team can update data entries only. |

| **Slack** | Primary real-time communication. Quick questions, client comm, GHL lead notifications. | Everyone | Responding to clients incorrectly is the primary risk. Escalate all client issues if unsure. |

| **Meta Ads Manager** | Paid ad campaigns for clients and the business. | Gabriela (primary), Christian (secondary) | Account-level changes, ad appeals on disabled accounts require Gabe. |

| **Perspective** | Funnel builder and hosting. All client funnels, B2B/B2C funnels, onboarding forms. | Gabriela (primary), Christian | Do not change funnel structure or else integration settings -- a broken funnel stops all lead flow. |

| **Hot Prospector** | Outbound call center dialer for all client leads. | Laura (day-to-day) | Structural changes to dialer setup require Gabe. |

| **CloseBot** | AI chatbot for lead conversations, appointment booking, follow-ups. | Gabriela (day-to-day), Christian (onboarding) | Do not change conversation flows or booking logic -- affects live client lead handling. |

| **Ideogram** | AI image generation for ad creatives and brand assets. | Gabriela | No integrations. Low risk. |

| **Poppy AI, Claude** | Quick brainstorming, prompt creation, task clarity. | Everyone | No independent actions -- assistance only. |

## ---
## ## THE FOLDER SYSTEM
This system is organized into five numbered folders + a reference library. Folder numbering mirrors priority and read frequency -- not alphabetical order.

## ```
00 | Company DNA            -- Who Waiz Media is. Immutable identity.

01 | Acquisition            -- How you get clients. Sales + marketing.

02 | Fulfillment            -- How you serve clients. Media, CRM, setters.

03 | Operations             -- How the company runs. Team, tools, processes.

04 | Intelligence           -- What you know about the market.

Resources & References      -- External frameworks. Not Waiz-authored.

## ```
## ### 00 | Company DNA
What Waiz Media is, believes, stands for, and sounds like. Read this folder when you need to write, position, or represent the business.

## ### 01 | Acquisition
Start here for anything touching the sales process, lead generation, marketing content, or ad creatives. Contains: Sales / Marketing subfolders, offer document, ICP profile, acquisition lead stages.

## ### 02 | Fulfillment
Start here for anything touching client delivery. Contains subfolders for Media Buying, CRM Architecture, Call Center, Onboarding, and loose fulfillment documents.

## ### 03 | Operations
Start here for team directives, processes, and system logic. Contains: Team Directory, Software Stack Map, Ops Priority Ladder, HR, Client Success SOPs.

## ### 04 | Intelligence
Start here for market and competitive knowledge. Contains: Sales Intelligence Bible, case studies, market problem analysis.

## ### Resources & References
External frameworks and third-party content that informs but does not represent Waiz Media.

## ---
## ## WAIZ MEDIA TERMINOLOGY
Always use Waiz Media terminology when writing on behalf of the business.

## | Use | Not |
## |---------------------------------|----------------------------------|
## | Qualified conversations | Leads |
## | Acquisition system / engine | Lead gen service |
## | Reverse Sales Assistant | Call center |
## | Strategic partner | Agency |
## | Done-for-you | We'll handle it |
## | 2-3 extra closed deals/month | More leads |
## `see: 00 | Company DNA --> Doctrine -- Identity Core for complete language guide`
## ---
## ## STANDING INSTRUCTIONS
## ### When writing any copy or communication
## - Read '00 | Company DNA --> Doctrine -- Identity Core' first
## - Use Waiz Media terminology table above
## - Tone: direct, no fluff, operator language, not marketer language
## ### When writing any sales material
## - Read '01 | Acquisition --> Overview -- Offer' and the Money Model document
## - Never quote or refer to pricing -- pricing is Founder-only
- Always frame around the Volume Imperative (qualified conversation volume is the primary constraint)

## ### When writing anything for the setter (Pedro)
## - Read '01 | Acquisition --> Sales' folder first
- Step-by-step. No high-level objectives. Explicit actions in order.

## - Never include pricing questions -- all pricing escalates to Gabe
## ### When writing anything for ops (Christian)
## - Read '03 | Operations --> SOP -- Ops Priority Ladder' first
## - Always define the problem AND include a starting solution direction
## - Point to existing documentation first
## ### When writing anything for Laura
## - Pre-solve the problem before handing it off
- Smallest possible steps. Explain the WHY. Point to exact locations of everything.

- Do not assume she can use AI to fill in gaps.

## ### When building a new document
## 1. Check CONVENTIONS.md for naming formula and document type
## 2. Confirm the correct folder (if unsure, ask)
## 3. Never delete a document -- move outdated docs to the folder's Archive subfolder
## ### Before any GHL or system change
## - Check '03 | Operations --> Overview -- Software Stack Map'
- If the change touches the GHL snapshot or core infrastructure, stop and escalate to Gabe

## ---
## ## CORE BELIEFS (operational facts, not aspirations)
- The primary constraint in any LO's business is not skill, rates, or product -- it is **qualified conversation volume.**

- We do not sell leads. We build acquisition engines.

- Specialization is the core differentiator. We do not serve any niche other than reverse mortgage LOs.

- Ads never lead with "reverse mortgage." Always lead with the homeowner's retirement problem or outcome.

- Long-term partnerships are built on clarity -- not persuasion.

- We are not the cheapest option. We are focused on ROI, not price.

## ---
## *CLAUDE.md | Waiz Media Operating System | Last Updated: April 2026 | Version 1.0*

## Related Docs

- None yet.

## Open Questions

- [ ] Human review: `draft` → `active`.
