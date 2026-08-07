# DSCR Lead Source ROI Calculator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a two-column Current vs Waiz lead-source ROI calculator for DSCR sales calls — internal Funnel Simulator sub-tab plus public sandbox URL — with linked spend, bidirectional CPL/leads, optional program fee, tooltips, and worst/best Waiz guidance.

**Architecture:** Pure client-side core under `src/lib/lead-source-roi/` (types, config, math, state). Shared `LeadSourceRoiCalculator` UI. Internal shell = Funnel Simulator host with sub-tabs (Funnel | Lead source ROI). Public shell = unauth `/tools/lead-source-roi` (middleware bypass). State share via base64 JSON query param `s=`, separate from existing Funnel Simulator `sim=`.

**Tech Stack:** Next.js App Router, React client components, existing Mr. Waiz dark ops styles, `node:test` + `tsx` (same as `kpi-simulator.test.ts`).

**Spec:** [docs/superpowers/specs/2026-08-07-dscr-lead-source-roi-calculator-design.md](../specs/2026-08-07-dscr-lead-source-roi-calculator-design.md)

**Repos:**
- Implementation → Mr. Waiz:
  ```bash
  cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
  ```
- Spec + this plan → Wm-os (`docs/superpowers/`)

When commands below say `MRWAIZ`, use the path above.

---

## File map

| File | Responsibility |
|------|----------------|
| `src/lib/lead-source-roi/types.ts` | Input/outcome/state types |
| `src/lib/lead-source-roi/config.ts` | Seeds, Waiz ranges, tooltips, disclaimer |
| `src/lib/lead-source-roi/math.ts` | Pure outcomes + worst/best packs + delta |
| `src/lib/lead-source-roi/state.ts` | Drivers, link rules, patches, encode/decode, defaults |
| `src/lib/lead-source-roi/math.test.ts` | Math unit tests |
| `src/lib/lead-source-roi/state.test.ts` | Drivers, links, encode/decode tests |
| `src/components/LeadSourceRoiCalculator.tsx` | Shared calculator UI |
| `src/components/FunnelSimulatorHub.tsx` | Sub-tabs: Funnel \| Lead source ROI |
| `src/components/DashboardView.tsx` | Mount hub; URL params for mode + ROI state |
| `src/app/tools/lead-source-roi/page.tsx` | Public unauth shell |
| `src/middleware.ts` | Bypass `/tools/lead-source-roi` |
| `package.json` | Include new test files in `test` script |

**Do not modify** `src/lib/kpi-simulator.ts` formula tables — this is a sibling product.

---

### Task 1: Types + config

**Files:**
- Create: `src/lib/lead-source-roi/types.ts`
- Create: `src/lib/lead-source-roi/config.ts`

- [ ] **Step 1: Create types**

```ts
// src/lib/lead-source-roi/types.ts

export type VolumeDriver = "cpl" | "leads";

export type SideKey = "current" | "waiz";

/** One side of the bake-off (Current or With Waiz). */
export type SideInputs = {
  ad_spend: number;
  cpl: number;
  leads: number;
  driver: VolumeDriver;
  /** 0–100 */
  contact_rate_pct: number;
  /** 0–100 — of contacts, not of leads */
  close_rate_pct: number;
  avg_commission: number;
  /** Used only when compare.include_fees is true */
  program_fee: number;
};

export type CompareState = {
  current: SideInputs;
  waiz: SideInputs;
  link_spend: boolean;
  link_commission: boolean;
  include_fees: boolean;
};

export type SideOutcomes = {
  leads: number;
  contacts: number;
  deals: number;
  gross_commission: number;
  investment: number;
  net_commission: number;
  /** gross / investment; null if investment <= 0 */
  roi_multiple: number | null;
  /** (gross - investment) / investment; null if investment <= 0 */
  roi_pct: number | null;
  /** ad_spend / contacts; null if contacts <= 0 */
  cost_per_conversation: number | null;
  /** investment / contacts when fees matter; same as above if fees off */
  cost_per_conversation_loaded: number | null;
};

export type DeltaOutcomes = {
  contacts: number;
  deals: number;
  net_commission: number;
  cost_per_conversation: number | null;
  roi_multiple: number | null;
  roi_pct: number | null;
};

export type CompareResult = {
  current: SideOutcomes;
  waiz: SideOutcomes;
  waiz_worst: SideOutcomes;
  waiz_best: SideOutcomes;
  delta: DeltaOutcomes;
};
```

- [ ] **Step 2: Create config (placeholder seeds — founder retunes later)**

