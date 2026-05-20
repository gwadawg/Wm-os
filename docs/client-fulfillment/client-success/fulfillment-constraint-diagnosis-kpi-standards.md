---
title: Fulfillment Constraint Diagnosis And KPI Standards
domain: client-fulfillment
owner: client-success
status: active
last_updated: 2026-05-20
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Fulfillment Constraint Diagnosis & KPI standards.docx
artifact_type: kpi
---

# Fulfillment Constraint Diagnosis And KPI Standards

## Purpose

KPI tiers and layer owners for fulfillment diagnosis.

## Scope

Companion to constraint troubleshooting SOP.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **client-success**.

## When To Use

Use per source document and related operating docs.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).

## Metrics

- See [KPIs](../../kpis/README.md) as metrics are formalized.

## Operating Content

## WAIZ MEDIA
## Constraint Diagnosis & Performance Recovery Guide
## Full-Funnel Diagnostic Reference  ·  Internal Use  ·  Confidential
## Ads  →  Landing Page  →  Call Center  →  Client (LO)
This document is the operational bible for diagnosing underperformance in any Waiz Media client account. Every metric, every benchmark, and every solution path is documented here so that the Media Buyer, AI Agent (Manus), Operations (Christian), and Client Success (Laura) can identify constraints and act without ambiguity — and without unnecessary escalation to the Founder.

⚠️  Rule: Never implement a fix without first diagnosing the correct layer. The wrong fix wastes time and can actively make performance worse. Use this document to diagnose first, then act.

## 1.  Layer 1 — Ad Performance Metrics
These metrics live inside Meta (Facebook/Instagram) Ads Manager. If any of these are off, you are either spending money wrong, burning your audience, or attracting the wrong people. Fix these before diagnosing anything downstream.

## 1.1  Click-Through Rate (CTR)
## Owner: Media Buyer (Gabriela)
## Formula: Clicks ÷ Impressions × 100
CTR tells you whether your creative is compelling enough to interrupt a scroll. A falling CTR is almost always the first signal of creative fatigue — the audience has seen the ad too many times and is tuning it out. In the reverse mortgage space, CTR is especially important because the product carries pre-existing negative associations; a weak hook means the prospect never gets to hear the value proposition.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 0.8%
Creative has stopped working. Swap immediately. Do not wait for CPQL to confirm — you already have confirmation. Pull the ad, test a new hook and format.

## ⚠️ Below KPI
## 0.8% – 1.2%
Underperforming. Schedule a creative refresh within 7 days. Review whether the hook leads with an outcome (not the product name). Check frequency — fatigue may already be setting in.

## ✅ At KPI
## 1.3% – 2.5%
Healthy. Creative is resonating with the audience. Continue monitoring weekly. No action needed unless CPQL starts rising.

## 🏆 Above KPI
## > 2.5%
Excellent engagement. Document the hook, format, and audience. Use this as a creative template for other accounts.

Solutions & Levers:

Test a new hook — lead with an emotional outcome, not the product name ('Eliminate your mortgage payment' vs 'Reverse Mortgage Info')

Switch creative format — if running image, test video; if running talking-head, test testimonial style

Revisit the opening 3 seconds of any video — this determines whether the viewer continues

Check that ad copy speaks to a single archetype (Security-Seeker, Strategic Retiree, Squeezed Homeowner, Legacy Planner) — diluted messaging kills CTR

## 1.2  Ad Frequency
## Owner: Media Buyer (Gabriela)
## Formula: Total Impressions ÷ Reach
Frequency measures how many times the average person in your target audience has seen your ad. Too low and you haven't built enough familiarity to convert. Too high and you're burning your audience — driving up CPL and CPQL while CTR collapses. This is the canary in the coal mine for audience saturation.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## > 4.0
Audience is fatigued. Creative must be refreshed or audience must be expanded immediately. Continuing to spend at this frequency is burning budget and poisoning retargeting data.

## ⚠️ Below KPI
## 3.0 – 4.0
Approaching fatigue. Prepare a new creative rotation within 7 days. Monitor CTR closely — it will start declining before CPQL reflects it.

