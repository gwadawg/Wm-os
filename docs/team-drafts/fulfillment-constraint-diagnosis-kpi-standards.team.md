---
team_title: "Fulfillment KPI Standards"
team_role: client_success
source_repo_path: "docs/client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md"
approved: true
draft_updated: 2026-05-28
---

<!-- Edit below. Publish uses Google Doc template (Objection Categories styles). -->

**WAIZ MEDIA**

*Client Success Team  |  Internal Use Only  |  2026*

# Overview

KPI tiers and layer owners for fulfillment diagnosis.

- Who: Client-Success
- When: When this procedure applies
**Before You Start**

Use per source document and related operating docs.

Companion to constraint troubleshooting SOP.

# How To Do It

## Owner

## Ads → Landing Page → Call Center → Client

- This document is the operational bible for diagnosing underperformance in any Waiz Media client account.
- Every metric, every benchmark, and every solution path is documented here so that the Media Buyer, AI Agent (Manus), Operations (Christian), and Client Success (Laura) can identify
⚠️  Rule: Never implement a fix without first diagnosing the correct layer. The wrong fix wastes time and can actively make performance worse. Use this document to diagnose first, then act.

## 1. Layer 1 — Ad Performance Metrics

These metrics live inside Meta (Facebook/Instagram) Ads Manager. If any of these are off, you are either spending money wrong, burning your audience, or attracting the wrong people. Fix these before diagnosing anything downstream.

## Formula: Clicks ÷ Impressions × 100

- CTR tells you whether your creative is compelling enough to interrupt a scroll.
- A falling CTR is almost always the first signal of creative fatigue — the audience has seen the ad too many times and is tuning it out.
- In the reverse mortgage space, CTR is especially important because the product carries pre-existing negative associations; a weak hook means the prospect never gets to hear the val
## < 0.8%

Creative has stopped working. Swap immediately. Do not wait for CPQL to confirm — you already have confirmation. Pull the ad, test a new hook and format.

## 0.8% – 1.2%

Underperforming. Schedule a creative refresh within 7 days. Review whether the hook leads with an outcome (not the product name). Check frequency — fatigue may already be setting in.

## 1.3% – 2.5%

Healthy. Creative is resonating with the audience. Continue monitoring weekly. No action needed unless CPQL starts rising.

## > 2.5%

Excellent engagement. Document the hook, format, and audience. Use this as a creative template for other accounts.

**Solutions & Levers**

Test a new hook — lead with an emotional outcome, not the product name ('Eliminate your mortgage payment' vs 'Reverse Mortgage Info')

Switch creative format — if running image, test video; if running talking-head, test testimonial style

Revisit the opening 3 seconds of any video — this determines whether the viewer continues

Check that ad copy speaks to a single archetype (Security-Seeker, Strategic Retiree, Squeezed Homeowner, Legacy Planner) — diluted messaging kills CTR

## Formula: Total Impressions ÷ Reach

Frequency measures how many times the average person in your target audience has seen your ad. Too low and you haven't built enough familiarity to convert. Too high and you're burning your audience — driving up CPL and CPQL while CTR collapses. This is the canary in the coal mine for audience saturation.

## > 4.0

Audience is fatigued. Creative must be refreshed or audience must be expanded immediately. Continuing to spend at this frequency is burning budget and poisoning retargeting data.

## 3.0 – 4.0

Approaching fatigue. Prepare a new creative rotation within 7 days. Monitor CTR closely — it will start declining before CPQL reflects it.

## 1.5 – 3.0

Healthy range. The audience is seeing the brand enough to build familiarity without burning out. This is the sweet spot for trust-building in a long-cycle product like reverse mortgages.

## < 1.5

Flag as potentially too low. May indicate audience is too broad, budget is too low for meaningful reach, or campaign just launched. Confirm with CPL trends before acting.

**Solutions & Levers**

## Formula: Total Ad Spend ÷ Total Leads Generated

- CPL measures what it costs to get one person to opt into the funnel. It is a secondary metric — always evaluate CPL alongside CPQL and the Opt-In Rate.
- A low CPL with a low Opt-In Rate means your ad is compelling but your landing page is losing people.
- A low CPL with a high CPQL gap means you're getting cheap leads that can't be qualified.
## > $25

Critically high. Immediate creative and targeting review required. Check for audience saturation (frequency), ad creative age, and whether the landing page is receiving traffic but converting poorly.

## $20 – $24.99

Above target. Begin optimization. Review creative fatigue, audience overlap, and whether targeting is too narrow. Check if landing page load speed is an issue.

## $15 – $19.99

