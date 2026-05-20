---
title: WM Acquisition Report Data System
domain: operations
owner: operations
status: draft
last_updated: 2026-05-20
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/02 _ Operations/WM Acquisition Report  Complete Data System Documentation.docx
artifact_type: reference
---

# WM Acquisition Report Data System

## Purpose

Documentation for the acquisition reporting data system.

## Scope

Reporting infrastructure.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **operations**.

## When To Use

Use per source document and related operating docs.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).

## Metrics

- See [KPIs](../../kpis/README.md) as metrics are formalized.

## Operating Content

## WM Acquisition Report: Complete Data System Documentation
## Executive Summary
The WM Acquisition Report is a comprehensive data management system designed to track acquisition costs, team performance, and conversion metrics across the entire sales funnel. The system enables leadership to make data-driven decisions about ad spending, team productivity, funnel optimization, and revenue forecasting.

Primary Users: CEO, Sales Representatives Primary Use Cases: Budget allocation, performance management, funnel optimization, revenue forecasting Data Sources: Ad platforms (Meta/Facebook), CRM/booking system (GHL), internal team tracking

## Part 1: Business Context & Data Flow
## 1.1 The Sales Funnel
The WM Acquisition Report tracks leads through a multi-stage sales funnel with distinct booking and show stages:

Ads → Leads → Intro Booked → Intro Showed → Demo Booked → Demo Showed → Offers → Closes

## ↓              ↓              ↓              ↓           ↓         ↓
## (Booking)      (Show)       (Booking)      (Show)      (Made)    (Paid)
## 
Each stage represents a critical decision point where leads either progress or drop out. The system measures both the volume at each stage and the quality of progression (conversion rates, show rates, close rates). Importantly, we track both when an appointment is booked and when it actually occurs (show), as no-shows are a significant funnel leak.

## 1.2 Key Business Metrics
The system tracks three categories of metrics:

## Metric Category
## Purpose
## Example
## Acquisition Costs
## Understand ROI on ad spend
## Cost per lead, cost per demo, cost per close
## Team Performance
## Evaluate individual contributor effectiveness
## Setter show rates, closer offer rates, close rates
## Funnel Health
## Identify bottlenecks and optimization opportunities
## Booking rates, show rates, offer rates
## 1.3 Data Collection Points
Data enters the system from three primary sources:

## Ad Platforms (Meta/Facebook) → Ads Data sheet
## GHL (Go High Level) → Dials sheet, Appointments sheet (auto-populated)
## Manual Entry → Leads sheet, Offers sheet, Agent sheet
## Part 2: Data Sheets & Their Roles
## 2.1 “Ads Data” Sheet
Purpose: Track all advertising spend and performance metrics from Meta/Facebook campaigns.

Key Fields:

## A:A Date — The date the ad was active/spent
## B:B Amount spent — Total cost for that day's ads
## C:C Adset — The ad set name (grouping of ads)
## D:D Ad Name — Individual ad creative name
## Reach, Impressions, CPM — Performance metrics
## Unique Outbound Clicks, Cost Per Unique Outbound Click — Click-through data
## Source — Always "Facebook" (can expand to other platforms in future)
Data Frequency: Daily updates from Meta API Grain: One row per day per ad/adset combination Primary Use: Calculate cost per acquisition metrics (cost per lead, cost per demo, cost per close)

How It Connects:

## Joins to Leads sheet by Date (Ads Data date = Leads Date Created)
## Aggregates total daily spend, then divides by leads/appointments/closes to calculate unit economics
## 2.2 “Leads” Sheet
Purpose: Central repository of all prospects who have entered the funnel, regardless of source.

Key Fields:

## A:A Date Created — When the lead was first added to the system
## B:B ID — Unique lead identifier (can be blank for older leads)
## C:C Lead Name — Contact name
## D:D Email,
## E:E Phone Number — Contact information
## F:F Source — How the lead entered (Meta, Cold Call, etc.)
## G:G Offer — Type of offer presented (RM, Skool, etc.)
## H:H Qualified — Whether the lead met qualification criteria (Not currently in use)
Data Frequency: Real-time as leads are added Grain: One row per unique lead (no duplicates) Primary Use:

## Filter for Meta leads only (for cost per acquisition calculations)
## Count total leads for booking rate calculations
## Join key to connect ads spend to appointments
Important Notes:

## No duplicate leads — if someone inquires twice, they appear once
## Older leads may not have an ID field populated
## Source field is critical for filtering (Meta vs. Cold Call vs. other sources)
How It Connects:

