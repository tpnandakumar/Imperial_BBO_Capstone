from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image
from scipy.interpolate import griddata
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "figures"
DATA = ROOT / "BBO_Dashboard/data/complete_internal_evidence.csv"
W12 = ROOT / "Week_12/week_12_figure_data_summary.csv"
W13 = ROOT / "Week_13/week_13_figure_data_summary.csv"
RL = ROOT / "Week_13/RL_DECISION_EXPERIMENT/outputs/rl_week13_policy_results.csv"
CLUSTER = ROOT / "BBO_Dashboard/hpo_results/week10_clustering_hpo_all_results.csv"
HPO = ROOT / "BBO_Dashboard/hpo_results/posthoc_surrogate_hpo_all_results.csv"

NAVY, BLUE, TEAL, GOLD, RED, PURPLE, GREY = "#102A43", "#2F6B9A", "#2A9D8F", "#E9A23B", "#C44536", "#7755A6", "#64748B"
sns.set_theme(style="whitegrid", context="notebook")

CAPTIONS = {
    11: "Normalised portfolio progress rose unevenly. The flat sections show why later decisions had to distinguish a genuine stopping point from a search that had simply stalled.",
    12: "Thirty-three of 104 weekly queries set a new observed record. Record timing differed by function, so the remaining value of another query was not evenly distributed.",
    13: "F1 observations form a narrow high-response region. Colour shows measured output on a logarithmic scale; the shading is an interpolation and not the hidden equation.",
    14: "F2 retained a broad favourable region around the Week 12 winner. The Week 13 decline shows why another local step could not be assumed to improve it.",
    15: "F3 is shown in a two-component projection of its three inputs. The final query reached a new observed best, but the projection does not establish global optimality.",
    16: "F4 exploration repeatedly left the productive basin. Returning to the earlier coordinate restored and reproduced the best observed output.",
    17: "F5's four-dimensional observations project towards a high-output edge. The measured sequence supported boundary refinement, while the background remains an estimate between sparse points.",
    18: "F6's five-dimensional projection contains overlapping observations with different returns. That overlap is consistent with the repeatability concern identified prospectively.",
    19: "F7's six-dimensional projection shows a compact high-response neighbourhood. Exact repeats supported retaining the established winner rather than reopening broad exploration.",
    20: "F8's eight-dimensional projection separates the retained winner from weaker observations. Sparse coverage prevents the projected map from proving a global optimum.",
    21: "Record-setting frequency varied from three to six weekly queries per function. Counting records alongside their timing avoids treating one late gain as evidence of steady progress.",
    22: "The latest observed best occurred early for some functions and in the final round for others. This timing informed whether to retain, refine, repeat or stop.",
    23: "L1 movement fell as several searches matured, but not uniformly. Zero movement in later rounds marks deliberate replication or retention rather than missing data.",
    24: "Within-function normalisation makes gains and reversals comparable despite incompatible output scales. It reveals where movement bought information without necessarily buying score.",
    25: "Exact repeats separated reproducible winners from variable returns. F1, F4, F7 and F8 reproduced; F6 returned a different value at the same coordinate.",
    26: "Week 13 movement and normalised reward change were not proportional. F5 gained after a small boundary step, F2 declined after an even smaller local move, and F6 changed without movement.",
    27: "For functions above two dimensions, the first two principal components captured most observed query-path variance. This diagnoses coordinated movement, not objective-function causality.",
    28: "High coordinate correlations show that several inputs moved together. Such redundancy explains why visible movement can exaggerate the amount of independent information collected.",
    29: "Week 10 cluster counts were selected by silhouette score within each function. These clusters organised sparse observations but did not validate a true number of hidden basins.",
    30: "Chronological surrogate error varied sharply by function even after hyperparameter comparison. The result supports using surrogates as decision aids rather than treating every prediction as equally reliable.",
}


def load_weekly():
    data = pd.read_csv(DATA)
    weekly = data[data.source.str.match(r"week_\d+")].copy()
    weekly["week"] = weekly.source.str.extract(r"(\d+)").astype(int)
    return data, weekly.sort_values(["function", "week"])


def decorate(ax, heading, subheading):
    ax.set_title(heading, loc="left", fontsize=15, fontweight="bold", color=NAVY, pad=16)
    ax.text(0, 1.01, subheading, transform=ax.transAxes, fontsize=9, color=GREY, va="bottom")


