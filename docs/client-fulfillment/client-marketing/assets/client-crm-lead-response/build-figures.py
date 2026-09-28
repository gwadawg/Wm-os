#!/usr/bin/env python3
"""Render the diagram set for the Client CRM Lead Response Playbook PDF.

Usage: python3 build-figures.py
Outputs PNGs beside this script. Palette follows the Waiz brand doctrine and
matches rm-creative-playbook/build-figures.py so client PDFs read as one family.
"""

import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                Rectangle)

OUT = pathlib.Path(__file__).resolve().parent

NAVY = "#061A4A"
STEEL = "#1C4C80"
SKY = "#9FC2E8"
WASH = "#E4EDF8"
PAPER = "#FFFFFF"
TINT = "#F7FAFD"
INK = "#0B1220"
MUTED = "#5F6B7C"
LINE = "#C9D6E6"
GREEN = "#1F7A5C"
CLAY = "#9C5B3C"

FONT = "DejaVu Sans"
plt.rcParams["font.family"] = FONT

PRINT_W = 6.05  # A4 minus 2.8cm margins, the body text column


def canvas(w, h, width=None):
    fig = plt.figure(figsize=(width or PRINT_W, (width or PRINT_W) * h / w), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 * h / w)
    ax.axis("off")
    fig.patch.set_facecolor(PAPER)
    return fig, ax


def save(fig, name, bg=PAPER):
    path = OUT / f"{name}.png"
    fig.savefig(path, facecolor=bg, edgecolor="none",
                bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)
    print(path.name)


def box(ax, x, y, w, h, fc=PAPER, ec=LINE, lw=1.2, r=1.6, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z))


def label(ax, x, y, text, size=9, color=INK, weight="normal",
          ha="center", va="center", style="normal", z=5):
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, style=style, zorder=z, linespacing=1.45)


def arrow(ax, p1, p2, color=STEEL, lw=1.5, style="-|>", rad=0.0, z=3, ls="-"):
    ax.add_patch(FancyArrowPatch(
        p1, p2, arrowstyle=style, mutation_scale=12, color=color,
        linewidth=lw, linestyle=ls,
        connectionstyle=f"arc3,rad={rad}", zorder=z,
        shrinkA=2, shrinkB=2))


def chip(ax, x, y, w, h, text, fc, tc=PAPER, size=10):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f"round,pad=0,rounding_size={h/2}",
        facecolor=fc, edgecolor="none", zorder=4))
    label(ax, x + w / 2, y + h / 2, text, size=size, color=tc, weight="bold")


