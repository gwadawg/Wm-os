---
title: Setting Up Facebook Lead Form
domain: client-fulfillment
owner: community-education
status: draft
last_updated: 2026-05-20
review_cycle: quarterly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Client Course Material/Skool Community/Bootcamp /SOP  Setting Up Your Facebook Lead Form 📝.docx
artifact_type: sop
---

# Setting Up Facebook Lead Form

## Purpose

Skool/bootcamp SOP for Facebook lead form setup.

## Scope

Client-facing course; link internal media-buying SOP when exists.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **community-education**.

## When To Use

Use per source document and related operating docs.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).

## Metrics

- See [KPIs](../../kpis/README.md) as metrics are formalized.

## Operating Content

## SOP: Setting Up Your Facebook Lead Form 📝
## Introduction: Building Your Lead Bridge 🌉
Imagine a potential customer sees your ad and is interested. What happens next? If you don't have a website or a landing page, that interest vanishes. A Facebook Lead Form is the bridge that captures that interest instantly, right within the Facebook app. It's the fastest way to turn a curious scroller into a valuable lead.

Why This Matters: For beginners, building a high-converting landing page is a huge hurdle. Lead Forms remove that barrier, allowing you to start collecting leads—names, emails, phone numbers—from day one, with just a few clicks. This SOP will guide you through the exact steps to create a Lead Form that works, and how to get those leads delivered where you need them.

Roadmap: We'll cover:

The basic setup of your Instant Form.

How to configure the form sections based on best practices.

The three primary ways to get your leads: sending them to a Google Sheet, to your own landing page, or directly into GoHighLevel (GHL).

## The Core Framework 🔄: Instant Lead Capture
The entire goal of a Facebook Lead Form (also called an "Instant Form") is to make it incredibly easy for someone to give you their information. It's pre-filled with their Facebook profile data, so they often only have to tap two buttons to become a lead. This low-friction process is perfect for beginners because it generates results quickly, building the momentum you need.

## Practical Breakdown 🛠️: Creating Your Lead Form Step-by-Step
Follow these instructions at the Ad Level of your campaign creation process.

## Before You Start
Privacy Policy URL: You MUST have a privacy policy page on a website to link to. Facebook requires this. If you don't have one, you can create a simple one using a free generator online and host it on a free platform like a Google Site.

## Part 1: The Basics
In your ad settings, scroll down to the "Destination" section.

Ensure "Instant Forms" is selected.

Click "Create Form".

Name Your Form: Give it a clear, descriptive name. E.g., "Free Guide Lead Form - [Date]". This is for your eyes only.

## [INSERT SCREENSHOT: Ad level view showing the 'Create Form' button]
## Part 2: Form Setup
## 1. Form Type
More Volume: This is the default and recommended for most beginners. It's a quick, two-tap process for the user.

Higher Intent: This adds a review step where users have to confirm their information. Use this only if you are getting a lot of low-quality leads.

Action: Select More Volume.

## 2. Intro (The Hook)
This is the first thing people see. Your goal is to remind them WHY they should fill out the form.

Image: Select "Use the image from your ad". This keeps the experience consistent and is the easiest option.

Headline: This should match the promise from your ad. Keep it short and benefit-focused.

## Example from image: See What Your Home Could Do for You
Description: Use the "List" format to break down the benefits into scannable bullet points. What will they get?

Example from image:

## Eliminate My Monthly Mortgage Payment
## Pay Off High-Interest Debt
## Upgrade Your Home
## [INSERT SCREENSHOT: The 'Intro' section filled out, matching the user's provided image.]
## 3. Questions
This is where you ask for the user's information. Less is more. The more you ask for, the fewer leads you will get.

Pre-fill Questions: Always start with Email and Full Name. Facebook will fill these in automatically for the user.

Custom Questions (Optional): Only add a custom question if it's absolutely essential for qualifying the lead. For beginners, it's best to stick to the pre-fill options.