## ✅ At KPI
## 1.5 – 3.0
Healthy range. The audience is seeing the brand enough to build familiarity without burning out. This is the sweet spot for trust-building in a long-cycle product like reverse mortgages.

## 🏆 Above KPI
## < 1.5
Flag as potentially too low. May indicate audience is too broad, budget is too low for meaningful reach, or campaign just launched. Confirm with CPL trends before acting.

Solutions & Levers:

## Expand the target audience — if radius is tight (under 30km equivalent), widen it
## Rotate to a new creative — different format, different hook, different archetype angle
## Introduce retargeting audiences to serve different creative to warm audiences vs cold
## Increase budget to reduce frequency dilution across a broader reach pool
## 1.3  Cost Per Lead (CPL)
## Owner: Media Buyer (Gabriela)
## Formula: Total Ad Spend ÷ Total Leads Generated
CPL measures what it costs to get one person to opt into the funnel. It is a secondary metric — always evaluate CPL alongside CPQL and the Opt-In Rate. A low CPL with a low Opt-In Rate means your ad is compelling but your landing page is losing people. A low CPL with a high CPQL gap means you're getting cheap leads that can't be qualified.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## > $25
Critically high. Immediate creative and targeting review required. Check for audience saturation (frequency), ad creative age, and whether the landing page is receiving traffic but converting poorly.

## ⚠️ Below KPI
## $20 – $24.99
Above target. Begin optimization. Review creative fatigue, audience overlap, and whether targeting is too narrow. Check if landing page load speed is an issue.

## ✅ At KPI
## $15 – $19.99
Within acceptable operational range. Monitor CPL alongside CPQL to ensure lead quality holds as you optimize for cost.

## 🏆 Above KPI
## < $15
Strong acquisition cost. Before scaling budget, validate CPQL and Lead-to-Qual % to confirm lead quality is holding. Cheap leads that don't qualify are not a win.

Solutions & Levers:

Simplify the landing page — if using a high-intent page with heavy copy, test a low-intent opt-in-only page to reduce friction

Review creative performance at the ad level — often one ad is dragging the overall CPL up

Broaden the audience if targeting is too narrow (audience too small = Facebook charges premium CPMs)

Reduce qualification questions on the landing page if CPL is high and intent signals in other metrics look healthy

## 1.4  Cost Per Qualified Lead (CPQL) — Primary Ad KPI
## Owner: Media Buyer (Gabriela)
## Formula: Total Ad Spend ÷ Total Qualified Leads
CPQL is the most important metric at the ad layer. A lead is only 'qualified' when it meets the pre-qualification criteria set by the call center. This metric reveals whether you are buying leads or buying qualified prospects. CPL tells you what you're spending — CPQL tells you what you're actually getting. If CPQL is significantly higher than CPL, the funnel has a quality leak.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## > $35
Campaign needs immediate intervention. Either creative is attracting wrong audience (targeting misalignment) or landing page is not filtering intent. Do not continue spending at this rate without a documented fix plan.

## ⚠️ Below KPI
## $30 – $34.99
Under target. Review creative fatigue and audience alignment. Begin a structured optimization plan with a 7-day resolution window.

## ✅ At KPI
## $20 – $29.99
At standard. Campaign is performing within acceptable range. Continue monitoring. No escalation required.

## 🏆 Above KPI
## < $20
Outperforming. Document the creative, targeting, and landing page configuration. Replicate on other accounts.

Solutions & Levers:

If CPL is fine but CPQL is high: targeting or messaging is attracting unqualified people — review creative angle vs. ICP

## Add or sharpen qualifying questions on the landing page to filter intent before opt-in
Review disqualification reasons from the call center — a pattern in why leads are not qualifying points directly to the ad targeting or messaging

Switch archetype — if the campaign is attracting curiosity-seekers rather than motivated prospects, shift to a more specific pain-point angle

## 2.  Layer 2 — Landing Page & Opt-In Performance
The landing page is the bridge between your ad and your lead. A high CTR with a high CPL almost always means the landing page is the constraint — people are clicking but not converting. This layer is invisible in most reporting dashboards, which is exactly why it gets missed.

