---
title: Perspective Funnel Setup SOP
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-21
review_cycle: monthly
source_document: source-docs/waiz-drive-export/Waiz Media OS/03 _ Client Fulfillment/Media Buying/Media Buying (SOPs)/MB Creative Process/Perspective Funnel Setup SOP.docx
artifact_type: sop
---

# Perspective Funnel Setup SOP

## Purpose

Configure Perspective funnel for client campaigns.

## Scope

Funnel tech setup.

## Trigger

Implementation phase after kickoff.

## Inputs

- Client branding
- Offer
- Qualification questions

## Outputs

- Live funnel URL for ads

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Client-facing copy must follow [RM Compliance Guardrails](../../client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md) when applicable.

## Operating Content

SOP: Perspective Funnel Setup

This document outlines the standard operating procedure for setting up a Perspective funnel for clients, including GoHighLevel integration and Meta Pixel setup.

1. Funnel Duplication and Initial Setup

Duplicate the Funnel Template:

Navigate to the Perspective funnel template.

Click the three dots and select "Duplicate".

Rename the duplicated funnel to the client's name (e.g., "Brian Ashbee Funnel").

Adjust the Logo:

If the client has a logo, upload it to the header. If not, create a simple logo using a tool like Ideogram.

Ensure the logo has a transparent background. Use a background removal tool if necessary.

Replace the placeholder logo with the client's logo.

Fix the Footer:

Update the footer with the client's company name, MLO name, and NMLS ID.

Add the company's address and contact information.

Copy the updated footer and paste it into the footer of the thank-you page as well.

2. Page Customization

Opt-in Page:

Ensure the footer is updated on both opt-in page variations (e.g., "Remove Mortgage Payment" and "Cash Out").

Thank-You Page:

Update Testimonials: Replace the placeholder testimonials with the client's actual testimonials. If none are available, use generic ones but update the names.

Update Biography:

Replace "Meet Client Name" with the client's actual name (e.g., "Meet Brian Ashbee").

Add the client's headshot. Ensure it is in a square format (4x4). Use Canva to resize if necessary.

Update the biography with the client's information. You can use an AI tool to help rewrite and optimize the biography for the thank-you page.

Update "Learn More" Button: Change the URL on the "Learn More About the Company" button to the client's company website.

Update Privacy Policy & Terms of Agreement:

If the client has a privacy policy and terms of agreement, link to them in the footer.

If not, you will need to create them.

3. Integration

GoHighLevel Integration:

In Perspective, go to "Apps" and activate the GoHighLevel integration.

Select the correct client account.

Map the custom fields from the Perspective funnel to the corresponding fields in GoHighLevel.

Add the tag external form.

Save the integration settings.

Meta Pixel Integration:

In Perspective, go to "Apps" and activate the Meta integration.

Paste the Meta Pixel ID and Access Token.

Map the "lead" event to the form submission. The event should trigger on the button click of the last page of the form.

Save the integration settings.

4. Publishing

Publish the Funnel:

Once all the setup and customization is complete, publish the funnel.

Make sure to select the domain hecm.homequityhacks.com.

Edit the end of the URL to the client's account name (e.g., hecm.homequityhacks.com/clientname).

Publish the funnel.

Update ClickUp:

Copy the published funnel URL.

Paste the URL into the client's account page in ClickUp for future reference.