## Joins to Ads Data by Date Created (aggregates daily ad spend)
## Joins to Appointments by ID (Lead ID)
## Joins to Offers by ID (Lead ID)
## 2.3 “Appointments” Sheet
Purpose: Track all scheduled appointments and their outcomes (showed/no-show).

Key Fields:

## A:A Date Created — When the appointment was scheduled
## B:B Lead ID — Links to the Leads sheet
## C:C Appointment ID — Unique identifier for this specific appointment
## D:D Lead Name,
## E:E Phone Number — Contact info (denormalized for convenience)
F:F Appointment Type — "Intro" or "Demo" (Or Bamfam/Followup - these type of appointments aren’t Meta metrics)

G:G Booking Source — How the appointment was sourced (Aged, New, etc.) — used for future segmentation

## H:H How was booked — "customer booked" (setter booked) or "Customer booked" (lead self-booked)
I:I Date Apt Created — Date the appointment was Created (this is best used for booking rates)

J:J Date of Appt — When the appointment actually occurred (This is used when calculating Show rates)

K:K Appt Status — "Y" (showed) or "N" (no-show), “C” (Cancelled), “X” (Our team didn’t show)

L:L Qualified - Here is still being built out but should say yes or no if they’re qualified or not

M:M Setter — Name of the team member who booked the appointment (if customer booked, this will be blank)

## Call Taken By — Name of the team member who conducted the call
Data Frequency: Real-time as appointments are booked (via GHL integration) Grain: One row per appointment (a single lead can have multiple appointments) Primary Use:

## Calculate booking rates (% of leads that booked an intro/demo)
## Calculate show rates (% of appointments that showed)
## Track individual setter and closer performance
## Join to Offers to calculate close rates
Critical Date Fields:

## Date Apt Created — Used for booking metrics (when was the appointment scheduled?)
## Date of Appt — Used for show rate metrics (when did the appointment occur?)
How It Connects:

## Joins to Leads by Lead ID
## Joins to Offers by Appointment ID (to see which appointments resulted in offers)
Two instances of this table in blended data: one for booking metrics (Date Apt Created), one for show rates (Date of Appt)

## 2.4 “Offers” Sheet
Purpose: Track all offers made and their outcomes (closed or not).

Key Fields:

## A:A Date — When the offer was made
## B:B Lead ID — Links to the Leads sheet
C:C Appointment ID — Links to the Appointments sheet (shows which appointment led to this offer)

