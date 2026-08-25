from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.base import clone
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from bbd_001_system_identification import load_history
from bbd_010_f6_specific_decryption import static_gp

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 6
D = 5
MIN_TRAIN = 5
MIN_CORRECTION_TRAIN = 3


def safe_spearman(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3 or np.ptp(a[ok]) == 0 or np.ptp(b[ok]) == 0:
        return np.nan, np.nan
    r, p = spearmanr(a[ok], b[ok])
    return float(r), float(p)


def walk_forward_static_gp(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    previous_residual = 0.0

    for i in range(MIN_TRAIN, len(g)):
        model = static_gp(D)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[:i], y[:i])
            pred, std = model.predict(X[i:i+1], return_std=True)
        pred = float(pred[0])
        std = float(std[0])
        residual = float(y[i] - pred)
        distances = np.linalg.norm(X[:i] - X[i], axis=1)
        nearest_distance = float(distances.min())
        nearest_index = int(np.argmin(distances))
        nearest_output_difference = float(abs(y[i] - y[nearest_index]))
        movement = float(np.linalg.norm(X[i] - X[i - 1]))

        # Local response roughness: dispersion of the three nearest historical outputs.
        k = min(3, i)
        nn = np.argsort(distances)[:k]
        local_output_std = float(np.std(y[nn], ddof=0)) if k > 1 else 0.0

        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "static_gp_prediction": pred,
            "residual": residual,
            "absolute_residual": abs(residual),
            "gp_predictive_std": std,
            "nearest_coordinate_distance": nearest_distance,
            "movement_from_previous": movement,
            "local_output_std": local_output_std,
            "nearest_output_difference": nearest_output_difference,
            "previous_residual": previous_residual,
        })
        previous_residual = residual

    return pd.DataFrame(rows)


def residual_diagnostics(wf: pd.DataFrame) -> pd.DataFrame:
    predictors = [
        "week",
        "gp_predictive_std",
        "nearest_coordinate_distance",
        "movement_from_previous",
        "local_output_std",
        "nearest_output_difference",
        "previous_residual",
    ]
    rows = []
    for predictor in predictors:
        r_signed, p_signed = safe_spearman(wf[predictor].to_numpy(), wf["residual"].to_numpy())
        r_abs, p_abs = safe_spearman(wf[predictor].to_numpy(), wf["absolute_residual"].to_numpy())
        rows.append({
            "predictor": predictor,
            "spearman_with_signed_residual": r_signed,
            "signed_residual_p_value": p_signed,
            "spearman_with_absolute_residual": r_abs,
            "absolute_residual_p_value": p_abs,
        })
    return pd.DataFrame(rows)


def correction_model():
    return Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=1.0)),
    ])


def expanding_residual_correction(wf: pd.DataFrame, predictors: list[str]) -> pd.DataFrame:
    rows = []
    y_res = wf["residual"].to_numpy(float)
    base_pred = wf["static_gp_prediction"].to_numpy(float)
    actual = wf["actual"].to_numpy(float)
    X = wf[predictors].to_numpy(float)

    for i in range(MIN_CORRECTION_TRAIN, len(wf)):
        model = clone(correction_model())
        model.fit(X[:i], y_res[:i])
        predicted_residual = float(model.predict(X[i:i+1])[0])
        corrected_prediction = float(base_pred[i] + predicted_residual)
        rows.append({
            "week": int(wf.loc[i, "week"]),
            "actual": float(actual[i]),
            "baseline_prediction": float(base_pred[i]),
            "predicted_residual": predicted_residual,
            "corrected_prediction": corrected_prediction,
            "baseline_absolute_error": abs(float(actual[i] - base_pred[i])),
            "corrected_absolute_error": abs(float(actual[i] - corrected_prediction)),
        })
    return pd.DataFrame(rows)