```ts
// src/lib/lead-source-roi/config.ts
import type { CompareState, SideInputs } from "./types";

export const TOOL_TITLE = "Lead source ROI";
export const TOOL_SUBTITLE =
  "Same ad budget. Better economics downstream. DSCR lead-source bake-off.";

export const PUBLIC_DISCLAIMER =
  "Illustrative model for planning discussion. Results vary. Not a guarantee of performance or ROI.";

/** Placeholder demo — retune when DSCR deliverable bands are approved. */
export const DEMO_CURRENT: SideInputs = {
  ad_spend: 10_000,
  cpl: 75,
  leads: 0, // resolved by driver
  driver: "cpl",
  contact_rate_pct: 20,
  close_rate_pct: 15,
  avg_commission: 4_500,
  program_fee: 0,
};

export const DEMO_WAIZ: SideInputs = {
  ad_spend: 10_000,
  cpl: 55,
  leads: 0,
  driver: "cpl",
  contact_rate_pct: 32,
  close_rate_pct: 18,
  avg_commission: 4_500,
  program_fee: 3_500,
};

export const DEFAULT_COMPARE_STATE: CompareState = {
  current: { ...DEMO_CURRENT },
  waiz: { ...DEMO_WAIZ },
  link_spend: true,
  link_commission: true,
  include_fees: false,
};

/**
 * Waiz deliverable bands for captions + worst/best packs.
 * CPL: worst = higher $; best = lower $.
 * Rates: worst = lower %; best = higher %.
 */
export const WAIZ_RANGES = {
  cpl: { worst: 70, best: 45 },
  contact_rate_pct: { worst: 25, best: 40 },
  close_rate_pct: { worst: 14, best: 22 },
} as const;

export const FIELD_TOOLTIPS: Record<
  string,
  { definition: string; why: string }
> = {
  ad_spend: {
    definition: "Monthly media budget on this lead source.",
    why: "Locks the fair apples-to-apples spend story.",
  },
  cpl: {
    definition: "Cost per lead = ad spend ÷ leads.",
    why: "Lower CPL only wins if contact and close hold up.",
  },
  leads: {
    definition: "Leads generated at this spend and CPL.",
    why: "Top of the contact → close → commission chain.",
  },
  contact_rate_pct: {
    definition: "Share of leads that became a real conversation.",
    why: "Pickup and answer quality drive cost per conversation.",
  },
  close_rate_pct: {
    definition: "Share of conversations that fund or close.",
    why: "Close is measured on people spoken with — not raw leads.",
  },
  avg_commission: {
    definition: "Average gross commission per closed deal.",
    why: "Turns deals into dollars so net ROI is concrete.",
  },
  program_fee: {
    definition: "Monthly program or vendor fee (loaded cost).",
    why: "Shows full-loaded ROI when you include platform cost.",
  },
};

export function rangeCaption(
  field: keyof typeof WAIZ_RANGES,
): string {
  const r = WAIZ_RANGES[field];
  if (field === "cpl") {
    return `Typical deliverable: $${r.best}–$${r.worst}`;
  }
  return `Typical deliverable: ${r.worst}–${r.best}%`;
}
```

- [ ] **Step 3: Commit**

```bash
cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
git add src/lib/lead-source-roi/types.ts src/lib/lead-source-roi/config.ts
git commit -m "feat(lead-source-roi): add types and config seeds"
```

---

### Task 2: Math module (TDD)

**Files:**
- Create: `src/lib/lead-source-roi/math.ts`
- Create: `src/lib/lead-source-roi/math.test.ts`

- [ ] **Step 1: Write failing tests**

```ts
// src/lib/lead-source-roi/math.test.ts
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import {
  resolveVolume,
  simulateSide,
  simulateCompare,
  applyWaizPack,
} from "./math";
import type { CompareState, SideInputs } from "./types";
import { DEFAULT_COMPARE_STATE } from "./config";

function side(over: Partial<SideInputs> = {}): SideInputs {
  return {
    ad_spend: 10_000,
    cpl: 100,
    leads: 0,
    driver: "cpl",
    contact_rate_pct: 20,
    close_rate_pct: 25,
    avg_commission: 4_000,
    program_fee: 2_000,
    ...over,
  };
}

describe("lead-source-roi math", () => {
  it("resolveVolume with driver=cpl derives leads from spend/cpl", () => {
    const v = resolveVolume(side({ ad_spend: 10_000, cpl: 100, driver: "cpl" }));
    assert.equal(v.leads, 100);
    assert.equal(v.cpl, 100);
  });

  it("resolveVolume with driver=leads derives cpl from spend/leads", () => {
    const v = resolveVolume(
      side({ ad_spend: 10_000, leads: 200, driver: "leads", cpl: 0 }),
    );
    assert.equal(v.leads, 200);
    assert.equal(v.cpl, 50);
  });

  it("resolveVolume guards zero divisor", () => {
    const v = resolveVolume(side({ ad_spend: 10_000, cpl: 0, driver: "cpl" }));
    assert.equal(v.leads, 0);
  });

  it("simulateSide: contact and close chain + ROI formulas", () => {
    // 100 leads, 20% contact = 20, 25% close = 5 deals
    // gross = 5 * 4000 = 20000; investment ad only = 10000
    const out = simulateSide(
      side({
        ad_spend: 10_000,
        cpl: 100,
        driver: "cpl",
        contact_rate_pct: 20,
        close_rate_pct: 25,
        avg_commission: 4_000,
        program_fee: 2_000,
      }),
      false,
    );
    assert.equal(out.leads, 100);
    assert.equal(out.contacts, 20);
    assert.equal(out.deals, 5);
    assert.equal(out.gross_commission, 20_000);
    assert.equal(out.investment, 10_000);
    assert.equal(out.net_commission, 10_000);
    assert.equal(out.roi_multiple, 2);
    assert.equal(out.roi_pct, 1);
    assert.equal(out.cost_per_conversation, 500);
  });

  it("simulateSide includes program fee when includeFees true", () => {
    const out = simulateSide(
      side({
        ad_spend: 10_000,
        cpl: 100,
        driver: "cpl",
        contact_rate_pct: 20,
        close_rate_pct: 25,
        avg_commission: 4_000,
        program_fee: 2_000,
      }),
      true,
    );
    assert.equal(out.investment, 12_000);
    assert.equal(out.net_commission, 8_000);
    assert.ok(out.cost_per_conversation_loaded != null);
    assert.equal(out.cost_per_conversation_loaded, 600); // 12000/20
  });

  it("simulateSide returns null ROI when investment is 0", () => {
    const out = simulateSide(
      side({ ad_spend: 0, cpl: 100, program_fee: 0 }),
      false,
    );
    assert.equal(out.roi_multiple, null);
    assert.equal(out.roi_pct, null);
  });

  it("applyWaizPack worst raises CPL and lowers rates", () => {
    const base = side({
      cpl: 55,
      contact_rate_pct: 32,
      close_rate_pct: 18,
      driver: "cpl",
    });
    const worst = applyWaizPack(base, "worst");
    assert.ok(worst.cpl >= base.cpl);
    assert.ok(worst.contact_rate_pct <= base.contact_rate_pct);
    assert.ok(worst.close_rate_pct <= base.close_rate_pct);
    assert.equal(worst.driver, "cpl");
  });

  it("simulateCompare: worst net <= base net <= best net for demo shape", () => {
    const state: CompareState = {
      ...DEFAULT_COMPARE_STATE,
      include_fees: false,
      link_spend: true,
    };
    const r = simulateCompare(state);
    assert.ok(r.waiz_worst.net_commission <= r.waiz.net_commission + 1e-9);
    assert.ok(r.waiz.net_commission <= r.waiz_best.net_commission + 1e-9);
    assert.equal(
      r.delta.net_commission,
      r.waiz.net_commission - r.current.net_commission,
    );
  });
});
```