## 2.1  Opt-In Rate (Landing Page Conversion Rate)
## Owner: Media Buyer (Gabriela)
## Formula: Leads Submitted ÷ Landing Page Visitors × 100
Opt-In Rate is the missing link between ad performance and lead volume. If CTR is strong and CPC is low, but CPL is still high, the opt-in rate is almost certainly the problem. These benchmarks are intentionally conservative — the qualification friction built into Waiz funnels is designed to filter intent, which naturally suppresses raw opt-in rate in exchange for higher lead quality. A higher opt-in rate is not always better: if it climbs well above 30%, qualification may be too soft and CPQL will suffer.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 10%
Critical. The page is rejecting nearly all clicks. Immediate audit required — check headline message match with the ad, page load speed, number of form fields, and whether qualification questions are creating too much pre-opt-in friction. This level of drop-off is a page problem, not an ad problem.

## ⚠️ Below KPI
## 10% – 14.9%
Below target. The page is losing a significant portion of motivated clicks. Diagnose one variable at a time: start with the headline (message match), then form field count, then qualification question placement. Consider whether questions should move to post-opt-in.

## ✅ At KPI
## 15% – 29.9%
At standard. This is the expected range for a Waiz funnel with intentional qualification friction. The page is filtering correctly. Monitor alongside Lead-to-Qual % — if both are healthy, the funnel is working as designed.

## 🏆 Above KPI
## > 30%
Above standard. Strong conversion given the friction in place. Validate that lead quality is holding — if CPQL is also at KPI, the funnel is optimized. If CPQL is rising, qualification may be too soft and additional friction should be added.

Solutions & Levers:

Run a headline audit — the landing page headline must directly continue the promise made in the ad (message match)

Test low-intent vs. high-intent page: a stripped-down opt-in-only page reduces friction and typically improves opt-in rate for cold traffic

## Reduce form fields to the minimum needed — every extra field reduces conversion
Check page load speed — delays over 3 seconds cause significant drop-off with the 62+ demographic

## Remove distractions — navigation links, pop-ups, or competing CTAs all reduce opt-in rate
Review qualification questions — too many pre-opt-in questions kill conversion; move qualifying to post-opt-in if necessary

## 2.2  Lead-to-Qualified Rate
## Owner: Media Buyer (Gabriela) + CSR Manager (Laura)
## Formula: Qualified Leads ÷ Total Leads × 100
This ratio is the quality report card for the entire top of funnel. If raw leads are coming in but fewer than 50% qualify, the ad creative or targeting is misaligned — it is attracting the wrong people. This is not a call center problem. Before concluding the call center is struggling, confirm this ratio is healthy.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 40%
Critical quality failure. Ads are generating largely unqualified traffic. This is a targeting or messaging mismatch — not a call center problem. Escalate to media buyer. Review audience profile against the four ICP archetypes.

## ⚠️ Below KPI
## 40% – 49%
Below target. Review audience targeting and funnel copy for alignment with the qualified prospect profile. Check disqualification reason patterns in the CRM.

## ✅ At KPI
## 50% – 65%
Acceptable. Campaign is attracting a reasonable mix of qualified prospects. Normal operating range.

## 🏆 Above KPI
## > 65%
Excellent targeting precision. Audience and messaging are highly aligned with the qualified prospect profile.

Solutions & Levers:

Pull disqualification reasons from ClickUp/CRM — patterns (wrong age, no home equity, already has a RM) point directly to targeting fixes

Sharpen the ICP archetype in the creative — generic senior-focused messaging attracts a broader, less qualified pool

## Add pre-qualifying questions to the landing page (age, homeownership status, approximate equity)
Review whether a specific creative or audience is driving the unqualified leads — kill that ad set first

## 3.  Layer 3 — Call Center Performance
The call center turns qualified leads into booked appointments. A healthy ad layer with a broken call center is the most common silent killer in this system. The leads are there — they're just not being converted. Diagnose this layer independently from the ad layer.

## 3.1  Contact Rate (Pickup Rate)
## Owner: CSR Manager (Laura)
## Formula: Leads Where Contact Was Made ÷ Total Dials Attempted × 100
Contact Rate measures how often the team actually reaches a live person when dialing. A low contact rate is almost always a phone number spam issue or a dial cadence problem — not a lead quality problem. This is a technical and operational issue, not a messaging issue.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 20%
Critical. Phone numbers are likely spam-flagged. Check the call tool (Hot Prospector or equivalent) number health status immediately. Do not continue burning leads with flagged numbers.

