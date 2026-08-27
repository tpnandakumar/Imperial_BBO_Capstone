from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "figures"
DATA = ROOT / "BBO_Dashboard/data/complete_internal_evidence.csv"
RL = ROOT / "Week_13/RL_DECISION_EXPERIMENT/outputs/rl_week13_policy_results.csv"
W13 = ROOT / "Week_13/week_13_analysis_summary.csv"

NAVY, BLUE, TEAL, GOLD, RED, PURPLE, GREY = "#102A43", "#2F6B9A", "#2A9D8F", "#E9A23B", "#C44536", "#7755A6", "#64748B"
sns.set_theme(style="whitegrid", context="notebook")

CAPTIONS = {
    1: "The prospective budget remained one portal evaluation per function per round, despite dimensionality rising from 2D to 8D. Strategy therefore had to allocate scarce information, not merely search harder.",
    2: "Best-so-far trajectories show that improvement arrived at different times. A single uniform optimiser would have ignored these function-specific stopping and continuation states.",
    3: "F5 rewarded controlled movement towards the feasible boundary. The final L1 movement of 0.011001 increased the returned output by 13.613221.",
    4: "Small local movement succeeded for F3 but failed for F2. Step size alone did not determine success; local geometry and direction remained decisive.",
    5: "F4 exploration produced large losses before the Week 1 coordinate was recovered and reproduced in Weeks 12 and 13. Recovery protected evidence already earned.",
    6: "Identical F6 inputs returned different values. Replication exposed unresolved response variability and prevented the latest observed best from being treated as a stable optimum.",
    7: "The analytical method matured from broad exploration to structural review, dimensional comparison and function-specific action. Each addition answered a decision problem created by the preceding evidence.",
    8: "Week 13 actions were assigned using only Weeks 1 to 12 data. The held-out result created new observed bests for F3, F5 and F6, retained four winners and rejected F2's continued local step.",
    9: "Success required four linked properties: objective performance, adaptation, falsifiable reasoning and query efficiency. A record without repeatability could not satisfy the full definition.",
    10: "Peer comparison identified a shared emphasis on diagnosis, replication and falsification. The synthesis adds a prospective ledger so that every diagnosis can be traced to a changed action.",
}


def save(fig, number, slug):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"Figure_{number:02d}_{slug}.jpg"
    fig.subplots_adjust(bottom=0.20)
    fig.text(0.055, 0.035, f"Figure {number}. {CAPTIONS[number]}  Source: verified Imperial BBO project data and documented peer reflection.",
             fontsize=8.2, color=GREY, ha="left", va="bottom", wrap=True)
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with Image.open(path) as im:
        im.convert("RGB").save(path, "JPEG", quality=89, optimize=True, progressive=True)
    return path


def title(ax, heading, subheading):
    ax.set_title(heading, loc="left", fontsize=15, fontweight="bold", color=NAVY, pad=16)
    ax.text(0, 1.01, subheading, transform=ax.transAxes, fontsize=9, color=GREY, va="bottom")


def weekly():
    d = pd.read_csv(DATA)
    w = d[d.source.str.match(r"week_\d+")].copy()
    w["week"] = w.source.str.extract(r"(\d+)").astype(int)
    return d, w.sort_values(["function", "week"])