- [ ] **Step 2: Run tests — expect FAIL (module missing)**

```bash
cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
npx --yes tsx --test src/lib/lead-source-roi/math.test.ts
```

Expected: fail to resolve `./math` or missing exports.

- [ ] **Step 3: Implement math.ts**

```ts
// src/lib/lead-source-roi/math.ts
import { WAIZ_RANGES } from "./config";
import type {
  CompareResult,
  CompareState,
  DeltaOutcomes,
  SideInputs,
  SideOutcomes,
} from "./types";

export function resolveVolume(side: SideInputs): { leads: number; cpl: number } {
  const spend = Math.max(0, side.ad_spend || 0);
  if (side.driver === "leads") {
    const leads = Math.max(0, side.leads || 0);
    const cpl = leads > 0 ? spend / leads : 0;
    return { leads, cpl };
  }
  const cpl = Math.max(0, side.cpl || 0);
  const leads = cpl > 0 ? spend / cpl : 0;
  return { leads, cpl };
}

function clampPct(n: number): number {
  if (!Number.isFinite(n)) return 0;
  return Math.min(100, Math.max(0, n));
}

export function simulateSide(
  side: SideInputs,
  includeFees: boolean,
): SideOutcomes {
  const { leads, cpl: _cpl } = resolveVolume(side);
  const contact = clampPct(side.contact_rate_pct) / 100;
  const close = clampPct(side.close_rate_pct) / 100;
  const contacts = leads * contact;
  const deals = contacts * close;
  const gross = deals * Math.max(0, side.avg_commission || 0);
  const fee = includeFees ? Math.max(0, side.program_fee || 0) : 0;
  const investment = Math.max(0, side.ad_spend || 0) + fee;

  const roi_multiple = investment > 0 ? gross / investment : null;
  const roi_pct = investment > 0 ? (gross - investment) / investment : null;
  const cost_per_conversation =
    contacts > 0 ? Math.max(0, side.ad_spend || 0) / contacts : null;
  const cost_per_conversation_loaded =
    contacts > 0 ? investment / contacts : null;

  return {
    leads,
    contacts,
    deals,
    gross_commission: gross,
    investment,
    net_commission: gross - investment,
    roi_multiple,
    roi_pct,
    cost_per_conversation,
    cost_per_conversation_loaded,
  };
}

export function applyWaizPack(
  base: SideInputs,
  pack: "worst" | "best",
): SideInputs {
  const r = WAIZ_RANGES;
  return {
    ...base,
    driver: "cpl",
    cpl: pack === "worst" ? r.cpl.worst : r.cpl.best,
    contact_rate_pct:
      pack === "worst"
        ? r.contact_rate_pct.worst
        : r.contact_rate_pct.best,
    close_rate_pct:
      pack === "worst" ? r.close_rate_pct.worst : r.close_rate_pct.best,
    // leads discarded; driver cpl recomputes
    leads: 0,
  };
}

function deltaOf(
  current: SideOutcomes,
  waiz: SideOutcomes,
): DeltaOutcomes {
  const dCpc =
    current.cost_per_conversation != null &&
    waiz.cost_per_conversation != null
      ? waiz.cost_per_conversation - current.cost_per_conversation
      : null;
  const dMult =
    current.roi_multiple != null && waiz.roi_multiple != null
      ? waiz.roi_multiple - current.roi_multiple
      : null;
  const dPct =
    current.roi_pct != null && waiz.roi_pct != null
      ? waiz.roi_pct - current.roi_pct
      : null;
  return {
    contacts: waiz.contacts - current.contacts,
    deals: waiz.deals - current.deals,
    net_commission: waiz.net_commission - current.net_commission,
    cost_per_conversation: dCpc,
    roi_multiple: dMult,
    roi_pct: dPct,
  };
}

export function simulateCompare(state: CompareState): CompareResult {
  const current = simulateSide(state.current, state.include_fees);
  const waiz = simulateSide(state.waiz, state.include_fees);
  const waiz_worst = simulateSide(
    applyWaizPack(state.waiz, "worst"),
    state.include_fees,
  );
  const waiz_best = simulateSide(
    applyWaizPack(state.waiz, "best"),
    state.include_fees,
  );
  return {
    current,
    waiz,
    waiz_worst,
    waiz_best,
    delta: deltaOf(current, waiz),
  };
}
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
npx --yes tsx --test src/lib/lead-source-roi/math.test.ts
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/lib/lead-source-roi/math.ts src/lib/lead-source-roi/math.test.ts
git commit -m "feat(lead-source-roi): pure math + unit tests"
```

