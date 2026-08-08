"""Exploratory clustering analysis for BBO Week 10.

Uses the repository's recovered exact history and only observations from Weeks 1 to 10.
Week 11 outputs are never read. Clustering is decision support, not proof of a global optimum.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "PFRAMOS" / "data" / "recovered_exact_history.csv"
OUT = ROOT / "Week_10" / "week_10_cluster_summary.csv"

DECISIONS = {
    1: "Explore", 2: "Refine", 3: "Refine", 4: "Reassess",
    5: "Exploit", 6: "Reassess", 7: "Refine", 8: "Boundary test",
}


def load_history():
    df = pd.read_csv(HISTORY)
    df = df[df["Week"].between(1, 10)].copy()
    if len(df) != 80:
        raise ValueError(f"Expected 80 observations through Week 10, found {len(df)}")
    return df


def analyse_function(df, function):
    sub = df[df["Function"] == function].sort_values("Week").copy()
    dim = int(sub["Dimension"].iloc[0])
    cols = [f"Input_{i}" for i in range(1, dim + 1)]
    X = sub[cols].to_numpy(float)
    y = sub["Output"].to_numpy(float)
    norm = np.sqrt(dim)

    D = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2) / norm
    np.fill_diagonal(D, np.inf)
    nn_idx = D.argmin(axis=1)
    nn_dist = D.min(axis=1)

    candidates = []
    for k in (2, 3):
        km = KMeans(n_clusters=k, random_state=42, n_init=50).fit(X)
        candidates.append((silhouette_score(X, km.labels_), k, km.labels_))
    sil, k, labels = max(candidates, key=lambda z: z[0])

    ranks = (-y).argsort().argsort() + 1
    rows = []
    for i, row in enumerate(sub.itertuples(index=False)):
        vector = "-".join(f"{v:.6f}" for v in X[i])
        rows.append({
            "Function": function,
            "Week": int(row.Week),
            "Input": vector,
            "Output": repr(float(y[i])),
            "Output_rank_within_function": int(ranks[i]),
            "Cluster": int(labels[i]) + 1,
            "Selected_k": k,
            "Silhouette": f"{sil:.6f}",
            "Nearest_neighbour_week": int(sub.iloc[nn_idx[i]]["Week"]),
            "Nearest_neighbour_distance": f"{nn_dist[i]:.8f}",
            "Decision_after_Week_10": DECISIONS[function] if int(row.Week) == 10 else "",
        })
    return rows


def main():
    df = load_history()
    rows = []
    for function in range(1, 9):
        rows.extend(analyse_function(df, function))
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"Wrote {len(rows)} verified observation rows to {OUT}")
    print("Interpret clusters cautiously: ten observations per function are sparse, especially in higher dimensions.")


if __name__ == "__main__":
    main()
