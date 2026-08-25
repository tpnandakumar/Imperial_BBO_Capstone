from __future__ import annotations

from pathlib import Path
import math

import numpy as np
import pandas as pd
from scipy.stats import norm

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 6
D = 5
ALPHA = 0.05


def repeat_groups(g: pd.DataFrame) -> list[pd.DataFrame]:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    return [grp.copy() for _, grp in g.groupby(xcols, sort=False) if len(grp) >= 2]


def pooled_within_coordinate_sigma(groups: list[pd.DataFrame]) -> tuple[float, float, int]:
    sse = 0.0
    df = 0
    for grp in groups:
        y = grp["output"].to_numpy(float)
        sse += float(np.sum((y - np.mean(y)) ** 2))
        df += len(y) - 1
    sigma2 = sse / df if df > 0 else np.nan
    return float(math.sqrt(sigma2)), float(sigma2), int(df)


def pairwise_repeat_table(groups: list[pd.DataFrame]) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for grp in groups:
        coords = grp.iloc[0][xcols].to_numpy(float)
        y = grp["output"].to_numpy(float)
        weeks = grp["week"].to_numpy(int)
        for i in range(len(grp)):
            for j in range(i + 1, len(grp)):
                rows.append({
                    "coordinate": "-".join(f"{v:.6f}" for v in coords),
                    "week_a": int(weeks[i]),
                    "week_b": int(weeks[j]),
                    "output_a": float(y[i]),
                    "output_b": float(y[j]),
                    "difference": float(y[j] - y[i]),
                    "absolute_difference": abs(float(y[j] - y[i])),
                })
    return pd.DataFrame(rows)


def group_summary(groups: list[pd.DataFrame]) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for grp in groups:
        y = grp["output"].to_numpy(float)
        coords = grp.iloc[0][xcols].to_numpy(float)
        rows.append({
            "coordinate": "-".join(f"{v:.6f}" for v in coords),
            "n_repeats": len(y),
            "mean_output": float(np.mean(y)),
            "sample_sd": float(np.std(y, ddof=1)) if len(y) > 1 else np.nan,
            "range": float(np.max(y) - np.min(y)),
            "min_output": float(np.min(y)),
            "max_output": float(np.max(y)),
        })
    return pd.DataFrame(rows)


def precision_design(sigma: float) -> pd.DataFrame:
    rows = []
    z = norm.ppf(1 - ALPHA / 2)
    for margin in (0.01, 0.02, 0.025, 0.05):
        n = math.ceil((z * sigma / margin) ** 2)
        rows.append({
            "target_half_width": margin,
            "confidence_level": 1 - ALPHA,
            "estimated_sigma": sigma,
            "required_repeats_for_mean_precision": max(2, n),
        })
    return pd.DataFrame(rows)


def shift_detection_design(sigma: float) -> pd.DataFrame:
    rows = []
    z_alpha = norm.ppf(1 - ALPHA / 2)
    for delta in (0.025, 0.05, 0.075, 0.10):
        for power in (0.80, 0.90):
            z_beta = norm.ppf(power)
            n = math.ceil(2 * ((z_alpha + z_beta) * sigma / delta) ** 2)
            rows.append({
                "target_state_shift": delta,
                "power": power,
                "alpha": ALPHA,
                "estimated_sigma": sigma,
                "repeats_per_state_or_context": max(2, n),
                "total_evaluations_two_states": 2 * max(2, n),
            })
    return pd.DataFrame(rows)


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    groups = repeat_groups(g)
    grp_summary = group_summary(groups)
    pairs = pairwise_repeat_table(groups)
    sigma, sigma2, df = pooled_within_coordinate_sigma(groups)

    max_diff = float(pairs["absolute_difference"].max()) if not pairs.empty else np.nan
    mean_abs_diff = float(pairs["absolute_difference"].mean()) if not pairs.empty else np.nan

    deterministic_exact_falsified = bool(max_diff > 0) if np.isfinite(max_diff) else False

    # Under an iid Gaussian repeatability model, the SD of a pairwise difference is sqrt(2)*sigma.
    pair_sd = math.sqrt(2) * sigma if np.isfinite(sigma) else np.nan
    pairs["standardised_difference_under_iid"] = pairs["difference"] / pair_sd if pair_sd > 0 else np.nan
    pairs["two_sided_tail_probability_under_iid"] = (
        2 * (1 - norm.cdf(np.abs(pairs["standardised_difference_under_iid"])))
        if pair_sd > 0 else np.nan
    )

    precision = precision_design(sigma)
    shifts = shift_detection_design(sigma)

    summary = pd.DataFrame([{
        "function": F,
        "repeat_groups": len(groups),
        "repeat_occurrences": int(sum(len(x) for x in groups)),
        "repeat_pairs": len(pairs),
        "pooled_within_coordinate_sigma": sigma,
        "pooled_within_coordinate_variance": sigma2,
        "pooled_variance_df": df,
        "mean_absolute_repeat_difference": mean_abs_diff,
        "max_absolute_repeat_difference": max_diff,
        "coordinate_only_exact_determinism_falsified": deterministic_exact_falsified,
        "iid_variation_compatible_with_current_repeats": bool((pairs["two_sided_tail_probability_under_iid"] > 0.05).all()) if not pairs.empty else False,
        "hidden_state_identified": False,
        "repeatability_conclusion": "static_surface_plus_unresolved_repeat_variation",
        "exact_function_recovered": False,
        "independent_repeat_experiment_required": True,
    }])

    grp_summary.to_csv(OUT / "BBD_016_F6_REPEAT_GROUP_SUMMARY.csv", index=False)
    pairs.to_csv(OUT / "BBD_016_F6_PAIRWISE_REPEAT_TESTS.csv", index=False)
    precision.to_csv(OUT / "BBD_016_F6_REPEAT_PRECISION_DESIGN.csv", index=False)
    shifts.to_csv(OUT / "BBD_016_F6_STATE_SHIFT_POWER_DESIGN.csv", index=False)
    summary.to_csv(OUT / "BBD_016_F6_REPEATABILITY_HYPOTHESIS_SUMMARY.csv", index=False)

    print("BBD 016 F6 repeatability hypothesis testing")
    print("\nRepeat-group summary")
    print(grp_summary.to_string(index=False))
    print("\nPairwise repeat tests")
    print(pairs.to_string(index=False))
    print("\nPrecision design")
    print(precision.to_string(index=False))
    print("\nState-shift power design")
    print(shifts.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