---

### Task 3: State — drivers, links, encode/decode (TDD)

**Files:**
- Create: `src/lib/lead-source-roi/state.ts`
- Create: `src/lib/lead-source-roi/state.test.ts`

- [ ] **Step 1: Write failing tests**

```ts
// src/lib/lead-source-roi/state.test.ts
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import {
  createDefaultState,
  patchSide,
  setLinkSpend,
  setIncludeFees,
  encodeCompareState,
  decodeCompareState,
  normalizeSide,
} from "./state";
import { resolveVolume } from "./math";

describe("lead-source-roi state", () => {
  it("createDefaultState resolves volume on both sides", () => {
    const s = createDefaultState();
    const c = resolveVolume(s.current);
    assert.ok(c.leads > 0);
    assert.equal(s.link_spend, true);
    assert.equal(s.include_fees, false);
  });

  it("patch current spend with link_spend mirrors to waiz", () => {
    let s = createDefaultState();
    s = patchSide(s, "current", { ad_spend: 20_000 });
    assert.equal(s.current.ad_spend, 20_000);
    assert.equal(s.waiz.ad_spend, 20_000);
  });

  it("unlinked spend does not mirror", () => {
    let s = setLinkSpend(createDefaultState(), false);
    s = patchSide(s, "current", { ad_spend: 15_000 });
    assert.equal(s.current.ad_spend, 15_000);
    assert.notEqual(s.waiz.ad_spend, 15_000);
  });

  it("editing cpl sets driver and recomputes leads", () => {
    let s = createDefaultState();
    s = patchSide(s, "current", { cpl: 50 });
    assert.equal(s.current.driver, "cpl");
    assert.equal(s.current.leads, s.current.ad_spend / 50);
  });

  it("editing leads sets driver and recomputes cpl", () => {
    let s = createDefaultState();
    s = patchSide(s, "current", { leads: 250 });
    assert.equal(s.current.driver, "leads");
    assert.equal(s.current.cpl, s.current.ad_spend / 250);
  });

  it("link_commission mirrors avg_commission", () => {
    let s = createDefaultState();
    s = patchSide(s, "current", { avg_commission: 6_000 });
    assert.equal(s.waiz.avg_commission, 6_000);
  });

  it("encode/decode round-trips", () => {
    let s = createDefaultState();
    s = patchSide(s, "current", { ad_spend: 12_345, contact_rate_pct: 22 });
    s = setIncludeFees(s, true);
    const enc = encodeCompareState(s);
    const dec = decodeCompareState(enc);
    assert.ok(dec);
    assert.equal(dec!.current.ad_spend, 12_345);
    assert.equal(dec!.current.contact_rate_pct, 22);
    assert.equal(dec!.include_fees, true);
    assert.equal(dec!.waiz.ad_spend, 12_345);
  });

  it("decode garbage returns null", () => {
    assert.equal(decodeCompareState("%%%not-base64%%%"), null);
  });

  it("normalizeSide clamps percentages", () => {
    const n = normalizeSide({
      ad_spend: 1000,
      cpl: 10,
      leads: 0,
      driver: "cpl",
      contact_rate_pct: 150,
      close_rate_pct: -5,
      avg_commission: 100,
      program_fee: 0,
    });
    assert.equal(n.contact_rate_pct, 100);
    assert.equal(n.close_rate_pct, 0);
  });
});
```

- [ ] **Step 2: Run — expect FAIL**

```bash
npx --yes tsx --test src/lib/lead-source-roi/state.test.ts
```

- [ ] **Step 3: Implement state.ts**

