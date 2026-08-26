"""Reproducible hyperparameter optimisation for the Imperial BBO dashboard."""

from __future__ import annotations

from itertools import product

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge


def tune_surrogate(
    coordinates: np.ndarray,
    outputs: np.ndarray,
    degrees: tuple[int, ...] = (1, 2, 3),
    alphas: tuple[float, ...] = (1e-6, 1e-4, 1e-2, 1e-1, 1.0, 10.0),
    minimum_training_rows: int = 5,
) -> tuple[pd.DataFrame, dict[str, float | int]]:
    """Tune polynomial degree and Ridge alpha using expanding chronological validation."""
    coordinates = np.asarray(coordinates, dtype=float)
    outputs = np.asarray(outputs, dtype=float)
    if len(outputs) < minimum_training_rows + 2:
        raise ValueError("At least seven sequential observations are required for HPO.")
    output_scale = float(np.ptp(outputs)) or 1.0
    rows: list[dict[str, float | int]] = []
    for degree, alpha in product(degrees, alphas):
        predictions: list[float] = []
        actual: list[float] = []
        for boundary in range(minimum_training_rows, len(outputs)):
            model = Pipeline([
                ("scale", StandardScaler()),
                ("polynomial", PolynomialFeatures(degree=degree, include_bias=False)),
                ("ridge", Ridge(alpha=alpha)),
            ])
            model.fit(coordinates[:boundary], outputs[:boundary])
            predictions.append(float(model.predict(coordinates[boundary:boundary + 1])[0]))
            actual.append(float(outputs[boundary]))
        rmse = float(np.sqrt(mean_squared_error(actual, predictions)))
        rows.append({
            "degree": degree,
            "alpha": alpha,
            "chronological_rmse": rmse,
            "normalised_rmse": rmse / output_scale,
            "validation_predictions": len(actual),
        })
    results = pd.DataFrame(rows).sort_values(["normalised_rmse", "degree", "alpha"]).reset_index(drop=True)
    winner = results.iloc[0].to_dict()
    return results, winner


def tune_clustering(
    coordinates: np.ndarray,
    cluster_counts: tuple[int, ...] = (2, 3, 4, 5, 6),
    n_init_values: tuple[int, ...] = (10, 25, 50),
    random_state: int = 42,
) -> tuple[pd.DataFrame, dict[str, float | int]]:
    """Tune KMeans cluster count and restart count using silhouette score."""
    coordinates = np.asarray(coordinates, dtype=float)
    scaled = StandardScaler().fit_transform(coordinates)
    rows: list[dict[str, float | int]] = []
    for clusters, n_init in product(cluster_counts, n_init_values):
        if clusters >= len(scaled):
            continue
        model = KMeans(n_clusters=clusters, n_init=n_init, random_state=random_state)
        labels = model.fit_predict(scaled)
        rows.append({
            "clusters": clusters,
            "n_init": n_init,
            "random_state": random_state,
            "silhouette_score": float(silhouette_score(scaled, labels)),
            "inertia": float(model.inertia_),
        })
    if not rows:
        raise ValueError("There are not enough observations for the selected cluster search.")
    results = pd.DataFrame(rows).sort_values(
        ["silhouette_score", "inertia"], ascending=[False, True]
    ).reset_index(drop=True)
    winner = results.iloc[0].to_dict()
    return results, winner
