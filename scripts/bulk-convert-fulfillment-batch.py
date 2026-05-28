#!/usr/bin/env python3
"""One-time batch: Drive export → canonical docs/client-fulfillment/*.md"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from lib.paths import drive_export_root

_export = drive_export_root()
if _export is None:
    raise SystemExit(
        "Drive export not found. Clone wm-os-archive next to Wm-os "
        "(see docs/_inventory/raw-export-archive.md)."
    )
BASE = _export / "Waiz Media OS/03 _ Client Fulfillment"
DOCS = REPO / "docs/client-fulfillment"
TODAY = "2026-05-21"

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paras: list[str] = []
    for p in root.iter(f"{W_NS}p"):
        texts = [t.text for t in p.iter(f"{W_NS}t") if t.text]
        if texts:
            line = "".join(texts).strip()
            if line:
                paras.append(line)
    return "\n\n".join(paras)


def md_body(text: str) -> str:
    """Light structure: ALL CAPS short lines → h3; Phase N: → h2."""
    blocks = text.split("\n\n")
    out: list[str] = []
    for b in blocks:
        line = b.strip()
        if not line:
            continue
        if re.match(r"^Phase \d+:", line):
            out.append(f"## {line}")
        elif len(line) < 80 and line.isupper() and any(c.isalpha() for c in line):
            out.append(f"### {line.title()}")
        elif line.startswith("## "):
            out.append(line)
        else:
            out.append(line)
    return "\n\n".join(out)


def _root_rel(rel_path: str, target: str) -> str:
    depth = rel_path.count("/")
    return ("../" * (depth + 1)) + target


def write_md(
    rel_path: str,
    *,
    title: str,
    owner: str,
    artifact: str,
    source_rel: str,
    purpose: str,
    scope: str,
    trigger: str,
    inputs: list[str],
    outputs: list[str],
    status: str = "draft",
    review: str = "monthly",
    related: list[str] | None = None,
    body_text: str,
) -> None:
    path = DOCS / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    src = f"source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/{source_rel}"
    inputs_md = "\n".join(f"- {i}" for i in inputs) or "- See operating content below."
    outputs_md = "\n".join(f"- {o}" for o in outputs) or "- See operating content below."
    related_md = ""
    if related:
        related_md = "\n\n## Related Docs\n\n" + "\n".join(f"- {r}" for r in related)

    identity = _root_rel(rel_path, "company/doctrine-identity-core-april-26.md")
    sot = _root_rel(rel_path, "SOURCE-OF-TRUTH.md")
    compliance = _root_rel(rel_path, "client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md")

    content = f"""---
title: {title}
domain: client-fulfillment
owner: {owner}
status: {status}
last_updated: {TODAY}
review_cycle: {review}
source_document: {src}
artifact_type: {artifact}
---

# {title}

## Purpose

{purpose}

## Scope

{scope}

## Trigger

{trigger}

## Inputs

{inputs_md}

## Outputs

{outputs_md}

## Quality Bar

- Align with [Identity Core]({identity}) and [SOURCE-OF-TRUTH]({sot}).
- Client-facing copy must follow [RM Compliance Guardrails]({compliance}) when applicable.

## Operating Content

{md_body(body_text)}
{related_md}
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(REPO)}")


