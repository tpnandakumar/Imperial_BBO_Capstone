from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

from bbd_001_system_identification import DIMS, load_history

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)

ALPHAS = [1e-6, 1e-4, 1e-2, 0.1, 1.0, 10.0, 100.0]


def transitions_for_function(g: pd.DataFrame, dim: int) -> pd.DataFrame:
    g = g.sort_values("week").reset_index(drop=True)
    rows = []
    xcols = [f"x{i}" for i in range(1, dim + 1)]
    for j in range(1, len(g)):
        prev = g.iloc[j - 1]
        cur = g.iloc[j]
        dx = np.array([float(cur[c]) - float(prev[c]) for c in xcols], dtype=float)
        dy = float(cur["output"] - prev["output"])
        norm = float(np.linalg.norm(dx))
        l1 = float(np.abs(dx).sum())
        if norm > 0:
            directional_slope = dy / norm
            unit = dx / norm
        else:
            directional_slope = np.nan
            unit = np.zeros(dim)
        dominant_idx = int(np.argmax(np.abs(dx))) if l1 > 0 else -1
        dominance_ratio = float(np.max(np.abs(dx)) / l1) if l1 > 0 else np.nan
        row = {
            "function": int(cur["function"]),
            "from_week": int(prev["week"]),
            "to_week": int(cur["week"]),
            "y_from": float(prev["output"]),
            "y_to": float(cur["output"]),
            "delta_y": dy,
            "step_norm": norm,
            "directional_slope": directional_slope,
            "dominant_coordinate": dominant_idx + 1 if dominant_idx >= 0 else 0,
            "dominance_ratio": dominance_ratio,
        }
        for i in range(dim):
            row[f"dx{i+1}"] = dx[i]
            row[f"unit_dx{i+1}"] = unit[i]
        rows.append(row)
    return pd.DataFrame(rows)


def loo_alpha_score(X: np.ndarray, y: np.ndarray, alpha: float) -> float:
    preds = []
    truths = []
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        if mask.sum() < 2:
            continue
        model = Ridge(alpha=alpha, fit_intercept=False)
        model.fit(X[mask], y[mask])
        preds.append(float(model.predict(X[i : i + 1])[0]))
        truths.append(float(y[i]))
    return float(mean_absolute_error(truths, preds)) if preds else np.nan


def fit_gradient(trans: pd.DataFrame, dim: int, recent_n: int | None = None) -> dict:
    work = trans[trans["step_norm"] > 0].copy()
    if recent_n is not None:
        work = work.tail(recent_n)
    dxcols = [f"dx{i}" for i in range(1, dim + 1)]
    X = work[dxcols].to_numpy(float)
    y = work["delta_y"].to_numpy(float)
    if len(y) < 3:
        return {"alpha": np.nan, "loo_mae": np.nan, "null_mae": np.nan, "r2_like": np.nan, "gradient": np.full(dim, np.nan), "n_transitions": len(y)}

    scores = {a: loo_alpha_score(X, y, a) for a in ALPHAS}
    alpha = min(scores, key=lambda a: np.inf if np.isnan(scores[a]) else scores[a])
    model = Ridge(alpha=alpha, fit_intercept=False)
    model.fit(X, y)
    pred = model.predict(X)
    mae = float(np.mean(np.abs(y - pred)))
    null = float(np.mean(np.abs(y - np.mean(y))))
    r2_like = 1.0 - float(np.sum((y - pred) ** 2) / max(np.sum((y - np.mean(y)) ** 2), 1e-15))
    return {
        "alpha": float(alpha),
        "loo_mae": float(scores[alpha]),
        "training_mae": mae,
        "null_mae": null,
        "r2_like": r2_like,
        "gradient": model.coef_.astype(float),
        "n_transitions": len(y),
    }


def add_predictions(trans: pd.DataFrame, gradient: np.ndarray, dim: int) -> pd.DataFrame:
    out = trans.copy()
    if np.any(np.isnan(gradient)):
        out["gradient_predicted_delta_y"] = np.nan
        out["gradient_residual"] = np.nan
        out["alignment_with_gradient"] = np.nan
        return out
    dxcols = [f"dx{i}" for i in range(1, dim + 1)]
    X = out[dxcols].to_numpy(float)
    pred = X @ gradient
    out["gradient_predicted_delta_y"] = pred
    out["gradient_residual"] = out["delta_y"].to_numpy(float) - pred
    gnorm = float(np.linalg.norm(gradient))
    aligns = []
    for dx in X:
        dnorm = float(np.linalg.norm(dx))
        aligns.append(float(np.dot(dx, gradient) / (dnorm * gnorm)) if dnorm > 0 and gnorm > 0 else np.nan)
    out["alignment_with_gradient"] = aligns
    return out


