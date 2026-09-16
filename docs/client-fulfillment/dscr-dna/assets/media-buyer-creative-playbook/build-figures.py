#!/usr/bin/env python3
"""Figures for the DSCR Media Buyer Creative Playbook PDF."""

import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = pathlib.Path(__file__).resolve().parent

NAVY = "#061A4A"
STEEL = "#1C4C80"
SKY = "#9FC2E8"
WASH = "#E4EDF8"
PAPER = "#FFFFFF"
INK = "#0B1220"
MUTED = "#5F6B7C"
LINE = "#C9D6E6"
AMBER = "#C47A12"
GREEN = "#1F7A5C"
CLAY = "#9C5B3C"

FONT = "DejaVu Sans"
plt.rcParams["font.family"] = FONT
PRINT_W = 6.05


def canvas(w, h):
    fig = plt.figure(figsize=(PRINT_W, PRINT_W * h / w), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 * h / w)
    ax.axis("off")
    fig.patch.set_facecolor(PAPER)
    return fig, ax


def save(fig, name):
    path = OUT / f"{name}.png"
    fig.savefig(path, facecolor=PAPER, edgecolor="none",
                bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(path.name)


def box(ax, x, y, w, h, fc=PAPER, ec=LINE, lw=1.4, r=1.4, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z))


def label(ax, x, y, text, size=9, color=INK, weight="normal",
          ha="center", va="center", z=5):
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=z, linespacing=1.35)


def arrow(ax, p1, p2, color=STEEL, lw=1.4, z=3):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle="-|>", mutation_scale=11, color=color,
        linewidth=lw, zorder=z, shrinkA=2, shrinkB=2))


def fig_bucket_map():
    """Four bucket cards + shared warm strip."""
    fig, ax = canvas(100, 72)

    label(ax, 50, 68, "What stops this investor from acting today?",
          size=11, color=NAVY, weight="bold")

    cards = [
        (3, 36, "DENIED", "Bank says no", "Program reveal", "nodocs-speed", WASH, STEEL),
        (27, 36, "DEADLINE", "Note has a date", "Mapped exit", "balloon-exit", "#FFF4E5", AMBER),
        (51, 36, "IDLE", "Equity sits", "Belief break", "cashout-grow", "#EAF5F0", GREEN),
        (75, 36, "IN-MARKET", "Already shopping", "Offer / terms", "ratecard-centered", "#F3EEF0", CLAY),
    ]
    for x, y, title, sub, job, slug, fc, ec in cards:
        box(ax, x, y, 22, 26, fc=fc, ec=ec, lw=1.8)
        label(ax, x + 11, y + 21, title, size=10, color=ec, weight="bold")
        label(ax, x + 11, y + 15.5, sub, size=7.5, color=MUTED)
        label(ax, x + 11, y + 9.5, job, size=8, color=INK, weight="bold")
        label(ax, x + 11, y + 4, f"`{slug}`", size=6.5, color=MUTED)

    for x in (14, 38, 62):
        arrow(ax, (x + 11, 36), (x + 11, 28), color=LINE, lw=1.1)

    box(ax, 8, 8, 84, 16, fc=NAVY, ec=NAVY)
    label(ax, 50, 18.5, "SHARED WARM (any door that entered)", size=8.5,
          color="#9FC2E8", weight="bold")
    label(ax, 50, 12.5,
          "Outcome / uses   ·   Checklist / terms   ·   Lender authority",
          size=9, color=PAPER)

    save(fig, "fig-bucket-map")


def fig_sort_rule():
    """Decision tree: deadline → denied → idle → in-market."""
    fig, ax = canvas(100, 78)

    label(ax, 50, 74, "Sorting rule — one ad = one bucket", size=11,
          color=NAVY, weight="bold")

    steps = [
        (58, "1. Date on the note?", "DEADLINE", AMBER, "#FFF4E5"),
        (44, "2. Conventional would say no?", "DENIED", STEEL, WASH),
        (30, "3. Could act but isn't?", "IDLE", GREEN, "#EAF5F0"),
        (16, "4. Already shopping terms?", "IN-MARKET", CLAY, "#F3EEF0"),
    ]

    box(ax, 8, 62, 48, 8, fc=WASH, ec=STEEL)
    label(ax, 32, 66, "Open the creative. Ask in order ↓", size=9, color=INK)

    y_prev = 62
    for y, q, ans, ec, fc in steps:
        arrow(ax, (18, y_prev), (18, y + 7.5), color=LINE, lw=1.2)
        box(ax, 8, y, 48, 7.5, fc=PAPER, ec=LINE)
        label(ax, 32, y + 3.75, q, size=8.5, color=INK)
        box(ax, 62, y, 30, 7.5, fc=fc, ec=ec, lw=1.6)
        label(ax, 77, y + 3.75, f"→  {ans}", size=9, color=ec, weight="bold")
        # NO branch hint
        if y > 16:
            label(ax, 56, y + 3.75, "No", size=7, color=MUTED, ha="left")
        y_prev = y

    label(ax, 50, 5,
          "If the ad speaks to a pain, it is never IN-MARKET.",
          size=8, color=MUTED)

    save(fig, "fig-sort-rule")