## [INSERT SCREENSHOT: The 'Questions' section showing Email and Full Name added.]
## 4. Privacy Policy
Link Text: Simply write "Privacy Policy".

Link URL: Paste the URL to your privacy policy page here. This is non-negotiable.

The Destination 🥅: Where Do Your Leads Go?

After someone fills out the form, you need to tell Facebook where to send them and how you'll get their data. You have three main options.

## Option
## Best For
## Requires
## A: Google Sheet
## Beginners without a CRM
## Free Zapier account
## B: Landing Page
## Those with an existing website
## A built "Thank You" page
## C: GoHighLevel (GHL)
## GHL users — most powerful
## A GHL sub-account
## Option A: Send Leads to a Google Sheet (Recommended for Beginners)
This is the best option for beginners. It requires a simple automation, but once it's set up, your leads will appear in a spreadsheet automatically.

Key Takeaway: Facebook does NOT have a direct, real-time integration with Google Sheets. You must use a third-party "connector" tool. The most common is Zapier.

How It Works (High-Level):

In the Facebook Form: In the "Ending" section, write a simple thank you message.

Headline: Thanks, you're all set!

Description: Your information has been received. We'll be in touch shortly!

Set up the Connection:

Create a free account at Zapier.com.

Create a new "Zap".

Trigger: Select "Facebook Lead Ads".

Action: Select "Google Sheets" and choose "Create Spreadsheet Row".

Follow the on-screen instructions to map your form fields (Name, Email) to the columns in your Google Sheet.

## [INSERT DIAGRAM: A simple flowchart showing: Facebook Lead Form -> Zapier -> Google Sheet]
## Option B: Send Leads to Your Landing Page
Use this option if you have a website or landing page with a "Thank You" page already built.

In the Facebook Form: Go to the "Ending" section.

Headline: Write a clear transition. E.g., Thanks! Click below to continue.

Call-to-action button text: This is the text on the button. Make it clear what the next step is.

## Examples: Visit Website, Download Now, Learn More
Call-to-action button link: Paste the URL of your landing page or thank you page here.

## [INSERT SCREENSHOT: The 'Ending' section configured for the 'Visit Website' option.]
Important: With this method, you still need to download your leads manually from Facebook unless you set up a CRM connection.

## Option C: Send Leads Directly to GoHighLevel (GHL) 🚀
This is the most powerful option if you use GoHighLevel as your CRM. It sends leads from Facebook directly into your GHL account in real time, allowing you to trigger automated follow-up campaigns—texts, emails, calls—the moment someone submits the form. This method completely replaces the need for Zapier.

Key Takeaway: GHL has a direct, native integration with Facebook Lead Ads. This is the recommended method for any GHL user as it's faster, more reliable, and free (no Zapier subscription needed).

How It Works (High-Level):

Connect Your Facebook Account in GHL: You give GHL permission to access your Facebook Page and lead forms.

Map Your Form Fields: You tell GHL which fields on your Facebook form correspond to which fields on the contact record in GHL (e.g., "Full Name" from Facebook maps to the "Name" field in GHL).

Test the Connection: You send a test lead to confirm everything is flowing correctly before spending money on ads.

[INSERT DIAGRAM: A simple flowchart showing: Facebook Lead Form -> GoHighLevel CRM -> Automated SMS/Email Follow-up]

Step-by-Step Setup:

## Part 1: Connect Your Facebook Page to GHL
Inside your GHL Sub-Account, click on Settings in the bottom-left corner of the screen.

In the left-hand menu within Settings, scroll down and click Integrations.

Find the Facebook & Instagram card and click Connect.

A pop-up window will appear asking you to log into Facebook. Log into the account that has Admin access to the Facebook Page you are running ads for.

Grant all the requested permissions. Do not skip or deny any. This is the most common cause of the integration failing.

Select the correct Facebook Page from the list and choose your sync preference:

