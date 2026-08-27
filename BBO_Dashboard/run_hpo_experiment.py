"""Run and save the capstone HPO evidence for all eight BBO functions."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from hpo_engine import tune_clustering, tune_surrogate


ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "complete_internal_evidence.csv"
OUTPUT_DIR = ROOT / "hpo_results"
DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


def main() -> None:
    evidence = pd.read_csv(DATA_FILE)
    evidence["source_order"] = evidence.source.map(
        {"starter": 0, **{f"week_{week:02d}": week for week in range(1, 14)}}
    )
    evidence = evidence.sort_values(["function", "source_order", "sequence"])
    OUTPUT_DIR.mkdir(exist_ok=True)
    surrogate_rows: list[pd.DataFrame] = []
    cluster_rows: list[pd.DataFrame] = []
    winner_rows: list[dict[str, float | int | str]] = []
    for function, dimensions in DIMENSIONS.items():
        frame = evidence[evidence.function == function]
        week10 = frame[frame.source.isin([f"week_{week:02d}" for week in range(1, 11)])]
        coordinate_columns = [f"x{index}" for index in range(1, dimensions + 1)]
        coordinates = frame[coordinate_columns].to_numpy(float)
        outputs = frame.output.to_numpy(float)

        surrogate_results, surrogate_winner = tune_surrogate(coordinates, outputs)
        surrogate_results.insert(0, "function", f"F{function}")
        surrogate_rows.append(surrogate_results)
        cluster_results, cluster_winner = tune_clustering(
            week10[coordinate_columns].to_numpy(float),
            cluster_counts=(2, 3),
            n_init_values=(50,),
            random_state=42,
        )
        cluster_results.insert(0, "function", f"F{function}")
        cluster_rows.append(cluster_results)
        winner_rows.append({
            "function": f"F{function}",
            "evidence_week_analysed": 10,
            "submission_week_informed": 11,
            "method": "KMeans exploratory clustering HPO",
            "candidate_clusters": "2,3",
            "selected_clusters": int(cluster_winner["clusters"]),
            "n_init": 50,
            "random_state": 42,
            "selection_measure": "silhouette score",
            "selection_score": float(cluster_winner["silhouette_score"]),
            "observations": len(week10),
        })

    pd.concat(surrogate_rows, ignore_index=True).to_csv(
        OUTPUT_DIR / "posthoc_surrogate_hpo_all_results.csv", index=False
    )
    pd.concat(cluster_rows, ignore_index=True).to_csv(
        OUTPUT_DIR / "week10_clustering_hpo_all_results.csv", index=False
    )
    pd.DataFrame(winner_rows).to_csv(OUTPUT_DIR / "week10_hpo_selected_settings.csv", index=False)


if __name__ == "__main__":
    main()