def save(fig, number, slug):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"Figure_{number:02d}_{slug}.jpg"
    fig.subplots_adjust(bottom=0.21)
    fig.text(0.055, 0.035, f"Figure {number}. {CAPTIONS[number]}  Source: verified Imperial BBO project data.",
             fontsize=8.2, color=GREY, ha="left", va="bottom", wrap=True)
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with Image.open(path) as image:
        image.convert("RGB").save(path, "JPEG", quality=88, optimize=True, progressive=True)


def normalise(values):
    values = np.asarray(values, dtype=float)
    span = np.nanmax(values) - np.nanmin(values)
    return np.zeros_like(values) if span == 0 else (values - np.nanmin(values)) / span


def response_map(data, weekly, function, number):
    dims = function if function <= 2 else function + 1
    dims = [2, 2, 3, 4, 4, 5, 6, 8][function - 1]
    cols = [f"x{i}" for i in range(1, dims + 1)]
    q = data[data.function.eq(function)].dropna(subset=cols + ["output"]).copy()
    X = q[cols].to_numpy()
    if dims == 2:
        P = X
        xlab, ylab = "x1", "x2"
    else:
        P = PCA(n_components=2).fit_transform(StandardScaler().fit_transform(X))
        xlab, ylab = "Observed PC1", "Observed PC2"
    z = normalise(q.output.to_numpy())
    fig, ax = plt.subplots(figsize=(10.8, 6.0))
    if len(q) >= 10:
        gx = np.linspace(P[:, 0].min(), P[:, 0].max(), 90)
        gy = np.linspace(P[:, 1].min(), P[:, 1].max(), 90)
        xx, yy = np.meshgrid(gx, gy)
        zz = griddata(P, z, (xx, yy), method="linear")
        if np.isfinite(zz).any():
            ax.contourf(xx, yy, zz, levels=12, cmap="viridis", alpha=.72)
    starter = q.source.eq("starter")
    ax.scatter(P[starter, 0], P[starter, 1], c=z[starter], cmap="viridis", vmin=0, vmax=1,
               s=28, alpha=.55, edgecolor="white", linewidth=.3, label="Starter observations")
    weekly_mask = ~starter
    ax.plot(P[weekly_mask, 0], P[weekly_mask, 1], color="white", lw=1.2, alpha=.8, zorder=3)
    sc = ax.scatter(P[weekly_mask, 0], P[weekly_mask, 1], c=z[weekly_mask], cmap="viridis", vmin=0, vmax=1,
                    s=78, edgecolor=NAVY, linewidth=.6, label="Weekly queries", zorder=4)
    best_i = int(np.nanargmax(q.output.to_numpy()))
    ax.scatter(P[best_i, 0], P[best_i, 1], marker="*", s=340, c=GOLD, edgecolor="white", linewidth=1.2,
               label="Best observed", zorder=5)
    fig.colorbar(sc, ax=ax, label="Normalised measured output")
    ax.set(xlabel=xlab, ylabel=ylab)
    ax.legend(frameon=True, loc="best", fontsize=8)
    decorate(ax, f"F{function}: observed response landscape", f"{dims} input dimensions | measured observations with an interpolated two-dimensional view")
    save(fig, number, f"f{function}_response_landscape")


