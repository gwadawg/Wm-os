---
title: "Client CRM Lead Response Playbook (Leads-Only / DIY)"
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-09-28
review_cycle: quarterly
shareability: paying-client
artifact_type: playbook
audience:
  - client
content_layer: canonical
product: general
delivery_group: lead-nurture
methodology_sources:
  - docs/client-fulfillment/client-marketing/playbook-nurture-framework.md
delivery:
  - github
  - team-drive
---

# Client CRM Lead Response Playbook (Leads-Only / DIY)

> **North star:** When a Waiz lead enters your CRM, you know exactly what happens automatically, what you need to do manually, and how your updates help us send you better leads.

## Purpose

Client-facing launch training for **leads-only clients** using the Waiz CRM (LeadConnector / GHL). Covers the full lead journey: notification → drip → response → pipeline → tags → fields → notes → outcome reporting. This is the source doc for the shareable PDF playbook delivered at client launch.

## Scope

| Included | Excluded |
|----------|----------|
| CRM walkthrough for leads-only clients | Product-specific sales training (RM / DSCR playbooks) |
| Drip behavior, pipeline stages, tags, custom fields, notes | Waiz internal automation builds and workflow specs |
| Outcome reporting back to Waiz | Ad account and campaign management |
| Daily CRM routine + what not to touch | Appointment/call-center flows |

## Owner

Client Success. Delivered by CSM at client launch.

## Trigger

Use this playbook when:

- A leads-only (DIY nurture) client launches and needs CRM training
- A client asks how tags, pipeline stages, or reporting work
- A CSM prepares a launch kit for a new leads-only client

## Inputs

- Client CRM sub-account live with pipeline, drip, and notification settings configured
- Client login credentials issued
- Reporting form (outcome form) link for the client
- Screenshots captured from the client's actual sub-account (or neutral demo account)

## Outputs

- Client can respond to leads, move pipeline stages, tag correctly, fill fields, take notes, and report outcomes without CSM hand-holding
- Shareable PDF exported and delivered at launch

---

## Section format (used for every PDF section)

Each section in the PDF follows this four-block layout:

1. **What you're looking at** — plain-English explanation of the screenshot
2. **What happens automatically** — what the CRM/drip handles
3. **What you need to do** — exact action steps
4. **Why it matters** — speed-to-lead, organization, reporting, lead quality

---

## Playbook sections

### 1. Welcome / What This Playbook Covers

- What the client receives: leads, automated first-touch SMS drip, pipeline, contact records
- What Waiz handles: lead capture, CRM setup, drip, campaign optimization
- What the client handles: calling, replying, qualifying, tagging, updating outcomes
- `[GRAPHIC: "You + Waiz" responsibility split — two-column visual]`

### 2. CRM Overview: What You'll See Inside