Within acceptable operational range. Monitor CPL alongside CPQL to ensure lead quality holds as you optimize for cost.

## < $15

Strong acquisition cost. Before scaling budget, validate CPQL and Lead-to-Qual % to confirm lead quality is holding. Cheap leads that don't qualify are not a win.

**Solutions & Levers**

Simplify the landing page — if using a high-intent page with heavy copy, test a low-intent opt-in-only page to reduce friction

Review creative performance at the ad level — often one ad is dragging the overall CPL up

Broaden the audience if targeting is too narrow (audience too small = Facebook charges premium CPMs)

Reduce qualification questions on the landing page if CPL is high and intent signals in other metrics look healthy

## Formula: Total Ad Spend ÷ Total Qualified Leads

- CPQL is the most important metric at the ad layer. A lead is only 'qualified' when it meets the pre-qualification criteria set by the call center.
- This metric reveals whether you are buying leads or buying qualified prospects. CPL tells you what you're spending — CPQL tells you what you're actually getting.
- If CPQL is significantly higher than CPL, the funnel has a quality leak.
## > $35

Campaign needs immediate intervention. Either creative is attracting wrong audience (targeting misalignment) or landing page is not filtering intent. Do not continue spending at this rate without a documented fix plan.

## $30 – $34.99

Under target. Review creative fatigue and audience alignment. Begin a structured optimization plan with a 7-day resolution window.

## $20 – $29.99

At standard. Campaign is performing within acceptable range. Continue monitoring. No escalation required.

## < $20

Outperforming. Document the creative, targeting, and landing page configuration. Replicate on other accounts.

**Solutions & Levers**

If CPL is fine but CPQL is high: targeting or messaging is attracting unqualified people — review creative angle vs. ICP

## Add Or Sharpen Qualifying Questions On The Landing Pa…

Review disqualification reasons from the call center — a pattern in why leads are not qualifying points directly to the ad targeting or messaging

Switch archetype — if the campaign is attracting curiosity-seekers rather than motivated prospects, shift to a more specific pain-point angle

## 2. Layer 2 — Landing Page & Opt-in Performance

The landing page is the bridge between your ad and your lead. A high CTR with a high CPL almost always means the landing page is the constraint — people are clicking but not converting. This layer is invisible in most reporting dashboards, which is exactly why it gets missed.

## Formula: Leads Submitted ÷ Landing Page Visitors × 100

- Opt-In Rate is the missing link between ad performance and lead volume. If CTR is strong and CPC is low, but CPL is still high, the opt-in rate is almost certainly the problem.
- These benchmarks are intentionally conservative — the qualification friction built into Waiz funnels is designed to filter intent, which naturally suppresses raw opt-in rate in exc
- A higher opt-in rate is not always better: if it climbs well above 30%, qualification may be too soft and CPQL will suffer.
## < 10%

LO is struggling to convert. First, verify lead quality is matching the ICP — pull the qualification notes for attended appointments and check alignment. If lead quality is sound, the issue is in the LO's consultation process.

## 10% – 14.9%

Below target. The page is losing a significant portion of motivated clicks. Diagnose one variable at a time: start with the headline (message match), then form field count, then qualification question placement. Consider whether questions should move to post-opt-in.

## 15% – 29.9%

At standard. This is the expected range for a Waiz funnel with intentional qualification friction. The page is filtering correctly. Monitor alongside Lead-to-Qual % — if both are healthy, the funnel is working as designed.

## > 30%

Above standard. Document what is working — scripts, timing, objection responses. Use as the baseline reference.

**Solutions & Levers**

Pull call recordings and audit the first 60 seconds — most failed bookings break down at the opening or at the first objection

Review objection handling for the top 3 objections in the reverse mortgage space: 'the bank takes your house,' 'I need to think about it,' 'I'm not interested'

Ensure SDRs are not leading with the product name — frame the call around the outcome first

Check whether the AI bot (between SDR contacts) is warming or cooling the lead — review AI message sequences

Confirm calendar availability is open — leads cannot book if no slots exist in the next 10 days

## Reduce Form Fields To The Minimum Needed — Every Extr…

Check page load speed — delays over 3 seconds cause significant drop-off with the 62+ demographic

## Remove Distractions — Navigation Links, Pop-ups, Or C…

Review qualification questions — too many pre-opt-in questions kill conversion; move qualifying to post-opt-in if necessary

## Formula: Qualified Leads ÷ Total Leads × 100

This ratio is the quality report card for the entire top of funnel. If raw leads are coming in but fewer than 50% qualify, the ad creative or targeting is misaligned — it is attracting the wrong people. This is not a call center problem. Before concluding the call center is struggling, confirm this ratio is healthy.