def repeat_context(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for coords, grp in g.groupby(xcols, sort=False, dropna=False):
        if len(grp) < 2:
            continue
        vals = grp.sort_values("week")
        outputs = vals["output"].to_numpy(float)
        weeks = vals["week"].to_numpy(int)
        coord = "-".join(f"{float(v):.6f}" for v in coords)
        for j in range(1, len(vals)):
            rows.append({
                "coordinate": coord,
                "earlier_week": int(weeks[j - 1]),
                "later_week": int(weeks[j]),
                "week_gap": int(weeks[j] - weeks[j - 1]),
                "earlier_output": float(outputs[j - 1]),
                "later_output": float(outputs[j]),
                "signed_change": float(outputs[j] - outputs[j - 1]),
                "absolute_change": float(abs(outputs[j] - outputs[j - 1])),
            })
    return pd.DataFrame(rows)


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    yrange = float(np.ptp(g["output"].to_numpy(float))) or 1.0

    wf = walk_forward_static_gp(g)
    wf.to_csv(OUT / "BBD_011_F6_STATIC_GP_RESIDUALS.csv", index=False)

    diag = residual_diagnostics(wf)
    diag.to_csv(OUT / "BBD_011_F6_RESIDUAL_DIAGNOSTICS.csv", index=False)

    repeat = repeat_context(g)
    repeat.to_csv(OUT / "BBD_011_F6_REPEAT_CONTEXT.csv", index=False)

    correction_sets = {
        "uncertainty_only": ["gp_predictive_std"],
        "novelty_only": ["nearest_coordinate_distance"],
        "movement_only": ["movement_from_previous"],
        "previous_residual_only": ["previous_residual"],
        "local_roughness_only": ["local_output_std"],
        "combined_observable": [
            "gp_predictive_std",
            "nearest_coordinate_distance",
            "movement_from_previous",
            "local_output_std",
            "previous_residual",
        ],
    }

    comp_rows = []
    correction_frames = []
    for name, predictors in correction_sets.items():
        pred = expanding_residual_correction(wf, predictors)
        pred.insert(0, "correction_model", name)
        correction_frames.append(pred)
        if pred.empty:
            continue
        base_mae = float(pred["baseline_absolute_error"].mean())
        corrected_mae = float(pred["corrected_absolute_error"].mean())
        comp_rows.append({
            "correction_model": name,
            "predictors": "+".join(predictors),
            "n_corrected_forward_tests": len(pred),
            "baseline_mae_same_tests": base_mae,
            "corrected_mae": corrected_mae,
            "normalised_corrected_mae": corrected_mae / yrange,
            "mae_gain_over_baseline": base_mae - corrected_mae,
            "improves_baseline": bool(corrected_mae < base_mae),
        })

    corrections = pd.DataFrame(comp_rows).sort_values("corrected_mae").reset_index(drop=True)
    if not corrections.empty:
        corrections.insert(0, "rank", np.arange(1, len(corrections) + 1))
    corrections.to_csv(OUT / "BBD_011_F6_RESIDUAL_CORRECTION_COMPETITION.csv", index=False)
    if correction_frames:
        pd.concat(correction_frames, ignore_index=True).to_csv(
            OUT / "BBD_011_F6_RESIDUAL_CORRECTION_PREDICTIONS.csv", index=False
        )

    baseline_mae = float(wf["absolute_residual"].mean())
    strongest_abs = diag.loc[diag["spearman_with_absolute_residual"].abs().idxmax()]
    strongest_signed = diag.loc[diag["spearman_with_signed_residual"].abs().idxmax()]
    best_correction = corrections.iloc[0] if not corrections.empty else None

    # Conservative interpretation: with eight walk-forward residuals, correlations are exploratory.
    # A residual mechanism is promoted only if an expanding correction improves prediction.
    if best_correction is not None and bool(best_correction["improves_baseline"]):
        residual_interpretation = f"structured_residual_candidate:{best_correction['correction_model']}"
    else:
        residual_interpretation = "unresolved_variability_no_predictive_correction"

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "n_walk_forward_residuals": len(wf),
        "static_gp_walk_forward_mae": baseline_mae,
        "static_gp_normalised_walk_forward_mae": baseline_mae / yrange,
        "strongest_signed_residual_association": strongest_signed["predictor"],
        "strongest_signed_spearman": float(strongest_signed["spearman_with_signed_residual"]),
        "strongest_abs_residual_association": strongest_abs["predictor"],
        "strongest_abs_spearman": float(strongest_abs["spearman_with_absolute_residual"]),
        "best_residual_correction": None if best_correction is None else best_correction["correction_model"],
        "best_residual_correction_gain": np.nan if best_correction is None else float(best_correction["mae_gain_over_baseline"]),
        "repeat_pairs": len(repeat),
        "max_repeat_absolute_change": 0.0 if repeat.empty else float(repeat["absolute_change"].max()),
        "residual_interpretation": residual_interpretation,
        "exact_function_recovered": False,
        "independent_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_011_F6_RESIDUAL_DECOMPOSITION_SUMMARY.csv", index=False)

    print("BBD 011 F6 residual decomposition")
    print("\nResidual diagnostics")
    print(diag.to_string(index=False))
    print("\nResidual correction competition")
    print(corrections.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
