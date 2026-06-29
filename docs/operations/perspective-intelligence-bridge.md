---
title: Perspective Intelligence Bridge — Perspective MCP to Wm-os
domain: operations
owner: founder
status: draft
last_updated: 2026-06-24
review_cycle: quarterly
artifact_type: playbook
---

# Perspective Intelligence Bridge — Perspective MCP → Wm-os

**Purpose:** Define how live Perspective Funnel data (structure, step conversion, leads) feeds Wm-os client fulfillment and media-buying knowledge — without storing lead PII or daily metric dumps in git.

**One-sentence job:** Perspective MCP owns live funnel ops; Supabase owns downstream lead KPIs; Wm-os stores client funnel registry, specs, and distilled optimization notes.

**Setup entry:** [Perspective Funnel Setup SOP](../client-fulfillment/media-buying/perspective-funnel-setup-sop.md)

**Client registry:** [perspective-client-manifest.yaml](../client-fulfillment/media-buying/perspective-client-manifest.yaml)

## System of record

| System | Role | Stores lead PII / time-series? |
|--------|------|--------------------------------|
| **Perspective (MCP)** | Layer 0a: funnel structure, in-platform leads, step analytics | Yes (canonical for funnel UI) |
| **Supabase — WM Reporting** | Layer 0b: `events` after GHL ingest (leads, appointments, shows) | Yes (canonical for portfolio KPIs) |
| **Wm-os (git)** | Layer 2: manifest, form specs, SOPs, distilled funnel notes | No — registry + patterns only |
| **ClickUp client file** | Operational mirror of published funnel URL | No |

Supabase project: **WM Reporting** (`fszmndldcvrrmitfbwde`). Same database as the Mr. Waiz dashboard (`call-center-reporting-template`).

**MCP endpoint:** `https://perspective-api.co/mcp` (Perspective Funnels). Do **not** use `api.perspective.co/mcp` — OAuth metadata mismatches and `mcp-remote` fails. Not `getperspective.ai`, which is a different product.

## Four-layer model

```
Layer 0 — Live systems
  Perspective MCP · funnel pages · step conversion · in-platform leads
  Supabase events · qualified · appointments · shows (post-GHL)

Layer 1 — Client manifest (git)
  perspective-client-manifest.yaml · funnel_id · published_url · ghl_sub_account

Layer 2 — Wm-os distilled knowledge (git)
  perspective-funnel-setup-sop · rm-funnel-form-spec · dscr-funnel-form-spec · funnel optimization notes

Layer 3 — Agent actions
  Build/duplicate funnels · diagnose step drop-off · sync manifest after publish
```

**Rule:** Layer 0 owns live funnel data and lead records. Layers 2+ never store Perspective lead exports, contact details, or daily step-metric time series in git.

## Cursor MCP configuration

Configured in `~/.cursor/mcp.json`:

```json
"perspective": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://perspective-api.co/mcp"]
}
```

**First use:** Restart Cursor, then ask a Perspective-related question. `mcp-remote` opens a browser for OAuth sign-in (same flow as Claude **Customize → Connectors**).

**Troubleshooting:** If auth fails after a prior attempt, clear stale OAuth cache: `rm -rf ~/.mcp-auth`, then retry.

### OAuth shows Perspective “Oops, something went wrong”

Cursor’s built-in OAuth redirect sometimes fails even when the MCP URL is correct. **Workaround — authenticate in Terminal first** (tokens are shared with Cursor’s `mcp-remote`):

```bash
npx -y -p mcp-remote@latest mcp-remote-client https://perspective-api.co/mcp
```

1. Browser opens → sign in to Perspective and approve access.
2. Wait for `Connected successfully!` in Terminal.
3. In Cursor: **Cmd+Shift+P → “Cursor: Clear All MCP Tokens”** (optional), then restart Cursor.
4. Toggle **perspective** MCP on — it should reuse `~/.mcp-auth` and skip the broken browser step.

If the same error appears in Terminal too, click **See details for this error** on the Perspective page and email **support@perspective.co** — likely an account or MCP-access issue on their side.