## < 40%

Critical quality failure. Ads are generating largely unqualified traffic. This is a targeting or messaging mismatch — not a call center problem. Escalate to media buyer. Review audience profile against the four ICP archetypes.

## 40% – 49%

Below target. Review audience targeting and funnel copy for alignment with the qualified prospect profile. Check disqualification reason patterns in the CRM.

## 50% – 65%

Acceptable. Campaign is attracting a reasonable mix of qualified prospects. Normal operating range.

## > 65%

Excellent targeting precision. Audience and messaging are highly aligned with the qualified prospect profile.

**Solutions & Levers**

Pull disqualification reasons from ClickUp/CRM — patterns (wrong age, no home equity, already has a RM) point directly to targeting fixes

Sharpen the ICP archetype in the creative — generic senior-focused messaging attracts a broader, less qualified pool

## Add Pre-qualifying Questions To The Landing Page

Review whether a specific creative or audience is driving the unqualified leads — kill that ad set first

## 3. Layer 3 — Call Center Performance

The call center turns qualified leads into booked appointments. A healthy ad layer with a broken call center is the most common silent killer in this system. The leads are there — they're just not being converted. Diagnose this layer independently from the ad layer.

## Formula: Leads Where Contact Was Made ÷ Total Dials A…

Contact Rate measures how often the team actually reaches a live person when dialing. A low contact rate is almost always a phone number spam issue or a dial cadence problem — not a lead quality problem. This is a technical and operational issue, not a messaging issue.

## < 20%

Critical. Phone numbers are likely spam-flagged. Check the call tool (Hot Prospector or equivalent) number health status immediately. Do not continue burning leads with flagged numbers.

## 20% – 29%

Below target. Rotate phone numbers. Review dial timing windows — best contact windows are 8–10am and 4–6pm prospect local time. Ensure dial cadence is running correctly.

## 30% – 45%

Acceptable. Normal operational range for this industry and demographic.

## > 45%

Strong contact rate. Validate that lead data quality is contributing. Document dial timing and number rotation practices.

**Solutions & Levers**

Rotate phone numbers immediately if spam-flagged — obtain new numbers in the correct local area code

## Audit Dial Timing — Shift Outreach To 8–10am And 4–6p…

Check speed-to-lead: first contact attempt must be within 5 minutes of form submission — after 10 minutes, pickup probability drops dramatically

## Ensure Ai Follow-up Sequences (text/email) Are Runnin…

Review dial cadence — leads should be contacted at least once per day for 5 days before moving to a cold nurture stage

## Formula: Appointments Booked ÷ Total Leads Contacted …

- Booking Rate is the call center's single most important output. This is not just about volume of dials — it is about the quality of the conversation once contact is made.
- A qualified lead who picks up the phone should be converted to a booked appointment at a high rate.
- If contact rate is healthy but booking rate is not, the issue is in the script, objection handling, or SDR execution.
## 0% – 20%

Critical. Immediate audit of scripts, objection handling, and SDR execution required. Pull call recordings. Identify whether the issue is rapport-building, handling the 'reverse mortgage' stigma, or closing on the appointment. Escalate to Founder same day.

## 20% – 24.9%

Below target. Review script quality, objection handling sequences, and lead contact timing. Set a 5-business-day resolution window. Pull sample call recordings for coaching.

## 25% – 30%

At standard. Normal operating range. Continue monitoring for consistency week over week.

## 4. Layer 4 — Client (lo) Performance

These metrics measure what happens after a lead is booked. Waiz Media does not directly control these — but we are accountable for the quality of what we hand off, and low performance here always triggers an investigation of the layers above.

## Formula: Appointments Attended ÷ Total Appointments B…

- Show Rate is the bridge between the call center and the LO. A booked appointment that doesn't show is a complete waste of every upstream dollar spent.
- Low show rate is most often caused by insufficient confirmation and reminder sequences, but it can also indicate a mismatch between what was promised on the booking call and what t
## < 51%

Critical. More than half of booked appointments are not showing. Audit confirmation sequences, appointment reminders, and whether the LO is fulfilling their follow-up responsibilities. Check if dispositions are being logged — a no-show that isn't logged doesn't trigger re-engagement.

## 51% – 55%

Below target. Review the confirmation cadence: immediate confirmation text, 24-hour reminder, 4-hour reminder, 30-minute reminder. Confirm all four are triggering correctly in GHL.

## 56% – 70%

At standard. Normal operating range. Continue monitoring.