def generate():
    d, w = weekly()
    dims = np.array([2, 2, 3, 4, 4, 5, 6, 8])

    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    x = np.arange(1, 9)
    ax.bar(x - .18, dims, .36, color=BLUE, label="Input dimensions")
    ax.bar(x + .18, np.repeat(13, 8), .36, color=TEAL, label="Prospective queries")
    ax.set_xticks(x, [f"F{i}" for i in x]); ax.set_ylabel("Count")
    title(ax, "A fixed query budget across unequal search spaces", "Eight functions received the same 13-round budget despite different dimensionality")
    ax.legend(frameon=False, ncol=2)
    save(fig, 1, "budget_and_dimensionality")

    fig, ax = plt.subplots(figsize=(10.8, 5.9))
    rows = []
    for f in range(1, 9):
        q = w[w.function.eq(f)]
        lo, hi = q.output.min(), q.output.max(); span = hi - lo or 1
        rows.append((q.output.cummax() - lo) / span)
    sns.heatmap(np.vstack(rows), cmap="YlGnBu", vmin=0, vmax=1, ax=ax,
                yticklabels=[f"F{i}" for i in range(1, 9)], xticklabels=range(1, 14),
                cbar_kws={"label": "Normalised best-so-far"})
    ax.set(xlabel="Week", ylabel="Function")
    title(ax, "When improvement occurred", "Plateaux and late gains created different action states across the portfolio")
    save(fig, 2, "best_so_far_heatmap")

    q = w[w.function.eq(5)]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10.8, 6.6), sharex=True)
    a1.plot(q.week, q.output, "o-", color=TEAL, lw=2.4); a1.set_ylabel("Returned output")
    for c in ["x1", "x2", "x3", "x4"]: a2.plot(q.week, q[c], marker=".", label=c)
    a2.set(xlabel="Week", ylabel="Coordinate", ylim=(-.03, 1.03)); a2.legend(ncol=4, frameon=False)
    title(a1, "F5: controlled boundary exploitation", "Repeated directional evidence justified progressively smaller movements")
    save(fig, 3, "f5_boundary_exploitation")

    s = pd.read_csv(W13)
    z = s[s.function.isin(["Function 2", "Function 3"])].copy()
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    xx = np.arange(2)
    bars = ax.bar(xx, z.exact_change, color=[RED, TEAL], width=.58)
    ax.axhline(0, color=NAVY, lw=.8); ax.set_xticks(xx, ["F2\nL1 move 0.005", "F3\nL1 move 0.015"])
    ax.set_ylabel("Week 13 output change")
    for b, v in zip(bars, z.exact_change): ax.text(b.get_x()+b.get_width()/2, v, f"{v:+.6f}", ha="center", va="bottom" if v >= 0 else "top", fontweight="bold")
    title(ax, "Local refinement produced opposite outcomes", "A small step was not automatically a safe step")
    save(fig, 4, "local_refinement_contrast")

    q = w[w.function.eq(4)]
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    best = q.output.max(); ax.plot(q.week, q.output, "o-", color=BLUE)
    ax.axhline(best, color=TEAL, ls="--", label=f"Recovered best {best:.6f}")
    ax.fill_between(q.week, q.output, best, color=RED, alpha=.12, label="Exploration loss")
    ax.set(xlabel="Week", ylabel="Returned output"); ax.legend(frameon=False)
    title(ax, "F4: exploration, falsification and recovery", "The earlier winner was restored after alternative regions failed")
    save(fig, 5, "f4_recovery")

    q = w[w.function.eq(6)]
    keys = ["x1", "x2", "x3", "x4", "x5"]
    repeated = q[q[keys].round(6).duplicated(keep=False)]
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    ax.plot(q.week, q.output, "o-", color=BLUE, alpha=.35, label="All weekly returns")
    ax.scatter(repeated.week, repeated.output, s=120, color=RED, label="Repeated coordinate", zorder=4)
    for r in repeated.itertuples(): ax.annotate(f"W{int(r.week)} {r.output:.6f}", (r.week, r.output), xytext=(5, 7), textcoords="offset points", fontsize=8)
    ax.set(xlabel="Week", ylabel="Returned output"); ax.legend(frameon=False)
    title(ax, "F6: replication as measurement investigation", "The same input did not imply a fixed response")
    save(fig, 6, "f6_replication")

    stages = ["Explore", "Refine", "Cluster", "PCA", "Policy"]
    start = [1, 4, 10, 11, 12]; width = [3, 6, 1, 1, 2]
    fig, ax = plt.subplots(figsize=(10.8, 5.4))
    colors = [BLUE, TEAL, GOLD, PURPLE, RED]
    for i, (lab, st, wd, col) in enumerate(zip(stages, start, width, colors)):
        ax.barh(0, wd, left=st-.5, height=.48, color=col); ax.text(st-.5+wd/2, 0, lab, ha="center", va="center", color="white", fontweight="bold")
    ax.set(xlim=(.5, 13.5), ylim=(-.6, .6), yticks=[], xlabel="Week", xticks=range(1, 14))
    title(ax, "The method changed when the decision problem changed", "Analytical complexity was added only when accumulated evidence required it")
    save(fig, 7, "method_progression")

    r = pd.read_csv(RL)
    r["change"] = (r.week13_reward - r.best_reward_to_week12) / r.reward_range_to_week12.replace(0, np.nan) * 100
    r["change"] = r.change.fillna(0)
    outcome = np.select([r.week13_new_best, r.week13_retained_best], ["New best", "Best retained"], default="No improvement")
    cmap = {"New best": TEAL, "Best retained": BLUE, "No improvement": RED}
    fig, ax = plt.subplots(figsize=(10.8, 5.9))
    ax.bar(r.function, r.change, color=[cmap[o] for o in outcome]); ax.axhline(0, color=NAVY, lw=.8)
    for i, row in enumerate(r.itertuples()): ax.text(i, row.change, f"{row.selected_action_label}\n{outcome[i]}", ha="center", va="bottom" if row.change >= 0 else "top", fontsize=7)
    ax.set(ylabel="Change from Week 12 best (% observed range)", xlabel="Function")
    title(ax, "Prospective Week 13 policy evaluation", "Actions were selected before the Week 13 outputs were known")
    save(fig, 8, "prospective_policy")

    criteria = ["Outcome", "Adaptability", "Falsifiability", "Efficiency"]
    evidence = np.array([[1, .8, .7, .8], [.7, 1, 1, .8], [.5, .9, 1, .9], [.8, .8, .7, 1]])
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    sns.heatmap(evidence, annot=True, fmt=".1f", cmap="YlGnBu", vmin=0, vmax=1, ax=ax,
                xticklabels=criteria, yticklabels=["Record", "Negative", "Repeat", "Stop"],
                cbar_kws={"label": "Conceptual contribution"})
    ax.set(xlabel="Success criterion", ylabel="Evidence type")
    title(ax, "A defensible definition of optimisation success", "No single outcome type satisfied every criterion")
    save(fig, 9, "success_definition")

    cols = ["Problem identification", "Structural probes", "Replication", "Pre-registration", "Adaptive allocation"]
    mat = np.array([[1, .7, 1, .8, 1], [1, 1, 1, 1, .6], [1, 1, 1, 1, 1]])
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    sns.heatmap(mat, annot=np.array([["Primary", "Support", "Primary", "Support", "Primary"], ["Primary", "Primary", "Primary", "Primary", "Limited"], ["Primary"]*5]),
                fmt="", cmap="PuBuGn", vmin=0, vmax=1, ax=ax, cbar=False,
                xticklabels=cols, yticklabels=["My approach", "Eduardo's post", "Combined improvement"])
    ax.set_xlabel("Documented strategy component")
    title(ax, "Peer comparison and synthesis", "Shared principles were strengthened by a prospective action ledger")
    save(fig, 10, "peer_synthesis")


if __name__ == "__main__":
    generate()
