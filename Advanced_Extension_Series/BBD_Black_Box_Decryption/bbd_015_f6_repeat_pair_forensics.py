from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.preprocessing import StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 6
D = 5


def safe_spearman(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if len(a) < 3 or np.std(a) == 0 or np.std(b) == 0:
        return np.nan, np.nan
    r, p = spearmanr(a, b)
    return float(r), float(p)


def build_round_context(hist: pd.DataFrame) -> pd.DataFrame:
    """Create same-round cross-function context without altering the F6 coordinates."""
    pivot = hist.pivot_table(index="week", columns="function", values="output", aggfunc="first").sort_index()
    pivot.columns = [f"round_f{int(c)}_output" for c in pivot.columns]
    # Scale each function across rounds so large-valued functions do not dominate distance.
    scaled = pd.DataFrame(
        StandardScaler().fit_transform(pivot),
        index=pivot.index,
        columns=[c.replace("_output", "_z") for c in pivot.columns],
    )
    return pd.concat([pivot, scaled], axis=1).reset_index()


def build_f6_occurrence_table(hist: pd.DataFrame) -> pd.DataFrame:
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True).copy()
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)

    g["coordinate"] = g[xcols].apply(lambda r: "-".join(f"{float(v):.6f}" for v in r), axis=1)
    g["previous_output"] = np.r_[np.nan, y[:-1]]
    g["previous_output_change"] = np.r_[np.nan, np.diff(y)]
    g["next_output"] = np.r_[y[1:], np.nan]
    g["movement_from_previous"] = np.nan
    g["movement_to_next"] = np.nan
    g["previous_coordinate_similarity"] = np.nan
    if len(g) > 1:
        prev_move = np.linalg.norm(X[1:] - X[:-1], axis=1)
        g.loc[1:, "movement_from_previous"] = prev_move
        g.loc[:-2 if False else len(g)-2, "movement_to_next"] = prev_move

    # Distance from current coordinate to the coordinate immediately before it.
    for i in range(1, len(g)):
        g.loc[i, "previous_coordinate_similarity"] = 1.0 - float(np.linalg.norm(X[i] - X[i-1]) / np.sqrt(D))

    # Position in the complete F6 response trajectory.
    g["trajectory_output_rank"] = g["output"].rank(method="average", pct=True)
    g["week_scaled"] = (g["week"] - g["week"].min()) / max(float(g["week"].max() - g["week"].min()), 1.0)

    round_ctx = build_round_context(hist)
    g = g.merge(round_ctx, on="week", how="left")
    return g


def repeated_occurrences(occ: pd.DataFrame) -> pd.DataFrame:
    counts = occ["coordinate"].value_counts()
    repeated = counts[counts > 1].index
    out = occ[occ["coordinate"].isin(repeated)].copy()
    out["repeat_number"] = out.groupby("coordinate").cumcount() + 1
    out["repeat_group_size"] = out.groupby("coordinate")["coordinate"].transform("size")
    return out


def pair_table(rep: pd.DataFrame) -> pd.DataFrame:
    pre_features = [
        "week_scaled",
        "previous_output",
        "previous_output_change",
        "movement_from_previous",
        "previous_coordinate_similarity",
    ]
    round_features = [c for c in rep.columns if c.startswith("round_f") and c.endswith("_z") and not c.startswith("round_f6_")]
    forensic_features = pre_features + ["next_output", "movement_to_next"] + round_features

    rows: list[dict] = []
    for coordinate, grp in rep.groupby("coordinate", sort=False):
        grp = grp.sort_values("week").reset_index(drop=True)
        for a in range(len(grp)):
            for b in range(a + 1, len(grp)):
                ra, rb = grp.iloc[a], grp.iloc[b]
                row = {
                    "coordinate": coordinate,
                    "week_a": int(ra["week"]),
                    "week_b": int(rb["week"]),
                    "week_gap": int(rb["week"] - ra["week"]),
                    "output_a": float(ra["output"]),
                    "output_b": float(rb["output"]),
                    "output_change": float(rb["output"] - ra["output"]),
                    "abs_output_change": abs(float(rb["output"] - ra["output"])),
                }
                for feature in forensic_features:
                    va, vb = ra.get(feature, np.nan), rb.get(feature, np.nan)
                    try:
                        va, vb = float(va), float(vb)
                        row[f"delta__{feature}"] = vb - va if np.isfinite(va) and np.isfinite(vb) else np.nan
                        row[f"abs_delta__{feature}"] = abs(vb - va) if np.isfinite(va) and np.isfinite(vb) else np.nan
                    except (TypeError, ValueError):
                        row[f"delta__{feature}"] = np.nan
                        row[f"abs_delta__{feature}"] = np.nan
                rows.append(row)
    return pd.DataFrame(rows)


