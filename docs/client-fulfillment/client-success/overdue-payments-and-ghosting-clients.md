---
title: Overdue Payments And Ghosting Clients
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-05-21
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Client Success (SOPs)/Overdue Payments & Ghosting Clients.docx
artifact_type: sop
---

# Overdue Payments And Ghosting Clients

## Purpose

Handle billing failures and disengaged clients.

## Scope

Billing and retention edge cases.

## Trigger

Failed payment or client unresponsive 14+ days.

## Inputs

- Billing status
- Last contact date

## Outputs

- Documented resolution or churn

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when applicable.

## Operating Content

Overdue Payments & Ghosting Clients

Overdue Payments & Ghosting Clients

Introduction

In this video, I'm breaking down the exact systems we use to handle the two most common and anxiety-inducing payment scenarios: clients whose payments decline and clients who pay you and then completely ghost.

It’s goal is two things:

To give you a system to increase your accounts receivable %

The % of money you should collect that you actually collect (pay plans, MRR…)

To give you a system to protect yourself from chargebacks from ghosting clients

By creating a clear paper trail of your follow-up.

The Fundamentals

There are few things more frustrating than seeing a payment decline from a client paying you a JUICY retainer, one of those is when a client pays you, seems excited on the sales call, and then disappears off the face of the earth. That shit triggers massive anxiety because you know a chargeback or a refund request could be coming at any minute.

Now the wrong way of handling this would be to just let it slide and hope for the best. I used to do this in the past and the likelihood of you getting a chargeback or refund request at any minute in the next year or so is pretty damn high - so the way we solve this is by having systems in place to follow up with these clients, while protecting your CSM team's time.

Payment Scenarios

Here’s a breakdown of how we handle both of these scenarios:

S1: The Client Pays and Then Ghosts

This is when a client pays their invoice, seems fine, and then goes completely silent. No onboarding form, no replies to emails, nothing.

The Goal: Your primary goal here is to create a bulletproof paper trail of follow-up. This is your defense against a future chargeback where they might claim, "I paid but never received any service."

The Process:

Automated & Manual Follow-Up (First 7 Days):

For the first 7 days, we hit them with a mix of automated and manual follow-up. This is already built into the Client GHL Sub-Account you set up in the previous video

We have the CSM involved in this process calling the client because this is NOT a “payment request” - at this point we’ve already collected payment, we just need to get them on the onboarding call

The Cost Incurred Framing:

In your follow-up messages, I’d recommend making it seem like you've already started working on their account and have allocated resources.

Ex: "Hey [NAME], just following up on the onboarding form. My team has already started mapping out your initial campaign strategy, and we're excited to get started, but we need that form to proceed."

Does it matter if you've actually started? No. The point is, their payment has taken up your time and a spot you could have given to another client. You need to be compensated for that. This framing helps justify keeping the payment if they never respond.

The "Hail Mary" Attempts (After Day 7):

If they're still ghosting after a week, it's time for the final attempts. There's not much else you can do beyond this.

Call their Google My Business phone number.

Find alternative business emails and reach out.

Find them on Facebook and Instagram and send them a DM.

If they still don't respond and never do, at least you know you’ve done your part

and have a clear record of attempting to deliver the service.

If you want to keep this top of mind for your CSM so they don't have to remember everyday who to follow up with, you can set up a simple automation to send a daily notification to a "csm-notis" Slack channel for every client who is in the "ghosting" stage.

S2: The Client's Payment Declines

This is when a recurring payment fails, or a final payment on a plan doesn't go through.

Your CSM or the person responsible for the client relationship and their results, should NEVER be the one chasing overdue payments.

Why? Because the second they start asking for money, the entire dynamic of the relationship changes. It becomes transactional. The client starts thinking, "Oh, the only reason they're being nice to me is because I'm paying them." It erodes trust and makes the CSM's job of coaching and supporting them ten times harder.

Think about it like a police interrogation. You have the "bad cop" who is aggressive and applies pressure, and the "good cop" who builds rapport and seems like they're on your side. In our agency, the CSM is always the good cop. Their job is to be the client's biggest advocate. The "bad cop" - the person who has to have the uncomfortable money conversation - should be someone else entirely.

The bottom line is we DO NOT want your CSM chasing this money. Instead, we bring in a Billing VA.

Who is the Billing VA?

This doesn't have to be a dedicated person, especially if you're sub-$100k/mo. It can be an existing VA on your team who has an extra 30 minutes a day.

The way we do this is by creating a separate Slack account for this person (ex: "Jenny - Billing"). The profile picture needs to look as friendly as possible. This sounds stupid, but trust me, it helps. People are more likely to respond positively to a friendly-looking person asking for money than a generic company account. With our first billing VA we even changed her name from “Sharmaine” to “Sarah” at the time to make her sound even friendlier. The rule of thumb here is the cuter they look and the cuter their name the better.

The Process:

The "Billing VA" follows the Client Payment overdue SOP

Client Payment Overdue SOP

They fill out the "Payment Overdue Form" (which is in the Client GHL Sub-Account)

This triggers the automated follow-up sequence and a make.com scenario that:

Updates your project management tool (ex: Monday.com) to show the payment is overdue.

Notifies your internal team in a dedicated Slack channel.

Can automatically send a reminder to the client in Slack

We also have our billing VA keep a log of all overdue payments on a “hot list” - you may have heard me talking about this with multiple different positions, but this is one centralized place I can go to see all overdue payments. When we fill out the payment overdue form this gets automatically updated, and we have this on the same sheet as our churn tracker. So if you don't have this on yours already, I’d recommend adding it.

Here’s the template: Overdue Payment Hot List

Incentivizing Your Billing VA:

To motivate your VA, you can put a simple commission structure in place based on the percentage of projected receivables they collect each month.

95%+ collected = $300 bonus

90% – 94% = $200 bonus

85% – 89% = $100 bonus

The way this works is for example, if you have $100k in MRR you're projected to collect that month, if she collects $95k+ she gets $300. Pretty damn simple.

The Setup

Alright, now I'm going to show you how to set up the technical side of the overdue payment system.

Confirm you have the payment overdue form in the client management sub account

We setup this up in the client sub account video

Download the Payment Overdue scenario and import it into your make.com account

Follow the setup shown in the video

Slack internal notis

Slack client notis

Add to PM tool

Paste the webhook into the payment overdue webhook

This means when this form is filed it will trigger this webhook

Changing The Card On File

On all of our follow up messages to overdue payment clients, we link a form which they can fill to update their payment method - you need to make sure this information is pushed to you when it's submitted by doing the following:

Confirm you have the card info form in the client management sub account

Download the card info submission scenario and import it into your make.com account

Setup the task on your PM tool and internal slack noti

Paste the webhook into the payment method webhook

Besides that you now have the system built out, all that's left to do is make a video breaking down the payment overdue system, attach it to the overdue SOP I’ve given you, and assign them the responsibility of chasing people down moving forward.

One final tip is I’d recommend pinning the overdue payment hot list and taking a few mins each day to review it so you can stay on track - this is on my habit tracker to review everyday.

