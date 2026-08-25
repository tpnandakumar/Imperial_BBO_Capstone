from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

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


def build_observable_context(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    week = g["week"].to_numpy(float)

    movement = np.zeros(len(g), dtype=float)
    prev_y = np.r_[y[0], y[:-1]]
    nearest_dist = np.zeros(len(g), dtype=float)
    local_mean = np.zeros(len(g), dtype=float)
    local_std = np.zeros(len(g), dtype=float)

    for i in range(len(g)):
        if i > 0:
            movement[i] = float(np.linalg.norm(X[i] - X[i - 1]))
            dists = np.linalg.norm(X[:i] - X[i], axis=1)
            nearest_dist[i] = float(np.min(dists))
            k = min(3, i)
            idx = np.argsort(dists)[:k]
            vals = y[:i][idx]
            local_mean[i] = float(np.mean(vals))
            local_std[i] = float(np.std(vals, ddof=0))
        else:
            local_mean[i] = float(y[i])

    week_scaled = (week - week.min()) / max(float(week.max() - week.min()), 1.0)
    return pd.DataFrame({
        "week_scaled": week_scaled,
        "previous_output": prev_y,
        "movement": movement,
        "nearest_distance": nearest_dist,
        "local_mean": local_mean,
        "local_std": local_std,
    })


def baseline_residuals(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        model = static_gp(D)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[:i], y[:i])
            pred, std = model.predict(X[i:i+1], return_std=True)
        rows.append({
            "index": i,
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "baseline_prediction": float(pred[0]),
            "gp_std": float(std[0]),
            "residual": float(y[i] - pred[0]),
        })
    return pd.DataFrame(rows)


def latent_candidates(context: pd.DataFrame, residual_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    feature_cols = ["week_scaled", "previous_output", "movement", "nearest_distance", "local_mean", "local_std"]
    rows = []
    score_rows = []

    ctx = context.iloc[residual_df["index"].to_numpy(int)].reset_index(drop=True)
    R = residual_df["residual"].to_numpy(float)

    for n_comp in (1, 2):
        if len(ctx) <= n_comp + 2:
            continue
        pipe = Pipeline([
            ("scale", StandardScaler()),
            ("pca", PCA(n_components=n_comp, random_state=42)),
        ])
        Z = pipe.fit_transform(ctx[feature_cols].to_numpy(float))
        latent = Z[:, 0]
        corr = float(np.corrcoef(latent, R)[0, 1]) if np.std(latent) > 0 and np.std(R) > 0 else 0.0

        preds = []
        actuals = []
        for i in range(3, len(R)):
            model = Ridge(alpha=1.0)
            model.fit(Z[:i], R[:i])
            pred = float(model.predict(Z[i:i+1])[0])
            preds.append(pred)
            actuals.append(float(R[i]))
        corrected_mae = float(mean_absolute_error(actuals, preds)) if preds else np.nan
        same_base = float(np.mean(np.abs(actuals))) if preds else np.nan
        gain = same_base - corrected_mae if preds else np.nan

        rows.append({
            "latent_components": n_comp,
            "latent1_residual_correlation": corr,
            "eligible_forward_tests": len(preds),
            "baseline_residual_mae_same_tests": same_base,
            "latent_corrected_residual_mae": corrected_mae,
            "mae_gain": gain,
            "improves_baseline": bool(gain > 0) if np.isfinite(gain) else False,
        })

        loadings = pipe.named_steps["pca"].components_
        for comp_i in range(n_comp):
            for feature, loading in zip(feature_cols, loadings[comp_i]):
                score_rows.append({
                    "latent_components": n_comp,
                    "component": comp_i + 1,
                    "feature": feature,
                    "loading": float(loading),
                    "absolute_loading": abs(float(loading)),
                })

    return pd.DataFrame(rows), pd.DataFrame(score_rows)


def repeated_context(g: pd.DataFrame, context: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for coords, grp in g.groupby(xcols, sort=False):
        if len(grp) < 2:
            continue
        idxs = grp.index.to_list()
        vals = grp["output"].to_numpy(float)
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                ia, ib = idxs[a], idxs[b]
                rows.append({
                    "coordinate": "-".join(f"{float(v):.6f}" for v in coords),
                    "week_a": int(g.loc[ia, "week"]),
                    "week_b": int(g.loc[ib, "week"]),
                    "output_a": float(vals[a]),
                    "output_b": float(vals[b]),
                    "output_change": float(vals[b] - vals[a]),
                    "abs_output_change": abs(float(vals[b] - vals[a])),
                    "context_distance": float(np.linalg.norm(context.iloc[ib].to_numpy(float) - context.iloc[ia].to_numpy(float))),
                })
    return pd.DataFrame(rows)


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    context = build_observable_context(g)
    resid = baseline_residuals(g)
    competition, loadings = latent_candidates(context, resid)
    repeats = repeated_context(g, context)

    resid.to_csv(OUT / "BBD_013_F6_BASELINE_RESIDUALS.csv", index=False)
    competition.to_csv(OUT / "BBD_013_F6_LATENT_COMPETITION.csv", index=False)
    loadings.to_csv(OUT / "BBD_013_F6_LATENT_LOADINGS.csv", index=False)
    repeats.to_csv(OUT / "BBD_013_F6_REPEAT_CONTEXT_DISTANCE.csv", index=False)

    if competition.empty:
        best_name = "none"
        best_gain = 0.0
        latent_supported = False
    else:
        ranked = competition.sort_values("latent_corrected_residual_mae").reset_index(drop=True)
        best = ranked.iloc[0]
        best_name = f"pca_{int(best['latent_components'])}_component"
        best_gain = float(best["mae_gain"])
        latent_supported = bool(best_gain > 0)

    repeat_corr = np.nan
    if len(repeats) >= 2 and repeats["context_distance"].std(ddof=0) > 0 and repeats["abs_output_change"].std(ddof=0) > 0:
        repeat_corr = float(np.corrcoef(repeats["context_distance"], repeats["abs_output_change"])[0, 1])

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "n_walk_forward_residuals": len(resid),
        "best_latent_model": best_name,
        "best_latent_mae_gain": best_gain,
        "latent_observable_context_supported": latent_supported,
        "repeat_pairs": len(repeats),
        "repeat_context_vs_abs_change_correlation": repeat_corr,
        "interpretation": "observable_low_dimensional_context_candidate" if latent_supported else "no_observable_latent_context_advantage",
        "exact_function_recovered": False,
        "independent_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_013_F6_LATENT_RECONSTRUCTION_SUMMARY.csv", index=False)

    print("BBD 013 F6 latent-variable reconstruction")
    print("\nLatent competition")
    print(competition.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
