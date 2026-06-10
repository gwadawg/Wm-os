---
title: A-Z Client Onboarding SOP
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-06-10
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Onboarding/Updated A-Z Onboarding Document.docx
artifact_type: sop
---

# A-Z Client Onboarding SOP

## Purpose

Gated, step-by-step onboarding from payment through launch.

## Scope

CSM, tech, media buying, fulfillment manager from close to go-live.

## Trigger

New client payment confirmed and New Client Form submitted.

## Inputs

- New Client Form
- Onboarding form
- Kickoff form
- QA form
- Launch form

## Outputs

- Live ads
- Slack channels
- GHL configured
- Launch call complete

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when applicable.

## Operating Content

Updated A-Z Onboarding Document

Updated A-Z Onboarding Document

This document outlines the complete, step-by-step client onboarding process, integrating the original A-Z technical setup with the newly structured dependency and communication framework.

Core Principles

Gated Workflow: Tasks only begin when their required input (milestone) is completed.

Clear Communication: Client communication is tied to specific stage changes, not internal confusion.

Systematic Readiness: Launch readiness is a calculated state based on QA and department completion.

## Phase 1: New Client Paid & Activation

This phase kicks off once a new client has formally agreed to the terms of service and completed the payment. It involves critical actions by the Closer and automated steps to initiate the onboarding journey.

**System of record:** Mr. Waiz (Supabase `clients` table) holds the master client record for reporting, billing, and CEO metrics. ClickUp Client Hub remains the task execution layer for onboarding checklists. Make.com orchestrates both — call Mr. Waiz **before** GHL contact creation and Slack setup.

Actions & Dependencies

Closer fills out the **GHL New Client Form** (Business Name, Client Name, Email, Phone, Contract, Offer, etc.).

Make.com automation (in order):

1. **Mr. Waiz** — `POST /api/admin/onboard` creates/updates the Supabase client (`lifecycle_status: new_account`) and a ClickUp Client Hub task; returns `client_id` and `clickup_task_id`.
2. **GHL** — contact creation in the client subaccount (unchanged).
3. **Slack** — team notification, manager assignment, channel creation (General & Scheduling).
4. **ClickUp** — downstream onboarding checklist tasks may reference the Client Hub task id from step 1.

Do **not** manually add clients in Mr. Waiz Client Roster for every new close — that tab is for corrections and missing fields (e.g. `ghl_location_id`).

Communication

Internal: Slack notification alerts the team.

Client-facing: No direct communication yet beyond the sales handoff.

## Phase 2: Welcome Email & CSM Outreach

This phase focuses on formally welcoming the client, providing essential resources, and scheduling the onboarding call.

Actions & Dependencies

Automation sends the Onboarding Welcome Email (includes Onboarding Form link, contract reminder, Slack/Skool sign-in).

CSM is notified internally to prepare for engagement.

CSM calls the client to welcome them, schedule the Onboarding Call, and remind them to complete the Onboarding Form.

Communication

Client-facing: Welcome email sent; CSM phone call.

## Phase 3: Onboarding Form Submitted

The client submits the detailed onboarding form, providing critical information for technical setup and A2P registration.

Actions & Dependencies

Blocked until: Client submits the Onboarding Form.

Automation triggers: Slack notification, ClickUp task updated with onboarding info, Google Drive folder created, resource links added.

Tech team begins A2P Verification process if EIN is provided.

Communication

Internal: Slack notification informs the team.

## Phase 4: Pre-Call Review & Onboarding Call

The CSM prepares for and conducts the onboarding call to align on strategy, expectations, and next steps.

Actions & Dependencies

CSM completes Pre-Call Checklist (reviews form, contract, sales notes).

Onboarding Call takes place: Establish leadership, build implementation pathway, get FB/CRM access, get assets, set ROI projections, and book the Launch Call.

CSM fills out the Kickoff Form to confirm all details.

Communication

Client-facing: Live Onboarding Call.

## Phase 5: Kickoff Completed & Implementation

With the strategy aligned and kickoff form submitted, the focus shifts to the technical and media setup.

Actions & Dependencies

Blocked until: Kickoff Form is submitted.

Tech Team Tasks: Phone number setup, edit custom values, configure calendars, funnel design, AI Bot (Closebot) setup, call center setup.

Media Buyer Tasks: Data & pixel configuration, Facebook Ads buildout, update fulfillment tracker.

Communication

Client-facing: Slack General channel for questions/issues; Slack Scheduling channel for appointments.

## Phase 6: Quality Assurance (QA)

Internal quality assurance checks on the technical and media setup before launch.

Actions & Dependencies

Blocked until: Department implementation tasks are completed.

Tech QA: Check A2P, funnel (price, color, offer, mobile view), calendar integration, triggers.

Media Buyer QA: Check campaign name, budget, page/ad account, offer details, landing page link, pixel.

QA Form submission automatically updates the main ClickUp task.

Communication

Internal: QA confirmation and launch readiness signal.

## Phase 7: Launch Call & Go-Live

The final comprehensive walkthrough with the client and the official launch of their campaigns.

Actions & Dependencies

Blocked until: QA is fully completed and approved.

CSM conducts Launch Call: Set expectations, show assets created, book 7-day check-in.

Project Manager does final check-in (ads, funnels, payments).

Fulfillment manager fills out Launch Form to notify team and client that ads are live.

Communication

Client-facing: Live Launch Call; Launch notification message.


## Related Docs

- [Onboarding To Launch Communication](onboarding-to-launch-client-communication.md)
- [Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md)
- [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md)