## D:D Name,
## E:E PhoneNumber
## F:F Closed? — "Y" (payment received) or "N" (not closed)
## G:G Cash Collected — Amount paid (if closed)
## H:H (DOn’t use this)
## I:I Offer — Type of offer ("Core Offer", "Skool", etc.)
J:J Appointment Type — Type of appointment that led to offer (denormalized) (Or if you have the appointment ID attached to the sheet, you can source the appointment that way

K:K Setter Name of the person who set that appointment. (this will be used to allocate the commissions and reporting for the quality of the appointments the setter makes

L:L Offered By — Name of the person who made the offer (typically the closer)

Data Frequency: Real-time as offers are made Grain: One row per offer (a single lead can have multiple offers, but typically only Skool offers are tracked multiple times) Primary Use:

## Calculate offer rates (% of demos that received an offer)
## Calculate close rates (% of offers that closed)
## Track closer performance (offer rate, close rate)
## Segment by offer type (Skool vs. non-Skool)
Important Notes:

## Most offers are made during demos (90% of the time)
## Follow-up calls may also result in offers
## Skool offers are tracked separately from other offers
## "Closed" means payment was received (not just a signed contract)
How It Connects:

## Joins to Leads by Lead ID
## Joins to Appointments by Appointment ID
## Provides the final conversion point in the funnel
## 2.5 Agent Sheet
Purpose: Store team member information and commission structure.

Key Fields:

## Agent name
## Role (Setter, Closer, etc.)
## Commission breakdown
## Other compensation details
Data Frequency: Updated as team structure changes Grain: One row per team member Primary Use: Reference data for team member names, roles, and compensation

How It Connects:

## Referenced in Appointments sheet (Setter, Call Taken By)
## Referenced in Offers sheet (Offered By)
## Used to validate team member names across the system
## 2.6 Dials Sheet
Purpose: Track all phone calls/dials made from GHL (Go High Level).

Key Fields:

## Dial date/time
## Phone number dialed
## Duration
## Outcome (connected, voicemail, etc.)
Data Frequency: Real-time from GHL Grain: One row per dial attempt Primary Use: Calculate team productivity (dials per day, connection rates)

Note: Not currently integrated into the Looker Studio dashboard, but available for future analysis.

## 2.7 Intro Call Review & Closer Calls Sheets (DON’T USE FOR DASHBOARD
Purpose: Store recordings, notes, and AI-generated summaries of calls for quality assurance and training.

Key Fields:

## Call recording link
## Call transcript/summary
## Call notes
## Opportunity score
## Key takeaways
Data Frequency: Updated after each call Grain: One row per call Primary Use:

## Quality assurance and coaching
## AI training and analysis
## Identifying patterns in successful vs. unsuccessful calls
Important Note: These sheets are not connected to the main data system and are primarily used for internal review and AI training purposes.

## Part 3: Data Relationships & Joins
## 3.1 The Blended Data Structure
To calculate acquisition costs and performance metrics, the data is combined using a blended data source in Looker Studio. This blend connects four main tables:

## Ads Data
## ↓ (join by Date)
## Leads Data
## ↓ (join by Lead ID)
## Appointments Data (Instance 1: Date Apt Created for booking metrics)
## Appointments Data (Instance 2: Date of Appt for show rate metrics)
## ↓ (join by Appointment ID)
## Offers Data
## 3.2 Join Logic
## Join
## Left Table
## Right Table
## Join Key
## Join Type
## Purpose
## 1
## Ads Data
## Leads
## Date = Date Created
## Left Outer
## Aggregate daily ad spend to leads created that day
## 2
## Leads
## Appointments (Booking)
## ID = Lead ID
## Left Outer
## Connect leads to appointments they booked
## 3
## Appointments (Booking)
## Appointments (Show Rates)
## Lead ID = Lead ID
## Left Outer
## Duplicate appointments table with different date range
## 4
## Appointments
## Offers
## Appointment ID = Appointment ID
## Left Outer
## Connect appointments to offers made
Why Left Outer Joins?

## Ensures all ad spend is preserved (even days with zero leads)
## Ensures all leads are preserved (even if they didn't book)
## Ensures all appointments are preserved (even if no offer was made)
## 3.3 Date Range Strategy
The blend uses two different date ranges for Appointments:

## Instance
## Date Field
## Purpose
## Used For
## Appointments (Booking)
## Date Apt Created
When was the appointment scheduled?

## Booking rates, total demos booked
## Appointments (Show Rates)
## Date of Appt
When did the appointment occur?

## Show rates, demos showed
This allows accurate reporting on both "when did we book this?" and "when did it happen and did they show?"

## Part 4: Key Metrics & Calculations
## 4.1 Acquisition Cost Metrics
These metrics calculate the cost to acquire leads and customers at each stage of the funnel.

## Cost per Lead (Meta only)
## Total Ad Spend / Count of Meta Leads
## 
Shows the average cost to generate a qualified lead from Meta ads.

## Cost per Intro
## Total Ad Spend / Count of Intro Appointments
## 
Shows the cost to generate an intro appointment (first call).

## Cost per Intro Showed
## Total Ad Spend / Count of Intro Appointments that Showed
## 
Shows the cost to get someone on an actual intro call (accounting for no-shows).

## Cost per Demo
## Total Ad Spend / Count of Demo Appointments
## 
Shows the cost to advance a lead to a demo (second call).

## Cost per Demo Showed
## Total Ad Spend / Count of Demo Appointments that Showed
## 
Shows the cost to get someone on an actual demo call.

## Cost per Offer (non-Skool)
## Total Ad Spend / Count of Non-Skool Offers Made
## 
Shows the cost to generate a sales opportunity.

## Cost per Close (non-Skool)
## Total Ad Spend / Count of Non-Skool Closes
## 
Shows the customer acquisition cost (CAC) — the most important metric for profitability.

## 4.2 Conversion Metrics
These metrics measure how efficiently leads move through each stage of the funnel.

## True Intro Booking Rate
## Unique Leads That Booked (first time only)
## / Total Leads Created
## 
What % of leads book an intro call?

## Intro Show Rate
Count of Intros that Showed / Count of Total Intros Taken Place (Date of Appt)

## 
What % of intro appointments actually show up?

## Demo Booking Rate
## Count of Demo Appointments Booked / Count of Intros that Showed
## 
What % of leads who showed for an intro advance to a demo (book a demo)?

## Demo Show Rate
## Count of Demos that Showed /Count of Total Demos Taken Place (Date of Appt)
## 
What % of demo appointments actually show up?

## Offer Rate (non-Skool)
## Count of Non-Skool Offers / Count of Demos that Showed
## 
What % of demos that showed result in an offer?

## Close Rate (non-Skool)
## Count of Non-Skool Closes / Count of Non-Skool Offers
## 
What % of offers convert to paid customers (payment received)?

## 4.3 Team Performance Metrics
These metrics evaluate individual contributor performance.

Setter Performance:

Total Intros Taken — How many intro appointments did this setter take?

Total Demos Booked — How many demos did this setter book?

Demo Show Rate — What % of demos they booked actually showed?

Booking Rate (Intros Showed to Demos Booked) — What % of intros they conducted that showed advanced to demos (booked a demo)?

Total Closes from Their Bookings — How many deals closed from demos they booked?

Closer Performance:

Total Demos Conducted — How many demos did this closer conduct?

## Demo’s Taken— Total amount of Demos that were taken
Offer Rate — What % of demos they conducted that showed resulted in an offer (Offer rate for skool + Offer rate for everything other than skool?

Close Rate — What % of offers they made closed (be sure to separate for skool and the other offers)?

Total Closes — How many deals did they close?

## Part 5: Filtering & Segmentation
## 5.1 Primary Filters
The Looker Studio dashboard includes the following filters to segment data:

## Filter
## Field
## Purpose
## Example Values
## Date Range
## Date of Appt or Date Apt Created
## View metrics for specific time periods
## Mar 1-31, 2026
## Setter
## Setter
## View metrics for a specific setter
## Pedro Rio, [Future setters]
## Closer
## Call Taken By or Offered By
## View metrics for a specific closer
## [Your name], [Future closers]
## 5.2 Future Segmentation Options
The system is designed to support additional segmentation in the future:

## Field
## Current Use
## Future Use
## Booking Source
## Informational
## Segment performance by source (Aged, New, etc.)
## Offer
## Separate Skool tracking
## Compare Core Offer vs. Skool offer performance
## Source (Leads)
## Filter for Meta leads
## Compare Meta vs. Cold Call acquisition costs
## Part 6: Data Quality & Integrity
## 6.1 Critical Fields for Accuracy
For the system to work correctly, these fields must be populated accurately:

## Field
## Sheet
## Importance
## Notes
## Lead ID
## Leads, Appointments, Offers
## Critical
## Must match across sheets for joins to work
## Appointment ID
## Appointments, Offers
## Critical
## Must be unique and match for offer tracking
## Date of Appt
## Appointments
## Critical
## Used for show rate calculations
## Appt Status
## Appointments
## Critical
## Must be "Y" or "N" “X” or “C”
Closed?

## Offers
## Critical
## Must be "Y" or "N"
## Setter
## Appointments
## Important
## Must match Agent sheet names
## Call Taken By
## Appointments
## Important
## Must match Agent sheet names
## Offered By
## Offers
## Important
## Must match Agent sheet names
## 6.2 Common Data Issues
## Issue
## Cause
## Impact
## Solution
## Percentages over 100%
## Duplicate rows in Appointments table
## Inflated metrics
## Check for duplicate Appointment IDs
## Missing data in metrics
## Lead ID or Appointment ID not populated
## Incomplete tracking
## Backfill missing IDs or use alternative join key
## Mismatched names
## Typos in Setter/Closer names
## Inaccurate team performance
## Standardize names in Agent sheet
## Date mismatches
## Different date formats
## Join failures
## Ensure all dates are in same format (YYYY-MM-DD)
## 6.3 Data Validation Checklist
Before trusting dashboard metrics, verify:

## All Lead IDs in Appointments sheet match a Lead ID in Leads sheet
## All Appointment IDs in Offers sheet match an Appointment ID in Appointments sheet
## No duplicate Appointment IDs in Appointments sheet
## All dates are in consistent format
## Appt Status values are only "Y" or "N"
## Closed? values are only "Y" or "N"
## Setter and Closer names match the Agent sheet exactly
## Part 7: Using the Data for Decision-Making
## 7.1 CEO-Level Decisions
Question: "How much should I spend on ads next month?" Metrics to Review: Cost per close (non-Skool), close rate, demo show rate Logic: If cost per close is $X and you want Y closes, you need $X*Y in ad spend. Adjust based on funnel health.

Question: "Where is our biggest funnel bottleneck?" Metrics to Review: All conversion rates (booking, show, offer, close) Logic: The lowest conversion rate is your constraint. Focus optimization efforts there.

Question: "Is our team performing well?" Metrics to Review: Setter show rates, closer offer rates, closer close rates Logic: Compare individual performance to team average. Identify top performers and underperformers.

## 7.2 Sales Manager Decisions
Question: "How many dials should we target this week?" Metrics to Review: Dial volume, booking rate, intros booked Logic: If booking rate is X%, and you want Y demos, calculate required dials.

Question: "Why are demo show rates declining?" Metrics to Review: Demo show rate by setter, intro call review recordings Logic: Check if specific setters have lower show rates. Review their intro calls for quality issues.

Question: "Which setter is performing best?" Metrics to Review: Setter show rates, booking rates, closes from their bookings Logic: Identify top performer's techniques and coach others.

## 7.3 Individual Rep Decisions
Question: "How am I performing compared to the team?" Metrics to Review: Your metrics vs. team average Logic: Identify your strengths and weaknesses. Focus on improvement areas.

Question: "Why are my close rates low?" Metrics to Review: Your offer rate, close rate, offer types Logic: If offer rate is low, focus on demo quality. If close rate is low, focus on offer presentation.

## Part 8: Future Enhancements
## 8.1 Planned Expansions
As the business scales, the system can be enhanced to track:

Multiple Setters & Closers: Already built into the data structure; just add new names to Agent sheet

## Multiple Ad Platforms: Add Google Ads, LinkedIn, TikTok to Ads Data sheet
## Booking Source Segmentation: Use Booking Source field to compare Aged vs. New lead performance
## Offer Type Comparison: Compare Core Offer vs. Skool vs. other offer types
## Lead Source Comparison: Compare Meta vs. Cold Call vs. other sources
## Geographic Segmentation: Add location field to Leads sheet
## Product/Service Segmentation: Add product field to Offers sheet
## Revenue Tracking: Add revenue amount to Offers sheet (currently only tracks payment received)
## 8.2 System Scalability
The current system is designed to scale:

## Unlimited Leads: No row limits in Google Sheets (up to 10M rows)
## Unlimited Appointments: Each lead can have multiple appointments
## Unlimited Offers: Each appointment can have multiple offers (though typically only Skool)
## Multiple Team Members: Setter and Closer fields can accommodate any number of team members
## Multiple Ad Platforms: Ads Data sheet can include data from multiple sources
## Part 9: Glossary
## Term
## Definition
## Lead
## A prospect who has entered the funnel (either through ads or cold outreach)
## Intro
## First appointment/call with a lead (typically 15-30 min discovery call)
## Demo
## Second appointment/call with a lead (typically 30-60 min product demonstration)
## Show Rate
## Percentage of scheduled appointments where the lead actually showed up
## Booking Rate
## Percentage of leads who booked an appointment at a given stage
## Offer
## A sales proposal presented to a lead (typically during or after a demo)
## Close
## A lead who paid (payment received = "Y" in Closed? field)
## Setter
## Team member who books appointments and conducts intro calls
## Closer
## Team member who conducts demos and makes offers
## CAC
## Customer Acquisition Cost (total ad spend / number of closes)
## Funnel
## The progression of leads from initial contact through close
## Conversion Rate
## Percentage of leads who progress from one stage to the next
## Cost per Acquisition
## Average cost to acquire a customer (or lead, or appointment, depending on stage)
## Skool Offer
## A specific offer type that is tracked separately from other offers
## GHL
## Go High Level (CRM/booking system used to manage appointments)
## Part 10: Contact & Support
For questions about this system or to request changes:

## Data Issues: Check the Data Quality & Integrity section (Part 6)
## Metric Definitions: See the Key Metrics & Calculations section (Part 4)
## Dashboard Help: Refer to the Filtering & Segmentation section (Part 5)
## System Changes: Document the change request and the business reason for it
## Appendix: Sample Queries
## A.1 Calculate Cost per Close for March 2026
Steps:

## Filter Ads Data by Date: Mar 1-31, 2026
## Sum Amount spent
Filter Offers by Date: Mar 1-31, 2026 AND Closed? = "Y" AND Offer != "Skool"

## Count distinct Lead IDs
## Divide: Total Ad Spend / Count of Closes
## A.2 Calculate Setter Show Rate for March 2026
Steps:

## Filter Appointments by Date of Appt: Mar 1-31, 2026
## Filter by Setter: [Selected Setter]
Filter by Appointment Type: "Intro" (for intro show rate) or "Demo" (for demo show rate)

## Count Appointments where Appt Status = "Y"
## Count all Appointments
## Divide: Showed / Total
## A.3 Calculate Closer Close Rate for March 2026
Steps:

## Filter Appointments by Date of Appt: Mar 1-31, 2026
## Filter by Call Taken By: [Selected Closer]
## Filter by Appointment Type: "Demo"
## Filter by Appt Status: "Y" (demos that showed)
## Join to Offers where Offer != "Skool"
## Count Offers where Closed? = "Y"
## Count all Offers
## Divide: Closed / Total Offers

## Related Docs

- None yet.

## Open Questions

- [ ] Human review: `draft` → `active`.
