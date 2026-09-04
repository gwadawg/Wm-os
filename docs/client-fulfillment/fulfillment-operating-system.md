---
title: Fulfillment Operating System
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-07-08
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/(synthesized)
artifact_type: overview
---

# Fulfillment Operating System

## Purpose

Single entry point for how Waiz delivers after a client signs — onboarding, launch, lead engine, campaign phases, and troubleshooting.

## Scope

All post-close client delivery. Excludes Waiz acquisition (see acquisition/).

## Trigger

Any AI or team work on client fulfillment, onboarding, creatives, nurture, or account health.

## Inputs

- Approved offer and contract
- New Client Form submission

## Outputs

- Live client campaign
- Documented client in ClickUp/GHL/Slack

## Quality Bar

- Align with [Identity Core](../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow product compliance guardrails: [RM Compliance Guardrails](../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) for reverse mortgage; [DSCR Compliance Guardrails](../client-fulfillment/dscr-dna/dscr-compliance-guardrails.md) for DSCR refinance.

## Operating Content

## How To Use This Doc

Load this page first for any client-fulfillment question. Follow links to the canonical SOP for execution detail.

## Delivery Timeline (Gated)

| Phase | Name | Canonical doc | Gate |
|-------|------|---------------|------|
| 1 | Paid & activation | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md) | New Client Form |
| 2 | Welcome & CSM | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md) | Welcome email + call |
| 3 | Onboarding form | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md) | Form submitted |
| 4 | Onboarding call | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md) | Kickoff form |
| 5 | Implementation | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md), [New Client Campaign Setup](media-buying/new-client-campaign-setup-sop.md) | Kickoff complete |
| 6 | QA | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md) | QA form |
| 7 | Launch | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md), [Client Success Slack Touchpoint Playbook](onboarding/onboarding-to-launch-client-communication.md) | Launch form |

## Lead Engine (After Launch)

| Stage | Doc |
|-------|-----|
| Full map | [Fulfillment Lead Lifecycle](fulfillment-lead-lifecycle.md) |
| Ads & creative | [RM Ad Playbook](client-marketing/rm-ad-playbook.md), [Ad Copy And Angle Library](media-buying/ad-copy-angle-library-rm.md), [AI RM Ad Image Creation](media-buying/ai-rm-ad-image-creation-sop.md) |
| CRM & bot | [CRM Infrastructure](crm-architecture/crm-infrastructure.md), [WM AI Bot](crm-architecture/how-wm-ai-bot-works.md), [Claimed Tag](crm-architecture/how-claimed-tag-works.md) |
| Nurture | [RM Text Drip 2025](client-marketing/rm-text-drip-2025.md), [10-Day RM Drip](client-marketing/10-day-rm-drip-campaign.md), [RM Lead Nurture Drip](client-marketing/rm-lead-nurture-drip-sequence.md) |
| Call center scripts | [Call Center Script Factory SOP](call-center/sop-call-center-script-factory.md) |

### DSCR refinance line (when client product = DSCR)

| Stage | Doc |
|-------|-----|
| Product pod (load first) | [DSCR DNA](dscr-dna/README.md) |
| Strategy | [DSCR GTM And Positioning Brief](dscr-dna/dscr-gtm-positioning-brief.md) |
| Offer anchor | [DSCR Offer And Funnel Map](dscr-dna/dscr-offer-and-funnel-map.md) |
| Ads & creative | [Intelligence ICP DSCR](dscr-dna/intelligence-icp-dscr.md) (AI), [Campaign Master Angles](dscr-dna/dscr-campaign-master-angles.md) (expand), [DSCR Static Image Generator](dscr-dna/dscr-static-image-generator-project.md) |
| Funnel / lander | [DSCR Lander Build Pack](dscr-dna/dscr-lander-build-pack.md), [DSCR Funnel Form Spec](dscr-dna/dscr-funnel-form-spec.md) |
| Nurture | [DSCR Lead Nurture And Booking — Laura](dscr-dna/dscr-nurture-and-booking-laura.md) |
| Setter / team training | [DSCR Team Product FAQ](dscr-dna/dscr-team-product-faq.md), [DSCR Setter Script](dscr-dna/dscr-setter-appointment-script.md) |
| Measurement | [DSCR KPI And Test Scorecard](dscr-dna/dscr-kpi-and-test-scorecard.md) |

## Campaign Maturity (CS Lens)

| Phase | Weeks | Doc |
|-------|-------|-----|
| Testing | 1–4 | [Campaign Phase Performance Blueprint](client-success/campaign-phase-performance-blueprint.md) |
| Optimization | 4–8 | Same |
| Compounding | 8+ | Same |

## When Performance Breaks

1. [Campaign Phase Performance Blueprint](client-success/campaign-phase-performance-blueprint.md) — normal vs abnormal for phase
2. [Constraint Troubleshooting SOP](client-success/constraint-troubleshooting-sop.md) — layer-by-layer fixes
3. [Fulfillment Constraint Diagnosis KPI Standards](client-success/fulfillment-constraint-diagnosis-kpi-standards.md)
4. [Reset Call SOP](client-success/reset-call-sop.md) if still off-track

## Compliance (Always)

Load the guardrails for the **client's product line**:

- **Reverse mortgage:** [RM Compliance Guardrails](reverse-mortgage-dna/rm-compliance-guardrails.md), [Doctrine Reverse Mortgage](reverse-mortgage-dna/doctrine-reverse-mortgage.md), [Doctrine RM Marketing](reverse-mortgage-dna/doctrine-rm-marketing.md)
- **DSCR refinance:** [DSCR Compliance Guardrails](dscr-dna/dscr-compliance-guardrails.md), [Intelligence ICP DSCR](dscr-dna/intelligence-icp-dscr.md)

## AI Quick Load Order

1. This doc
2. Compliance guardrails + angle library
3. Lifecycle + phase blueprint
4. Task-specific SOP (onboarding, MB, nurture, CS, call center)

## Subfolder Index

| Folder | Role |
|--------|------|
| [onboarding/](onboarding/README.md) | Post-close through launch |
| [infrastructure/](infrastructure/README.md) | CRM hub |
| [crm-architecture/](crm-architecture/README.md) | GHL + bot specs |
| [client-marketing/](client-marketing/README.md) | Strategy, drips, playbooks |
| [media-buying/](media-buying/README.md) | Campaign execution SOPs |
| [client-success/](client-success/README.md) | Post-launch CS + troubleshooting |
| [call-center/](call-center/README.md) | B2C fulfillment call-center scripts and QA lifecycle |
| [reverse-mortgage-dna/](reverse-mortgage-dna/README.md) | Product, ICP, compliance |
| [dscr-dna/](dscr-dna/README.md) | DSCR refinance product, ICP, funnel, setter |
| [client-playbooks/](client-playbooks/README.md) | Client playbooks index + creation guide |
| [course-material/](course-material/README.md) | Course material & client education (links to canonical) |

