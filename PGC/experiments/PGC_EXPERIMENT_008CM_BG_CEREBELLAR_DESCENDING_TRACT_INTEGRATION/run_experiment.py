"""PGC Experiment 008CM: reproducible closed-loop modulation simulation.

British English. Requires NumPy and pandas.
Run: python run_experiment.py
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
import pandas as pd

SEEDS = [1709, 1721, 1741, 1753, 1777, 1801, 1811, 1823, 1831, 1847]
ARMS = [
    "baseline",
    "basal_ganglia_only",
    "cerebellar_only",
    "bg_cerebellar",
    "full_integrated",
]
SCENARIOS = {
    "overfitting_pressure": (0.08, 0.0, 1.35, 0.0),
    "underfitting_pressure": (0.03, 0.0, 0.45, 0.0),
    "abrupt_distribution_shift": (0.04, 0.9, 1.0, 0.0),
    "noisy_validation": (0.18, 0.15, 1.0, 0.0),
    "excessive_update_gain": (0.05, 0.0, 1.8, 0.0),
    "rotational_perturbation": (0.05, 0.2, 1.0, 0.38),
}


def simulate(seed: int, scenario: str, arm: str, steps: int = 120) -> dict:
    noise, drift, gain_multiplier, rotation = SCENARIOS[scenario]
    rng = np.random.default_rng(seed)
    x = np.array([-1.2, 1.1], float)
    velocity = np.zeros(2)
    target = np.array([1.0, -0.8], float)
    errors, costs, modules, track = [], [], [], []
    hyperdirect = 0
    previous_error = np.linalg.norm(target - x)
    correction_reversals = 0
    previous_control = None

    for step in range(steps):
        if scenario == "abrupt_distribution_shift" and step == 55:
            target = np.array([-0.75, 1.15])
        elif drift and scenario != "abrupt_distribution_shift":
            target += drift * 0.002 * np.array([math.sin(step / 11), math.cos(step / 13)])

        observed_target = target + rng.normal(0, noise, 2)
        error_vector = observed_target - x
        error = np.linalg.norm(target - x)
        control = 0.18 * gain_multiplier * error_vector
        active_modules = 1

        if rotation:
            cosine, sine = math.cos(rotation), math.sin(rotation)
            control = np.array([[cosine, -sine], [sine, cosine]]) @ control

        if arm in ("basal_ganglia_only", "bg_cerebellar", "full_integrated"):
            active_modules += 1
            trend = error - previous_error
            direct = 1 + 0.22 * np.tanh(max(0, error - 0.45))
            indirect = 1 / (1 + 1.6 * max(0, trend) + 2.2 * max(0, 0.25 - error))
            control *= direct * indirect
            if np.linalg.norm(control) > 0.5 or trend > 0.28:
                control *= 0.18
                hyperdirect += 1

        if arm in ("cerebellar_only", "bg_cerebellar", "full_integrated"):
            active_modules += 1
            predicted = x + control + 0.55 * velocity
            if np.linalg.norm(target - predicted) > error:
                control *= 0.45
            control -= 0.52 * velocity
            control = np.clip(control, -0.32, 0.32)

        if arm == "full_integrated":
            active_modules += 4
            desired = target - x
            desired_norm = np.linalg.norm(desired)
            control_norm = np.linalg.norm(control)
            if desired_norm > 1e-9 and control_norm > 1e-9:
                alignment = np.dot(desired / desired_norm, control / control_norm)
                if alignment < 0.65:
                    control = 0.72 * control + 0.28 * control_norm * desired / desired_norm
            control += 0.08 * desired
            limit = 0.22 + 0.06 * np.tanh(error)
            control_norm = np.linalg.norm(control)
            if control_norm > limit:
                control *= limit / control_norm
            if error < 0.35:
                control += 0.045 * desired
            control -= 0.12 * velocity

        if (
            previous_control is not None
            and np.linalg.norm(control) > 0.03
            and np.linalg.norm(previous_control) > 0.03
            and np.dot(control, previous_control) < 0
        ):
            correction_reversals += 1
        previous_control = control.copy()

        velocity = control + rng.normal(0, 0.01, 2)
        x = x + velocity
        realised_error = np.linalg.norm(target - x)
        errors.append(realised_error)
        track.append(realised_error > 0.8 and step > 20)
        modules.append(active_modules)
        costs.append(active_modules + 4 * np.linalg.norm(control))
        previous_error = error

    error_series = np.asarray(errors)
    steady = error_series[20:]
    recovery_step = steps
    for index in range(20, steps - 5):
        if np.all(error_series[index:index + 5] < 0.22):
            recovery_step = index
            break
    entered = np.where(error_series < 0.22)[0]
    overshoot = 0.0 if not len(entered) else float(max(0, error_series[entered[0]:].max() - 0.22))

    return {
        "seed": seed,
        "scenario": scenario,
        "arm": arm,
        "steps": steps,
        "mean_target_error": float(steady.mean()),
        "final_error": float(error_series[-10:].mean()),
        "accuracy_proxy": float(np.exp(-error_series[-10:].mean())),
        "oscillation_index": float(np.std(np.diff(steady))),
        "stability_index": float(1 / (1 + np.std(steady) + np.std(np.diff(steady)))),
        "loss_of_track_events": int(sum(track)),
        "correction_reversals": correction_reversals,
        "overshoot_proxy": overshoot,
        "hyperdirect_brakes": hyperdirect,
        "recovery_step": recovery_step,
        "mean_active_modules": float(np.mean(modules)),
        "normalised_compute_cost": float(np.mean(costs)),
    }


def normalise_high(values):
    return (values - values.min()) / (values.max() - values.min() + 1e-12)


def normalise_low(values):
    return (values.max() - values) / (values.max() - values.min() + 1e-12)


def main() -> None:
    output = Path(__file__).resolve().parent
    per_run = pd.DataFrame(
        [simulate(seed, scenario, arm) for seed in SEEDS for scenario in SCENARIOS for arm in ARMS]
    )
    summary = per_run.groupby("arm").agg(
        runs=("seed", "count"),
        mean_accuracy=("accuracy_proxy", "mean"),
        mean_target_error=("mean_target_error", "mean"),
        mean_final_error=("final_error", "mean"),
        mean_oscillation=("oscillation_index", "mean"),
        mean_stability=("stability_index", "mean"),
        total_loss_of_track=("loss_of_track_events", "sum"),
        mean_correction_reversals=("correction_reversals", "mean"),
        mean_overshoot=("overshoot_proxy", "mean"),
        mean_recovery_step=("recovery_step", "mean"),
        mean_active_modules=("mean_active_modules", "mean"),
        mean_compute_cost=("normalised_compute_cost", "mean"),
    ).reset_index()
    summary["composite_score"] = (
        0.25 * normalise_high(summary.mean_accuracy)
        + 0.20 * normalise_high(summary.mean_stability)
        + 0.15 * normalise_low(summary.mean_target_error)
        + 0.10 * normalise_low(summary.mean_oscillation)
        + 0.10 * normalise_low(summary.total_loss_of_track)
        + 0.10 * normalise_low(summary.mean_recovery_step)
        + 0.10 * normalise_low(summary.mean_compute_cost)
    )
    summary = summary.sort_values("composite_score", ascending=False)
    per_run.to_csv(output / "per_run_results.csv", index=False)
    summary.to_csv(output / "system_summary.csv", index=False)
    winner = summary.iloc[0].to_dict()
    result = {
        "experiment_id": "PGC_EXPERIMENT_008CM_BG_CEREBELLAR_DESCENDING_TRACT_INTEGRATION",
        "status": "executed_development_simulation",
        "total_runs": len(per_run),
        "winner": winner["arm"],
        "winner_metrics": winner,
        "integration_decision": "Experimental opt-in integration only.",
        "evidence_boundary": "Synthetic controller simulation only; no biological equivalence, clinical validity, electrical energy regeneration or direct monetary cost claim.",
    }
    (output / "results_summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
