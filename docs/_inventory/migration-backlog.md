---
title: Migration And Operational Gap Backlog
domain: inventory
owner: operations
status: active
last_updated: 2026-05-20
review_cycle: weekly
---

# Migration And Operational Gap Backlog

Use this backlog to turn the raw Google Drive export into durable AI-ready company documentation.

## Phase 1: Source Of Truth Setup

- [x] Confirm top-level operating domains match how Waiz Media actually works.
- [x] Decide whether acquisition remains one domain or splits into sales and marketing top-level domains. **Decision: one `acquisition` domain with `sales/`, `marketing/`, `intelligence/`, `offer/` subfolders.**
- [x] Decide ownership roles for company, acquisition, operations, client fulfillment, media buying, client success, and onboarding docs. See [domain-owners.md](domain-owners.md).
- [x] Convert `CLAUDE.md.docx` and `CONVENTIONS.md.docx` into canonical Markdown repo guidance if their content is current. See `docs/repo-conventions.md` and `docs/repo-ai-instructions-from-drive.md` (compare with root `CLAUDE.md` before merging).

## Phase 2: Convert High-Priority Docs

- [x] Convert `Waiz Media OS/00 _ Company DNA/Doctrine _ Brand and Visual Identity _ April 26.docx` to `docs/company/doctrine-brand-and-visual-identity-april-26.md`.
- [x] Convert `Waiz Media OS/00 _ Company DNA/Doctrine _ Identity Core _ April 26.docx` to `docs/company/doctrine-identity-core-april-26.md`.
- [x] Convert `Waiz Media OS/00 _ Company DNA/Overview _ Money Model _ April 26.docx` to `docs/company/overview-money-model-april-26.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Intelligence/WM Sales Intelligence Bible.docx` to `docs/acquisition/intelligence/wm-sales-intelligence-bible.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Marketing/Resources & References/SOP -- Money Tales Email Copy Framework.docx` to `docs/acquisition/marketing/sop-money-tales-email-copy-framework.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Objection Handling Master Guide.docx` to `docs/acquisition/sales/objection-handling-master-guide.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Discovery Call Script 01_2026.docx` to `docs/acquisition/sales/discovery-call-script-2026.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Disqualifying & Financial Qualification.docx` to `docs/acquisition/sales/disqualifying-financial-qualification.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Intro Call Qualification Framework.docx` to `docs/acquisition/sales/intro-call-qualification-framework.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/No Shows & Maximizing Show Rates (Setter Levers).docx` to `docs/acquisition/sales/no-shows-maximizing-show-rates-setter-levers.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Sales Admin Work/EOD Report SOP (Setters & Closers).docx` to `docs/acquisition/sales/eod-report-sop-setters-closers.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales Admin Work/Setter Daily Operations Playbook_...` to `docs/acquisition/sales/setter-daily-operations-playbook.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Script -- Demo Call.docx` to `docs/acquisition/sales/script-demo-call.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/Script -- Intro Call Basic.docx` to `docs/acquisition/sales/script-intro-call-basic.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/WM Objection Handling Word Tracking.docx` to `docs/acquisition/sales/wm-objection-handling-word-tracking.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales (SOPs)/WM _ Reframe Beliefs_.docx` to `docs/acquisition/sales/wm-reframe-beliefs.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales Discovery Framework (Hell,Bridges,Heaven,Fuel).docx` to `docs/acquisition/sales/sales-discovery-framework-hell-bridges-heaven-fuel.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/Sales calls Demo Analyisis_.docx` to `docs/acquisition/sales/sales-calls-demo-analysis.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/Sales/WM Objection Categories_.docx` to `docs/acquisition/sales/wm-objection-categories.md`.
- [x] Convert `Waiz Media OS/01 _ Acquisition/WM_Sales_Call_Tracker.xlsx` to `docs/acquisition/wm-sales-call-tracker.md` (wrapper; raw xlsx preserved).
- [x] Convert `Waiz Media OS/02 _ Operations/HR-People (SOPs)/Team Responsiblity Directory.docx` to `docs/operations/people/team-responsibility-directory.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/HR-People (SOPs)/VA Performance Bonus  Booking & Show Rate Tiers.docx` to `docs/operations/people/va-performance-bonus-booking-show-rate-tiers.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/HR-People (SOPs)/VA Role  Master Task List & Performance Expectations.docx` to `docs/operations/people/va-role-master-task-list-performance-expectations.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/MB Hiring-Onboarding/MB_ Initial Onboarding Steps.docx` to `docs/operations/hiring/mb-initial-onboarding-steps.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/MB Hiring-Onboarding/Media Buyer - Onboarding Call SOP.docx` to `docs/operations/hiring/media-buyer-onboarding-call-sop.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/MB Hiring-Onboarding/Media Buyer Assessment Call SOP.docx` to `docs/operations/hiring/media-buyer-assessment-call-sop.md`.
- [x] ~~Convert Media Buyer Job Scorecard(1)~~ — **superseded** per [duplicate-resolutions.md](duplicate-resolutions.md).
- [x] Convert `Waiz Media OS/02 _ Operations/MB Hiring-Onboarding/Media Buyer Job Scorecard.docx` to `docs/operations/hiring/media-buyer-job-scorecard.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/MB Hiring-Onboarding/Media Buyer Onboarding & Bootcamp.docx` to `docs/operations/hiring/media-buyer-onboarding-bootcamp.md`.
- [x] ~~Convert Ops Constraint Troubleshooting~~ — **superseded**; canonical → `docs/client-fulfillment/client-success/constraint-troubleshooting-sop.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/Ops (SOPs)/How to send out HE Billing Reports.docx` to `docs/operations/systems/how-to-send-out-he-billing-reports.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/Ops (SOPs)/Identifying technical issues with clients.docx` to `docs/operations/systems/identifying-technical-issues-with-clients.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/Ops (SOPs)/OPS Manager Priority Ladder.docx` to `docs/operations/systems/ops-manager-priority-ladder.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/Ops (SOPs)/RM Client KPI Check_.docx` to `docs/operations/systems/rm-client-kpi-check.md`.
- [x] Convert Manus SOP (plain-text export) to `docs/operations/systems/sop-optimizing-manus-for-maximum-effectiveness.md`.
- [x] Convert `Waiz Media OS/02 _ Operations/WM Acquisition Report  Complete Data System Documentation.docx` to `docs/operations/reporting/wm-acquisition-report-data-system.md`.
- [x] Convert `Waiz Media OS/03 _ Client Fulfillment/CRM Architecture/CRM Infrustructure.docx` to `docs/client-fulfillment/crm-architecture/crm-infrastructure.md`.
- [x] Convert `Waiz Media OS/03 _ Client Fulfillment/CRM Architecture/How WM AI Bot Works.docx` to `docs/client-fulfillment/crm-architecture/how-wm-ai-bot-works.md`.
- [x] Convert constraint troubleshooting (CS March 2026) to `docs/client-fulfillment/client-success/constraint-troubleshooting-sop.md`.
- [x] Convert fulfillment KPI diagnosis doc to `docs/client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md`.
- [x] Convert `Waiz Media OS/03 _ Client Fulfillment/Client Course Material/Skool Community/Bootcamp /SOP  Setting Up Your Facebook Lead Form 📝.docx` to `docs/client-fulfillment/course-material/sop-setting-up-facebook-lead-form.md`.
- [x] Convert `Waiz Media OS/03 _ Client Fulfillment/Client Course Material/Skool Community/Bootcamp /lead_nurture_playbook.docx` to `docs/client-fulfillment/course-material/lead-nurture-playbook.md`.

## Phase 3: Gap Analysis

- [ ] Add owners to every active SOP and playbook.
- [ ] Add triggers, inputs, outputs, and definition of done to every SOP.
- [ ] Add KPIs to sales, media buying, onboarding, and client success workflows.
- [ ] Identify which SOPs should become automations or prompt workflows.
- [x] Archive superseded docs after canonical replacements are approved. See `docs/archive/superseded-sources.md` and [SPINE.md](../SPINE.md) (stabilization approved 2026-05-20).