CONVERSIONS: list[dict] = [
    {
        "rel": "fulfillment-operating-system.md",
        "title": "Fulfillment Operating System",
        "owner": "client-success",
        "artifact": "overview",
        "source_rel": "(synthesized)",
        "status": "active",
        "review": "monthly",
        "purpose": "Single entry point for how Waiz delivers after a client signs — onboarding, launch, lead engine, campaign phases, and troubleshooting.",
        "scope": "All post-close client delivery. Excludes Waiz acquisition (see acquisition/).",
        "trigger": "Any AI or team work on client fulfillment, onboarding, creatives, nurture, or account health.",
        "inputs": ["Approved offer and contract", "New Client Form submission"],
        "outputs": ["Live client campaign", "Documented client in ClickUp/GHL/Slack"],
        "body_text": None,  # custom below
    },
    {
        "rel": "onboarding/a-z-client-onboarding-sop.md",
        "src": "Onboarding/Updated A-Z Onboarding Document.docx",
        "title": "A-Z Client Onboarding SOP",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Gated, step-by-step onboarding from payment through launch.",
        "scope": "CSM, tech, media buying, fulfillment manager from close to go-live.",
        "trigger": "New client payment confirmed and New Client Form submitted.",
        "inputs": ["New Client Form", "Onboarding form", "Kickoff form", "QA form", "Launch form"],
        "outputs": ["Live ads", "Slack channels", "GHL configured", "Launch call complete"],
        "related": [
            "[Onboarding To Launch Communication](onboarding-to-launch-client-communication.md)",
            "[Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md)",
            "[Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md)",
        ],
    },
    {
        "rel": "onboarding/onboarding-to-launch-client-communication.md",
        "src": "Onboarding/Onboarding (SOPs)/Onboarding To Launch Client Communication.docx",
        "title": "Onboarding To Launch Client Communication",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Client-facing communication templates and timing tied to onboarding milestones.",
        "scope": "Emails, Slack, SMS patterns from welcome through launch.",
        "trigger": "Each onboarding phase transition per A-Z SOP.",
        "inputs": ["Phase completion in ClickUp", "Client contact info"],
        "outputs": ["Client informed at each gate", "Reduced launch confusion"],
    },
    {
        "rel": "client-success/campaign-phase-performance-blueprint.md",
        "src": "Archive/Client Fulfillment 8 Week Timeline (Post Close).docx",
        "title": "Campaign Phase Performance Blueprint",
        "owner": "client-success",
        "artifact": "doctrine",
        "status": "active",
        "purpose": "Define Testing, Optimization, and Compounding phases so CS and AI can judge if client concerns are normal.",
        "scope": "Internal only — not for direct client distribution.",
        "trigger": "Client questions results, slow pipeline, or KPI review.",
        "inputs": ["Campaign launch date", "Current week", "KPI benchmarks"],
        "outputs": ["Phase-appropriate response", "Escalation only when abnormal"],
        "related": [
            "[Constraint Troubleshooting SOP](constraint-troubleshooting-sop.md)",
            "[Fulfillment Constraint Diagnosis KPI Standards](fulfillment-constraint-diagnosis-kpi-standards.md)",
        ],
    },
    {
        "rel": "fulfillment-lead-lifecycle.md",
        "src": "Fulfillment Lead Lifecycle.docx",
        "title": "Fulfillment Lead Lifecycle",
        "owner": "client-success",
        "artifact": "overview",
        "purpose": "End-to-end map of the lead engine Waiz runs for clients (awareness through long-term pipeline).",
        "scope": "Training and internal alignment; complements CRM and bot docs.",
        "trigger": "Onboarding education, client questions about how leads flow, AI context for nurture/creative.",
        "inputs": ["Live campaign", "CRM configured"],
        "outputs": ["Client understands stages", "Team aligns fixes to correct stage"],
        "related": [
            "[CRM Infrastructure](crm-architecture/crm-infrastructure.md)",
            "[How The WM AI Bot Works](crm-architecture/how-wm-ai-bot-works.md)",
            "[How Claimed Tag Works](crm-architecture/how-claimed-tag-works.md)",
        ],
    },
    {
        "rel": "crm-architecture/how-claimed-tag-works.md",
        "src": "CRM Architecture/How Claimed Tag Works.docx",
        "title": "How Claimed Tag Works",
        "owner": "operations",
        "artifact": "automation",
        "status": "active",
        "purpose": "Explain lead claiming, ownership, and scheduling handoff in GHL.",
        "scope": "CRM tags, call center, LO calendar booking.",
        "trigger": "Lead assignment disputes, booking workflow changes, nurture timing.",
        "inputs": ["New lead in CRM", "ISA/bot contact attempt"],
        "outputs": ["Claimed lead owned by correct LO", "Appointment on calendar"],
    },
    {
        "rel": "media-buying/ad-copy-angle-library-rm.md",
        "src": "Media Buying/Media Buying (SOPs)/MB Creative Process/Ad Copy & Angle Library (RM).docx",
        "title": "Ad Copy And Angle Library (RM)",
        "owner": "media-buying-lead",
        "artifact": "playbook",
        "purpose": "Canonical angles, headlines, and primary text for RM Meta ads.",
        "scope": "Media buyers and AI creative generation.",
        "trigger": "New client creative build, creative refresh, constraint layer 1 fixes.",
        "inputs": ["Client offer", "Compliance guardrails", "Approved angles"],
        "outputs": ["Ad copy variants with risk ratings", "UTM patterns"],
        "related": ["[MB RM Ad Copy Standards](mb-rm-ad-copy-standards.md)", "[AI RM Ad Image Creation SOP](ai-rm-ad-image-creation-sop.md)"],
    },
    {
        "rel": "media-buying/mb-rm-ad-copy-standards.md",
        "src": "Media Buying/Media Buying (SOPs)/MB Resources/MB _ RM _ Ad copy.docx",
        "title": "MB RM Ad Copy Standards",
        "owner": "media-buying-lead",
        "artifact": "reference",
        "purpose": "Quick-reference headlines and primary text table with angles and risk levels.",
        "scope": "Meta ad copy only.",
        "trigger": "Writing or reviewing ad copy.",
        "inputs": ["Angle library"],
        "outputs": ["Approved copy variant selected"],
    },
    {
        "rel": "media-buying/ai-rm-ad-image-creation-sop.md",
        "src": "Media Buying/Media Buying (SOPs)/MB Creative Process/How to Use AI to Create Reverse Mortgage Ad Images.docx",
        "title": "AI RM Ad Image Creation SOP",
        "owner": "media-buying-lead",
        "artifact": "sop",
        "purpose": "Step-by-step AI image generation for compliant RM static ads.",
        "scope": "Static creatives; not UGC video.",
        "trigger": "New creative batch or testing new angles.",
        "inputs": ["Angle", "Brand/compliance rules", "Prompt templates"],
        "outputs": ["Approved image assets uploaded to ad account"],
    },
    {
        "rel": "media-buying/new-client-campaign-setup-sop.md",
        "src": "Media Buying/Media Buying (SOPs)/Ad Management/New Client Campaign Set-Up.docx",
        "title": "New Client Campaign Setup SOP",
        "owner": "media-buying-lead",
        "artifact": "sop",
        "purpose": "Build and launch Meta campaigns for a new client after kickoff.",
        "scope": "Campaign structure, pixel, budgets, initial ad sets.",
        "trigger": "Kickoff form submitted (A-Z Phase 5).",
        "inputs": ["FB/BM access", "Funnel URL", "Creative assets", "Tracker updated"],
        "outputs": ["Campaign ready for QA", "Fulfillment tracker current"],
    },
    {
        "rel": "media-buying/month-1-ad-account-management-sop.md",
        "src": "Media Buying/Media Buying (SOPs)/Ad Management/Month 1 Ad Account Management.docx",
        "title": "Month 1 Ad Account Management SOP",
        "owner": "media-buying-lead",
        "artifact": "sop",
        "purpose": "Daily/weekly media buying operations for the first month (testing phase).",
        "scope": "Month 1 post-launch; pairs with campaign phase blueprint.",
        "trigger": "Ads live through end of week 4 (Testing phase).",
        "inputs": ["Performance data", "Constraint SOP", "Phase blueprint"],
        "outputs": ["Optimization decisions logged in ClickUp"],
    },
    {
        "rel": "media-buying/perspective-funnel-setup-sop.md",
        "src": "Media Buying/Media Buying (SOPs)/MB Creative Process/Perspective Funnel Setup SOP.docx",
        "title": "Perspective Funnel Setup SOP",
        "owner": "media-buying-lead",
        "artifact": "sop",
        "purpose": "Configure Perspective funnel for client campaigns.",
        "scope": "Funnel tech setup.",
        "trigger": "Implementation phase after kickoff.",
        "inputs": ["Client branding", "Offer", "Qualification questions"],
        "outputs": ["Live funnel URL for ads"],
    },
    {
        "rel": "media-buying/ads-for-dummies-waizmedia-sop.md",
        "src": "Media Buying/Media Buying (SOPs)/SOP -- Ads For Dummies - WaizMedia.docx",
        "title": "Ads For Dummies WaizMedia SOP",
        "owner": "media-buying-lead",
        "artifact": "sop",
        "purpose": "Foundational Meta ads reference for Waiz media buyers.",
        "scope": "General MB education and troubleshooting primer.",
        "trigger": "New MB ramp or account basics review.",
        "inputs": [],
        "outputs": [],
    },
    {
        "rel": "client-marketing/rm-text-drip-2025.md",
        "src": "RM _ Text drip 2025.docx",
        "title": "RM Text Drip 2025",
        "owner": "client-success",
        "artifact": "script",
        "purpose": "Canonical SMS drip sequences for RM leads in GHL.",
        "scope": "Post-opt-in text nurture; align with bot and claimed-tag flow.",
        "trigger": "CRM workflow build or sequence refresh.",
        "inputs": ["Lead stage", "Disposition", "Claimed status"],
        "outputs": ["Configured GHL SMS workflows"],
        "related": ["[10-Day RM Drip Campaign](10-day-rm-drip-campaign.md)", "[How The WM AI Bot Works](../crm-architecture/how-wm-ai-bot-works.md)"],
    },
    {
        "rel": "client-marketing/10-day-rm-drip-campaign.md",
        "src": "Client Course Material/Skool Community/Templates/10-Day Reverse Mortgage Drip Campaign (Email + SMS).docx",
        "title": "10-Day RM Drip Campaign (Email + SMS)",
        "owner": "client-success",
        "artifact": "playbook",
        "purpose": "Ten-day email and SMS nurture templates for new RM leads.",
        "scope": "GHL workflows; may be adapted per client.",
        "trigger": "Sequence build during tech implementation.",
        "inputs": ["CRM custom values", "Compliance guardrails"],
        "outputs": ["Live 10-day workflow"],
    },
    {
        "rel": "client-marketing/rm-lead-nurture-drip-sequence.md",
        "src": "Client Course Material/Skool Community/Templates/Drip Sequence_ Reverse Mortgage Lead Nurture.docx",
        "title": "RM Lead Nurture Drip Sequence",
        "owner": "client-success",
        "artifact": "playbook",
        "purpose": "Extended nurture drip beyond initial speed-to-lead.",
        "scope": "Email/SMS; internal canonical — Skool links here.",
        "trigger": "Pipeline nurture or re-engagement build.",
        "inputs": ["Lead temperature", "Stage in lifecycle"],
        "outputs": ["Workflow templates in GHL"],
        "related": ["[Lead Nurture Playbook](../course-material/lead-nurture-playbook.md) (training — links here for copy)"],
    },
    {
        "rel": "client-marketing/rm-ad-playbook.md",
        "src": "Media Buying/RM Ad Playbook.docx",
        "title": "RM Ad Playbook",
        "owner": "media-buying-lead",
        "artifact": "playbook",
        "purpose": "Strategic playbook for RM Meta ad creative and campaign structure.",
        "scope": "Strategy layer; execution in media-buying/.",
        "trigger": "Campaign planning, creative strategy, client onboarding call prep.",
        "inputs": ["Client market", "Offer", "DNA docs"],
        "outputs": ["Creative brief direction"],
    },
    {
        "rel": "client-marketing/reverse-mortgage-ads-playbook.md",
        "src": "Media Buying/Media Buying (SOPs)/Reverse Mortgage Ads Playbook.docx",
        "title": "Reverse Mortgage Ads Playbook",
        "owner": "media-buying-lead",
        "artifact": "playbook",
        "purpose": "Operational RM ads playbook for Waiz-managed campaigns.",
        "scope": "Meta ads for clients.",
        "trigger": "New campaign or creative refresh.",
        "inputs": [],
        "outputs": [],
    },
    {
        "rel": "client-marketing/meta-andromeda-rm-rules.md",
        "src": "Media Buying/Media Buying (SOPs)/The New Rules of Meta Advertising - Andromeda (for Reverse Mortgages).docx",
        "title": "Meta Andromeda Rules For Reverse Mortgages",
        "owner": "media-buying-lead",
        "artifact": "doctrine",
        "purpose": "Platform rules and Andromeda-era constraints for RM advertisers.",
        "scope": "Meta policy and structure decisions.",
        "trigger": "Account issues, creative rejection, structural changes.",
        "inputs": [],
        "outputs": [],
    },
    {
        "rel": "client-success/post-launch-client-success-system.md",
        "src": "Client Success (SOPs)/SOP_ Post-Launch Client Success System.docx",
        "title": "Post-Launch Client Success System",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Operating system for CSM after ads go live.",
        "scope": "Check-ins, reviews, escalation paths.",
        "trigger": "Launch form submitted — ads live.",
        "inputs": ["Phase blueprint", "KPI standards"],
        "outputs": ["Scheduled reviews", "Documented account health"],
    },
    {
        "rel": "client-success/client-growth-stages.md",
        "src": "Client Success (SOPs)/Doctrine -- Client Growth Stages.docx",
        "title": "Client Growth Stages",
        "owner": "client-success",
        "artifact": "doctrine",
        "purpose": "Define client maturity stages and what Waiz expects at each.",
        "scope": "CS planning and QBRs.",
        "trigger": "Account reviews, expansion conversations.",
        "inputs": ["Performance history", "Tenure"],
        "outputs": ["Stage-appropriate goals and interventions"],
    },
    {
        "rel": "client-success/reset-call-sop.md",
        "src": "Client Success (SOPs)/The Reset Call.docx",
        "title": "Reset Call SOP",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Structured reset conversation when account is off-track.",
        "scope": "CS and founder escalation.",
        "trigger": "Persistent underperformance after constraint fixes.",
        "inputs": ["Constraint diagnosis", "Phase blueprint"],
        "outputs": ["Reset plan in ClickUp"],
    },
    {
        "rel": "client-success/client-success-daily-responsibilities.md",
        "src": "Client Success (SOPs)/Client Success Daily Responsibilites.docx",
        "title": "Client Success Daily Responsibilities",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Daily CS cadence and accountability.",
        "scope": "CS team daily ops.",
        "trigger": "Each business day.",
        "inputs": ["ClickUp queue", "Client Slack", "KPI dashboards"],
        "outputs": ["Touched accounts", "Logged actions"],
    },
    {
        "rel": "client-success/overdue-payments-and-ghosting-clients.md",
        "src": "Client Success (SOPs)/Overdue Payments & Ghosting Clients.docx",
        "title": "Overdue Payments And Ghosting Clients",
        "owner": "client-success",
        "artifact": "sop",
        "purpose": "Handle billing failures and disengaged clients.",
        "scope": "Billing and retention edge cases.",
        "trigger": "Failed payment or client unresponsive 14+ days.",
        "inputs": ["Billing status", "Last contact date"],
        "outputs": ["Documented resolution or churn"],
    },
    {
        "rel": "reverse-mortgage-dna/doctrine-reverse-mortgage.md",
        "src": "Reverse Mortgage DNA/Doctrine -- Reverse Mortgage -- 03.36.docx",
        "title": "Doctrine Reverse Mortgage",
        "owner": "founder",
        "artifact": "doctrine",
        "purpose": "Core RM product and market doctrine for all client copy and strategy.",
        "scope": "All fulfillment copy and training.",
        "trigger": "Any RM messaging, ads, or nurture draft.",
        "inputs": [],
        "outputs": [],
        "status": "active",
    },
    {
        "rel": "reverse-mortgage-dna/doctrine-rm-marketing.md",
        "src": "Reverse Mortgage DNA/Doctrine -- RM Marketing -- 04.26.docx",
        "title": "Doctrine RM Marketing",
        "owner": "founder",
        "artifact": "doctrine",
        "purpose": "Marketing doctrine specific to reverse mortgage client campaigns.",
        "scope": "Ads, funnels, nurture.",
        "trigger": "Creative or funnel decisions.",
        "inputs": [],
        "outputs": [],
        "status": "active",
    },
    {
        "rel": "reverse-mortgage-dna/intelligence-icp-rm.md",
        "src": "Reverse Mortgage DNA/Intelligence -- ICP RM -- 04.26.docx",
        "title": "Intelligence ICP RM",
        "owner": "founder",
        "artifact": "reference",
        "purpose": "Borrower ICP and archetypes for targeting and messaging.",
        "scope": "Audience and creative angle selection.",
        "trigger": "Campaign setup, creative brief.",
        "inputs": [],
        "outputs": [],
    },
    {
        "rel": "reverse-mortgage-dna/intelligence-rm-product.md",
        "src": "Reverse Mortgage DNA/Intelligence -- RM Product -- 04.26.docx",
        "title": "Intelligence RM Product",
        "owner": "founder",
        "artifact": "reference",
        "purpose": "Product facts and value framing for compliant copy.",
        "scope": "All client-facing education and ads.",
        "trigger": "Copy that mentions product mechanics.",
        "inputs": [],
        "outputs": [],
    },
    {
        "rel": "reverse-mortgage-dna/rm-compliance-guardrails.md",
        "src": "Archive/RM Compliance & Guardrails.docx",
        "title": "RM Compliance Guardrails",
        "owner": "founder",
        "artifact": "doctrine",
        "purpose": "Non-negotiable compliance rules for AI and human copy.",
        "scope": "All RM ads, SMS, email, bot scripts.",
        "trigger": "Any copy draft or review.",
        "inputs": [],
        "outputs": ["Compliant copy or explicit human review flag"],
        "status": "active",
    },
]