def main() -> None:
    hist = load_history()
    all_transitions = []
    gradient_rows = []
    summary_rows = []
    axis_rows = []

    for f in range(1, 9):
        dim = DIMS[f]
        g = hist[hist["function"] == f].copy()
        trans = transitions_for_function(g, dim)
        global_fit = fit_gradient(trans, dim)
        local_fit = fit_gradient(trans, dim, recent_n=min(5, len(trans)))
        trans = add_predictions(trans, global_fit["gradient"], dim)
        all_transitions.append(trans)

        gvec = global_fit["gradient"]
        lvec = local_fit["gradient"]
        gnorm = float(np.linalg.norm(gvec)) if not np.any(np.isnan(gvec)) else np.nan
        lnorm = float(np.linalg.norm(lvec)) if not np.any(np.isnan(lvec)) else np.nan
        cos_gl = np.nan
        if np.isfinite(gnorm) and np.isfinite(lnorm) and gnorm > 0 and lnorm > 0:
            cos_gl = float(np.dot(gvec, lvec) / (gnorm * lnorm))

        for i in range(dim):
            gradient_rows.append({
                "function": f,
                "coordinate": i + 1,
                "global_gradient": float(gvec[i]) if not np.isnan(gvec[i]) else np.nan,
                "local_gradient_last5": float(lvec[i]) if not np.isnan(lvec[i]) else np.nan,
                "global_abs_rank": 0,
                "global_sign": "increase" if np.isfinite(gvec[i]) and gvec[i] > 0 else "decrease" if np.isfinite(gvec[i]) and gvec[i] < 0 else "uncertain",
                "local_sign": "increase" if np.isfinite(lvec[i]) and lvec[i] > 0 else "decrease" if np.isfinite(lvec[i]) and lvec[i] < 0 else "uncertain",
            })

        # Near-axis moves give the closest available empirical partial derivative evidence.
        near_axis = trans[(trans["step_norm"] > 0) & (trans["dominance_ratio"] >= 0.80)].copy()
        for _, r in near_axis.iterrows():
            c = int(r["dominant_coordinate"])
            dx = float(r[f"dx{c}"])
            axis_rows.append({
                "function": f,
                "from_week": int(r["from_week"]),
                "to_week": int(r["to_week"]),
                "coordinate": c,
                "dominance_ratio": float(r["dominance_ratio"]),
                "delta_coordinate": dx,
                "delta_y": float(r["delta_y"]),
                "empirical_partial_slope": float(r["delta_y"] / dx) if dx != 0 else np.nan,
            })

        summary_rows.append({
            "function": f,
            "n_transitions": int(global_fit["n_transitions"]),
            "selected_ridge_alpha": global_fit["alpha"],
            "global_gradient_loo_mae": global_fit["loo_mae"],
            "global_gradient_training_mae": global_fit.get("training_mae", np.nan),
            "delta_y_null_mae": global_fit["null_mae"],
            "global_gradient_r2_like": global_fit["r2_like"],
            "global_gradient_norm": gnorm,
            "local_gradient_norm": lnorm,
            "global_local_gradient_cosine": cos_gl,
            "near_axis_transitions": int(len(near_axis)),
        })

    gradients = pd.DataFrame(gradient_rows)
    for f in range(1, 9):
        idx = gradients["function"] == f
        vals = gradients.loc[idx, "global_gradient"].abs().rank(method="min", ascending=False)
        gradients.loc[idx, "global_abs_rank"] = vals.astype("Int64")

    pd.concat(all_transitions, ignore_index=True).to_csv(OUT / "BBD_003_TRANSITION_DIAGNOSTICS.csv", index=False)
    gradients.to_csv(OUT / "BBD_003_COORDINATE_GRADIENTS.csv", index=False)
    pd.DataFrame(summary_rows).to_csv(OUT / "BBD_003_GRADIENT_SUMMARY.csv", index=False)
    pd.DataFrame(axis_rows).to_csv(OUT / "BBD_003_NEAR_AXIS_DERIVATIVES.csv", index=False)

    print("BBD 003 gradient summary")
    print(pd.DataFrame(summary_rows).to_string(index=False))
    print("\nCoordinate gradient estimates")
    print(gradients.to_string(index=False))
    print(f"\nOutputs written to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
