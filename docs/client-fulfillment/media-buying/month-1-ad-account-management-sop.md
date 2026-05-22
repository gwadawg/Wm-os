---
title: Month 1 Ad Account Management SOP
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-21
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Media Buying/Media Buying (SOPs)/Ad Management/Month 1 Ad Account Management.docx
artifact_type: sop
---

# Month 1 Ad Account Management SOP

## Purpose

Daily/weekly media buying operations for the first month (testing phase).

## Scope

Month 1 post-launch; pairs with campaign phase blueprint.

## Trigger

Ads live through end of week 4 (Testing phase).

## Inputs

- Performance data
- Constraint SOP
- Phase blueprint

## Outputs

- Optimization decisions logged in ClickUp

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when applicable.

## Operating Content

Operational Standard

Operational Standard

From Launch to Scale — Loan Officer Lead Generation

Who this is for: Any team member managing a Meta ad account for a loan officer. Daily budget: $35–$150. Max acceptable CPL: $25. Goal: Qualified leads, not just volume.

Core Philosophy

Three principles govern every decision in this account.

Stability is the only real currency at low spend. Before scaling, the campaign must be stable. A consistent $50/day campaign is worth more than a volatile $150/day one.

The algorithm is your partner, not your enemy. Meta's system learns what "a good result" looks like from the signals you give it. Every unnecessary edit, premature kill, or aimless new ad is noise that slows down learning.

Test like a scientist, not a gambler. Every test has a Control (what we know works) and a Variable (one new thing being tested). We measure success by the overall health of the campaign, not just the CPL of the new ad.

Decision Rules

Reference these rules every time you make a decision. No exceptions.

The 2x CPL Rule: Never kill an ad before it has spent at least $50 (2x the $25 target CPL). An ad that has spent $30 with no leads has not been fairly tested. One that has spent $60 with no leads has

Metric

Threshold

What It Means

What to Do

CTR (Link)

Below 0.8%

Hook Failure — the ad is not stopping the scroll

Revisit the first 3 seconds of video or the headline

0.8% – 1.5%

Average performance

Monitor; do not kill yet

Above 1.5%

Strong hook

Protect this ad; let it run

### Cpl

At or below $25

On target

Scale the budget

$25 – $35

Marginal

Check CTR and landing page CVR

Above $35

Failing

Identify the root cause before killing

High CTR + High CPL

—

Landing page or lead form is broken

The ad works; fix the post-click experience

High CPM + Low CTR

—

Audience mismatch

The ad is reaching the wrong people

Frequency

Above 2.5 in < 7 days

Creative fatigue beginning

Prepare new creative; do not kill yet

Above 3.5

Active fatigue

Introduce new creative immediately

The 4PI Framework: How to Read Any Ad

The 4PI framework is the lens used to diagnose what role each ad is playing in the funnel. Read these four metrics together — not in isolation.

4PI Metric

What It Tells You

Spend

What the algorithm believes will produce results. Concentrated spend over multiple days = a true winner.

Frequency

The temperature of the audience. Near 1.0 = reaching new people (TOFU). Above 1.4 = reaching warm, intent-heavy people (BOFU).

### Cpm

The cost of distribution. Low CPM = the platform rewards the ad. High CPM = competitive, high-intent audience.

### Cpl

The business outcome. Is it at, above, or below the $25 target?

How to read the combination:

4PI Pattern

Funnel Stage

What It Means

High Spend / Low Frequency / Low CPM / Weak CPL

### Tofu

Reaching new people; they are not ready to convert yet

Moderate Spend / Mid Frequency / Mid CPM / Improving CPL

### Mofu

Bridging curiosity and intent

Low Spend / High Frequency / High CPM / Strong CPL

### Bofu

Closing warm, intent-heavy leads

A healthy account has all three layers active. Most new accounts only have BOFU creative and wonder why they cannot scale. You cannot scale BOFU without TOFU feeding the top.

How to Check Trends in Meta Ads Manager

When this SOP says "check if CPL is trending downward" or "check if frequency is rising," here is exactly how to do it.

Checking CPL Trend (Line Chart)

Go to Ads Manager → Campaigns tab

Click the name of the campaign you want to analyze

In the right-side panel, click "View Charts"

