from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.kernel_ridge import KernelRidge
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
RANDOM_STATE = 42


def gp(kernel):
    return GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        random_state=RANDOM_STATE,
        n_restarts_optimizer=2,
    )


def gp_kernel_matern(nu: float):
    return ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(D), length_scale_bounds=(1e-3, 1e3), nu=nu
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))


def gp_kernel_rbf():
    return ConstantKernel(1.0, (1e-3, 1e3)) * RBF(
        length_scale=np.ones(D), length_scale_bounds=(1e-3, 1e3)
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))


def gp_kernel_rq():
    return ConstantKernel(1.0, (1e-3, 1e3)) * RationalQuadratic(
        length_scale=1.0, alpha=1.0,
        length_scale_bounds=(1e-3, 1e3), alpha_bounds=(1e-3, 1e3)
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))


def polynomial_ridge(degree: int, alpha: float):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def walk_forward(g: pd.DataFrame, estimator) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        model = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[:i], y[:i])
            pred = float(np.asarray(model.predict(X[i:i+1])).ravel()[0])
        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": pred,
            "residual": float(y[i] - pred),
            "absolute_error": abs(float(y[i] - pred)),
        })
    return pd.DataFrame(rows)


def repeat_floor(g: pd.DataFrame) -> tuple[int, int, float, float]:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    groups = 0
    nonidentical = 0
    max_range = 0.0
    errors = []
    for _, grp in g.groupby(xcols, sort=False):
        if len(grp) < 2:
            continue
        groups += 1
        vals = grp["output"].to_numpy(float)
        rng = float(np.ptp(vals))
        max_range = max(max_range, rng)
        if rng > 1e-12:
            nonidentical += 1
        med = float(np.median(vals))
        errors.extend(np.abs(vals - med).tolist())
    return groups, nonidentical, max_range, float(np.mean(errors)) if errors else 0.0


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    candidates = [
        ("gp_matern_0.5", gp(gp_kernel_matern(0.5))),
        ("gp_matern_1.5", gp(gp_kernel_matern(1.5))),
        ("gp_matern_2.5_baseline", gp(gp_kernel_matern(2.5))),
        ("gp_rbf", gp(gp_kernel_rbf())),
        ("gp_rational_quadratic", gp(gp_kernel_rq())),
        ("poly2_ridge_0.01", polynomial_ridge(2, 0.01)),
        ("poly2_ridge_0.1", polynomial_ridge(2, 0.1)),
        ("poly3_ridge_1.0", polynomial_ridge(3, 1.0)),
        ("kernel_ridge_rbf", Pipeline([
            ("scale", StandardScaler()),
            ("kr", KernelRidge(alpha=0.1, kernel="rbf", gamma=1.0)),
        ])),
        ("extra_trees", ExtraTreesRegressor(n_estimators=400, min_samples_leaf=1, random_state=RANDOM_STATE)),
        ("random_forest", RandomForestRegressor(n_estimators=400, min_samples_leaf=1, random_state=RANDOM_STATE)),
        ("gradient_boosting", GradientBoostingRegressor(random_state=RANDOM_STATE, n_estimators=100, max_depth=2, learning_rate=0.05, loss="huber")),
    ]

    rows = []
    all_preds = []
    for name, estimator in candidates:
        pred = walk_forward(g, estimator)
        pred.insert(0, "model", name)
        all_preds.append(pred)
        mae = float(mean_absolute_error(pred["actual"], pred["prediction"]))
        rows.append({
            "model": name,
            "walk_forward_tests": len(pred),
            "walk_forward_mae": mae,
            "normalised_walk_forward_mae": mae / yrange,
            "median_absolute_error": float(pred["absolute_error"].median()),
            "max_absolute_error": float(pred["absolute_error"].max()),
            "residual_std": float(pred["residual"].std(ddof=0)),
        })

    comp = pd.DataFrame(rows).sort_values("normalised_walk_forward_mae").reset_index(drop=True)
    comp.insert(0, "rank", np.arange(1, len(comp) + 1))
    comp.to_csv(OUT / "BBD_014_F6_DETERMINISTIC_SURFACE_COMPETITION.csv", index=False)
    preds = pd.concat(all_preds, ignore_index=True)
    preds.to_csv(OUT / "BBD_014_F6_WALK_FORWARD_PREDICTIONS.csv", index=False)

    baseline = comp.loc[comp["model"] == "gp_matern_2.5_baseline"].iloc[0]
    best = comp.iloc[0]
    gain = float(baseline["normalised_walk_forward_mae"] - best["normalised_walk_forward_mae"])
    relative_gain = gain / float(baseline["normalised_walk_forward_mae"]) if float(baseline["normalised_walk_forward_mae"]) else 0.0

    repeat_groups, nonidentical_groups, max_repeat_range, repeat_mae_floor = repeat_floor(g)
    geometry_refined = bool(best["model"] != "gp_matern_2.5_baseline" and gain > 0.002)

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "best_deterministic_model": best["model"],
        "best_normalised_walk_forward_mae": float(best["normalised_walk_forward_mae"]),
        "baseline_model": "gp_matern_2.5_baseline",
        "baseline_normalised_walk_forward_mae": float(baseline["normalised_walk_forward_mae"]),
        "absolute_normalised_gain_over_baseline": gain,
        "relative_gain_over_baseline": relative_gain,
        "deterministic_geometry_refinement_supported": geometry_refined,
        "repeat_groups": repeat_groups,
        "nonidentical_repeat_groups": nonidentical_groups,
        "max_repeat_range": max_repeat_range,
        "repeat_coordinate_mae_floor": repeat_mae_floor,
        "coordinate_only_exact_determinism_falsified": bool(nonidentical_groups > 0),
        "exact_function_recovered": False,
        "independent_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_014_F6_DETERMINISTIC_SURFACE_SUMMARY.csv", index=False)

    print("BBD 014 F6 deterministic surface refinement")
    print(comp.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
