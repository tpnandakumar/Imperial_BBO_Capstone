from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone

from surrogate_evaluator import DATA, evaluate, function_xy, model_library

HERE = Path(__file__).resolve().parent
OUT = HERE / "surrogate_extension_candidates.csv"
RANDOM_STATE = 42
N_GLOBAL = 50000
N_LOCAL = 25000
LOCAL_SCALE = 0.03
TOP_K = 25


def selected_model(fn: int, model_name: str, n_samples: int, dimension: int):
    for candidate in model_library(n_samples, dimension):
        if candidate.name == model_name:
            return clone(candidate.estimator)
    raise KeyError(f"Unknown selected model {model_name} for F{fn}")


def historical_best(df: pd.DataFrame, fn: int):
    part = df.loc[df["Function"] == fn].copy()
    idx = part["Output"].astype(float).idxmax()
    row = part.loc[idx]
    dim = int(row["Dimension"])
    x = np.array([float(row[f"Input_{j}"]) for j in range(1, dim + 1)])
    return x, float(row["Output"]), int(row["Week"])


def generate_candidates(best_x: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    dim = len(best_x)
    global_x = rng.random((N_GLOBAL, dim))
    local_x = np.clip(
        best_x + rng.normal(loc=0.0, scale=LOCAL_SCALE, size=(N_LOCAL, dim)),
        0.0,
        1.0,
    )

    # Include direct axis perturbations and clipped boundary probes so that
    # the search does not depend entirely on random draws.
    deterministic = [best_x.copy()]
    for j in range(dim):
        for step in (0.0025, 0.005, 0.01, 0.02, 0.05):
            low = best_x.copy()
            high = best_x.copy()
            low[j] = max(0.0, low[j] - step)
            high[j] = min(1.0, high[j] + step)
            deterministic.extend([low, high])
        lower_boundary = best_x.copy()
        upper_boundary = best_x.copy()
        lower_boundary[j] = 0.0
        upper_boundary[j] = 1.0
        deterministic.extend([lower_boundary, upper_boundary])

    deterministic_x = np.unique(np.vstack(deterministic), axis=0)
    all_x = np.vstack([global_x, local_x, deterministic_x])
    labels = np.array(
        ["global"] * len(global_x)
        + ["local"] * len(local_x)
        + ["structured"] * len(deterministic_x)
    )
    return all_x, labels


def nearest_sample_distance(candidates: np.ndarray, observed: np.ndarray) -> np.ndarray:
    # Euclidean distance in original [0,1] coordinate space.
    # The small data set makes this direct calculation inexpensive enough.
    result = np.empty(len(candidates))
    batch = 5000
    for start in range(0, len(candidates), batch):
        block = candidates[start:start + batch]
        d = np.sqrt(((block[:, None, :] - observed[None, :, :]) ** 2).sum(axis=2))
        result[start:start + len(block)] = d.min(axis=1)
    return result


def gp_mean_std(model, X: np.ndarray):
    # Pipeline support: transform through all preprocessing stages, then ask
    # the final Gaussian Process estimator for mean and standard deviation.
    if hasattr(model, "named_steps") and "model" in model.named_steps:
        final = model.named_steps["model"]
        if final.__class__.__name__ == "GaussianProcessRegressor":
            transformed = X
            for name, step in model.steps[:-1]:
                transformed = step.transform(transformed)
            return final.predict(transformed, return_std=True)
    return model.predict(X), np.full(len(X), np.nan)


def build_candidates() -> pd.DataFrame:
    if not DATA.exists():
        from build_surrogate_dataset import build
        build()

    _, selection = evaluate()
    df = pd.read_csv(DATA)
    rng = np.random.default_rng(RANDOM_STATE)
    rows = []

    for fn in range(1, 9):
        X, y = function_xy(df, fn)
        dim = X.shape[1]
        selected = selection.loc[selection["Function"] == fn].iloc[0]
        model = selected_model(fn, selected["Model"], len(y), dim)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X, y)

        best_x, best_y, best_week = historical_best(df, fn)
        candidate_x, source = generate_candidates(best_x, rng)
        pred_mean, pred_std = gp_mean_std(model, candidate_x)
        distance = nearest_sample_distance(candidate_x, X)

        # Conservative extrapolation penalty. A large predicted value far from
        # every observed point should not automatically become the winner.
        observed_range = float(np.max(y) - np.min(y))
        scale = observed_range if observed_range > 0 else max(abs(best_y), 1.0)
        distance_penalty = 0.15 * scale * distance
        conservative_score = pred_mean - distance_penalty

        # For GP models, retain a separate exploration score as a diagnostic.
        if np.isfinite(pred_std).any():
            exploration_score = pred_mean + 1.0 * np.nan_to_num(pred_std, nan=0.0) - distance_penalty
        else:
            exploration_score = conservative_score.copy()

        exploit_idx = np.argsort(conservative_score)[-TOP_K:][::-1]
        explore_idx = np.argsort(exploration_score)[-TOP_K:][::-1]
        chosen = []
        seen = set()
        for mode, indices in (("exploit", exploit_idx), ("explore", explore_idx)):
            for idx in indices:
                key = tuple(np.round(candidate_x[idx], 12))
                if key in seen:
                    continue
                seen.add(key)
                chosen.append((mode, idx))
                if sum(1 for m, _ in chosen if m == mode) >= 5:
                    break

        for mode, idx in chosen:
            row = {
                "Function": fn,
                "Dimension": dim,
                "SelectedModel": selected["Model"],
                "ValidationRelativeRMSE": selected["RelativeRMSE_toObservedRange"],
                "ValidationInterpretation": selected["ValidationInterpretation"],
                "CandidateRole": mode,
                "CandidateSource": source[idx],
                "PredictedMean": float(pred_mean[idx]),
                "PredictedStd": float(pred_std[idx]) if np.isfinite(pred_std[idx]) else np.nan,
                "NearestObservedDistance": float(distance[idx]),
                "ConservativeScore": float(conservative_score[idx]),
                "HistoricalBestOutput": best_y,
                "HistoricalBestWeek": best_week,
                "PredictedGainOverHistoricalBest": float(pred_mean[idx] - best_y),
            }
            for j in range(1, 9):
                row[f"x{j}"] = float(candidate_x[idx, j - 1]) if j <= dim else np.nan
            rows.append(row)

    result = pd.DataFrame(rows)
    result.to_csv(OUT, index=False)
    return result


if __name__ == "__main__":
    candidates = build_candidates()
    columns = [
        "Function", "SelectedModel", "ValidationInterpretation", "CandidateRole",
        "PredictedMean", "PredictedStd", "NearestObservedDistance",
        "HistoricalBestOutput", "PredictedGainOverHistoricalBest",
    ]
    print(candidates[columns].to_string(index=False))
    print(f"\nWrote {OUT}")