## > 70%

Client Suc.

## Ensure No-shows Are Being Dispositioned Immediately —…

Add a commitment question on the booking page: 'Are you 100% committed to attending this consultation?' with a yes/no hard gate

Check whether appointments are being booked too far out — the further out, the lower the show rate; prioritize next-3-day availability

Review whether the AI bot is being left on after booking — per the SOP, the AI turns off at booking and drip campaigns take over; confirm this is happening correctly

## Formula: Deals Closed ÷ Appointments Attended × 100

- Close Rate measures the LO's conversion on live appointments.
- Waiz Media does not control this metric — but a consistently low close rate signals either a lead quality issue that needs investigation upstream, or an LO execution gap that requi
- If the LO is closing below 10%, investigate lead quality first before concluding it is a sales problem.
## 10% – 19%

Below target. Flag for a coaching conversation. Check whether the issue is sales skill, lead quality, or appointment quality. Review whether the LO is completing the pre-appointment prep steps.

## 20% – 35%

Standard range. LO is converting at an acceptable rate.

## > 35%

Client Suc.

## Formula: Total Ad Spend ÷ Total Qualified Conversatio…

- CQPCONV is the most important single number in the entire system.
- It synthesizes every layer — ad efficiency, landing page conversion, call center booking rate, and show rate — into one figure.
- A CQPCONV that is healthy means the whole machine is working.
- A CQPCONV that is broken means at least one layer is failing, and you need to isolate which one using the sections above.
## > $225

Systemic failure across the funnel. At least one layer is critically underperforming. Work through Sections 1–4 in order to identify which layer is creating the drag. Notify Founder same day.

## $150 – $225

Something in the funnel is creating drag. Identify which layer — ads, landing page, call center booking rate, or show rate — is the bottleneck. Address within 5 business days.

## $80 – $149.99

Acceptable range. Normal operating range given CPL baseline and funnel conversion rates. Continue monitoring.

## < $80

Client Suc.

- Frequency < 1.5 is flagged as potentially too low — audience may be too broad or budget insufficient. Not a positive signal by default. Confirm with CPL trends.
## 5. Root Cause Decision Tree

When an account is flagged as 911 or Below KPI, use this decision tree to identify the root cause before acting. Match the condition that describes your current situation and follow the prescribed response. All root cause investigations must be documented in ClickUp.

## Landing Page

Opt-in rate is the constraint — clicks are happening but the landing page is losing them

Run opt-in rate audit. Test low-intent page. Check headline message match with ad.

## Lead Quality

Cheap leads but wrong audience. Targeting or messaging attracting unqualified people.

Pull disqualification reasons. Review creative angle vs. ICP archetypes. Tighten qualification questions.

## Lead Cost

Overall acquisition cost is too high. Audience too narrow or creative underperforming.

Rotate creatives. Fix targeting. Audit GHL automations for correct lead reporting.

## Call Center

Leads are qualified but call center is not converting. Dial, script, or AI issue.

Audit dial cadence. Check AI (Closebot) status. Pull call recordings for script review.

## Show Rate

Appointments booking but prospects not showing. Confirmation or prep failure.

Audit GHL reminder sequences. Check if dispositions are being logged. Review LO follow-up process.

## Data Issue

Attribution or reporting problem. The numbers don't add up — do not make operational changes.

Do not act. Escalate to Founder (Gabriel) immediately. Likely a tracking or attribution issue.

## Who Acts First

Escalate to Founder If...

## Ops + Client Success

Always — notify Gabriel same day. No exceptions.

## Client Success Flags It

Immediately — data/attribution issue requiring Founder investigation.

## Media Buyer Executes

Only if repeated rejections or strategy change is needed.

## Csr Manager Audits

If no improvement after 5 business days.

## Client Success Contacts Lo

If LO is unresponsive or fix requires system changes.

## Ops (christian) Diagnoses

Before any fix — all GHL changes require Founder approval.

## Media Buyer Refreshes Creative

Only if fix requires budget reallocation or audience strategy change.

## Waiz Media · Constraint Diagnosis Guide · Internal Co…

Questions or benchmark updates: escalate to Gabriel Goertzen (Founder) before modifying any standard.

## Done Right Looks Like

## When To Get Help

Questions, pricing, or exceptions → escalate to Gabriel (Client-Success team).

## Related Procedures

- Client Performance Diagnostic Rulebook (coming soon)
> **📌 REMEMBER**
>
> If this doc conflicts with what you heard elsewhere, follow this doc and tell Gabriel.


<div align="center">

*Waiz Media | Internal Document | Confidential*

</div>