New Leads Only: Only syncs leads submitted after this connection is made (recommended).

All Leads: Pulls in historical leads as well.

Click Connect and Continue. You should see a green "Integration successful" banner appear.

[INSERT SCREENSHOT: GHL Settings > Integrations page with the Facebook & Instagram card highlighted.]

Important: You must be an Admin of both the Facebook Page and the Business Manager it belongs to. If you don't see your page in the dropdown, this is a permissions issue on the Facebook side.

## Part 2: Map Your Lead Form Fields
Once your page is connected, you need to tell GHL exactly how to read the data coming from your form.

Stay in the Settings > Integrations section.

Look for a section or tab called "Facebook Form Fields Mapping" and click on it.

You will see a list of all the Facebook Lead Forms associated with your connected page. Find the form you created earlier.

Click "Map Fields" next to your form.

For each field from your Facebook form, use the dropdown to select the matching Contact Field inside GHL:

## Full Name → Contact Name
## Email → Email
## Phone Number → Phone
Once all fields are mapped, click Save.

[INSERT SCREENSHOT: The GHL Facebook Form Field Mapping interface, showing the field dropdowns being matched up.]

## Part 3: Test Your Connection
Never skip this step. Testing ensures your leads will actually flow into GHL before you spend any ad budget.

Open a new browser tab and search for "Facebook Lead Ads Testing Tool" — the direct link is developers.facebook.com/tools/lead-ads-testing.

Select your Facebook Page and the Lead Form you just connected.

Click "Preview Form" or "Create Lead" to submit a test entry.

Go back to your GHL sub-account and navigate to Contacts.

The test lead should appear in your contacts list within 60 seconds.

[INSERT SCREENSHOT: The Facebook Lead Ads Testing Tool with the correct page and form selected.]

Troubleshooting Tip: If the test lead does not appear in GHL, the most common fix is a permissions issue. Go back to Settings > Integrations, disconnect the Facebook page, and reconnect it — making sure to approve every single permission Facebook requests during the login flow.

## Common Mistakes for Beginners ⛔️
No Privacy Policy: Your ad will be rejected without one.

Asking Too Many Questions: Every extra question you add will dramatically reduce your conversion rate. Stick to Name and Email to start.

Forgetting to Connect Leads: Don't just let your leads sit inside Facebook. They get stale quickly. Set up your chosen connection method before you launch your ad.

No Thank You Message: The end of the form is crucial. Either thank the user (Option A) or send them to the next step (Option B). Don't leave them hanging.

Skipping the GHL Test: If you use GHL, always test with the Lead Ads Testing Tool before going live. A broken integration means lost leads and wasted ad spend.

## Action Steps / Implementation ✅
Create a Privacy Policy: Use a free online generator and host it.

Choose Your Destination: Decide which option fits your setup — Google Sheet, Landing Page, or GoHighLevel.

Build Your Form: Follow the steps in the "Practical Breakdown" section.

(If using Google Sheets) Set Up Your Zapier Connection: Create your Zapier account and build the simple workflow to connect Facebook to your Sheet.

(If using GHL) Connect, Map, and Test: Follow the three-part GHL setup in Option C and confirm leads are flowing before launching.

Publish Your Form & Launch Your Ad!

## Resources to Implement 🧰
Zapier: https://zapier.com — The tool for connecting your Lead Forms to Google Sheets (Option A).

Google Sites: https://sites.google.com — A free and easy way to host your privacy policy if you don't have a website.

GHL Facebook Integration Guide: https://help.gohighlevel.com/support/solutions/articles/48001157632 — Official GHL step-by-step guide for connecting Facebook.

Facebook Lead Ads Testing Tool: https://developers.facebook.com/tools/lead-ads-testing — Use this to test your GHL or Zapier connection before going live.

## Related Docs

- None yet.

## Open Questions

- [ ] Human review: `draft` → `active`.