def association_table(pairs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in [c for c in pairs.columns if c.startswith("abs_delta__")]:
        tmp = pairs[[col, "abs_output_change"]].dropna()
        if len(tmp) < 3:
            continue
        r, p = safe_spearman(tmp[col].to_numpy(float), tmp["abs_output_change"].to_numpy(float))
        rows.append({
            "feature": col.replace("abs_delta__", ""),
            "n_pairs": len(tmp),
            "spearman_abs_context_change_vs_abs_output_change": r,
            "p_value": p,
            "absolute_spearman": abs(r) if np.isfinite(r) else np.nan,
        })
    return pd.DataFrame(rows).sort_values("absolute_spearman", ascending=False).reset_index(drop=True)


def fingerprint_distances(rep: pd.DataFrame, pairs: pd.DataFrame) -> pd.DataFrame:
    pre_cols = ["week_scaled", "previous_output", "previous_output_change", "movement_from_previous", "previous_coordinate_similarity"]
    round_cols = [c for c in rep.columns if c.startswith("round_f") and c.endswith("_z") and not c.startswith("round_f6_")]

    def distance_for(cols: list[str], wa: int, wb: int) -> float:
        sub = rep[cols].copy()
        # Median imputation is used only to make a descriptive distance defined.
        sub = sub.fillna(sub.median(numeric_only=True)).fillna(0.0)
        Z = StandardScaler().fit_transform(sub)
        idx_a = rep.index[rep["week"] == wa][0]
        idx_b = rep.index[rep["week"] == wb][0]
        pos_a = rep.index.get_loc(idx_a)
        pos_b = rep.index.get_loc(idx_b)
        return float(np.linalg.norm(Z[pos_b] - Z[pos_a]))

    out = pairs[["coordinate", "week_a", "week_b", "abs_output_change"]].copy()
    out["pre_evaluation_fingerprint_distance"] = [distance_for(pre_cols, int(a), int(b)) for a, b in zip(out.week_a, out.week_b)]
    out["cross_function_round_distance"] = [distance_for(round_cols, int(a), int(b)) for a, b in zip(out.week_a, out.week_b)]
    out["combined_fingerprint_distance"] = np.sqrt(
        out["pre_evaluation_fingerprint_distance"] ** 2 + out["cross_function_round_distance"] ** 2
    )
    return out


def main() -> None:
    hist = load_history()
    occ = build_f6_occurrence_table(hist)
    rep = repeated_occurrences(occ).reset_index(drop=True)
    pairs = pair_table(rep)
    assoc = association_table(pairs)
    fp = fingerprint_distances(rep, pairs)

    rep.to_csv(OUT / "BBD_015_F6_REPEAT_OCCURRENCES.csv", index=False)
    pairs.to_csv(OUT / "BBD_015_F6_REPEAT_PAIR_DIFFERENCES.csv", index=False)
    assoc.to_csv(OUT / "BBD_015_F6_REPEAT_PAIR_ASSOCIATIONS.csv", index=False)
    fp.to_csv(OUT / "BBD_015_F6_REPEAT_FINGERPRINT_DISTANCES.csv", index=False)

    fp_rows = []
    for c in ["pre_evaluation_fingerprint_distance", "cross_function_round_distance", "combined_fingerprint_distance"]:
        r, p = safe_spearman(fp[c].to_numpy(float), fp["abs_output_change"].to_numpy(float))
        fp_rows.append({"fingerprint": c, "spearman_with_abs_output_change": r, "p_value": p})
    fp_assoc = pd.DataFrame(fp_rows)

    strongest = assoc.iloc[0] if not assoc.empty else None
    strongest_name = str(strongest["feature"]) if strongest is not None else "none"
    strongest_r = float(strongest["spearman_abs_context_change_vs_abs_output_change"]) if strongest is not None else np.nan

    pre_r = float(fp_assoc.loc[fp_assoc["fingerprint"] == "pre_evaluation_fingerprint_distance", "spearman_with_abs_output_change"].iloc[0])
    round_r = float(fp_assoc.loc[fp_assoc["fingerprint"] == "cross_function_round_distance", "spearman_with_abs_output_change"].iloc[0])

    # With four pairwise comparisons, no association is treated as confirmatory.
    context_candidate = bool(np.isfinite(strongest_r) and abs(strongest_r) >= 0.8)
    summary = pd.DataFrame([{
        "function": F,
        "repeat_groups": int(rep["coordinate"].nunique()),
        "repeat_occurrences": len(rep),
        "repeat_pairs": len(pairs),
        "max_repeat_absolute_output_change": float(pairs["abs_output_change"].max()),
        "strongest_individual_context_feature": strongest_name,
        "strongest_individual_abs_spearman": strongest_r,
        "pre_evaluation_fingerprint_spearman": pre_r,
        "cross_function_round_fingerprint_spearman": round_r,
        "sequence_context_candidate": context_candidate,
        "interpretation": "descriptive_sequence_context_lead_only" if context_candidate else "no_repeat_pair_context_explanation_established",
        "exact_function_recovered": False,
        "independent_query_required": True,
    }])
    fp_assoc.to_csv(OUT / "BBD_015_F6_FINGERPRINT_ASSOCIATIONS.csv", index=False)
    summary.to_csv(OUT / "BBD_015_F6_REPEAT_PAIR_FORENSIC_SUMMARY.csv", index=False)

    print("BBD 015 F6 repeat-pair forensic reconstruction")
    print("\nRepeated occurrences")
    print(rep[["coordinate", "week", "output", "repeat_number", "previous_output", "movement_from_previous", "next_output"]].to_string(index=False))
    print("\nRepeat pairs")
    print(pairs[["coordinate", "week_a", "week_b", "output_change", "abs_output_change"]].to_string(index=False))
    print("\nStrongest individual associations")
    print(assoc.head(10).to_string(index=False))
    print("\nFingerprint associations")
    print(fp_assoc.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
