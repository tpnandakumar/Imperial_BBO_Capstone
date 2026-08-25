from __future__ import annotations

from pathlib import Path
import sys
import warnings

import numpy as np
import pandas as pd
from scipy.stats import qmc
from sklearn.base import clone
from sklearn.metrics import mean_absolute_error

from bbd_001_system_identification import load_history
from bbd_023_f5_specific_decryption import gp, poly_ridge

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
SOC_DIR = HERE.parent / "SOC_Surrogate_Optimisation_Competition"
if str(SOC_DIR) not in sys.path:
    sys.path.insert(0, str(SOC_DIR))
from surrogate_evaluator import model_library  # noqa: E402

F = 5
D = 4
MIN_TRAIN = 5
RANDOM_STATE = 42


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
            pred = float(np.asarray(model.predict(X[i:i + 1])).ravel()[0])
        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": pred,
            "absolute_error": abs(float(y[i]) - pred),
        })
    return pd.DataFrame(rows)


def select_diverse(df: pd.DataFrame, xcols: list[str], n: int = 10, min_sep: float = 0.25) -> pd.DataFrame:
    chosen = []
    for idx, row in df.sort_values("discrimination_score", ascending=False).iterrows():
        x = row[xcols].to_numpy(float)
        if not chosen:
            chosen.append(idx)
        else:
            prior = df.loc[chosen, xcols].to_numpy(float)
            if float(np.min(np.linalg.norm(prior - x, axis=1))) >= min_sep:
                chosen.append(idx)
        if len(chosen) >= n:
            break
    return df.loc[chosen].copy().reset_index(drop=True)