**Fallback:** Connect via [Claude Connectors](https://claude.ai/settings/connectors) using `https://perspective-api.co/mcp` for funnel ops until Cursor OAuth is stable.

## Two pipelines (join, don't duplicate)

| Question | Primary source | Secondary join |
|----------|----------------|----------------|
| Funnel step drop-off, page copy, form fields | Perspective MCP | Client DNA / form spec in Wm-os |
| CPL, qualified rate, booking rate, show rate | Supabase `events` | [ad-intelligence-bridge.md](ad-intelligence-bridge.md) for ad attribution |
| Leads in Perspective not in GHL | Perspective MCP vs GHL | [identifying-technical-issues-with-clients.md](systems/identifying-technical-issues-with-clients.md) |
| New client funnel from template | Perspective MCP + SOP | Update manifest after publish |

Do not treat Perspective in-platform analytics as a replacement for Supabase portfolio KPIs. GHL is the CRM of record after integration.

## Manifest sync workflow

After publishing or materially changing a client funnel:

```
1. Agent reads perspective-client-manifest.yaml for client_slug
2. Agent calls Perspective MCP: list funnels / get funnel by name or ID
3. Agent updates manifest row: funnel_id, published_url, last_synced_at, step_count
4. Agent confirms GHL field mapping still matches client DNA form spec
5. Paste published URL to ClickUp client file (human or agent reminder)
```

### Manifest row shape

See [perspective-client-manifest.yaml](../client-fulfillment/media-buying/perspective-client-manifest.yaml). Required fields per active client:

| Field | Purpose |
|-------|---------|
| `client_slug` | Stable key aligned with Supabase `clients` and DNA folders |
| `perspective_sub_account` | Perspective workspace / sub-account name |
| `funnel_id` | Perspective funnel ID (from MCP) |
| `funnel_name` | Display name in Perspective |
| `published_url` | Live URL (e.g. `hecm.homequityhacks.com/{slug}`) |
| `product` | `reverse` \| `dscr` \| `broad_forward` |
| `ghl_sub_account` | GHL location name for integration checks |
| `os_refs` | Related Wm-os docs (form spec, lander pack, DNA) |
| `last_synced_at` | ISO date of last MCP-backed manifest update |

## Agent prompts (examples)

| Intent | Example prompt |
|--------|----------------|
| Registry refresh | "Sync perspective-client-manifest from Perspective MCP for all active RM clients" |
| Step diagnosis | "Pull step conversion for {client} funnel; compare to 30-day qualified rate in Supabase" |
| New client build | "Duplicate RM template funnel for {client} per perspective-funnel-setup-sop; update NMLS footer" |
| Integration audit | "List Perspective leads for {client} last 7 days not matching GHL import" |
| Copy change | "Draft step-3 headline variants for {client} per RM compliance guardrails" |

## Funnel capture workflow (structure → Wm-os spec)

Use when building or refreshing a **generic funnel spec** (e.g.
[RM Funnel Form Spec](../client-fulfillment/reverse-mortgage-dna/rm-funnel-form-spec.md)) from a live
Perspective funnel. Do **not** write to git until the capture breakdown is reviewed if the user
requested a review checkpoint.

```
1. list_workspaces → resolve funnelId + workspace
2. get_crm_properties → question titles + field names (GHL mapping)
3. get_chart_metrics (chart_page_to_page_conversion_rate) → page order + step names
4. get_chart_metrics (chart_time_on_page) → dwell-time benchmarks (snapshot only)
5. get_kpi_metrics (kpi_conversion_rate, kpi_new_contacts) → reference KPIs (90d window)
6. Live browser walkthrough of published_url → headlines, answer options, thank-you blocks
   (MCP has no get_funnel / page-copy tool)
7. Cross-reference GHL nurture docs for post-submit cadence (not in Perspective)
8. Distill into generic spec; scrub client names; cite perspective:funnel:{funnel_id}
9. Update perspective-client-manifest.yaml template row + os_refs
```

### MCP limitations (known)

| Tool | Issue | Workaround |
|------|-------|------------|
| — | No `get_funnel` for page HTML/copy | Browser walkthrough of `published_url` |
| `list_sequences` | Output validation fails on non-UUID step IDs | Use GHL drip docs for post-submit email/SMS cadence |
| `get_insight_metrics` | Requires `insightId` in `question_XXXX` format | Browser for answer-option labels; CRM properties for question titles |
| `get_kpi_metrics` | Some subtypes return 404 on sparse funnels | Skip or widen date range |

### What syncs where after capture

| Artifact | Goes to |
|----------|---------|
| Page order, questions, conditionals, GHL fields | Product DNA funnel spec (`rm-funnel-form-spec.md`, `dscr-funnel-form-spec.md`) |
| funnel_id, published_url, step_count | `perspective-client-manifest.yaml` |
| Step drop-off / CPL / qualified rate | Perspective MCP or Supabase — **not** git time series |
| Full drip copy | Existing client-marketing nurture docs — link, don't duplicate |

## What never syncs to git

- Perspective lead exports (names, emails, phones)
- Daily step-metric time series
- Full funnel HTML / raw API JSON dumps
- OAuth tokens (live only in `~/.mcp-auth` via `mcp-remote`)

## What stays separate

| System | Why separate |
|--------|--------------|
| [ad-intelligence-bridge.md](ad-intelligence-bridge.md) | Ad creative winners — different capture schema |
| [call-intelligence-bridge.md](call-intelligence-bridge.md) | Call transcripts — different extraction schema |
| GHL automations | CRM workflows after lead ingest |

## Related

- [Perspective Funnel Setup SOP](../client-fulfillment/media-buying/perspective-funnel-setup-sop.md)
- [perspective-client-manifest.yaml](../client-fulfillment/media-buying/perspective-client-manifest.yaml)
- [Identifying technical issues with clients](systems/identifying-technical-issues-with-clients.md)
- [RM client KPI check](systems/rm-client-kpi-check.md)
- [DSCR funnel form spec](../client-fulfillment/dscr-dna/dscr-funnel-form-spec.md)
- [RM funnel form spec](../client-fulfillment/reverse-mortgage-dna/rm-funnel-form-spec.md)
