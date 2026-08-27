from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image


HERE = Path(__file__).resolve().parent
OUT = HERE / "figures" / "Figure_31_post_bbo_resolution.jpg"

NAVY = "#102A43"
BLUE = "#2F6B9A"
TEAL = "#2A9D8F"
GOLD = "#E9A23B"
PURPLE = "#7755A6"
RED = "#C44536"
PALE = "#F3F7FA"
GREY = "#475569"


def box(ax, x, y, w, h, title, body, colour):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018",
                           facecolor=PALE, edgecolor=colour, linewidth=2.2)
    ax.add_patch(patch)
    title_size = 10.8 if len(title) > 24 else 13
    ax.text(x + 0.018, y + h - 0.042, title, fontsize=title_size, fontweight="bold", color=colour, va="top")
    wrapped = "\n\n".join(fill(part, width=41) for part in body.split("\n\n"))
    ax.text(x + 0.018, y + h - 0.092, wrapped, fontsize=8.5, color=GREY, va="top", linespacing=1.28)


def build():
    fig, ax = plt.subplots(figsize=(13.2, 7.4))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    ax.text(0.04, 0.95, "FIGURE 31  |  POST-BBO RESOLUTION", fontsize=23, fontweight="bold", color=NAVY, va="top")
    ax.text(0.04, 0.895, "From constrained optimisation to function resolution after the official thirteen-round challenge",
            fontsize=12, color=GREY, va="top")

    box(ax, 0.04, 0.55, 0.27, 0.27, "OFFICIAL BBO CHALLENGE",
        "Aim: select strong inputs under a fixed weekly budget.\n\n"
        "Evidence: 175 starter observations, 104 prospective queries and eight hidden functions.", BLUE)

    box(ax, 0.365, 0.55, 0.27, 0.27, "BLACK BOX RESOLUTION (BBR)",
        "Aim: use the completed history to test structural explanations.\n\n"
        "Boundary: separate post-capstone research. It did not alter Imperial submissions, outputs or rankings.", TEAL)

    box(ax, 0.69, 0.55, 0.27, 0.27, "RESOLUTION QUESTION",
        "Optimisation asks: Which input should be tried?\n\n"
        "Resolution asks: Which structural explanation remains credible, what evidence contradicts it, and what new test could separate alternatives?", PURPLE)

    ax.annotate("", xy=(0.355, 0.685), xytext=(0.315, 0.685), arrowprops=dict(arrowstyle="-|>", lw=2.4, color=GOLD))
    ax.annotate("", xy=(0.68, 0.685), xytext=(0.64, 0.685), arrowprops=dict(arrowstyle="-|>", lw=2.4, color=GOLD))

    methods = [
        ("Residual analysis", "Unexplained structure and repeatability"),
        ("Gradient reconstruction", "Directional effects along the observed path"),
        ("Symbolic recovery", "Candidate mathematical expressions"),
        ("Benchmark matching", "Comparison with known function families"),
        ("Repeated coordinates", "Stability, variation and hidden-state tests"),
        ("Function-specific models", "Chronological prediction and falsification"),
    ]
    ax.text(0.04, 0.49, "EXPERIMENTAL RESOLUTION LAYER", fontsize=14, fontweight="bold", color=NAVY)
    for i, (name, detail) in enumerate(methods):
        col = i % 3
        row = i // 3
        x = 0.04 + col * 0.315
        y = 0.345 - row * 0.115
        ax.add_patch(FancyBboxPatch((x, y), 0.285, 0.082, boxstyle="round,pad=0.01,rounding_size=0.014",
                                    facecolor="white", edgecolor=[BLUE, TEAL, PURPLE][col], linewidth=1.5))
        ax.text(x + 0.012, y + 0.056, name, fontsize=10, fontweight="bold", color=NAVY, va="center")
        ax.text(x + 0.012, y + 0.024, detail, fontsize=8.2, color=GREY, va="center")

    def policy_box(x, y, w, label, colour, h=0.038):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.007,rounding_size=0.016",
                                    facecolor=colour, edgecolor=colour))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")

    centre_y = 0.132
    policy_box(0.012, 0.113, 0.075, "Evaluate", NAVY)
    policy_box(0.108, 0.113, 0.075, "Resolve", PURPLE)
    policy_box(0.215, 0.148, 0.09, "Explore", BLUE, h=0.032)
    policy_box(0.215, 0.086, 0.09, "Exploit", TEAL, h=0.032)
    policy_box(0.345, 0.113, 0.08, "Extend", GOLD)
    policy_box(0.46, 0.113, 0.085, "Optimise", NAVY)
    policy_box(0.58, 0.113, 0.075, "Evolve", PURPLE)
    policy_box(0.69, 0.113, 0.095, "Experiment", RED)
    policy_box(0.82, 0.113, 0.08, "Evaluate", NAVY)

    # Main route. The split shows that Explore and Exploit occupy the same
    # decision level, while the two-headed vertical arrow allows movement in
    # either direction between them.
    ax.annotate("", xy=(0.102, centre_y), xytext=(0.088, centre_y),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY))
    for y1 in (0.164, 0.102):
        ax.annotate("", xy=(0.21, y1), xytext=(0.185, centre_y),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY))
    for y0 in (0.164, 0.102):
        ax.annotate("", xy=(0.338, centre_y), xytext=(0.307, y0),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY))
    ax.annotate("", xy=(0.26, 0.142), xytext=(0.26, 0.122),
                arrowprops=dict(arrowstyle="<->", lw=1.7, color=GREY))
    for x0, x1 in ((0.426, 0.453), (0.546, 0.573), (0.656, 0.683), (0.786, 0.813)):
        ax.annotate("", xy=(x1, centre_y), xytext=(x0, centre_y),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY))

    # Evaluation closes the loop by returning evidence to the Explore/Exploit
    # decision rather than forcing either policy.
    ax.plot([0.86, 0.86, 0.05], [0.111, 0.066, 0.066], color=GREY, lw=1.4)
    ax.annotate("", xy=(0.05, 0.108), xytext=(0.05, 0.066),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY))
    ax.text(0.46, 0.071, "LOOP: the final evaluation becomes the next starting evaluation",
            fontsize=7.2, color=GREY, ha="center", va="bottom")

    caption = ("Embedded caption. BBO optimised under a limited prospective budget. Black Box Resolution preserved "
               "that official record and used the completed history to compare, reject and refine competing structural "
               "explanations. Static, recursive and transformed-difference models tested whether outputs reflected "
               "coordinates alone or also contained a sequential component.")
    ax.text(0.04, 0.012, fill(caption, width=190), fontsize=8.1, color=GREY, va="bottom", linespacing=1.12)

    fig.savefig(OUT, dpi=210, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with Image.open(OUT) as image:
        image.convert("RGB").save(OUT, "JPEG", quality=89, optimize=True, progressive=True)


if __name__ == "__main__":
    build()
