from __future__ import annotations

from pathlib import Path
import sys
import warnings

import numpy as np
import pandas as pd
from scipy.stats import qmc
from sklearn.base import clone
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import DIMS, load_history
from bbd_007_bbd_vs_soc_challenge import (
    BENCHMARKS,
    CENTRES,
    SCALES,
    benchmark_feature,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
ROOT = HERE.parents[1]
SOC_DIR = ROOT / "Advanced_Extension_Series" / "SOC_Surrogate_Optimisation_Competition"
sys.path.insert(0, str(SOC_DIR))
from surrogate_evaluator import model_library as soc_model_library  # noqa: E402

RANDOM_STATE = 42
SYMBOLIC_ALPHAS = [1e-4, 1e-2, 0.1, 1.0, 10.0]
MAX_MODELS = 5
N_SOBOL = 2 ** 14
TOP_QUERIES = 5
MIN_QUERY_SEPARATION_FRACTION = 0.12


def loo_predictions(estimator, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    pred = np.empty(len(y), dtype=float)
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        model = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[mask], y[mask])
        pred[i] = float(model.predict(X[i:i + 1])[0])
    return pred


def symbolic_pool(dim: int):
    rows = []
    for degree in (1, 2):
        for alpha in SYMBOLIC_ALPHAS:
            est = Pipeline([
                ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
                ("scale", StandardScaler()),
                ("ridge", Ridge(alpha=alpha)),
            ])
            rows.append((f"BBD_symbolic_d{degree}_a{alpha:g}", "symbolic", est))
    return rows


def benchmark_pool(X: np.ndarray, y: np.ndarray):
    rows = []
    for family in BENCHMARKS:
        best = None
        for centre in CENTRES:
            for scale in SCALES:
                v = benchmark_feature(X, family, centre, scale)
                pred = loo_predictions(LinearRegression(), v, y)
                mae = float(mean_absolute_error(y, pred))
                candidate = (mae, family, centre, scale)
                if best is None or candidate[0] < best[0]:
                    best = candidate
        mae, family, centre, scale = best
        rows.append((f"BBD_benchmark_{family}_c{centre:g}_s{scale:g}", "benchmark", (family, centre, scale), mae))
    return rows


def evaluate_model_pool(X: np.ndarray, y: np.ndarray):
    records = []
    for name, kind, obj in symbolic_pool(X.shape[1]):
        try:
            pred = loo_predictions(obj, X, y)
            records.append((float(mean_absolute_error(y, pred)), name, kind, obj))
        except Exception:
            pass

    for name, kind, obj, mae in benchmark_pool(X, y):
        records.append((mae, name, kind, obj))

    for candidate in soc_model_library(len(y), X.shape[1]):
        try:
            pred = loo_predictions(candidate.estimator, X, y)
            records.append((float(mean_absolute_error(y, pred)), f"SOC_{candidate.name}", "estimator", candidate.estimator))
        except Exception:
            pass

    records.sort(key=lambda z: z[0])

    selected = []
    seen_families = set()
    for row in records:
        _, name, kind, _ = row
        if kind == "symbolic":
            family = "symbolic_d1" if "_d1_" in name else "symbolic_d2"
        elif kind == "benchmark":
            family = name.split("_c", 1)[0]
        else:
            family = name
        if family in seen_families:
            continue
        selected.append(row)
        seen_families.add(family)
        if len(selected) >= MAX_MODELS:
            break
    return selected


def fit_model(choice, X: np.ndarray, y: np.ndarray):
    mae, name, kind, obj = choice
    if kind in {"symbolic", "estimator"}:
        fitted = clone(obj)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fitted.fit(X, y)
        return mae, name, kind, fitted

    family, centre, scale = obj
    v = benchmark_feature(X, family, centre, scale)
    fitted = LinearRegression().fit(v, y)
    return mae, name, kind, (fitted, family, centre, scale)


def predict_model(fitted_choice, X: np.ndarray):
    _, _, kind, obj = fitted_choice
    if kind in {"symbolic", "estimator"}:
        return np.asarray(obj.predict(X), dtype=float)
    fitted, family, centre, scale = obj
    return np.asarray(fitted.predict(benchmark_feature(X, family, centre, scale)), dtype=float)


def candidate_points(dim: int) -> np.ndarray:
    sampler = qmc.Sobol(d=dim, scramble=True, seed=RANDOM_STATE)
    points = sampler.random_base2(m=int(np.log2(N_SOBOL)))

    if dim <= 8:
        corners = np.array(
            [[float((mask >> j) & 1) for j in range(dim)] for mask in range(2 ** dim)],
            dtype=float,
        )
        points = np.vstack([points, corners])
    return np.unique(points, axis=0)


def novelty(points: np.ndarray, observed: np.ndarray) -> np.ndarray:
    dist = np.sqrt(((points[:, None, :] - observed[None, :, :]) ** 2).sum(axis=2)).min(axis=1)
    return np.clip(dist / np.sqrt(points.shape[1]), 0.0, 1.0)


def choose_diverse_top(points: np.ndarray, scores: np.ndarray, n: int, dim: int):
    order = np.argsort(scores)[::-1]
    chosen = []
    min_sep = MIN_QUERY_SEPARATION_FRACTION * np.sqrt(dim)
    for idx in order:
        p = points[idx]
        if all(np.linalg.norm(p - points[j]) >= min_sep for j in chosen):
            chosen.append(int(idx))
        if len(chosen) >= n:
            break
    return chosen


def main():
    hist = load_history()
    query_rows = []
    roster_rows = []

    for f in range(1, 9):
        d = DIMS[f]
        g = hist[hist["function"] == f].sort_values("week").reset_index(drop=True)
        xcols = [f"x{i}" for i in range(1, d + 1)]
        X = g[xcols].to_numpy(float)
        y = g["output"].to_numpy(float)
        yrange = float(np.ptp(y)) or 1.0
        ymedian = float(np.median(y))

        selected = evaluate_model_pool(X, y)
        fitted = [fit_model(c, X, y) for c in selected]
        for rank, (mae, name, kind, _) in enumerate(fitted, start=1):
            roster_rows.append({
                "function": f,
                "model_rank": rank,
                "model": name,
                "model_type": kind,
                "full_history_loo_mae": mae,
                "normalised_full_history_loo_mae": mae / yrange,
            })

        P = candidate_points(d)
        pred_matrix = np.column_stack([predict_model(m, P) for m in fitted])

        credible = np.all(np.isfinite(pred_matrix), axis=1)
        credible &= np.all(np.abs(pred_matrix - ymedian) <= 5.0 * yrange, axis=1)
        P = P[credible]
        pred_matrix = pred_matrix[credible]

        disagreement = np.std(pred_matrix, axis=1, ddof=0) / yrange
        max_spread = (np.max(pred_matrix, axis=1) - np.min(pred_matrix, axis=1)) / yrange
        nov = novelty(P, X)
        score = (0.65 * disagreement + 0.35 * max_spread) * (0.60 + 0.40 * nov)
        chosen = choose_diverse_top(P, score, TOP_QUERIES, d)

        for query_rank, idx in enumerate(chosen, start=1):
            row = {
                "function": f,
                "query_rank": query_rank,
                "discrimination_score": float(score[idx]),
                "normalised_prediction_std": float(disagreement[idx]),
                "normalised_prediction_spread": float(max_spread[idx]),
                "novelty": float(nov[idx]),
                "predicted_min": float(np.min(pred_matrix[idx])),
                "predicted_max": float(np.max(pred_matrix[idx])),
            }
            for j in range(d):
                row[f"x{j + 1}"] = float(P[idx, j])
            for m_idx, m in enumerate(fitted):
                row[f"prediction_{m_idx + 1}_{m[1]}"] = float(pred_matrix[idx, m_idx])
            query_rows.append(row)

    queries = pd.DataFrame(query_rows)
    roster = pd.DataFrame(roster_rows)
    queries.to_csv(OUT / "BBD_008_DISCRIMINATORY_QUERIES.csv", index=False)
    roster.to_csv(OUT / "BBD_008_MODEL_ROSTER.csv", index=False)

    best = queries[queries["query_rank"] == 1].copy()
    cols = ["function", "discrimination_score", "normalised_prediction_spread", "novelty"]
    print("BBD 008 highest-value discriminatory query per function")
    print(best[cols].to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
