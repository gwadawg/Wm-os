---
title: Client Launch Kit SOP
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-11
review_cycle: monthly
shareability: internal-fulfillment
artifact_type: sop
audience:
  - team
content_layer: canonical
product: general
delivery_group: onboarding
methodology_sources:
  - docs/client-fulfillment/onboarding/a-z-client-onboarding-sop.md
  - docs/client-fulfillment/fulfillment-lead-lifecycle.md
  - docs/client-fulfillment/shareability-boundaries.md
---

# Client Launch Kit SOP

## Purpose

Give every launching client a tangible, Waiz-branded leave-behind on the Launch Call — a PDF map of what is live, how to run Week 1, and where their files live — plus a living Drive folder for swipe files and URLs that change.

## Scope

| Included | Excluded |
|----------|----------|
| Per-client Launch Kit PDF (account map, not a playbook dump) | A new call type — this is the existing Launch Call |
| Client-safe Drive swipe pack + resource folder | Internal swipe research, Mr. Waiz ad rows, MB SOPs |
| Launch Call agenda that walks the PDF | Post-launch weekly CS calls → [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md) |
| RM and DSCR (self-serve or Laura) | Pricing, internal KPIs, campaign-phase numbers |

## Owner

CSM (same as the Launch Call). Fulfillment / assigned owner still submits the Launch Form.

## Trigger

QA is complete and the Launch Call is on the calendar. Start the kit **24–48 hours before** the call (same window as the pre-launch Slack in the [Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md)).

Do not start before QA. The PDF must describe what is actually live.

## Inputs

