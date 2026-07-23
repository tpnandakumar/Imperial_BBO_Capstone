"""Walk-forward model comparison for fit regulation in PFRAMOS.

The script compares deliberately simple and moderately flexible models. It
never selects a model from training error alone. Results are written to the
public audit area and contain no unsubmitted candidate coordinates.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

import numpy as np

from PFRAMOS.adapters.imperial_bbo.dataset import Observation, load_history


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "outputs" / "public" / "walk_forward_model_comparison.csv"


@dataclass(frozen=True)
class ModelSpec:
    name: str
    feature_builder: Callable[[np.ndarray], np.ndarray]
    ridge: float


def linear_features(x: np.ndarray) -> np.ndarray:
    return np.concatenate(([1.0], x))


def quadratic_features(x: np.ndarray) -> np.ndarray:
    features = [1.0]
    features.extend(x.tolist())
    features.extend((x * x).tolist())
    return np.asarray(features, dtype=float)


def sparse_quadratic_features(x: np.ndarray) -> np.ndarray:
    """Use linear terms and squares only, avoiding unrestricted interactions."""

    return quadratic_features(x)


MODEL_SPECS = (
    ModelSpec("ridge_linear", linear_features, 1e-3),
    ModelSpec("ridge_linear_strong", linear_features, 1e-1),
    ModelSpec("ridge_sparse_quadratic", sparse_quadratic_features, 1e-2),
)


def _fit_ridge(
    observations: Sequence[Observation],
    spec: ModelSpec,
) -> np.ndarray:
    design = np.vstack(
        [spec.feature_builder(np.asarray(item.coordinates, dtype=float)) for item in observations]
    )
    target = np.asarray([float(item.output) for item in observations], dtype=float)
    penalty = np.eye(design.shape[1], dtype=float) * spec.ridge
    penalty[0, 0] = 0.0
    return np.linalg.pinv(design.T @ design + penalty) @ design.T @ target


def _predict(observation: Observation, coefficients: np.ndarray, spec: ModelSpec) -> float:
    features = spec.feature_builder(np.asarray(observation.coordinates, dtype=float))
    return float(features @ coefficients)


def _baseline_prediction(training: Sequence[Observation], name: str) -> float:
    values = [float(item.output) for item in training]
    if name == "last_value":
        return values[-1]
    if name == "historical_mean":
        return float(sum(values) / len(values))
    raise ValueError(name)


def _direction_correct(previous: float, predicted: float, observed: float) -> int:
    predicted_direction = math.copysign(1.0, predicted - previous) if predicted != previous else 0.0
    observed_direction = math.copysign(1.0, observed - previous) if observed != previous else 0.0
    return int(predicted_direction == observed_direction)


def evaluate_function(observations: Sequence[Observation]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    minimum_training = 3

    model_names = ["last_value", "historical_mean"] + [spec.name for spec in MODEL_SPECS]
    accumulators: Dict[str, Dict[str, float]] = {
        name: {"absolute_error": 0.0, "squared_error": 0.0, "direction_correct": 0.0, "count": 0.0}
        for name in model_names
    }

    for index in range(minimum_training, len(observations)):
        training = observations[:index]
        test = observations[index]
        previous = float(training[-1].output)
        observed = float(test.output)

        predictions: Dict[str, float] = {
            "last_value": _baseline_prediction(training, "last_value"),
            "historical_mean": _baseline_prediction(training, "historical_mean"),
        }

        for spec in MODEL_SPECS:
            coefficients = _fit_ridge(training, spec)
            predictions[spec.name] = _predict(test, coefficients, spec)

        for name, predicted in predictions.items():
            error = predicted - observed
            item = accumulators[name]
            item["absolute_error"] += abs(error)
            item["squared_error"] += error * error
            item["direction_correct"] += _direction_correct(previous, predicted, observed)
            item["count"] += 1.0

    for name, values in accumulators.items():
        count = int(values["count"])
        rows.append(
            {
                "Model": name,
                "Walk_Forward_Count": count,
                "MAE": values["absolute_error"] / count,
                "RMSE": math.sqrt(values["squared_error"] / count),
                "Directional_Accuracy": values["direction_correct"] / count,
            }
        )

    best_mae = min(float(row["MAE"]) for row in rows)
    tolerance = 0.05
    for row in rows:
        row["Within_5pct_Efficiency_Basin"] = float(row["MAE"]) <= best_mae * (1.0 + tolerance)

    return rows


def main() -> None:
    history = load_history(REPOSITORY_ROOT, 1, 11)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "Function",
        "Model",
        "Walk_Forward_Count",
        "MAE",
        "RMSE",
        "Directional_Accuracy",
        "Within_5pct_Efficiency_Basin",
    ]

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for function, observations in sorted(history.items()):
            for row in evaluate_function(observations):
                writer.writerow({"Function": function, **row})

    print(f"Walk-forward comparison written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