- Left navigation tour: Conversations, Contacts, Opportunities, Calendars
- Desktop vs. mobile
- **LeadConnector mobile app** (call leads from anywhere):
  - iOS: [Lead Connector on the App Store](https://apps.apple.com/us/app/lead-connector/id1564302502)
  - Android: [Lead Connector on Google Play](https://play.google.com/store/apps/details?id=com.LeadConnector)
  - Log in with the same credentials as desktop
- `[SCREENSHOT: CRM home / left nav]`

### 3. What Happens When a New Lead Comes In

- Lead submits the ad form → contact is created in the CRM instantly
- Client receives a notification (mobile push / SMS / email as configured)
- Lead appears in the pipeline under `New Lead` — screenshot: [pipeline-new-lead.png](assets/client-crm-lead-response/pipeline-new-lead.png)
- **Best practice: call within 5 minutes** — speed-to-lead is the single biggest contact-rate lever
- `[GRAPHIC (custom): lead lifecycle map — Form → CRM → Drip → Response → You → Outcome]`

### 4. How the Automated Drip Works

- The lead receives the first SMS within ~5 minutes of inquiry
- **Messaging adapts to intent** — the sequence changes based on what the lead expressed on the form, so follow-ups match what they actually asked about
- **Messages are sent on behalf of your assistant**, not you — this avoids putting words in your mouth or representing you incorrectly before you've spoken with the lead
- The drip's only job is to start a conversation — it is not a replacement for calling
- The drip continues on schedule until the lead replies
- Reference screenshot (behind-the-scenes view): [drip-workflow.png](assets/client-crm-lead-response/drip-workflow.png)
- `[GRAPHIC (custom): simplified drip flow — intent branch → assistant SMS touches → lead replies → drip stops]`

### 5. What Happens When a Lead Responds

- The moment a lead replies, the drip stops automatically — no double-texting
- The opportunity is dispositioned to `Contacted` automatically
- From this point forward, **every reply is on you** — go to the **Conversations** tab (left nav) to read and respond, so the full history stays in one thread — screenshot: [conversations-tab.png](assets/client-crm-lead-response/conversations-tab.png)
- Works the same in the LeadConnector mobile app
- Reply fast: response within minutes keeps the conversation alive

### 6. Using the Pipeline to Stay Organized

- Pipeline lives under **Opportunities** in the left nav
- Leads enter at `New Lead`; automation moves them to `Contacted` on reply
- Client moves everything after that — keep stages current as status changes
- Stage definitions table (one line per stage): `New Lead`, `Contacted`, `Hot`, `Nurturing (3–6 Months)`, `Short to Close` `[TO FILL: confirm final stage list per client pipeline]`
- **You can add your own stages** in pipeline settings (Opportunities → Pipelines) if you want more granularity — just don't rename or delete the stages we set up
- Screenshot: [pipeline-new-lead.png](assets/client-crm-lead-response/pipeline-new-lead.png)

### 7. Lead Tags: The Only Two You Need

> Tags are simple on purpose. You only ever add two.

| Tag | When to add it | What it does |
|-----|----------------|--------------|
| `claimed` | You had a real conversation with the lead | Tracks your contact rate and lead intent — this is how we measure lead quality together |
| `kill-switch` | You want ALL automation stopped for this contact | Immediately turns off every automated message for that lead |

- Everything else — proposal, submitted, funded, disqualified — is **not a tag**. Those are reported through the Client Log form (next section)
- `[GRAPHIC (custom): two tag chips with one-line meanings — "claimed = I talked to them" / "kill-switch = stop all automation"]`

### 8. Contact Records: Custom Fields, Notes, and Lead Details

- **Contact info:** phone, email, source, form answers — auto-filled from the ad form
- **Custom fields:** left panel of the contact record — update as you learn more (timeline, amounts, details relevant to qualification)
- **Notes:** every real conversation leaves a note — call summary, objections, next step
- Rule of thumb: *use the fields we set up first; ask Waiz before creating new fields* (keeps data clean)
- `[SCREENSHOT: contact record with custom fields panel]`
- `[SCREENSHOT: notes tab with example note]`

### 9. Reporting Outcomes: The Client Log Form

All deal outcomes are reported through the **Client Log form** — not tags, not pipeline moves. Two event types:

**Conversion** — log when a lead reaches `Proposal`, `Submitted`, or `Funded`:

- Search the lead by name, pick the event type, enter loan size and date
- One submit per loan — same house with two loans = two submits
- Screenshot: [client-log-conversion.png](assets/client-crm-lead-response/client-log-conversion.png)

**Disqualified** — log when a lead doesn't qualify, with the reason:

- Reasons: LTV, FICO, Low Property Value, Seasoning, Low Income, Other — plus an optional notes field for context
- Screenshot: [client-log-disqualified.png](assets/client-crm-lead-response/client-log-disqualified.png)

Why it matters (two things):

1. We trace outcomes back to specific ads — kill what produces bad leads, scale what produces good ones
2. Cleaner outcome data lets us optimize campaigns toward the types of leads that actually turn into business

- `[TO FILL: Client Log form link / where the client accesses it]`
- `[GRAPHIC (custom): feedback loop — Your logged outcomes → Waiz optimization → Better leads]`

### 10. Daily CRM Routine

| When | Do this |
|------|---------|
| Morning | Check `New Lead` stage + unread conversations |
| After every call | Add a note, update tag, set next step |
| End of day | Clear unread messages, update pipeline stages |
| Weekly | Review `Contacted` → `Funded` stages; complete any missed outcome forms |

- `[GRAPHIC: daily routine checklist card]`

### 11. What Not To Touch

Do not edit without checking with Waiz first:

- Workflows / automations
- Pipeline structure (stage names, order)
- Core tags (renaming breaks tracking)
- Lead source fields
- SMS templates in the drip
- Integration settings
- User permissions

### 12. Troubleshooting / FAQs

- "I didn't get a notification" → check app notification permissions + `[TO FILL: notification settings path]`
- "The drip is still texting after the lead replied" → flag to Waiz immediately
- "I can't find a lead" → search Contacts by name/phone; check pipeline filters
- "Can I add my own leads?" → `[TO FILL: policy on manually added contacts]`
- `[TO FILL: CSM support contact / Slack channel]`

---

## Decision rules

| Condition | Action |
|-----------|--------|
| Lead replies to drip | Drip stops automatically; client takes over all replies in Conversations tab |
| Client has a real conversation | Add `claimed` tag |
| Client wants all automation off for a contact | Add `kill-switch` tag |
| Lead not qualified | Log **Disqualified** in Client Log form with reason |
| Proposal sent / submitted / funded | Log **Conversion** in Client Log form (one submit per loan) |
| Lead unreachable after full dial cadence | Move to nurture stage |
| Client wants a new custom field or pipeline stage | Fields: ask Waiz first. Stages: may add own in pipeline settings; never rename/delete Waiz stages |

## Quality bar

- Product-neutral language throughout — no reverse mortgage or DSCR references in the client PDF
- Every section pairs a screenshot or graphic with the four-block format
- No internal Waiz automation details (workflow names, bot specs) in the client-facing PDF
- Screenshots come from the client's sub-account or a clean demo account — no other clients' data visible

## Metrics

| Metric | Target direction | Notes |
|--------|------------------|-------|
| Speed-to-lead (first client touch) | Down (< 5 min) | Primary behavior this playbook drives |
| Contact rate (`claimed` tag %) | Up | Tracked via tags |
| Client Log completion rate (conversions + DQs) | Up | Feeds campaign optimization |
| Pipeline hygiene (leads in correct stage) | Up | CSM spot-checks |

## Related docs

### Methodology (from OS)

| Doc | What we reuse |
|-----|----------------|
| [Nurture Framework](playbook-nurture-framework.md) | Speed-to-lead and follow-up principles |
| [Lead Nurture Playbook — Waiz Meta Stack](playbook-lead-nurture.md) | Full-stack (bot+drip) counterpart for DFY clients |

### Execution (do not duplicate here)

| Doc | Role |
|-----|------|
| `[TO FILL: leads-only drip execution doc]` | Drip copy this playbook describes |

## Open questions

- [ ] Confirm final pipeline stage list for the DIY pipeline (screenshot shows: New Lead, Contacted, Hot, Nurturing (3–6 Months), Short to Close)
- [ ] Client Log form link + how clients access it (bookmark, sent per-lead, portal?)
- [ ] Contact-rate metric: does `claimed` % have a target we quote to clients?
- [ ] Notification channels configured by default (push / SMS / email)
- [ ] Screenshots still needed: contact record custom fields panel, notes tab
- [ ] CSM support contact for the FAQ section

---

**Reference example:** [playbook-lead-nurture.md](playbook-lead-nurture.md) · **Format spec:** [PLAYBOOK-FORMAT.md](../client-playbooks/PLAYBOOK-FORMAT.md)
