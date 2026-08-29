"""Generate colour coded Week 10 clustering figures from the exact BBO history.

Only Weeks 1 to 10 are used as analytical evidence. Week 11 outputs are excluded.
The authoritative history is read from BBO_Dashboard/data/complete_internal_evidence.csv.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "Week_10"
HISTORY = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
DPI = 300

FUNCTION_COLOURS = ["#2563EB", "#F59E0B", "#10B981", "#EF4444", "#8B5CF6", "#14B8A6", "#EC4899", "#64748B"]
STATUS_COLOURS = {
    "Explore": "#2563EB",
    "Refine": "#16A34A",
    "Exploit": "#15803D",
    "Boundary test": "#D97706",
    "Reassess": "#64748B",
}
DECISIONS = {
    1: "Explore", 2: "Refine", 3: "Refine", 4: "Reassess",
    5: "Exploit", 6: "Reassess", 7: "Refine", 8: "Boundary test",
}


def load_history():
    df = pd.read_csv(HISTORY)
    df = df[df["source"].str.match(r"week_\d{2}")].copy()
    df["Week"] = df["source"].str.removeprefix("week_").astype(int)
    df = df[df["Week"].between(1, 10)].copy()
    df["Function"] = df["function"].astype(int)
    df["Output"] = df["output"].astype(float)
    dimensions = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
    df["Dimension"] = df["Function"].map(dimensions)
    for i in range(1, 9):
        df[f"Input_{i}"] = df[f"x{i}"]
    if len(df) != 80:
        raise ValueError(f"Expected 80 Week 1 to 10 observations, found {len(df)}")
    return df


def input_matrix(df, function):
    sub = df[df["Function"] == function].sort_values("Week")
    dim = int(sub["Dimension"].iloc[0])
    cols = [f"Input_{i}" for i in range(1, dim + 1)]
    return sub, sub[cols].to_numpy(float)


def build_summary(df):
    rows = []
    for f in range(1, 9):
        sub, X = input_matrix(df, f)
        y = sub["Output"].to_numpy(float)
        candidates = []
        for k in (2, 3):
            km = KMeans(n_clusters=k, random_state=42, n_init=50).fit(X)
            candidates.append((silhouette_score(X, km.labels_), k, km.labels_))
        sil, k, labels = max(candidates, key=lambda z: z[0])
        best = int(np.argmax(y))
        norm = np.sqrt(X.shape[1])
        distances = np.linalg.norm(X - X[-1], axis=1) / norm
        nn = min(v for i, v in enumerate(distances) if i != len(distances) - 1)
        rows.append({
            "Function": f"F{f}",
            "Dimensions": X.shape[1],
            "Selected_k": k,
            "Silhouette": sil,
            "Best_week": int(sub.iloc[best]["Week"]),
            "Week10_output": y[-1],
            "W10_to_best_norm_distance": distances[best],
            "W10_nearest_neighbour_distance": nn,
            "W10_same_cluster_as_best": bool(labels[-1] == labels[best]),
            "Decision": DECISIONS[f],
        })
    return pd.DataFrame(rows)


def save(fig, stem):
    fig.savefig(OUTDIR / f"{stem}.png", dpi=DPI, bbox_inches="tight")
    fig.savefig(OUTDIR / f"{stem}.svg", bbox_inches="tight")
    plt.close(fig)


def figure_1(summary):
    fig, ax = plt.subplots(figsize=(12, 7.2))
    bars = ax.bar(range(8), summary["Silhouette"], color=FUNCTION_COLOURS)
    ax.set_xticks(range(8), [f"F{i}" for i in range(1, 9)])
    ax.set_ylabel("Silhouette score")
    ax.set_xlabel("BBO function")
    ax.set_title("Figure 1. Exploratory Cluster Separation Across Functions, Weeks 1 to 10", weight="bold")
    ax.grid(axis="y", alpha=0.22)
    for i, bar in enumerate(bars):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.012,
                f'{summary.loc[i, "Silhouette"]:.3f}\nk={int(summary.loc[i, "Selected_k"])}',
                ha="center", va="bottom", fontsize=9)
    fig.text(0.05, 0.018,
             "Embedded caption: Each function is analysed independently in its own input space. Bars show the best exploratory K-means separation for k = 2 or 3. Higher silhouette scores indicate clearer separation between sampled neighbourhoods, but ten observations per function remain sparse and do not establish the global structure of the hidden objective.",
             ha="left", va="bottom", fontsize=9, wrap=True)
    fig.subplots_adjust(bottom=0.20)
    save(fig, "week_10_clustering_figure_1_cluster_separation_colour")


def figure_2(df):
    sub, X = input_matrix(df, 5)
    y = sub["Output"].to_numpy(float)
    dist = np.linalg.norm(X - X[-1], axis=1) / np.sqrt(X.shape[1])
    fig, ax = plt.subplots(figsize=(12, 7.2))
    colours = plt.cm.viridis(np.linspace(0.12, 0.92, 10))
    sizes = 90 + 260 * (y - y.min()) / (y.max() - y.min())
    ax.scatter(dist, y, s=sizes, c=colours, edgecolor="white", linewidth=1.2, zorder=3)
    ax.plot(dist, y, color="#94A3B8", alpha=0.45, zorder=1)
    for week, dx, yy in zip(sub["Week"], dist, y):
        ax.annotate(f"W{int(week)}", (dx, yy), xytext=(6, 5), textcoords="offset points", fontsize=9, weight="bold")
    ax.axvspan(0, 0.04, color="#DCFCE7", alpha=0.60, label="Tight Week 9 to 10 neighbourhood")
    ax.set_xlabel("Normalised Euclidean distance from the Week 10 Function 5 query")
    ax.set_ylabel("Function 5 output")
    ax.set_title("Figure 2. Function 5 High-Value Cluster Near the Week 10 Boundary Region", weight="bold")
    ax.grid(alpha=0.22)
    ax.legend(loc="lower right")
    fig.text(0.05, 0.018,
             "Embedded caption: Function 5 increased from 1415.876 in Week 1 to 4394.868 by Week 9. Week 10 repeated the Week 9 query 0.120000, 0.997000, 0.999800, 0.999800 and reproduced 4394.868 exactly. Later high outputs are concentrated close to the Week 10 point, supporting cautious local exploitation without claiming that the global optimum has been reached.",
             ha="left", va="bottom", fontsize=9, wrap=True)
    fig.subplots_adjust(bottom=0.21)
    save(fig, "week_10_clustering_figure_2_function5_cluster_colour")


def figure_3(summary):
    fig, ax = plt.subplots(figsize=(14.5, 7.8))
    ax.axis("off")
    rows = []
    for _, r in summary.iterrows():
        rows.append([
            r["Function"], f'{int(r["Dimensions"])}D', f'{r["Week10_output"]:.6g}',
            f'W{int(r["Best_week"])}', f'{r["W10_to_best_norm_distance"]:.3f}',
            f'{r["W10_nearest_neighbour_distance"]:.3f}',
            "Yes" if r["W10_same_cluster_as_best"] else "No", r["Decision"]
        ])
    headers = ["Function", "Dim.", "Week 10 output", "Best week", "W10 to best\nnorm. distance",
               "W10 nearest\nneighbour", "Same cluster\nas best", "Week 11 decision"]
    table = ax.table(cellText=rows, colLabels=headers, cellLoc="center", colLoc="center",
                     colWidths=[.07, .06, .12, .08, .15, .14, .12, .18], loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.9)
    for c in range(len(headers)):
        table[(0, c)].set_facecolor("#0F2D4A")
        table[(0, c)].set_text_props(color="white", weight="bold")
    for i, r in enumerate(summary.itertuples(), start=1):
        table[(i, 0)].set_facecolor(FUNCTION_COLOURS[i - 1])
        table[(i, 0)].set_text_props(color="white", weight="bold")
        table[(i, 7)].set_facecolor(STATUS_COLOURS[r.Decision])
        table[(i, 7)].set_text_props(color="white", weight="bold")
        for c in range(1, 7):
            table[(i, c)].set_facecolor("#F8FAFC" if i % 2 else "#EEF2F7")
    ax.set_title("Figure 3. Week 10 Cluster Evidence to Week 11 Optimisation Decision", weight="bold", pad=20)
    ax.text(0.02, 0.105,
            "Decision colours: green = refine or exploit; amber = boundary testing; blue = continued exploration; grey = reassess or widen the search.",
            transform=ax.transAxes, fontsize=9.5, weight="bold")
    ax.text(0.02, 0.035,
            "Embedded caption: This table links clustering evidence available at the end of Week 10 to the next-query strategy. Distances are normalised by the square root of dimensionality. Week 11 outputs are excluded, so the decision column records a downstream choice rather than retrospective evidence.",
            transform=ax.transAxes, fontsize=9, wrap=True)
    save(fig, "week_10_clustering_figure_3_decision_evidence_colour")


def main():
    df = load_history()
    summary = build_summary(df)
    summary.to_csv(OUTDIR / "week_10_clustering_figure_source.csv", index=False)
    figure_1(summary)
    figure_2(df)
    figure_3(summary)
    print("Generated three verified colour clustering figures. Week 11 outputs were not used.")


if __name__ == "__main__":
    main()