```ts
// src/lib/lead-source-roi/state.ts
import { DEFAULT_COMPARE_STATE } from "./config";
import { resolveVolume } from "./math";
import type { CompareState, SideInputs, SideKey, VolumeDriver } from "./types";

function clampPct(n: number): number {
  if (!Number.isFinite(n)) return 0;
  return Math.min(100, Math.max(0, n));
}

function finite(n: unknown, fallback = 0): number {
  const x = typeof n === "number" ? n : Number(n);
  return Number.isFinite(x) ? x : fallback;
}

export function normalizeSide(raw: SideInputs): SideInputs {
  const driver: VolumeDriver = raw.driver === "leads" ? "leads" : "cpl";
  const base: SideInputs = {
    ad_spend: Math.max(0, finite(raw.ad_spend)),
    cpl: Math.max(0, finite(raw.cpl)),
    leads: Math.max(0, finite(raw.leads)),
    driver,
    contact_rate_pct: clampPct(finite(raw.contact_rate_pct)),
    close_rate_pct: clampPct(finite(raw.close_rate_pct)),
    avg_commission: Math.max(0, finite(raw.avg_commission)),
    program_fee: Math.max(0, finite(raw.program_fee)),
  };
  const vol = resolveVolume(base);
  return { ...base, leads: vol.leads, cpl: vol.cpl };
}

export function createDefaultState(): CompareState {
  return {
    current: normalizeSide(DEFAULT_COMPARE_STATE.current),
    waiz: normalizeSide({
      ...DEFAULT_COMPARE_STATE.waiz,
      ad_spend: DEFAULT_COMPARE_STATE.current.ad_spend,
      avg_commission: DEFAULT_COMPARE_STATE.current.avg_commission,
    }),
    link_spend: true,
    link_commission: true,
    include_fees: false,
  };
}

export function setLinkSpend(state: CompareState, on: boolean): CompareState {
  if (!on) return { ...state, link_spend: false };
  const waiz = normalizeSide({
    ...state.waiz,
    ad_spend: state.current.ad_spend,
  });
  return { ...state, link_spend: true, waiz };
}

export function setLinkCommission(state: CompareState, on: boolean): CompareState {
  if (!on) return { ...state, link_commission: false };
  const waiz = normalizeSide({
    ...state.waiz,
    avg_commission: state.current.avg_commission,
  });
  return { ...state, link_commission: true, waiz };
}

export function setIncludeFees(state: CompareState, on: boolean): CompareState {
  return { ...state, include_fees: on };
}

export type SidePatch = Partial<
  Pick<
    SideInputs,
    | "ad_spend"
    | "cpl"
    | "leads"
    | "contact_rate_pct"
    | "close_rate_pct"
    | "avg_commission"
    | "program_fee"
  >
>;

export function patchSide(
  state: CompareState,
  key: SideKey,
  patch: SidePatch,
): CompareState {
  const prev = state[key];
  let next: SideInputs = { ...prev };

  if (patch.cpl !== undefined) {
    next.cpl = Math.max(0, finite(patch.cpl));
    next.driver = "cpl";
  }
  if (patch.leads !== undefined) {
    next.leads = Math.max(0, finite(patch.leads));
    next.driver = "leads";
  }
  if (patch.ad_spend !== undefined) {
    next.ad_spend = Math.max(0, finite(patch.ad_spend));
  }
  if (patch.contact_rate_pct !== undefined) {
    next.contact_rate_pct = clampPct(finite(patch.contact_rate_pct));
  }
  if (patch.close_rate_pct !== undefined) {
    next.close_rate_pct = clampPct(finite(patch.close_rate_pct));
  }
  if (patch.avg_commission !== undefined) {
    next.avg_commission = Math.max(0, finite(patch.avg_commission));
  }
  if (patch.program_fee !== undefined) {
    next.program_fee = Math.max(0, finite(patch.program_fee));
  }

  next = normalizeSide(next);
  let out: CompareState = { ...state, [key]: next };

  if (key === "current" && out.link_spend && patch.ad_spend !== undefined) {
    out = {
      ...out,
      waiz: normalizeSide({ ...out.waiz, ad_spend: out.current.ad_spend }),
    };
  }
  if (
    key === "current" &&
    out.link_commission &&
    patch.avg_commission !== undefined
  ) {
    out = {
      ...out,
      waiz: normalizeSide({
        ...out.waiz,
        avg_commission: out.current.avg_commission,
      }),
    };
  }

  return out;
}

/** URL-safe-ish base64 JSON. Keep payload small. */
export function encodeCompareState(state: CompareState): string {
  const payload = {
    v: 1 as const,
    c: state.current,
    w: state.waiz,
    ls: state.link_spend,
    lc: state.link_commission,
    f: state.include_fees,
  };
  if (typeof btoa === "function") {
    return btoa(JSON.stringify(payload));
  }
  return Buffer.from(JSON.stringify(payload), "utf8").toString("base64");
}

export function decodeCompareState(encoded: string): CompareState | null {
  try {
    const json =
      typeof atob === "function"
        ? atob(encoded)
        : Buffer.from(encoded, "base64").toString("utf8");
    const parsed = JSON.parse(json) as {
      v?: number;
      c?: SideInputs;
      w?: SideInputs;
      ls?: boolean;
      lc?: boolean;
      f?: boolean;
    };
    if (!parsed?.c || !parsed?.w) return null;
    return {
      current: normalizeSide(parsed.c),
      waiz: normalizeSide(parsed.w),
      link_spend: parsed.ls !== false,
      link_commission: parsed.lc !== false,
      include_fees: !!parsed.f,
    };
  } catch {
    return null;
  }
}
```

- [ ] **Step 4: Run — expect PASS**

```bash
npx --yes tsx --test src/lib/lead-source-roi/state.test.ts src/lib/lead-source-roi/math.test.ts
```

- [ ] **Step 5: Commit**

```bash
git add src/lib/lead-source-roi/state.ts src/lib/lead-source-roi/state.test.ts
git commit -m "feat(lead-source-roi): drivers, links, encode/decode"
```

---

### Task 4: Shared calculator UI

**Files:**
- Create: `src/components/LeadSourceRoiCalculator.tsx`

