from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 6
D = 5
MIN_TRAIN = 5


def static_gp(dim: int):
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(dim), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))
    return GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        random_state=42,
        n_restarts_optimizer=2,
    )


def quadratic_ridge(alpha: float = 0.1):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def state_ridge(alpha: float = 1.0):
    return Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def build_state_features(g: pd.DataFrame) -> np.ndarray:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    week = g["week"].to_numpy(float)
    week_scaled = (week - week.min()) / max(float(week.max() - week.min()), 1.0)

    prev_y = np.r_[y[0], y[:-1]]
    delta_x = np.zeros(len(g), dtype=float)
    if len(g) > 1:
        delta_x[1:] = np.linalg.norm(X[1:] - X[:-1], axis=1)

    # Previous output and movement are observable state proxies at prediction time.
    return np.column_stack([X, week_scaled, prev_y, delta_x])


def walk_forward_predictions(g: pd.DataFrame, estimator, feature_mode: str) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X_static = g[xcols].to_numpy(float)
    X_state = build_state_features(g)
    y = g["output"].to_numpy(float)
    rows = []

    for i in range(MIN_TRAIN, len(g)):
        Xall = X_static if feature_mode == "static" else X_state
        model = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(Xall[:i], y[:i])
            pred = float(np.asarray(model.predict(Xall[i:i+1])).ravel()[0])
        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": pred,
            "absolute_error": abs(float(y[i]) - pred),
        })
    return pd.DataFrame(rows)


def repeated_coordinate_analysis(g: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    detail_rows = []
    summary_rows = []

    for coords, grp in g.groupby(xcols, dropna=False, sort=False):
        if len(grp) < 2:
            continue
        vals = grp["output"].to_numpy(float)
        weeks = grp["week"].to_numpy(int)
        coord_id = "-".join(f"{float(v):.6f}" for v in coords)
        summary_rows.append({
            "coordinate": coord_id,
            "n_repeats": len(grp),
            "first_week": int(weeks.min()),
            "last_week": int(weeks.max()),
            "output_mean": float(vals.mean()),
            "output_std_population": float(vals.std(ddof=0)),
            "output_range": float(vals.max() - vals.min()),
            "identical_outputs": bool(np.allclose(vals, vals[0], atol=1e-12, rtol=0.0)),
        })
        for _, row in grp.iterrows():
            detail_rows.append({
                "coordinate": coord_id,
                "week": int(row["week"]),
                "output": float(row["output"]),
            })
    return pd.DataFrame(summary_rows), pd.DataFrame(detail_rows)


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    xcols = [f"x{i}" for i in range(1, D + 1)]
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    repeated_summary, repeated_detail = repeated_coordinate_analysis(g)
    repeated_summary.to_csv(OUT / "BBD_010_F6_REPEAT_SUMMARY.csv", index=False)
    repeated_detail.to_csv(OUT / "BBD_010_F6_REPEAT_DETAIL.csv", index=False)

    candidates = [
        ("static_gp", static_gp(D), "static"),
        ("static_quadratic_ridge", quadratic_ridge(0.1), "static"),
        ("state_ridge", state_ridge(1.0), "state"),
        ("state_gp", static_gp(D + 3), "state"),
    ]

    competition = []
    prediction_frames = []
    for name, estimator, mode in candidates:
        pred = walk_forward_predictions(g, estimator, mode)
        pred.insert(0, "model", name)
        prediction_frames.append(pred)
        mae = float(mean_absolute_error(pred["actual"], pred["prediction"]))
        competition.append({
            "model": name,
            "feature_mode": mode,
            "walk_forward_tests": len(pred),
            "walk_forward_mae": mae,
            "normalised_walk_forward_mae": mae / yrange,
            "walk_forward_max_abs_error": float(pred["absolute_error"].max()),
        })

    comp = pd.DataFrame(competition).sort_values("normalised_walk_forward_mae").reset_index(drop=True)
    comp.insert(0, "rank", np.arange(1, len(comp) + 1))
    comp.to_csv(OUT / "BBD_010_F6_MODEL_COMPETITION.csv", index=False)
    pd.concat(prediction_frames, ignore_index=True).to_csv(
        OUT / "BBD_010_F6_WALK_FORWARD_PREDICTIONS.csv", index=False
    )

    # Quantify the irreducible inconsistency visible at exact repeated coordinates.
    if repeated_summary.empty:
        repeat_noise_floor_mae = 0.0
        max_repeat_range = 0.0
        nonidentical_groups = 0
    else:
        max_repeat_range = float(repeated_summary["output_range"].max())
        nonidentical_groups = int((~repeated_summary["identical_outputs"]).sum())
        # For a repeated coordinate, predicting the within-group median is the best constant
        # absolute-error predictor. Its error is an empirical lower bound for coordinate-only models.
        errors = []
        for coord, grp in repeated_detail.groupby("coordinate"):
            med = float(grp["output"].median())
            errors.extend(np.abs(grp["output"].to_numpy(float) - med).tolist())
        repeat_noise_floor_mae = float(np.mean(errors)) if errors else 0.0

    best = comp.iloc[0]
    state_best = comp[comp["feature_mode"] == "state"].iloc[0]
    static_best = comp[comp["feature_mode"] == "static"].iloc[0]
    state_gain = float(static_best["normalised_walk_forward_mae"] - state_best["normalised_walk_forward_mae"])

    mechanism = "state_or_hidden_context_supported" if state_gain > 0 else "static_surface_preferred"
    exact_recovered = False

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "best_model": best["model"],
        "best_feature_mode": best["feature_mode"],
        "best_normalised_walk_forward_mae": float(best["normalised_walk_forward_mae"]),
        "best_static_normalised_mae": float(static_best["normalised_walk_forward_mae"]),
        "best_state_normalised_mae": float(state_best["normalised_walk_forward_mae"]),
        "state_gain_over_static": state_gain,
        "repeat_groups": len(repeated_summary),
        "nonidentical_repeat_groups": nonidentical_groups,
        "max_repeat_range": max_repeat_range,
        "repeat_coordinate_mae_floor": repeat_noise_floor_mae,
        "mechanism_interpretation": mechanism,
        "exact_function_recovered": exact_recovered,
        "independent_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_010_F6_DECRYPTION_SUMMARY.csv", index=False)

    print("BBD 010 F6-specific decryption")
    print(comp.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