In the chart panel, click the metric dropdown and select "Cost per Lead"

Set the date range to "Last 7 Days"

The resulting line chart shows CPL for each day. Read it as follows:

What You See

What It Means

What to Do

Line moving downward over time

Algorithm is learning; CPL is improving

Stay patient; do not intervene

Line volatile but trending down

Normal early-stage fluctuation

Continue monitoring

Line flat or moving upward

Campaign is not improving

Refer to Decision Rules to diagnose

Checking Frequency Trend

Go to Ads Manager → Ads tab

Click the Columns dropdown → select "Customize Columns"

Search for and add "Frequency" to your view

Set the date range to "Last 7 Days"

Read frequency at the ad level. If any ad is above 2.5 in under 7 days, begin preparing new creative.

Checking Spend Concentration

Go to Ads Manager → Ads tab

Sort the "Amount Spent" column from highest to lowest

Look at the top 1–2 ads. Are they consuming more than 70% of the daily budget?

If yes, and their CPL is high, that is your biggest offender. If yes, and their CPL is strong, that is your winner — protect it.

Finding the Biggest Offender (Week 2 Action)

Go to Ads Manager → Ads tab

Set date range to "Last 7 Days"

Sort by "Amount Spent" (highest to lowest)

Look at the top spender. Check its "Cost per Lead"

If it has the highest spend AND the worst CPL → this is the biggest offender. Turn it off.

Week 1

WEEK 1 — Build the Foundation

Goal: Launch a stable campaign structure, gather initial data, and resist the urge to make changes.

Step 1: Campaign Setup

Create a single campaign with this exact structure:

Setting

Value

Campaign Type

Leads

Budget Type

Campaign Budget Optimization (CBO)

Daily Budget

Clients daily budget ($35–$150)

Number of Ad Sets

1

Audience

Broad (State only)

Why warm audiences first? At low budgets, cold-traffic broad audiences slow down learning. Warm audiences give the algorithm faster, more reliable signals — meaning you exit the learning phase sooner and with better data.

Step 2: Launch the Proto-Control (6 Ads)

Since this is a new account, there are no proven Control ads yet. The goal is to build one. Launch three A/B test pairs — six 3:2:2 Flexible Ads total — all inside the one ad set.

What is a 3:2:2 Flexible Ad? A single ad unit containing: 3 creatives (images or short videos) + 2 headlines + 2 primary texts. Meta automatically tests combinations and concentrates spend on what works. This keeps learning consolidated rather than fragmented across dozens of individual ads.

Each pair tests one strategic direction:

A/B Pair

Strategic Direction

What to Create

Pair 1

Market Research

Mirror the angles (not the copy) of top-performing competitor and loan officer accounts

Pair 2

Customer Language

Use real phrases from past client reviews, testimonials, or intake calls

Pair 3

Brand Messaging

Highlight the loan officer's specific differentiator — speed, a niche program, local expertise

Critical: All six ads must use the same format — all images or all videos. Mixing formats introduces a confounding variable that makes results unreadable.

Step 3: Do Nothing

For the first 5–7 days, do not touch the campaign. Do not change the budget, turn off ads, or edit copy. Any significant edit resets the learning phase. The campaign will show "Learning" status and CPLs will be volatile. This is normal — you are paying for education right now, not leads.

The One Exception — The Runaway Spend Ad

If, after 3–4 days, one ad is consuming more than 70–80% of daily spend and has produced zero leads, turn that single ad off. This is a damage control measure only. Do not replace it. Do not touch anything else. Return to the "do nothing" rule for the rest of the week.

How to check: Go to Ads Manager → Ads tab → sort by "Amount Spent" → check if the top ad has zero leads.

Week 2

WEEK 2 — Read the Data & Remove the Worst Offender

Goal: Analyze the initial data, identify the single biggest drain on the budget, and remove it.

Step 1: Evaluate the Blended Campaign Result

Look at the overall CPL for the entire campaign over the last 7 days. Do not look at individual ads yet.

How to check the blended CPL: Go to Ads Manager → Campaigns tab → set date range to "Last 7 Days" → look at the "Cost per Lead" column for the campaign row (not the ad set or ad rows).

Blended CPL

Interpretation

Action