# ── 1. Cover hero — lead in, you take over ───────────────────────────────────
def fig_hero():
    fig, ax = canvas(12, 6.6, width=9.0)

    # left: what the system does
    box(ax, 4, 14, 36, 34, fc=WASH, ec=WASH, r=2.0)
    label(ax, 22, 42, "THE SYSTEM", size=11.5, color=NAVY, weight="bold")
    label(ax, 22, 35.5, "Captures the lead,\nstarts the conversation", size=9, color=STEEL)
    box(ax, 12, 18, 20, 11, fc=PAPER, ec=STEEL, lw=1.4, r=1.4, z=4)
    label(ax, 22, 25.2, "New lead", size=8, color=NAVY, weight="bold")
    label(ax, 22, 21.4, "first text in 5 min", size=7.2, color=MUTED, style="italic")

    # right: what the client does
    box(ax, 60, 14, 36, 34, fc="#E7F2EC", ec="#E7F2EC", r=2.0)
    label(ax, 78, 42, "YOU", size=11.5, color=GREEN, weight="bold")
    label(ax, 78, 35.5, "Calls, replies,\nand closed deals", size=9, color="#2E5E4A")
    box(ax, 68, 18, 20, 11, fc=PAPER, ec=GREEN, lw=1.4, r=1.4, z=4)
    label(ax, 78, 25.2, "Lead replied", size=8, color=GREEN, weight="bold")
    label(ax, 78, 21.4, "your conversation now", size=7.2, color=MUTED, style="italic")

    arrow(ax, (43, 31), (57, 31), color=NAVY, lw=3.0, style="-|>")
    label(ax, 50, 36.5, "handoff", size=8.6, color=MUTED, style="italic")

    ax.plot([4, 96], [7.5, 7.5], color=NAVY, lw=2.0, zorder=5)
    ax.add_patch(Rectangle((4, 2.0), 92 * 0.34, 3.0, facecolor=NAVY,
                           edgecolor="none", zorder=6))
    ax.add_patch(Rectangle((4 + 92 * 0.34, 2.0), 92 * 0.66, 3.0,
                           facecolor=SKY, edgecolor="none", zorder=6))

    fig.patch.set_facecolor("#F4F6FA")
    fig.savefig(OUT / "hero-cover.png", facecolor="#F4F6FA", edgecolor="none",
                bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    print("hero-cover.png")


# ── 2. Responsibility split ──────────────────────────────────────────────────
def fig_split():
    fig, ax = canvas(9.4, 6.4)
    H = 100 * 6.4 / 9.4

    label(ax, 27, H - 6, "WAIZ HANDLES", size=10, color=NAVY, weight="bold")
    label(ax, 73, H - 6, "YOU HANDLE", size=10, color=GREEN, weight="bold")

    left = ["Lead capture from ads", "CRM setup + pipeline",
            "First-touch text drip", "Campaign optimization"]
    right = ["Calling new leads fast", "Replying once they answer",
             "Tags, notes, pipeline moves", "Logging outcomes"]

    for i, t in enumerate(left):
        y = H - 14 - i * 10.5
        box(ax, 6, y - 3.6, 42, 8, fc=WASH, ec=LINE, lw=1.0, r=1.4)
        ax.add_patch(Rectangle((6.6, y - 3.0), 1.0, 6.8, facecolor=NAVY,
                               edgecolor="none", zorder=4))
        label(ax, 10.6, y, t, size=8.4, color=INK, ha="left")

    for i, t in enumerate(right):
        y = H - 14 - i * 10.5
        box(ax, 52, y - 3.6, 42, 8, fc="#EDF6F1", ec=LINE, lw=1.0, r=1.4)
        ax.add_patch(Rectangle((52.6, y - 3.0), 1.0, 6.8, facecolor=GREEN,
                               edgecolor="none", zorder=4))
        label(ax, 56.6, y, t, size=8.4, color=INK, ha="left")

    save(fig, "fig-split")


# ── 3. Lead lifecycle map ────────────────────────────────────────────────────
def fig_lifecycle():
    fig, ax = canvas(9.4, 4.15)
    H = 100 * 4.15 / 9.4

    steps_top = [("1", "Lead submits\nthe ad form"),
                 ("2", "Contact appears\nin your CRM"),
                 ("3", "Assistant texts\nwithin 5 minutes")]
    steps_bot = [("4", "Lead replies,\ndrip stops"),
                 ("5", "You call and\ntext back"),
                 ("6", "You log the\noutcome")]

    def draw_row(steps, y, colors):
        xs = [6, 39, 72]
        bh = 13
        for (num, text), x, c in zip(steps, xs, colors):
            box(ax, x, y, 22, bh, fc=TINT, ec=c, lw=1.4, r=1.6)
            ax.add_patch(Circle((x + 3.6, y + 9.6), 2.2, facecolor=c,
                                edgecolor="none", zorder=5))
            label(ax, x + 3.6, y + 9.6, num, size=7.4, color=PAPER, weight="bold", z=6)
            label(ax, x + 12.6, y + 5.2, text, size=7.2, color=INK, ha="center")
        arrow(ax, (xs[0] + 23, y + 6.5), (xs[1] - 1, y + 6.5), color=STEEL, lw=1.4)
        arrow(ax, (xs[1] + 23, y + 6.5), (xs[2] - 1, y + 6.5), color=STEEL, lw=1.4)

    top_y = H - 16.5
    bot_y = 1.2
    draw_row(steps_top, top_y, [NAVY, NAVY, NAVY])
    arrow(ax, (83, top_y - 0.6), (17, bot_y + 14.2), color=STEEL, lw=1.4, rad=-0.22)
    draw_row(steps_bot, bot_y, [GREEN, GREEN, GREEN])

    label(ax, 50, H - 2.2, "AUTOMATIC", size=7.6, color=NAVY, weight="bold")
    label(ax, 72, bot_y + 15.6, "YOURS", size=7.6, color=GREEN, weight="bold")

    save(fig, "fig-lifecycle")


# ── 4. Drip flow (simplified for clients) ────────────────────────────────────
def fig_drip():
    fig, ax = canvas(9.4, 5.0)
    H = 100 * 5.0 / 9.4

    cx = 50
    bh = 6.6
    y1, y2, y3 = 45.2, 35.4, 25.6
    yd, dh = 16.0, 6.2

    box(ax, cx - 22, y1, 44, bh, fc=WASH, ec=NAVY, lw=1.5, r=1.4)
    label(ax, cx, y1 + bh / 2, "New lead comes in", size=8.6, color=NAVY, weight="bold")

    box(ax, cx - 22, y2, 44, bh, fc=TINT, ec=STEEL, lw=1.3, r=1.4)
    label(ax, cx, y2 + bh / 2, "We read what the lead asked about", size=8.2, color=INK)

    box(ax, cx - 22, y3, 44, bh, fc=TINT, ec=STEEL, lw=1.3, r=1.4)
    label(ax, cx, y3 + bh / 2, "Your assistant texts on your behalf", size=8.2, color=INK)

    arrow(ax, (cx, y1), (cx, y2 + bh + 0.3), color=STEEL, lw=1.5)
    arrow(ax, (cx, y2), (cx, y3 + bh + 0.3), color=STEEL, lw=1.5)
    arrow(ax, (cx, y3), (cx, yd + dh + 0.3), color=STEEL, lw=1.5)

    box(ax, cx - 15, yd, 30, dh, fc=PAPER, ec=NAVY, lw=1.5, r=3.0)
    label(ax, cx, yd + dh / 2, "Lead replies?", size=8.4, color=NAVY, weight="bold")

    box(ax, 5, 0.6, 42, 7.2, fc="#EDF6F1", ec=GREEN, lw=1.4, r=1.4)
    label(ax, 26, 5.2, "YES", size=7.4, color=GREEN, weight="bold")
    label(ax, 26, 2.6, "Drip stops. The conversation is yours.", size=7.2, color=INK)
    arrow(ax, (cx - 13, yd), (26, 8.2), color=GREEN, lw=1.5, rad=0.12)

    box(ax, 53, 0.6, 42, 7.2, fc=WASH, ec=STEEL, lw=1.3, r=1.4)
    label(ax, 74, 5.2, "NOT YET", size=7.4, color=STEEL, weight="bold")
    label(ax, 74, 2.6, "Follow-ups continue on schedule", size=7.2, color=INK)
    arrow(ax, (cx + 13, yd), (74, 8.2), color=STEEL, lw=1.5, rad=-0.12)

    save(fig, "fig-drip")


# ── 5. The two tags ──────────────────────────────────────────────────────────
def fig_tags():
    fig, ax = canvas(9.4, 4.6)
    H = 100 * 4.6 / 9.4

    chip(ax, 8, H - 15, 26, 8, "claimed", GREEN, size=10.5)
    label(ax, 40, H - 11, '"I had a real conversation with this lead."', size=8.8,
          color=INK, ha="left")
    label(ax, 40, H - 16.5, "Tracks your contact rate and lead quality.", size=7.8,
          color=MUTED, ha="left", style="italic")

    chip(ax, 8, H - 33, 26, 8, "kill-switch", CLAY, size=10.5)
    label(ax, 40, H - 29, '"Stop every automated message for this contact."', size=8.8,
          color=INK, ha="left")
    label(ax, 40, H - 34.5, "Use when a lead should not be texted again.", size=7.8,
          color=MUTED, ha="left", style="italic")

    ax.plot([8, 92], [4.5, 4.5], color=LINE, lw=1.0)
    label(ax, 50, 1.6, "Everything else (proposal, submitted, funded, DQ) goes in the Client Log form",
          size=7.6, color=MUTED, style="italic")

    save(fig, "fig-tags")


# ── 6. Feedback loop ─────────────────────────────────────────────────────────
def fig_loop():
    fig, ax = canvas(9.4, 6.2)
    H = 100 * 6.2 / 9.4

    nodes = [
        (22, H - 16, "You log outcomes", "conversions + DQs\nin the Client Log", NAVY),
        (78, H - 16, "We optimize", "trace results back\nto specific ads", STEEL),
        (50, 12, "Better leads", "budget shifts toward\nwhat turns into business", GREEN),
    ]
    for x, y, t, sub, c in nodes:
        box(ax, x - 17, y - 9, 34, 17, fc=TINT, ec=c, lw=1.6, r=2.0)
        label(ax, x, y + 3.2, t, size=9.4, color=c, weight="bold")
        label(ax, x, y - 3.4, sub, size=7.4, color=MUTED)

    arrow(ax, (40, H - 14), (60, H - 14), color=STEEL, lw=2.0, rad=-0.25)
    arrow(ax, (74, H - 26), (60, 18), color=STEEL, lw=2.0, rad=-0.25)
    arrow(ax, (40, 18), (26, H - 26), color=STEEL, lw=2.0, rad=-0.25)

    save(fig, "fig-loop")


# ── 7. Daily routine ─────────────────────────────────────────────────────────
def fig_routine():
    fig, ax = canvas(9.4, 6.6)
    H = 100 * 6.6 / 9.4

    rows = [
        ("MORNING", "Check the New Lead stage and unread conversations", NAVY),
        ("AFTER EVERY CALL", "Add a note, update the tag, set the next step", STEEL),
        ("END OF DAY", "Clear unread messages, update pipeline stages", GREEN),
        ("WEEKLY", "Review the pipeline and log any missed outcomes", CLAY),
    ]
    for i, (when, what, c) in enumerate(rows):
        y = H - 10 - i * 14
        box(ax, 6, y - 5, 88, 11, fc=TINT, ec=LINE, lw=1.0, r=1.6)
        ax.add_patch(Rectangle((6.6, y - 4.2), 1.2, 9.4, facecolor=c,
                               edgecolor="none", zorder=4))
        label(ax, 11, y + 2.2, when, size=8, color=c, weight="bold", ha="left")
        label(ax, 11, y - 2.4, what, size=8.6, color=INK, ha="left")

    save(fig, "fig-routine")


if __name__ == "__main__":
    fig_hero()
    fig_split()
    fig_lifecycle()
    fig_drip()
    fig_tags()
    fig_loop()
    fig_routine()