## ⚠️ Below KPI
## 20% – 29%
Below target. Rotate phone numbers. Review dial timing windows — best contact windows are 8–10am and 4–6pm prospect local time. Ensure dial cadence is running correctly.

## ✅ At KPI
## 30% – 45%
Acceptable. Normal operational range for this industry and demographic.

## 🏆 Above KPI
## > 45%
Strong contact rate. Validate that lead data quality is contributing. Document dial timing and number rotation practices.

Solutions & Levers:

Rotate phone numbers immediately if spam-flagged — obtain new numbers in the correct local area code

## Audit dial timing — shift outreach to 8–10am and 4–6pm local prospect time
Check speed-to-lead: first contact attempt must be within 5 minutes of form submission — after 10 minutes, pickup probability drops dramatically

## Ensure AI follow-up sequences (text/email) are running correctly alongside voice dials
Review dial cadence — leads should be contacted at least once per day for 5 days before moving to a cold nurture stage

## 3.2  Booking Rate — Primary Call Center KPI
## Owner: CSR Manager (Laura)
## Formula: Appointments Booked ÷ Total Leads Contacted × 100
Booking Rate is the call center's single most important output. This is not just about volume of dials — it is about the quality of the conversation once contact is made. A qualified lead who picks up the phone should be converted to a booked appointment at a high rate. If contact rate is healthy but booking rate is not, the issue is in the script, objection handling, or SDR execution.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## 0% – 20%
Critical. Immediate audit of scripts, objection handling, and SDR execution required. Pull call recordings. Identify whether the issue is rapport-building, handling the 'reverse mortgage' stigma, or closing on the appointment. Escalate to Founder same day.

## ⚠️ Below KPI
## 20% – 24.9%
Below target. Review script quality, objection handling sequences, and lead contact timing. Set a 5-business-day resolution window. Pull sample call recordings for coaching.

## ✅ At KPI
## 25% – 30%
At standard. Normal operating range. Continue monitoring for consistency week over week.

## 🏆 Above KPI
## > 30%
Above standard. Document what is working — scripts, timing, objection responses. Use as the baseline reference.

Solutions & Levers:

Pull call recordings and audit the first 60 seconds — most failed bookings break down at the opening or at the first objection

Review objection handling for the top 3 objections in the reverse mortgage space: 'the bank takes your house,' 'I need to think about it,' 'I'm not interested'

Ensure SDRs are not leading with the product name — frame the call around the outcome first

Check whether the AI bot (between SDR contacts) is warming or cooling the lead — review AI message sequences

Confirm calendar availability is open — leads cannot book if no slots exist in the next 10 days

## 4.  Layer 4 — Client (LO) Performance
These metrics measure what happens after a lead is booked. Waiz Media does not directly control these — but we are accountable for the quality of what we hand off, and low performance here always triggers an investigation of the layers above.

## 4.1  Show Rate — Primary Client KPI
## Owner: Client Success (Laura)
## Formula: Appointments Attended ÷ Total Appointments Booked × 100
Show Rate is the bridge between the call center and the LO. A booked appointment that doesn't show is a complete waste of every upstream dollar spent. Low show rate is most often caused by insufficient confirmation and reminder sequences, but it can also indicate a mismatch between what was promised on the booking call and what the appointment delivers.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 51%
Critical. More than half of booked appointments are not showing. Audit confirmation sequences, appointment reminders, and whether the LO is fulfilling their follow-up responsibilities. Check if dispositions are being logged — a no-show that isn't logged doesn't trigger re-engagement.

## ⚠️ Below KPI
## 51% – 55%
Below target. Review the confirmation cadence: immediate confirmation text, 24-hour reminder, 4-hour reminder, 30-minute reminder. Confirm all four are triggering correctly in GHL.

## ✅ At KPI
## 56% – 70%
At standard. Normal operating range. Continue monitoring.

## 🏆 Above KPI
## > 70%
Above standard. Document the LO's confirmation and prep practices as a best-practice case.