- [ ] **Step 1: Implement component**

Match Funnel Simulator colors (`#080f1e` / `#0a1628` panels, muted `#475569` / `#94a3b8`, green delta). Structure:

Props:

```ts
type Props = {
  /** Public shell shows disclaimer + lighter chrome helper copy */
  variant: "internal" | "public";
  initialEncoded?: string | null;
  onStateChange?: (encoded: string) => void;
};
```

Behavior requirements (implement fully in the file):

1. `useState` initialized via `decodeCompareState(initialEncoded) || createDefaultState()`.
2. On decode fail with provided `initialEncoded`, use defaults + show a small inline notice: “Couldn’t load shared state — showing demo.”
3. `useEffect` → `onStateChange?.(encodeCompareState(state))` whenever state changes.
4. Header: `TOOL_TITLE`, `TOOL_SUBTITLE`, buttons **Reset** (→ `createDefaultState()`), **Copy public link**:
   - Build: `${window.location.origin}/tools/lead-source-roi?s=${encodeURIComponent(encodeCompareState(state))}`
   - `navigator.clipboard.writeText` + temporary “Copied” label.
5. Controls row:
   - Radio/toggle: **Ad spend only** vs **Include program fee** → `setIncludeFees`
   - Toggle: **Spend linked** / **Unlinked** → `setLinkSpend`
   - Toggle: **Commission linked** / **Unlinked** → `setLinkCommission` (compact)
6. Two columns: **Current stack** | **With Waiz**
   - Fields with number inputs (not range sliders required): ad spend, CPL, leads, contact %, close %, avg commission, and program fee when `include_fees`.
   - Waiz column: under CPL, contact %, close % show `rangeCaption(...)`.
   - Each field label has a `?` button; on click/focus shows tooltip definition + why (popover or title-adjacent expand). Use existing simple pattern: absolute small panel, not a dependency.
   - Waiz spend input disabled when `link_spend`; commission disabled when `link_commission` (or still editable but documents mirror — prefer disabled read-through for clarity, with note “linked to Current”).
7. Outcomes section from `simulateCompare(state)`:
   - Rows: Contacts, Deals, Cost / conversation (use loaded when fees on; label “Cost / conversation (loaded)” when fees on), Net commission $, ROI ×, ROI %.
   - Three values per row: Current | Waiz base | Delta.
   - Under Waiz net $ and deals: secondary text  
     `Range: $worst – $best` from `waiz_worst` / `waiz_best`.
   - Hero strip: large delta net commission (green if ≥ 0, red if < 0).
8. Footer: always show `PUBLIC_DISCLAIMER` on `variant === "public"`; show a one-line version on internal too.
9. Formatting helpers local to file: money `$12,345`, pct `32.0%`, multiple `2.1×`, integer leads.

Scaffold start (expand to full JSX — engineer may refine markup but must hit requirements above):

```tsx
"use client";

import { useEffect, useMemo, useState } from "react";
import {
  FIELD_TOOLTIPS,
  PUBLIC_DISCLAIMER,
  TOOL_SUBTITLE,
  TOOL_TITLE,
  rangeCaption,
} from "@/lib/lead-source-roi/config";
import { simulateCompare } from "@/lib/lead-source-roi/math";
import {
  createDefaultState,
  decodeCompareState,
  encodeCompareState,
  patchSide,
  setIncludeFees,
  setLinkCommission,
  setLinkSpend,
  type SidePatch,
} from "@/lib/lead-source-roi/state";
import type { CompareState, SideKey } from "@/lib/lead-source-roi/types";

type Props = {
  variant: "internal" | "public";
  initialEncoded?: string | null;
  onStateChange?: (encoded: string) => void;
};

// ... helpers: formatMoney, formatPct, formatMult, FieldTooltip, SideColumn ...

export default function LeadSourceRoiCalculator({
  variant,
  initialEncoded,
  onStateChange,
}: Props) {
  const [loadError, setLoadError] = useState(false);
  const [copied, setCopied] = useState(false);
  const [state, setState] = useState<CompareState>(() => {
    if (initialEncoded) {
      const d = decodeCompareState(initialEncoded);
      if (d) return d;
      // mark error after mount via effect if needed
    }
    return createDefaultState();
  });

  useEffect(() => {
    if (initialEncoded && !decodeCompareState(initialEncoded)) {
      setLoadError(true);
    }
  }, [initialEncoded]);

  useEffect(() => {
    onStateChange?.(encodeCompareState(state));
  }, [state, onStateChange]);

  const result = useMemo(() => simulateCompare(state), [state]);

  function onPatch(key: SideKey, patch: SidePatch) {
    setState((s) => patchSide(s, key, patch));
  }

  async function copyPublicLink() {
    const url = `${window.location.origin}/tools/lead-source-roi?s=${encodeURIComponent(encodeCompareState(state))}`;
    try {
      await navigator.clipboard.writeText(url);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* ignore */
    }
  }

  // Render full UI per requirements 4–9.
  return (
    <div className="flex-1 min-h-0 overflow-auto p-4 md:p-6" style={{ color: "#e2e8f0" }}>
      {/* header, controls, columns, outcomes, disclaimer */}
      {(variant === "public" || true) && (
        <p className="text-xs mt-6" style={{ color: "#64748b" }}>
          {PUBLIC_DISCLAIMER}
        </p>
      )}
    </div>
  );
}
```

