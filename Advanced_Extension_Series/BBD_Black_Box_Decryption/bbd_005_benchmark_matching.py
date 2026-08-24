from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

from bbd_001_system_identification import DIMS, load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)

CENTRES = [0.0, 0.25, 0.5, 0.75, 1.0]
SCALES = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]


def sphere(z: np.ndarray) -> np.ndarray:
    return np.sum(z**2, axis=1)


def ellipsoid(z: np.ndarray) -> np.ndarray:
    d = z.shape[1]
    weights = 10.0 ** np.linspace(0.0, 3.0, d)
    return np.sum(weights * z**2, axis=1)


def rastrigin(z: np.ndarray) -> np.ndarray:
    d = z.shape[1]
    return 10.0 * d + np.sum(z**2 - 10.0 * np.cos(2.0 * np.pi * z), axis=1)


def ackley(z: np.ndarray) -> np.ndarray:
    d = z.shape[1]
    a, b, c = 20.0, 0.2, 2.0 * np.pi
    s1 = np.sum(z**2, axis=1) / d
    s2 = np.sum(np.cos(c * z), axis=1) / d
    return -a * np.exp(-b * np.sqrt(s1)) - np.exp(s2) + a + np.e


def griewank(z: np.ndarray) -> np.ndarray:
    idx = np.sqrt(np.arange(1, z.shape[1] + 1, dtype=float))
    return np.sum(z**2, axis=1) / 4000.0 - np.prod(np.cos(z / idx), axis=1) + 1.0


def schwefel(z: np.ndarray) -> np.ndarray:
    d = z.shape[1]
    return 418.9829 * d - np.sum(z * np.sin(np.sqrt(np.abs(z))), axis=1)


def rosenbrock(z: np.ndarray) -> np.ndarray:
    if z.shape[1] < 2:
        return np.zeros(z.shape[0])
    return np.sum(100.0 * (z[:, 1:] - z[:, :-1] ** 2) ** 2 + (1.0 - z[:, :-1]) ** 2, axis=1)


FAMILIES = {
    "sphere": sphere,
    "ellipsoid": ellipsoid,
    "rastrigin": rastrigin,
    "ackley": ackley,
    "griewank": griewank,
    "schwefel": schwefel,
    "rosenbrock": rosenbrock,
}


def transformed_feature(x: np.ndarray, family: str, centre: float, scale: float) -> np.ndarray:
    z = scale * (x - centre)
    return FAMILIES[family](z).reshape(-1, 1)


def affine_loocv(x: np.ndarray, y: np.ndarray, family: str, centre: float, scale: float) -> tuple[float, np.ndarray]:
    preds = np.zeros_like(y, dtype=float)
    for i in range(len(y)):
        train = np.ones(len(y), dtype=bool)
        train[i] = False
        phi_train = transformed_feature(x[train], family, centre, scale)
        phi_test = transformed_feature(x[~train], family, centre, scale)
        model = LinearRegression()
        model.fit(phi_train, y[train])
        preds[i] = model.predict(phi_test)[0]
    return float(mean_absolute_error(y, preds)), preds


def fit_affine(x: np.ndarray, y: np.ndarray, family: str, centre: float, scale: float):
    phi = transformed_feature(x, family, centre, scale)
    model = LinearRegression().fit(phi, y)
    pred = model.predict(phi)
    return float(model.intercept_), float(model.coef_[0]), pred


def main() -> None:
    hist = load_history()
    competition = []
    winners = []
    predictions = []

    bbd4_path = OUT / "BBD_004_RECOVERED_EQUATIONS.csv"
    bbd4 = pd.read_csv(bbd4_path) if bbd4_path.exists() else pd.DataFrame()

    for f in range(1, 9):
        dim = DIMS[f]
        g = hist[hist["function"] == f].sort_values("week").copy()
        xcols = [f"x{i}" for i in range(1, dim + 1)]
        x = g[xcols].to_numpy(float)
        y = g["output"].to_numpy(float)
        y_sd = float(np.std(y, ddof=1)) or 1.0

        candidates = []
        for family in FAMILIES:
            for centre in CENTRES:
                for scale in SCALES:
                    mae, _ = affine_loocv(x, y, family, centre, scale)
                    row = {
                        "function": f,
                        "family": family,
                        "centre": centre,
                        "scale": scale,
                        "loocv_mae": mae,
                        "normalised_loocv_mae": mae / y_sd,
                    }
                    competition.append(row)
                    candidates.append(row)

        winner = min(candidates, key=lambda r: r["normalised_loocv_mae"])
        intercept, output_scale, train_pred = fit_affine(
            x, y, winner["family"], winner["centre"], winner["scale"]
        )
        train_r2 = 1.0 - float(
            np.sum((y - train_pred) ** 2) / max(np.sum((y - np.mean(y)) ** 2), 1e-15)
        )
        _, cv_pred = affine_loocv(x, y, winner["family"], winner["centre"], winner["scale"])

        symbolic_nmae = np.nan
        if not bbd4.empty:
            match = bbd4[bbd4["function"] == f]
            if not match.empty:
                symbolic_nmae = float(match.iloc[0]["normalised_loocv_mae"])

        winners.append({
            "function": f,
            "winning_family": winner["family"],
            "centre": winner["centre"],
            "coordinate_scale": winner["scale"],
            "output_intercept": intercept,
            "output_scale": output_scale,
            "normalised_loocv_mae": winner["normalised_loocv_mae"],
            "training_r2_like": train_r2,
            "bbd004_symbolic_normalised_loocv_mae": symbolic_nmae,
            "benchmark_gain_over_bbd004": symbolic_nmae - winner["normalised_loocv_mae"] if np.isfinite(symbolic_nmae) else np.nan,
            "benchmark_beats_bbd004": bool(winner["normalised_loocv_mae"] < symbolic_nmae) if np.isfinite(symbolic_nmae) else False,
        })

        for week, truth, pred in zip(g["week"], y, cv_pred):
            predictions.append({
                "function": f,
                "week": int(week),
                "observed_output": float(truth),
                "benchmark_cv_prediction": float(pred),
                "residual": float(truth - pred),
                "winning_family": winner["family"],
            })

    comp = pd.DataFrame(competition)
    win = pd.DataFrame(winners)
    pred = pd.DataFrame(predictions)

    comp.to_csv(OUT / "BBD_005_BENCHMARK_COMPETITION.csv", index=False)
    win.to_csv(OUT / "BBD_005_BENCHMARK_WINNERS.csv", index=False)
    pred.to_csv(OUT / "BBD_005_BENCHMARK_PREDICTIONS.csv", index=False)

    print("BBD 005 benchmark-family summary")
    print(win[[
        "function", "winning_family", "centre", "coordinate_scale",
        "normalised_loocv_mae", "bbd004_symbolic_normalised_loocv_mae",
        "benchmark_gain_over_bbd004", "benchmark_beats_bbd004"
    ]].to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