Solutions & Levers:

Audit reminder sequence in GHL — all four touchpoints must fire: immediate, 24hr, 4hr, 30min

Confirm the LO is reviewing lead notes before the call — unprepared LOs produce cold conversations that lead to no-shows on the next call

## Ensure no-shows are being dispositioned immediately — delayed disposition delays re-engagement
Add a commitment question on the booking page: 'Are you 100% committed to attending this consultation?' with a yes/no hard gate

Check whether appointments are being booked too far out — the further out, the lower the show rate; prioritize next-3-day availability

Review whether the AI bot is being left on after booking — per the SOP, the AI turns off at booking and drip campaigns take over; confirm this is happening correctly

## 4.2  Close Rate
## Owner: Client Success (Laura) — reported by LO
## Formula: Deals Closed ÷ Appointments Attended × 100
Close Rate measures the LO's conversion on live appointments. Waiz Media does not control this metric — but a consistently low close rate signals either a lead quality issue that needs investigation upstream, or an LO execution gap that requires coaching. If the LO is closing below 10%, investigate lead quality first before concluding it is a sales problem.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## < 10%
LO is struggling to convert. First, verify lead quality is matching the ICP — pull the qualification notes for attended appointments and check alignment. If lead quality is sound, the issue is in the LO's consultation process.

## ⚠️ Below KPI
## 10% – 19%
Below target. Flag for a coaching conversation. Check whether the issue is sales skill, lead quality, or appointment quality. Review whether the LO is completing the pre-appointment prep steps.

## ✅ At KPI
## 20% – 35%
Standard range. LO is converting at an acceptable rate.

## 🏆 Above KPI
## > 35%
Strong performance. Consider showcasing as a case study. Document the LO's call framework.

Solutions & Levers:

Confirm the LO is reviewing the SDR call notes and lead details before each appointment

Share the ICP archetypes with the LO — knowing which archetype they're speaking to changes the entire consultation tone

Offer Module 3 (Waiz Sales Call training) as a coaching resource if close rate is persistently below 20%

If close rate is low and show rate is fine, pull a sample of attended appointments and audit the consultation quality

## 4.3  Cost Per Qualified Conversation (CQPCONV) — Full-Funnel KPI
## Owner: Client Success (Laura)
## Formula: Total Ad Spend ÷ Total Qualified Conversations That Occurred (Showed Appointments)
CQPCONV is the most important single number in the entire system. It synthesizes every layer — ad efficiency, landing page conversion, call center booking rate, and show rate — into one figure. A CQPCONV that is healthy means the whole machine is working. A CQPCONV that is broken means at least one layer is failing, and you need to isolate which one using the sections above.

## Tier
## Range / Value
## What It Means + What To Do
## 🚨 911 — Critical
## > $225
Systemic failure across the funnel. At least one layer is critically underperforming. Work through Sections 1–4 in order to identify which layer is creating the drag. Notify Founder same day.

## ⚠️ Below KPI
## $150 – $225
Something in the funnel is creating drag. Identify which layer — ads, landing page, call center booking rate, or show rate — is the bottleneck. Address within 5 business days.

## ✅ At KPI
## $80 – $149.99
Acceptable range. Normal operating range given CPL baseline and funnel conversion rates. Continue monitoring.

## 🏆 Above KPI
## < $80
Strong full-funnel performance. Document the ad setup, call center execution, and LO confirmation process for replication.

Solutions & Levers:

Use the Root Cause Decision Tree (Section 5) to identify which layer is causing a high CQPCONV

Do not optimize one layer in isolation — fixing CPL while ignoring show rate will not move CQPCONV

If all individual metrics appear at KPI but CQPCONV is still high, flag as a data/attribution issue and escalate to Founder — do not implement fixes blindly

## 5.  Root Cause Decision Tree
When an account is flagged as 911 or Below KPI, use this decision tree to identify the root cause before acting. Match the condition that describes your current situation and follow the prescribed response. All root cause investigations must be documented in ClickUp.

## Condition (Last 2 Weeks)
## Label As
## Likely Root Cause
## First Actions
## CTR is high + CPC is low, but CPL is still high
## Landing Page
Opt-in rate is the constraint — clicks are happening but the landing page is losing them