**Important:** Do not leave the scaffold stub — complete the two columns, outcomes table, and hero delta so the calculator is usable on a sales call. Prefer dense readable ops UI over marketing layout.

- [ ] **Step 2: Smoke-check TypeScript**

```bash
cd "/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy"
npx tsc --noEmit 2>&1 | head -40
```

Fix any type errors in the new files.

- [ ] **Step 3: Commit**

```bash
git add src/components/LeadSourceRoiCalculator.tsx
git commit -m "feat(lead-source-roi): shared calculator UI"
```

---

### Task 5: Internal shell — Funnel Simulator sub-tabs

**Files:**
- Create: `src/components/FunnelSimulatorHub.tsx`
- Modify: `src/components/DashboardView.tsx`

- [ ] **Step 1: Create hub**

```tsx
// src/components/FunnelSimulatorHub.tsx
"use client";

import { useState } from "react";
import FunnelSimulatorView from "./FunnelSimulatorView";
import LeadSourceRoiCalculator from "./LeadSourceRoiCalculator";
import type { MetricsResult } from "@/lib/metrics";

type SimTab = "funnel" | "lead_source_roi";

type Props = {
  metrics: MetricsResult | null;
  metricsLoading: boolean;
  clientLabel?: string;
  clientIsRm: boolean;
  dateRangeLabel: string;
  onViewActuals?: () => void;
  initialFunnelEncoded?: string | null;
  onFunnelStateChange?: (encoded: string) => void;
  initialRoiEncoded?: string | null;
  onRoiStateChange?: (encoded: string) => void;
  initialTab?: SimTab;
  onTabChange?: (tab: SimTab) => void;
};

export default function FunnelSimulatorHub(props: Props) {
  const [tab, setTab] = useState<SimTab>(props.initialTab || "funnel");

  function select(next: SimTab) {
    setTab(next);
    props.onTabChange?.(next);
  }

  return (
    <div className="flex-1 min-h-0 flex flex-col">
      <div
        className="flex gap-1 px-4 pt-3 pb-0 shrink-0"
        style={{ borderBottom: "1px solid rgba(255,255,255,0.06)" }}
      >
        {(
          [
            ["funnel", "Funnel"],
            ["lead_source_roi", "Lead source ROI"],
          ] as const
        ).map(([key, label]) => {
          const active = tab === key;
          return (
            <button
              key={key}
              type="button"
              onClick={() => select(key)}
              className="px-3 py-2 text-sm font-medium"
              style={{
                color: active ? "#f59e0b" : "#94a3b8",
                borderBottom: active ? "2px solid #f59e0b" : "2px solid transparent",
              }}
            >
              {label}
            </button>
          );
        })}
      </div>
      {tab === "funnel" ? (
        <FunnelSimulatorView
          metrics={props.metrics}
          metricsLoading={props.metricsLoading}
          clientLabel={props.clientLabel}
          clientIsRm={props.clientIsRm}
          dateRangeLabel={props.dateRangeLabel}
          onViewActuals={props.onViewActuals}
          initialEncoded={props.initialFunnelEncoded}
          onStateChange={props.onFunnelStateChange}
        />
      ) : (
        <LeadSourceRoiCalculator
          variant="internal"
          initialEncoded={props.initialRoiEncoded}
          onStateChange={props.onRoiStateChange}
        />
      )}
    </div>
  );
}
```

- [ ] **Step 2: Wire DashboardView**

1. Change lazy import of `FunnelSimulatorView` to `FunnelSimulatorHub` (or add parallel lazy import).
2. Replace `view === "kpi_simulator"` block that renders `FunnelSimulatorView` with `FunnelSimulatorHub`.
3. URL params:
   - Keep `sim` for funnel encode (existing `updateSimulatorUrl`).
   - Add `roi` for lead-source encode.
   - Add `simTab=funnel|lead_source_roi` (or `sub` if you prefer reuse) — on tab change write into query via `router.replace`.
4. Pass:
   - `initialFunnelEncoded={searchParams.get("sim")}`
   - `initialRoiEncoded={searchParams.get("roi")}`
   - `initialTab` from `searchParams.get("simTab") === "lead_source_roi" ? "lead_source_roi" : "funnel"`
   - `onRoiStateChange` that sets `view=kpi_simulator`, `roi=<encoded>`, preserves other params.

Example helper:

```ts
const updateRoiUrl = useCallback((encoded: string) => {
  const params = new URLSearchParams(searchParams.toString());
  params.set("view", "kpi_simulator");
  params.set("simTab", "lead_source_roi");
  params.set("roi", encoded);
  router.replace(`${pathname}?${params.toString()}`, { scroll: false });
}, [searchParams, pathname, router]);
```

- [ ] **Step 3: Manual check (dev server)**

```bash
npm run dev
```

Open dashboard → Funnel Simulator → switch **Lead source ROI** → change Current spend → Waiz spend tracks → Copy public link copies `/tools/...` URL.

- [ ] **Step 4: Commit**

```bash
git add src/components/FunnelSimulatorHub.tsx src/components/DashboardView.tsx
git commit -m "feat(lead-source-roi): Funnel Simulator sub-tab shell"
```

---

### Task 6: Public route + middleware bypass

**Files:**
- Create: `src/app/tools/lead-source-roi/page.tsx`
- Modify: `src/middleware.ts`