def generate():
    data, weekly = load_weekly()

    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    portfolio = []
    for f, q in weekly.groupby("function"):
        portfolio.append(pd.Series(normalise(q.output.cummax()), index=q.week))
    portfolio = pd.concat(portfolio, axis=1)
    ax.plot(portfolio.index, portfolio.mean(axis=1), "o-", color=TEAL, lw=2.8, label="Mean normalised best")
    ax.fill_between(portfolio.index, portfolio.min(axis=1), portfolio.max(axis=1), color=BLUE, alpha=.15,
                    label="Function range")
    ax.set(xlabel="Week", ylabel="Normalised best-so-far", xticks=range(1, 14), ylim=(-.03, 1.03))
    ax.legend(frameon=False)
    decorate(ax, "Portfolio progress across 13 rounds", "Best-so-far values normalised within each function before aggregation")
    save(fig, 11, "portfolio_progress")

    records = []
    for f, q in weekly.groupby("function"):
        prior = -np.inf
        for row in q.itertuples():
            is_record = row.output > prior
            records.append((f, row.week, int(is_record)))
            prior = max(prior, row.output)
    rec = pd.DataFrame(records, columns=["function", "week", "record"])
    pivot = rec.pivot(index="function", columns="week", values="record")
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    sns.heatmap(pivot, cmap=sns.color_palette(["#EDF2F7", TEAL], as_cmap=True), cbar=False, linewidths=.6,
                linecolor="white", ax=ax, yticklabels=[f"F{i}" for i in pivot.index])
    ax.set(xlabel="Week", ylabel="Function")
    decorate(ax, "Where weekly records were set", "Green cells mark a new observed best relative to earlier weekly queries")
    save(fig, 12, "record_timing")

    for f, number in zip(range(1, 9), range(13, 21)):
        response_map(data, weekly, f, number)

    counts = rec.groupby("function").record.sum()
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    bars = ax.bar([f"F{i}" for i in counts.index], counts, color=BLUE)
    ax.bar_label(bars, padding=3); ax.set(ylabel="Weekly record-setting queries", ylim=(0, max(counts) + 1))
    decorate(ax, "How often each search improved its record", "Record count is shown alongside, not instead of, final performance")
    save(fig, 21, "record_frequency")

    latest = weekly.loc[weekly.groupby("function").output.idxmax(), ["function", "week", "output"]]
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    bars = ax.barh([f"F{i}" for i in latest.function], latest.week, color=[TEAL if w == 13 else BLUE for w in latest.week])
    ax.bar_label(bars, labels=[f"Week {w}" for w in latest.week], padding=3)
    ax.set(xlabel="Week of latest observed best", xlim=(0, 14), xticks=range(1, 14))
    decorate(ax, "When the final observed best was reached", "Timing separates early retained winners from searches that were still improving")
    save(fig, 22, "latest_best_week")

    movement, changes = [], []
    for f, q in weekly.groupby("function"):
        dims = [2, 2, 3, 4, 4, 5, 6, 8][f - 1]
        cols = [f"x{i}" for i in range(1, dims + 1)]
        X = q[cols].to_numpy()
        move = np.r_[np.nan, np.abs(np.diff(X, axis=0)).sum(axis=1)]
        change = np.r_[np.nan, np.diff(q.output.to_numpy())]
        change = change / (q.output.max() - q.output.min() or 1)
        movement.append(move); changes.append(change)
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    sns.heatmap(np.vstack(movement), cmap="mako", ax=ax, yticklabels=[f"F{i}" for i in range(1, 9)],
                xticklabels=range(1, 14), cbar_kws={"label": "L1 input movement"})
    ax.set(xlabel="Week", ylabel="Function")
    decorate(ax, "How far each weekly query moved", "Movement is measured from the preceding weekly query within each function")
    save(fig, 23, "movement_heatmap")

    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    sns.heatmap(np.vstack(changes), cmap="RdBu_r", center=0, vmin=-1, vmax=1, ax=ax,
                yticklabels=[f"F{i}" for i in range(1, 9)], xticklabels=range(1, 14),
                cbar_kws={"label": "Output change / observed weekly range"})
    ax.set(xlabel="Week", ylabel="Function")
    decorate(ax, "What each movement returned", "Output changes are normalised within function so direction and scale can be compared")
    save(fig, 24, "normalised_change_heatmap")

    rep = pd.read_csv(W13)
    same = rep[rep.identical_input.eq("Yes")].copy()
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    xx = np.arange(len(same))
    ax.scatter(xx - .12, same.week_12_output, s=100, color=BLUE, label="Week 12")
    ax.scatter(xx + .12, same.week_13_output, s=100, color=TEAL, label="Week 13")
    for i, row in enumerate(same.itertuples()):
        ax.plot([i - .12, i + .12], [row.week_12_output, row.week_13_output], color=RED if row.exact_change else GREY, lw=2)
    ax.set_xticks(xx, same.function.str.replace("Function ", "F")); ax.set_ylabel("Returned output")
    ax.set_yscale("symlog", linthresh=.05); ax.legend(frameon=False)
    decorate(ax, "Replication outcome at the final round", "Identical inputs distinguish stable reproduction from response variation")
    save(fig, 25, "replication_outcome")

    rl = pd.read_csv(RL)
    rl["normalised_change"] = (rl.week13_reward - rl.best_reward_to_week12) / rl.reward_range_to_week12.replace(0, np.nan)
    rl["normalised_change"] = rl.normalised_change.fillna(0)
    w13 = pd.read_csv(W13)
    merged = rl.merge(w13[["function", "l1_input_movement"]].assign(function=lambda x: x.function.str.replace("Function ", "F")), on="function")
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    ax.axhline(0, color=GREY, lw=.8); ax.axvline(0, color=GREY, lw=.8)
    ax.scatter(merged.l1_input_movement, merged.normalised_change, s=130, c=np.arange(8), cmap="viridis", edgecolor=NAVY)
    for row in merged.itertuples(): ax.annotate(row.function, (row.l1_input_movement, row.normalised_change), xytext=(5, 5), textcoords="offset points")
    ax.set(xlabel="Week 13 L1 input movement", ylabel="Change from Week 12 best / prior observed range")
    decorate(ax, "Movement was not a proxy for benefit", "Final-round reward depended on direction, local geometry and repeatability")
    save(fig, 26, "movement_vs_reward")

    pca = pd.read_csv(W12).dropna(subset=["PC1_Ratio_Weeks_01_to_12"])
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    x = np.arange(len(pca)); ax.bar(x, pca.PC1_Ratio_Weeks_01_to_12, color=BLUE, label="PC1")
    ax.bar(x, pca.PC1_PC2_Cumulative_Weeks_01_to_12 - pca.PC1_Ratio_Weeks_01_to_12,
           bottom=pca.PC1_Ratio_Weeks_01_to_12, color=TEAL, label="PC2 additional")
    ax.set_xticks(x, pca.Function.str.replace("Function ", "F")); ax.set(ylabel="Explained query-path variance", ylim=(0, 1.05))
    ax.legend(frameon=False)
    decorate(ax, "Principal component compression of query paths", "Applied to F3 to F8; F1 and F2 retained direct two-dimensional geometry")
    save(fig, 27, "pca_explained_variance")

    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    bars = ax.bar(pca.Function.str.replace("Function ", "F"), pca.Maximum_Absolute_Coordinate_Correlation_Weeks_01_to_12, color=PURPLE)
    ax.bar_label(bars, labels=[f"{v:.3f}" for v in pca.Maximum_Absolute_Coordinate_Correlation_Weeks_01_to_12], padding=3, fontsize=8)
    ax.set(ylabel="Maximum absolute coordinate correlation", ylim=(0, 1.08))
    decorate(ax, "Redundancy within observed query trajectories", "Correlation describes submitted coordinates and does not identify causal variables")
    save(fig, 28, "coordinate_correlation")

    cluster = pd.read_csv(CLUSTER)
    selected = cluster.loc[cluster.groupby("function").silhouette_score.idxmax()].sort_values("function")
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    bars = ax.bar(selected.function, selected.silhouette_score, color=GOLD)
    ax.bar_label(bars, labels=[f"k={k}\n{s:.3f}" for k, s in zip(selected.clusters, selected.silhouette_score)], padding=3, fontsize=8)
    ax.set(ylabel="Best silhouette score", ylim=(0, 1.05))
    decorate(ax, "Week 10 clustering hyperparameter comparison", "The plotted cluster count maximised silhouette score for each function")
    save(fig, 29, "clustering_validation")

    hpo = pd.read_csv(HPO)
    best = hpo.loc[hpo.groupby("function").normalised_rmse.idxmin()].sort_values("function")
    fig, ax = plt.subplots(figsize=(10.8, 5.7))
    bars = ax.bar(best.function, best.normalised_rmse, color=[TEAL if v < 1 else RED for v in best.normalised_rmse])
    ax.bar_label(bars, labels=[f"d={d}, a={a:g}\n{v:.2f}" for d, a, v in zip(best.degree, best.alpha, best.normalised_rmse)], padding=3, fontsize=7)
    ax.axhline(1, color=GREY, ls="--", label="Error equals observed range")
    ax.set(ylabel="Lowest chronological normalised RMSE"); ax.legend(frameon=False)
    decorate(ax, "Post hoc chronological surrogate validation", "Best degree and regularisation setting shown per function without random train-test leakage")
    save(fig, 30, "surrogate_validation")


if __name__ == "__main__":
    generate()