- Kickoff Form facts (offer, market, who dials, product path)
- QA confirmation that each build piece is done
- Live URLs: funnel, CRM, calendar, ads, Slack, Skool
- Product path: `reverse-mortgage` or `dscr` (Mr. Waiz prefills from the client's vertical)
- Who works new leads: **Waiz** (call center for RM / Laura for DSCR) or **client** (LO / VA — gets playbooks). Mr. Waiz prefills from the service program: `core` → Waiz, `lead_gen` → client.
- Client Drive folder (created at OB Form)
- [Client Launch Kit Template](../../templates/client-launch-kit-template.md)

## Outputs

- Branded Launch Kit PDF generated in Mr. Waiz (versioned, `launch_kit` submission on the client file)
- Same PDF in the client Drive folder
- Client-safe swipe pack staged in the same folder
- Client walked the PDF on the Launch Call
- PDF link + folder link sent to the client Slack channel from Mr. Waiz before hangup
- Launch Form submitted (account treated as live)

## Tools

- **Mr. Waiz → Client Roster → Kit** — the execution path. Prefills from the client file, validates the intake, renders the branded PDF server-side, stores every version, and posts the links to Slack. No Cursor, no local scripts.
- Kickoff / QA / Launch Forms (Mr. Waiz)
- Client Google Drive folder
- Slack (client channel — sent from Mr. Waiz)
- Fallback only: `python3 scripts/build-launch-kit.py` — branded render (wraps minimax-pdf). Use when Mr. Waiz is down or a one-off kit needs copy that is not in the template yet.
- [Sample kit](assets/launch-kit-sample/client-launch-kit-sample.pdf) — visual reference only

### Where the copy lives

The template in this repo is the **source of truth for every word** in the kit. Mr. Waiz mirrors it as typed constants in `src/lib/launch-kit/copy/` with a `TEMPLATE_VERSION` stamp on every generated PDF. Copy changes go **Wm-os first, Mr. Waiz second**: edit the template + sample `content.json` here, then port to Mr. Waiz and bump `TEMPLATE_VERSION`. Never edit Mr. Waiz copy without updating this repo.

## Process

1. **Open the kit.** Mr. Waiz → Client Roster → client row → **Kit**. Available once Kickoff is complete (GHL mapping + OB recording). The wizard prefills product, who works leads, contact, company, go-live, funnel, CRM, and Drive root from the client file.
2. **Confirm the variant.** Product (Reverse mortgage / DSCR) × who works leads (Waiz call center / Laura vs. LO / VA). This picks the Week 1 page and the resource index. Call Center legacy clients require you to pick the product.
3. **Fill What's live.** Every URL from QA. Mark a property *Not part of this account* if it truly does not exist — never leave a guessed link. Funnel and CRM can never be N/A. Slack channel name is optional but recommended.
4. **Operator setup.** CSM name, who works leads (as a sentence subject), speed standard exactly as sold (leave blank if none was sold — the kit will say "as agreed on your kickoff"), market.
5. **Shareability gate.** Review step — the copy is fixed, so the gate is about the fields: no internal names, no numbers you did not sell, no repo paths. Save a draft if a URL is still pending.
6. **Generate.** Mr. Waiz renders the PDF, stores it as `v{n}` (regenerate = new version, nothing overwritten), logs a `launch_kit` submission on the client file, and posts a download link to the ops Slack channel. Open the PDF and eyeball every page.
7. **Stage the Drive folder.** Under the existing client Drive folder, create `Launch Kit/` with the subfolders in **Drive pack**. Download the PDF from Mr. Waiz and put it in `01-Launch-PDF`. Put only client-safe creatives in `03-Swipe-and-Ads`. Paste the `Launch Kit/` folder link back into the wizard (What's live → Launch Kit folder) and regenerate if it was blank.
8. **Pre-launch Slack.** Send the existing pre-launch touchpoint. Do not send the PDF yet unless the client asks — the call is the first walkthrough.
9. **Run the Launch Call off the PDF.** Follow **Launch Call agenda**. Screen-share the PDF. Click the live URLs. Get verbal approval on what was built.
10. **Send to client channel before hangup.** In the wizard's version list, click **Send to client** on the version you walked. Mr. Waiz posts a 7-day download link + the Drive folder link to the client's Slack channel and stamps the version as sent. Confirm they can open both. Drive is the permanent home; the Slack link expires.
11. **Launch Form.** Submit when go-live is scheduled and the kit is delivered. The Launch checklist shows a notice if no kit exists. → [A-Z Step 7](a-z-client-onboarding-sop.md#step-7--launch-call--launch-form)

### Launch Call agenda

Walk the PDF in order. Do not open internal SOPs on the call.

| # | PDF section | Job of the beat |
|---|-------------|-----------------|
| 1 | Cover + Welcome | Why they have this document. It is their map, not homework. Show "What's inside." |
| 2 | What's live | Click each URL. Confirm they can log in. Get approval on the build. |
| 3 | How the engine works | One-page client lens — ads → funnel → CRM → first contact → calendar. No build specs. |
| 4 | Week 1 operator checklist | Who dials, speed standard, BAMFAM, what to do when a lead hits. Role-play one inbound if time. |
| 5 | Resource index | Point at the playbooks. Do not teach them on this call. |
| 6 | Creative + swipe pack | Open the Drive folder. What they may use vs what Waiz runs. |
| 7 | First 30 days | Testing-phase frame in client language. Protect Week 1 motivation. |
| 8 | Who to ping | Slack for urgent; weekly call for everything else. |
| 9 | Close | Questions, approval, send PDF + folder, confirm next CS check-in. |

### Drive pack

```text
{Client Drive}/Launch Kit/
  01-Launch-PDF/          ← this client's PDF only
  02-Links/               ← optional shortcuts; URLs also live in the PDF
  03-Swipe-and-Ads/       ← their live ads + approved examples they can use
  04-Recordings/          ← launch-call recording after the call (optional)
```

**Client-safe swipe pack** = this client's live ads and approved examples they can reference or remix. Not the OS swipe library, not `creative-research/swipes/`, not Mr. Waiz rows.

### Shareability gate (required before generate)

The PDF is `paying-client`. The Drive pack is `paying-client`. This SOP is `internal-fulfillment`.

**Never put in the PDF or Drive pack**

- A-Z onboarding, Kickoff internals, QA checklists
- Media-buying SOPs, campaign setup, Andromeda ops
- GHL / bot / tag architecture
- Drip copy libraries and executable sequences
- [Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md) (translate expectations; do not attach)
- Internal swipe research or competitor ads we have not cleared for the client
- Pricing, internal KPI targets, phase numbers

**May put in the PDF**

- Their live URLs
- Client-lens engine map (from [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md), not how we build it)
- Week 1 operator rules in plain language
- Links to `paying-client` or `lo-course` playbooks (resource index only)
- Drive folder link for swipes
- First-30-days frame in client language
- Who to ping

→ [Shareability Boundaries](../shareability-boundaries.md)

### Product routing

| Path | Week 1 operator page | Resource index |
|------|----------------------|----------------|
| Reverse mortgage | LO / VA / call center as sold | Nurture playbook, RM ads playbook, HQ lead acquisition, BAMFAM |
| DSCR — self-serve | LO or VA works every lead; drip is the safety net | [DSCR Self-Serve Lead Response](../dscr-dna/playbook-dscr-self-serve-lead-nurture.md) |
| DSCR — Laura | Laura owns SMS / booking; LO owns consults | Do not also hand them the self-serve playbook as the daily system |

## Decision Rules

- If a live URL is missing after QA, delay the kit and ping the build owner. Do not ship a PDF with guessed links.
- If the client asks for “all the swipe files,” give the Drive pack — not the internal library.
- If they want a bookmarkable web page later, that is a v2 HTML hub. Do not substitute it for this PDF on the Launch Call.
- Per-client PDFs live in Mr. Waiz Storage (every version) and in the client Drive folder. Do not commit client PDFs to git. The [sample PDF](assets/launch-kit-sample/client-launch-kit-sample.pdf) is the only visual reference in the repo.
- The record of what shipped is the `launch_kit` submission on the Mr. Waiz client file (intake, version, template version, sent-to-client timestamp). No separate OS memory file is needed.
- If the client changes product path or who works leads after launch, regenerate from Mr. Waiz — the kit is available through `active` status.

## Quality Bar

- Every URL in the PDF opens on the day of the call.
- PDF section order matches the template. No extra internal sections.
- One section per page. No table rows, bullets, or callouts orphaned onto an otherwise empty page.
- Client can open the PDF and the Drive folder from Slack before the call ends.
- Expectations language does not promise volume, CPL, or closings in Week 1.
- Client-facing copy follows the product compliance guardrails ([RM](../reverse-mortgage-dna/rm-compliance-guardrails.md) / [DSCR](../dscr-dna/dscr-compliance-guardrails.md)).

## Escalation

- Missing build piece after QA → build owner, then CSM lead if it slips the call.
- Client cannot access CRM / ads / calendar on the call → pause go-live; fix access before Launch Form.
- Client rejects the build → do not submit Launch Form; log the delta and re-QA.
- Mr. Waiz Kit generate fails or Slack post fails → retry once; if still failing, render with the fallback script from the template and post the PDF manually. Report the error in ops Slack so it gets fixed.

## Metrics

- Kit ready ≥ 24 hours before the Launch Call
- PDF + Drive link sent before hangup
- Launch Form submitted the same day the account is scheduled live

## Related Docs

### Prerequisites (read before this SOP)

- [A-Z Client Onboarding SOP](a-z-client-onboarding-sop.md) — gated flow; this kit is a Step 7 output
- [Shareability Boundaries](../shareability-boundaries.md) — what may leave the building
- [Client Launch Kit Template](../../templates/client-launch-kit-template.md) — intake + section order + variant matrix; copy source of truth mirrored in Mr. Waiz
- Mr. Waiz `docs/CLIENT_ONBOARDING.md` § 3b Launch Kit — wizard, API, storage, Slack behaviour

### Handoffs (what happens after this SOP)

- [Client Success Slack Touchpoint Playbook](onboarding-to-launch-client-communication.md) — launch-day and Month 1 written cadence
- [Post-Launch Client Success System](../client-success/post-launch-client-success-system.md) — 30-day call cadence

### Reference (used during execution)

- [Fulfillment Lead Lifecycle](../fulfillment-lead-lifecycle.md) — client-lens engine map
- [Campaign Phase Performance Blueprint](../client-success/campaign-phase-performance-blueprint.md) — internal only; translate, do not attach
- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [Client playbooks catalog](../client-playbooks/catalog.md) — paying-client resource index