def main():
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    # Direct same-protocol rechallenge. The BBD 023 winning model is compared with the full SOC library.
    roster = [("BBD023_GP_Matern_2.5", gp("matern"))]
    roster += [(f"SOC_{c.name}", c.estimator) for c in model_library(len(g), D)]

    comp = []
    pred_tables = []
    for name, estimator in roster:
        p = walk_forward(g, estimator)
        p.insert(0, "model", name)
        pred_tables.append(p)
        mae = float(mean_absolute_error(p["actual"], p["prediction"]))
        comp.append({
            "model": name,
            "walk_forward_tests": len(p),
            "walk_forward_mae": mae,
            "normalised_walk_forward_mae": mae / yrange,
            "median_absolute_error": float(p["absolute_error"].median()),
            "max_absolute_error": float(p["absolute_error"].max()),
        })
    comp = pd.DataFrame(comp).sort_values("normalised_walk_forward_mae").reset_index(drop=True)
    comp.insert(0, "rank", np.arange(1, len(comp) + 1))
    comp.to_csv(OUT / "BBD_024_F5_DIRECT_SOC_RECHALLENGE.csv", index=False)
    pd.concat(pred_tables, ignore_index=True).to_csv(OUT / "BBD_024_F5_RECHALLENGE_PREDICTIONS.csv", index=False)

    bbd_row = comp[comp["model"] == "BBD023_GP_Matern_2.5"].iloc[0]
    soc_comp = comp[comp["model"].str.startswith("SOC_")].copy()
    best_soc = soc_comp.iloc[0]
    direct_winner = "BBD023_GP_Matern_2.5" if bbd_row["normalised_walk_forward_mae"] <= best_soc["normalised_walk_forward_mae"] else str(best_soc["model"])

    # Falsification roster keeps the BBD 023 winner, an interpretable quadratic candidate,
    # and the two strongest distinct SOC alternatives under the same chronological protocol.
    estimator_map = dict(roster)
    finalist_estimators = {
        "BBD023_GP_Matern_2.5": gp("matern"),
        "BBD023_quadratic_ridge_1e-4": poly_ridge(2, 1e-4),
    }
    for soc_name in soc_comp["model"].tolist():
        if soc_name not in finalist_estimators:
            finalist_estimators[soc_name] = estimator_map[soc_name]
        if len(finalist_estimators) >= 5:
            break

    fitted = {}
    for name, est in finalist_estimators.items():
        m = clone(est)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            m.fit(X, y)
        fitted[name] = m

    # Prospective identification search. Generated coordinates are hypotheses only, never black-box observations.
    sobol = qmc.Sobol(d=D, scramble=True, seed=RANDOM_STATE)
    candidates = sobol.random_base2(m=14)  # 16384 points
    corners = np.array(np.meshgrid(*[[0.0, 1.0]] * D)).T.reshape(-1, D)
    # Include boundary-near points because F5 historically concentrated near x2,x3,x4=1.
    eps = np.array([1e-4, 1e-3, 1e-2, 5e-2])
    boundary_pts = []
    for e in eps:
        for x1 in [0.0, 0.1, 0.25, 0.5, 1.0]:
            boundary_pts.append([x1, 1.0-e, 1.0-e, 1.0-e])
    C = np.vstack([candidates, corners, np.asarray(boundary_pts, dtype=float)])

    finalist_names = list(fitted.keys())
    pred_cols = {}
    for name, model in fitted.items():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            pred_cols[name] = np.asarray(model.predict(C), dtype=float).ravel()
    P = np.column_stack([pred_cols[name] for name in finalist_names])
    pred_std = np.std(P, axis=1)
    spread = np.max(P, axis=1) - np.min(P, axis=1)
    novelty = np.min(np.linalg.norm(C[:, None, :] - X[None, :, :], axis=2), axis=1)
    score = (pred_std / yrange) * (0.5 + novelty)

    qdf = pd.DataFrame(C, columns=xcols)
    qdf.insert(0, "function", F)
    qdf["discrimination_score"] = score
    qdf["normalised_prediction_std"] = pred_std / yrange
    qdf["normalised_prediction_spread"] = spread / yrange
    qdf["novelty"] = novelty
    qdf["predicted_min"] = np.min(P, axis=1)
    qdf["predicted_max"] = np.max(P, axis=1)
    for name in finalist_names:
        qdf[f"prediction_{name}"] = pred_cols[name]

    selected = select_diverse(qdf, xcols, n=10, min_sep=0.25)
    selected.insert(1, "query_rank", np.arange(1, len(selected) + 1))
    selected["coordinate"] = selected[xcols].apply(lambda r: "-".join(f"{float(v):.6f}" for v in r), axis=1)
    selected.to_csv(OUT / "BBD_024_F5_DISCRIMINATORY_QUERIES.csv", index=False)

    top = selected.iloc[0]
    summary = pd.DataFrame([{
        "function": F,
        "bbd023_matern_normalised_walk_forward_mae": float(bbd_row["normalised_walk_forward_mae"]),
        "best_soc_model_same_protocol": str(best_soc["model"]),
        "best_soc_normalised_walk_forward_mae": float(best_soc["normalised_walk_forward_mae"]),
        "direct_rechallenge_winner": direct_winner,
        "bbd_relative_gain_vs_best_soc": float((best_soc["normalised_walk_forward_mae"] - bbd_row["normalised_walk_forward_mae"]) / best_soc["normalised_walk_forward_mae"]),
        "top_discriminatory_coordinate": str(top["coordinate"]),
        "top_discrimination_score": float(top["discrimination_score"]),
        "top_normalised_prediction_spread": float(top["normalised_prediction_spread"]),
        "top_novelty": float(top["novelty"]),
        "models_in_falsification_roster": len(finalist_names),
        "exact_function_recovered": False,
        "independent_black_box_evaluation_required": True,
        "interpretation": "direct_same_protocol_rechallenge_plus_f5_discriminatory_falsification",
    }])
    summary.to_csv(OUT / "BBD_024_F5_RECHALLENGE_FALSIFICATION_SUMMARY.csv", index=False)

    print("BBD 024 F5 direct SOC rechallenge and discriminatory falsification")
    print("\nSame-protocol chronological competition")
    print(comp.to_string(index=False))
    print("\nTop discriminatory queries")
    cols = ["query_rank", "coordinate", "discrimination_score", "normalised_prediction_spread", "novelty"] + [f"prediction_{n}" for n in finalist_names]
    print(selected[cols].to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