Above $25 but trending downward

The system is learning

Be patient; do not intervene

Above $50 and not improving

The system is not learning

Proceed to Step 2

At or below $25

On target

Begin 4PI analysis; protect what is working

Step 2: Identify and Remove the Biggest Offender

Find the single ad that received the most spend AND delivered the worst CPL. This ad is consuming budget without producing proportional results.

How to find it:

Go to Ads Manager → Ads tab → set date range to "Last 7 Days"

Sort by "Amount Spent" (highest to lowest)

Cross-reference the top spenders with their "Cost per Lead"

The ad with the highest spend and worst CPL is the biggest offender

Turn it off. Turn off nothing else. Wait 2–3 days. Meta will re-allocate the budget across the remaining ads and new patterns will emerge.

Step 3: Begin 4PI Analysis

Now look at each remaining ad through the 4PI lens. For each ad, record:

4PI Question

Where to Find It in Ads Manager

Is spend concentrating or dispersing?

Ads tab → "Amount Spent" column, sorted high to low

What is the frequency trend?

Ads tab → add "Frequency" column via Customize Columns

Is CPM rising or falling?

Ads tab → add "CPM" column via Customize Columns

What is the CPL vs. account average?

Ads tab → "Cost per Lead" column

Document these observations. You are building a picture of which ads are performing which funnel jobs. This will directly inform the next creative tests.

Week 3

WEEK 3 — Build the Control & Launch the First Variable Test

Goal: Solidify your best-performing ads into a "Control" and introduce one new, intentional test.

Step 1: Define Your Control

By now, 3–5 ads should be consistently earning spend and producing results at or near the $25 CPL target. These are your Control ads — they represent "what good looks like today." Protect them.

Continue removing the single worst-performing ad every 2–3 days until only Control ads remain in the original ad set.

Step 2: Launch a Variable Ad Set

Create a second ad set inside the same CBO campaign. This is the Variable — the testing environment.

Use the 4PI analysis to determine what type of creative to test. The rule: build the creative that fills the biggest hole in the funnel.

4PI Signal

What the Funnel Needs

What to Build

Control ads have high frequency + strong CPL (BOFU)

New cold audiences at the top

TOFU creative — awareness-focused, broad appeal

CPMs are rising + CPL is worsening

Bridge between curiosity and intent

MOFU content — educational, trust-building

CTR is strong but CPL is weak

Better post-click experience

New landing page or lead form (not new creative)

Inside the Variable ad set, launch one concept as two 3:2:2 Flexible Ads. This gives the concept two chances to earn spend and gives Meta a fairer evaluation.

Step 3: Apply the Kill/Keep/Scale Framework

Decision

Criteria

Kill

Spent $50+ with zero or very high-CPL leads AND CTR below 0.8%

Keep (Monitor)

CPL above $25 but trending down; CTR healthy; frequency low

Keep (Protect)

CPL at or below $25; spend concentrating; frequency stable

Scale

CPL consistently below $25 over 5+ days; campaign stable

Duplicate & Test

High CTR but high CPL — the hook works; test a new landing page or lead form

Week 4

WEEK 4 — Scale with Automation

Goal: Implement automated rules to scale the budget without manual intervention and establish a sustainable creative rotation cycle.

Step 1: Set Up Performance Gate Scaling Rules

Create two automated rules in Meta Ads Manager. These rules manage the budget automatically.

How to create an automated rule: Ads Manager → top menu → "Automated Rules" → "Create Rule"

Scale-Up Rule:

Setting

Value

Apply to

All active campaigns (filter by campaign name, e.g., "LO-[Name]-PGS")

Condition

Cost Per Lead ≤ $22

Time Range

Last 7 days

Action

Increase daily budget by 5%

Maximum budget cap

2x current budget

Schedule

Once daily — Monday, Wednesday, Friday at midnight

Scale-Down Rule:

Setting

Value

Apply to

All active campaigns (same name filter)

Condition

Cost Per Lead > $30

Time Range

Last 7 days

Action

Decrease daily budget by 5%

Minimum budget floor

$35

Schedule

Once daily at midnight

Why Monday/Wednesday/Friday for scale-up? Running the scale-up rule only three times per week prevents the budget from compounding too aggressively. It also provides time to observe performance before pushing more spend.

