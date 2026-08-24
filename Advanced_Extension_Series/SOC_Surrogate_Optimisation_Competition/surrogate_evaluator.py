from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, RBF, WhiteKernel
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge

HERE = Path(__file__).resolve().parent
DATA = HERE / "complete_13_round_history.csv"
MODEL_RESULTS = HERE / "soc_validation_results.csv"
MODEL_SELECTION = HERE / "soc_model_selection.csv"

RANDOM_STATE = 42


@dataclass
class CandidateModel:
    name: str
    estimator: object


def model_library(n_samples: int, dimension: int) -> list[CandidateModel]:
    matern_kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(dimension), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-6, noise_level_bounds=(1e-10, 1e1))

    rbf_kernel = ConstantKernel(1.0, (1e-3, 1e3)) * RBF(
        length_scale=np.ones(dimension), length_scale_bounds=(1e-3, 1e3)
    ) + WhiteKernel(noise_level=1e-6, noise_level_bounds=(1e-10, 1e1))

    models = [
        CandidateModel(
            "GaussianProcess_Matern",
            Pipeline([
                ("scale", StandardScaler()),
                ("model", GaussianProcessRegressor(
                    kernel=matern_kernel,
                    normalize_y=True,
                    n_restarts_optimizer=2,
                    random_state=RANDOM_STATE,
                )),
            ]),
        ),
        CandidateModel(
            "GaussianProcess_RBF",
            Pipeline([
                ("scale", StandardScaler()),
                ("model", GaussianProcessRegressor(
                    kernel=rbf_kernel,
                    normalize_y=True,
                    n_restarts_optimizer=2,
                    random_state=RANDOM_STATE,
                )),
            ]),
        ),
        CandidateModel(
            "RandomForest",
            RandomForestRegressor(
                n_estimators=500,
                min_samples_leaf=1,
                random_state=RANDOM_STATE,
            ),
        ),
        CandidateModel(
            "ExtraTrees",
            ExtraTreesRegressor(
                n_estimators=500,
                min_samples_leaf=1,
                random_state=RANDOM_STATE,
            ),
        ),
        CandidateModel(
            "DistanceWeightedKNN",
            Pipeline([
                ("scale", StandardScaler()),
                ("model", KNeighborsRegressor(
                    n_neighbors=min(4, max(2, n_samples - 1)),
                    weights="distance",
                    p=2,
                )),
            ]),
        ),
    ]

    quadratic_terms = 1 + dimension + dimension * (dimension + 1) // 2
    if n_samples - 1 > quadratic_terms:
        models.append(
            CandidateModel(
                "QuadraticRidge",
                Pipeline([
                    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
                    ("scale", StandardScaler()),
                    ("model", Ridge(alpha=1e-6)),
                ]),
            )
        )

    return models


def function_xy(df: pd.DataFrame, fn: int) -> tuple[np.ndarray, np.ndarray]:
    part = df.loc[df["Function"] == fn].sort_values("Week")
    dim = int(part["Dimension"].iloc[0])
    cols = [f"Input_{j}" for j in range(1, dim + 1)]
    return part[cols].astype(float).to_numpy(), part["Output"].astype(float).to_numpy()


def leave_one_out_predictions(estimator, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    predictions = np.empty(len(y), dtype=float)
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        model = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[mask], y[mask])
        predictions[i] = float(model.predict(X[i : i + 1])[0])
    return predictions


def relative_rmse(rmse: float, y: np.ndarray) -> float:
    observed_range = float(np.max(y) - np.min(y))
    if observed_range == 0:
        return np.nan
    return rmse / observed_range


def evaluate() -> tuple[pd.DataFrame, pd.DataFrame]:
    if not DATA.exists():
        from build_surrogate_dataset import build
        build()

    df = pd.read_csv(DATA)
    records = []

    for fn in range(1, 9):
        X, y = function_xy(df, fn)
        dim = X.shape[1]

        for candidate in model_library(len(y), dim):
            try:
                pred = leave_one_out_predictions(candidate.estimator, X, y)
                mae = float(mean_absolute_error(y, pred))
                rmse = float(np.sqrt(mean_squared_error(y, pred)))
                medae = float(median_absolute_error(y, pred))
                maxae = float(np.max(np.abs(y - pred)))
                records.append({
                    "Function": fn,
                    "Dimension": dim,
                    "Model": candidate.name,
                    "MAE": mae,
                    "RMSE": rmse,
                    "MedianAbsoluteError": medae,
                    "MaxAbsoluteError": maxae,
                    "RelativeRMSE_toObservedRange": relative_rmse(rmse, y),
                    "ObservedMin": float(np.min(y)),
                    "ObservedMax": float(np.max(y)),
                    "ObservedRange": float(np.max(y) - np.min(y)),
                })
            except Exception as exc:
                records.append({
                    "Function": fn,
                    "Dimension": dim,
                    "Model": candidate.name,
                    "MAE": np.nan,
                    "RMSE": np.nan,
                    "MedianAbsoluteError": np.nan,
                    "MaxAbsoluteError": np.nan,
                    "RelativeRMSE_toObservedRange": np.nan,
                    "ObservedMin": float(np.min(y)),
                    "ObservedMax": float(np.max(y)),
                    "ObservedRange": float(np.max(y) - np.min(y)),
                    "Error": str(exc),
                })

    results = pd.DataFrame(records)
    valid = results.dropna(subset=["RMSE"]).copy()
    valid["RMSE_rank"] = valid.groupby("Function")["RMSE"].rank(method="min")
    valid["MAE_rank"] = valid.groupby("Function")["MAE"].rank(method="min")
    valid["CombinedRank"] = valid["RMSE_rank"] + 0.25 * valid["MAE_rank"]

    winners = (
        valid.sort_values(["Function", "CombinedRank", "RMSE", "MAE"])
        .groupby("Function", as_index=False)
        .first()
    )

    def label(value: float) -> str:
        if pd.isna(value):
            return "Unresolved"
        if value <= 0.10:
            return "Higher surrogate confidence"
        if value <= 0.25:
            return "Moderate surrogate confidence"
        return "Low surrogate confidence"

    winners["ValidationInterpretation"] = winners["RelativeRMSE_toObservedRange"].map(label)

    results.to_csv(MODEL_RESULTS, index=False)
    winners.to_csv(MODEL_SELECTION, index=False)
    return results, winners


if __name__ == "__main__":
    results, winners = evaluate()
    print("SOC winning surrogate per function")
    print(winners[["Function", "Model", "RMSE", "MAE", "RelativeRMSE_toObservedRange", "ValidationInterpretation"]].to_string(index=False))
    print(f"\nDetailed SOC validation: {MODEL_RESULTS}")
    print(f"SOC selection table: {MODEL_SELECTION}")