- [ ] **Step 1: Add middleware bypass**

In `src/middleware.ts`, add to `BYPASS_ROUTES`:

```ts
  '/tools/lead-source-roi',
```

Place near other public form/report routes.

- [ ] **Step 2: Public page**

```tsx
// src/app/tools/lead-source-roi/page.tsx
"use client";

import { useSearchParams } from "next/navigation";
import { Suspense } from "react";
import LeadSourceRoiCalculator from "@/components/LeadSourceRoiCalculator";
import { TOOL_TITLE } from "@/lib/lead-source-roi/config";

function CalculatorFromQuery() {
  const searchParams = useSearchParams();
  const encoded = searchParams.get("s");
  return (
    <LeadSourceRoiCalculator variant="public" initialEncoded={encoded} />
  );
}

export default function LeadSourceRoiPublicPage() {
  return (
    <div className="min-h-screen flex flex-col" style={{ background: "#080f1e" }}>
      <header
        className="px-4 py-3 flex items-center justify-between"
        style={{ borderBottom: "1px solid rgba(255,255,255,0.06)" }}
      >
        <div>
          <p className="text-xs uppercase tracking-wide" style={{ color: "#64748b" }}>
            Waiz Media
          </p>
          <h1 className="text-lg font-semibold" style={{ color: "#e2e8f0" }}>
            {TOOL_TITLE}
          </h1>
        </div>
      </header>
      <Suspense
        fallback={
          <p className="p-6 text-sm" style={{ color: "#94a3b8" }}>
            Loading calculator…
          </p>
        }
      >
        <CalculatorFromQuery />
      </Suspense>
    </div>
  );
}
```

Note: if Next requires a small `loading.tsx` or forces static, keep this client page simple. No auth imports.

- [ ] **Step 3: Verify unauth access**

With dev server running, open private window:

`http://localhost:3000/tools/lead-source-roi`

Expected: calculator, **no** redirect to `/login`.

Open a copied `?s=` link from internal tool: state prefilled; all fields editable.

- [ ] **Step 4: Commit**

```bash
git add src/app/tools/lead-source-roi/page.tsx src/middleware.ts
git commit -m "feat(lead-source-roi): public sandbox route"
```

---

### Task 7: Test script + final verification

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Expand test script**

Replace the `test` script with:

```json
"test": "npx --yes tsx --test src/lib/kpi-simulator.test.ts src/lib/lead-source-roi/math.test.ts src/lib/lead-source-roi/state.test.ts"
```

- [ ] **Step 2: Run full unit suite**

```bash
npm test
```

Expected: all existing kpi-simulator tests + new lead-source-roi tests pass.

- [ ] **Step 3: Spec acceptance checklist (manual)**

| Criterion | Check |
|-----------|--------|
| Current filled ≤ ~90s | Editable spend/CPL/rates |
| Hero delta net $ | Visible |
| Tooltips on fields | `?` works |
| Fee toggle | Off = media only; on = investment rises |
| Spend link | Tracks Current → Waiz |
| Full sandbox public | All fields editable both columns |
| Worst/best captions | Under Waiz CPL/contact/close |
| Outcome band | Range under net $ / deals |
| Disclaimer | Public footer |
| No kpi-simulator math changed | Diff only sibling files |

- [ ] **Step 4: Commit**

```bash
git add package.json
git commit -m "test(lead-source-roi): include ROI calculator in npm test"
```

---

### Task 8: Optional config retune note (no code required)

After first real DSCR sales use, founder updates only:

- `DEMO_CURRENT` / `DEMO_WAIZ`
- `WAIZ_RANGES`
- default `DEMO_WAIZ.program_fee`

File: `src/lib/lead-source-roi/config.ts`

No further feature work in v1.

---

## Spec coverage self-review

| Spec requirement | Task |
|------------------|------|
| Current vs Waiz columns | Task 4 |
| Linked spend + editable rates | Tasks 3–4 |
| Bidirectional spend/CPL/leads | Tasks 2–3 |
| Contact + close of contacts | Task 2 |
| Avg commission + link | Task 3–4 |
| Fee toggle C | Tasks 3–4 |
| ROI hero net $ + × + % | Task 4 |
| Cost per conversation | Task 2–4 |
| Tooltips | Task 4 + config |
| Worst/best captions + outcome band | Tasks 1–2, 4 |
| Full public sandbox | Tasks 4, 6 |
| URL share state | Tasks 3, 4, 5, 6 |
| Mr. Waiz Funnel sub-tab | Task 5 |
| Shared core | Tasks 1–3 |
| Unit tests | Tasks 2–3, 7 |
| Disclaimer | Task 1, 4 |
| No live metrics / no DB | Out by design |
| Sibling not merge into kpi-simulator | File map + Task 5 |

**Placeholder scan:** Seeds are intentionally named placeholders with retune path (Task 8). No TBD steps in implementation tasks.

**Type consistency:** `CompareState`, `SideInputs`, `VolumeDriver`, `patchSide`, `simulateCompare`, `encodeCompareState` used consistently across tasks.

---

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-08-07-dscr-lead-source-roi-calculator.md`.

Two execution options:

1. **Subagent-Driven (recommended)** — fresh subagent per task, review between tasks, fast iteration  
2. **Inline Execution** — execute tasks in this session with checkpoints  

Which approach?