Step 2: Establish a Creative Rotation Cycle

A healthy account is never static. Even the best ads will eventually exhaust their audience. The rotation cycle keeps the account fresh without introducing chaos.

Step

Action

1

Identify the weakest ad in the Control ad set (highest CPL, lowest spend concentration)

2

Build a new A/B concept in the Variable ad set (two 3:2:2 ads testing one new idea)

3

Let the Variable run until one concept clearly earns spend and improves blended CPL

4

Promote the winner from the Variable into the Control ad set

5

Retire the weakest Control ad

6

Repeat every 2–3 weeks

Creative Direction for Loan Officers

Test these angles in A/B pairs. Each angle maps to a specific funnel stage.

Angle

Core Message

Best Format

Funnel Stage

Remove the Payment

"What if you could eliminate your mortgage payment?"

Short video (UGC-style)

### Tofu

Cash Out

"Your home may have more equity than you think."

Static image with bold headline

### Tofu / Mofu

Breaking News

"New program allows [city] homeowners to..."

Static image (news-style)

### Tofu

Regret Prevention

"Most homeowners don't know about this until it's too late."

Short video

### Tofu / Mofu

Rate Drop Alert

"Rates just dropped. Here's what that means for your payment."

Static image

### Mofu

Proof / Testimonial

"We closed in 21 days. Here's how."

Video testimonial

### Bofu

Direct Response

"Get a free rate quote in 60 seconds. No obligation."

Static image with strong CTA

### Bofu

Common Mistakes to Avoid

Mistake

Why It Hurts

The Rule

Killing ads too early

An ad with $20 in spend has not been tested. You are making decisions on noise.

Never kill before $50 spent (2x CPL target).

Making too many changes at once

When you change three things simultaneously, you cannot identify which change caused the result.

Change one thing at a time. Wait at least 3 days before evaluating.

Chasing the cheapest CPL

A $10 lead that never answers the phone is worth less than a $25 lead that closes.

Track which leads are qualified. Pass that signal back to Meta if possible.

Launching too many ads

A $50/day budget spread across 10 ads gives each ad $5/day — not enough to learn anything.

Consolidate into fewer, stronger ads.

Scaling before stability

Increasing budget before the campaign exits the learning phase destroys performance.

Scale only after 5 consecutive days at or below $25 CPL.

Quick Reference: Week-by-Week Summary

Week

Primary Goal

Key Actions

What to Avoid

Week 1

Build the foundation

Launch 1 CBO campaign, 1 ad set, 6 ads (3 A/B pairs, all 3:2:2 format)

Any edits; killing ads; changing budget

Week 2

Read the data

Evaluate blended CPL; remove the single biggest spend-waster; begin 4PI analysis

Turning off multiple ads; changing targeting

Week 3

Solidify Control & test

Define 3–5 Control ads; launch 1 Variable ad set with 1 new concept (2 ads)

Testing more than one concept at a time

Week 4

Scale with automation

Set up automated scaling rules; establish creative rotation cycle

Manual budget changes; reactive decision-making

The Ongoing Weekly Diagnostic Loop

Once the account is past the initial ramp-up, follow this loop every week. The goal is to spend no more than 30 minutes per week on management. The system should run itself.

Step

Action

Where to Do It

1

Check the blended CPL for the last 7 days. Is it above or below $25?

Campaigns tab → "Cost per Lead" column

2

Run a 4PI analysis. Where is spend concentrating? What is the frequency trend? Is CPM rising?

Ads tab → Customize Columns to add Frequency and CPM

3

Identify the weakest Control ad. Is it still earning spend? Is its CPL trending up?

Ads tab → sort by "Cost per Lead"

4

Check the Variable ad set. Is the new concept earning spend? Is it improving the blended CPL?

Ads tab → filter by Variable ad set

5

Make one decision only. Kill the weakest ad, promote a winner, or launch a new test.

—

6

Let the automated rules handle the budget. Do not manually adjust unless the rules are failing.

Automated Rules → review rule history

Playbook synthesized from: AndroMeta One Campaign Method, Creative Testing After Andromeda, Lead Gen After Andromeda, and Meta Business Help Center official documentation.