Run opt-in rate audit. Test low-intent page. Check headline message match with ad.

## CPL is at KPI but CPQL is Below KPI
## Lead Quality
Cheap leads but wrong audience. Targeting or messaging attracting unqualified people.

Pull disqualification reasons. Review creative angle vs. ICP archetypes. Tighten qualification questions.

## CPL is Below KPI AND CPQL is Below KPI
## Lead Cost
Overall acquisition cost is too high. Audience too narrow or creative underperforming.

Rotate creatives. Fix targeting. Audit GHL automations for correct lead reporting.

## CPQL at KPI but Booking/Contact Rate is Below KPI
## Call Center
Leads are qualified but call center is not converting. Dial, script, or AI issue.

Audit dial cadence. Check AI (Closebot) status. Pull call recordings for script review.

## CPQL at KPI + Booking Rate at KPI + Show Rate < 56%
## Show Rate
Appointments booking but prospects not showing. Confirmation or prep failure.

Audit GHL reminder sequences. Check if dispositions are being logged. Review LO follow-up process.

## All individual metrics at KPI but CQPCONV > $225
## Data Issue
Attribution or reporting problem. The numbers don't add up — do not make operational changes.

Do not act. Escalate to Founder (Gabriel) immediately. Likely a tracking or attribution issue.

## 6.  Quick Reference: All Benchmarks at a Glance
## Metric
## 🚨 911
## ⚠️ Below KPI
## ✅ At KPI
## 🏆 Above KPI
## Owner
## CTR
## < 0.8%
## 0.8–1.2%
## 1.3–2.5%
## > 2.5%
## Media Buyer
## Frequency
## > 4.0
## 3.0–4.0
## 1.5–3.0
## < 1.5*
## Media Buyer
## CPL
## $25+
## $20–$24.99
## $15–$19.99
## < $15
## Media Buyer
## CPQL
## $35+
## $30–$34.99
## $20–$29.99
## < $20
## Media Buyer
## Opt-In Rate
## < 10%
## 10–14.9%
## 15–29.9%
## > 30%
## Media Buyer
## Lead-to-Qual %
## < 40%
## 40–49%
## 50–65%
## > 65%
## Media Buyer
## Contact Rate
## < 20%
## 20–29%
## 30–45%
## > 45%
## CSR Mgr
## Booking Rate
## 0–20%
## 20–24.9%
## 25–30%
## > 30%
## CSR Mgr
## Show Rate
## < 51%
## 51–55%
## 56–70%
## > 70%
Client Suc.

## Close Rate
## < 10%
## 10–19%
## 20–35%
## > 35%
Client Suc.

## CQPCONV
## > $225
## $150–$225
## $80–$149
## < $80
Client Suc.

* Frequency < 1.5 is flagged as potentially too low — audience may be too broad or budget insufficient. Not a positive signal by default. Confirm with CPL trends.

## 7.  Escalation Rules
## Scenario
## Who Acts First
Escalate to Founder If...

## Any metric hits 911 tier
## Ops + Client Success
Always — notify Gabriel same day. No exceptions.

## CQPCONV > $225 with all other metrics passing
## Client Success flags it
Immediately — data/attribution issue requiring Founder investigation.

## Ad creative swap needed
## Media Buyer executes
Only if repeated rejections or strategy change is needed.

## Booking Rate Below KPI for 2+ weeks
## CSR Manager audits
If no improvement after 5 business days.

## Show Rate Below KPI for 2+ weeks
## Client Success contacts LO
If LO is unresponsive or fix requires system changes.

## GHL automation failure affecting lead delivery
## Ops (Christian) diagnoses
Before any fix — all GHL changes require Founder approval.

## Frequency > 4.0 on any ad set
## Media Buyer refreshes creative
Only if fix requires budget reallocation or audience strategy change.

## WAIZ MEDIA  ·  Constraint Diagnosis Guide  ·  Internal Confidential  ·  March 2026
Questions or benchmark updates: escalate to Gabriel Goertzen (Founder) before modifying any standard.

## Related Docs

- None yet.

## Open Questions

- [x] Spine approved 2026-05-20 (`status: active`).