def fig_campaign_structure():
    """Cold test / cold scale / warm campaigns + ad sets."""
    fig, ax = canvas(100, 80)

    label(ax, 50, 76, "Meta structure — campaigns & ad sets", size=11,
          color=NAVY, weight="bold")

    # Three campaign columns
    camps = [
        (4, "{client}_dscr_cold_test", "ABO · earn a read", [
            ("cold_denied_reveal", "DENIED"),
            ("cold_deadline_exit", "DEADLINE"),
            ("cold_idle_belief", "IDLE"),
            ("cold_inmarket_terms", "IN-MARKET"),
        ], WASH, STEEL),
        (36, "{client}_dscr_cold_scale", "CBO · proven only", [
            ("scale_winners", "winners only"),
        ], "#EAF5F0", GREEN),
        (68, "{client}_dscr_warm", "ABO · engagers", [
            ("warm_outcome", "shared"),
            ("warm_offer", "shared"),
            ("warm_authority", "shared"),
        ], "#FFF4E5", AMBER),
    ]

    for x, title, sub, sets, fc, ec in camps:
        box(ax, x, 48, 28, 22, fc=fc, ec=ec, lw=1.8)
        label(ax, x + 14, 64, title, size=7, color=ec, weight="bold")
        label(ax, x + 14, 58.5, sub, size=7, color=MUTED)
        label(ax, x + 14, 52.5, "CAMPAIGN", size=6.5, color=MUTED)

        y = 40
        for name, tag in sets:
            box(ax, x + 1, y, 26, 6.5, fc=PAPER, ec=LINE)
            label(ax, x + 14, y + 4.1, name, size=6.5, color=INK, weight="bold")
            label(ax, x + 14, y + 1.6, tag, size=6, color=MUTED)
            y -= 8

    label(ax, 50, 6,
          "Rule: one bucket × one creative job = one ad set = one primary creative",
          size=8, color=NAVY, weight="bold")

    save(fig, "fig-campaign-structure")


def fig_label_card():
    """What to fill when labeling an ad."""
    fig, ax = canvas(100, 48)

    label(ax, 50, 44, "Label every concept with these four fields", size=11,
          color=NAVY, weight="bold")

    fields = [
        (6, "bucket", "DENIED · DEADLINE · IDLE · IN-MARKET"),
        (28, "creative_job", "reveal · exit · belief · outcome · terms · authority"),
        (50, "concept_slug", "nodocs-speed · balloon-exit · cashout-grow · ratecard…"),
        (72, "angle_ref", "proven #1–5  OR  new: one-line idea"),
    ]
    for x, key, val in fields:
        box(ax, x, 12, 20, 26, fc=WASH, ec=STEEL, lw=1.5)
        label(ax, x + 10, 32, key, size=9, color=STEEL, weight="bold")
        label(ax, x + 10, 22, val, size=6.5, color=INK)

    label(ax, 50, 5,
          "Ad name: dscr_{slug}_{format}_v{n}   ·   Bucket/job live in tags — not in the ad_name token",
          size=7.5, color=MUTED)

    save(fig, "fig-label-card")


def fig_ad_examples():
    """What each bucket ad looks like — example hooks."""
    fig, ax = canvas(100, 70)

    label(ax, 50, 66, "What the ad sounds like (quick recognition)", size=11,
          color=NAVY, weight="bold")

    rows = [
        (52, "DENIED", "Your tax returns say you're broke.\nYour rentals say otherwise.", STEEL, WASH),
        (38, "DEADLINE", "That bridge loan did its job.\nIt was never meant to stay.", AMBER, "#FFF4E5"),
        (24, "IDLE", "Your equity isn't a trophy.\nIt's inventory.", GREEN, "#EAF5F0"),
        (10, "IN-MARKET", "DSCR cash-out refinance.\nFICO · LTV · APR · no tax returns.", CLAY, "#F3EEF0"),
    ]
    for y, name, quote, ec, fc in rows:
        box(ax, 4, y, 18, 11, fc=fc, ec=ec, lw=1.6)
        label(ax, 13, y + 5.5, name, size=9, color=ec, weight="bold")
        box(ax, 26, y, 70, 11, fc=PAPER, ec=LINE)
        label(ax, 61, y + 5.5, quote, size=8.5, color=INK)

    save(fig, "fig-ad-examples")


if __name__ == "__main__":
    fig_bucket_map()
    fig_sort_rule()
    fig_campaign_structure()
    fig_label_card()
    fig_ad_examples()
    print("done")