FOS_BODY = """## How To Use This Doc

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
| 7 | Launch | [A-Z Client Onboarding SOP](onboarding/a-z-client-onboarding-sop.md), [Onboarding To Launch Communication](onboarding/onboarding-to-launch-client-communication.md) | Launch form |

## Lead Engine (After Launch)

| Stage | Doc |
|-------|-----|
| Full map | [Fulfillment Lead Lifecycle](fulfillment-lead-lifecycle.md) |
| Ads & creative | [RM Ad Playbook](client-marketing/rm-ad-playbook.md), [Ad Copy And Angle Library](media-buying/ad-copy-angle-library-rm.md), [AI RM Ad Image Creation](media-buying/ai-rm-ad-image-creation-sop.md) |
| CRM & bot | [CRM Infrastructure](crm-architecture/crm-infrastructure.md), [WM AI Bot](crm-architecture/how-wm-ai-bot-works.md), [Claimed Tag](crm-architecture/how-claimed-tag-works.md) |
| Nurture | [RM Text Drip 2025](client-marketing/rm-text-drip-2025.md), [10-Day RM Drip](client-marketing/10-day-rm-drip-campaign.md), [RM Lead Nurture Drip](client-marketing/rm-lead-nurture-drip-sequence.md) |

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

- [RM Compliance Guardrails](reverse-mortgage-dna/rm-compliance-guardrails.md)
- [Doctrine Reverse Mortgage](reverse-mortgage-dna/doctrine-reverse-mortgage.md)
- [Doctrine RM Marketing](reverse-mortgage-dna/doctrine-rm-marketing.md)

## AI Quick Load Order

1. This doc
2. Compliance guardrails + angle library
3. Lifecycle + phase blueprint
4. Task-specific SOP (onboarding, MB, nurture, CS)

## Subfolder Index

| Folder | Role |
|--------|------|
| [onboarding/](onboarding/README.md) | Post-close through launch |
| [infrastructure/](infrastructure/README.md) | CRM hub |
| [crm-architecture/](crm-architecture/README.md) | GHL + bot specs |
| [client-marketing/](client-marketing/README.md) | Strategy, drips, playbooks |
| [media-buying/](media-buying/README.md) | Campaign execution SOPs |
| [client-success/](client-success/README.md) | Post-launch CS + troubleshooting |
| [reverse-mortgage-dna/](reverse-mortgage-dna/README.md) | Product, ICP, compliance |
| [course-material/](course-material/README.md) | Skool training (links to canonical) |
"""


def main() -> None:
    for item in CONVERSIONS:
        if item["rel"] == "fulfillment-operating-system.md":
            write_md(
                item["rel"],
                title=item["title"],
                owner=item["owner"],
                artifact=item["artifact"],
                source_rel="(synthesized)",
                purpose=item["purpose"],
                scope=item["scope"],
                trigger=item["trigger"],
                inputs=item["inputs"],
                outputs=item["outputs"],
                status=item.get("status", "draft"),
                review=item.get("review", "monthly"),
                body_text=FOS_BODY,
            )
            continue

        src_path = BASE / item["src"]
        text = docx_text(src_path)
        write_md(
            item["rel"],
            title=item["title"],
            owner=item["owner"],
            artifact=item["artifact"],
            source_rel=item["src"],
            purpose=item["purpose"],
            scope=item["scope"],
            trigger=item["trigger"],
            inputs=item.get("inputs", []),
            outputs=item.get("outputs", []),
            status=item.get("status", "draft"),
            review=item.get("review", "monthly"),
            related=item.get("related"),
            body_text=text,
        )


if __name__ == "__main__":
    main()
