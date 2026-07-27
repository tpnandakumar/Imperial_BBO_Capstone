"""Run PGC Experiment 002 on the UCI Iris classification dataset."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from PGC.architecture.cognitive_router import CandidateConfiguration, route

EXPERTS = (
    "logistic_regression",
    "knn_5",
    "gaussian_nb",
    "decision_tree_depth3",
)


@dataclass(frozen=True)
class ArmResult:
    arm_id: str
    n_test: int
    task_success: float
    balanced_accuracy: float
    macro_f1: float
    log_loss: float
    routing_accuracy: float
    routing_regret: float
    abstention_rate: float
    mean_router_latency_ms: float
    static_expert: str | None


def entropy_uncertainty(probabilities: np.ndarray) -> float:
    values = np.clip(np.asarray(probabilities, dtype=float), 1e-12, 1.0)
    return float(-(values * np.log(values)).sum() / math.log(len(values)))


def bootstrap_accuracy(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    seed: int,
    n_resamples: int,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    scores: list[float] = []
    sample_count = len(y_true)
    for _ in range(n_resamples):
        index = rng.integers(0, sample_count, sample_count)
        scores.append(float(accuracy_score(y_true[index], y_pred[index])))
    return float(np.mean(scores)), float(np.std(scores))


def normalised_efficiency(latencies: dict[str, float]) -> dict[str, float]:
    values = np.asarray([latencies[name] for name in EXPERTS], dtype=float)
    minimum = float(values.min())
    maximum = float(values.max())
    if maximum <= minimum:
        return {name: 1.0 for name in EXPERTS}
    return {
        name: float(1.0 - 0.5 * (latencies[name] - minimum) / (maximum - minimum))
        for name in EXPERTS
    }


def build_models(seed: int) -> dict[str, object]:
    return {
        "logistic_regression": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, random_state=seed),
        ),
        "knn_5": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
        "gaussian_nb": GaussianNB(),
        "decision_tree_depth3": DecisionTreeClassifier(max_depth=3, random_state=seed),
    }


def dataset_checksum(features: np.ndarray, target: np.ndarray) -> str:
    digest = hashlib.sha256()
    digest.update(np.ascontiguousarray(features).tobytes())
    digest.update(np.ascontiguousarray(target).tobytes())
    return digest.hexdigest()


def run_seed(seed: int, bootstrap_resamples: int = 100) -> dict:
    dataset = load_iris()
    features = np.asarray(dataset.data, dtype=float)
    target = np.asarray(dataset.target, dtype=int)

    x_development, x_test, y_development, y_test = train_test_split(
        features,
        target,
        test_size=0.20,
        stratify=target,
        random_state=seed,
    )
    x_train, x_validation, y_train, y_validation = train_test_split(
        x_development,
        y_development,
        test_size=0.25,
        stratify=y_development,
        random_state=seed + 1000,
    )

    validation: dict[str, dict] = {}
    protected_test: dict[str, dict] = {}
    inference_latency: dict[str, float] = {}

    for expert_name, model in build_models(seed).items():
        model.fit(x_train, y_train)  # type: ignore[attr-defined]
        validation_probabilities = model.predict_proba(x_validation)  # type: ignore[attr-defined]
        validation_predictions = np.argmax(validation_probabilities, axis=1)

        class_recall = [
            float(
                np.mean(
                    validation_predictions[y_validation == class_index] == class_index
                )
            )
            for class_index in range(3)
        ]
        bootstrap_mean, bootstrap_std = bootstrap_accuracy(
            y_validation,
            validation_predictions,
            seed + sum(ord(character) for character in expert_name),
            bootstrap_resamples,
        )

        started = time.perf_counter()
        for _ in range(100):
            model.predict_proba(x_validation)  # type: ignore[attr-defined]
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        inference_latency[expert_name] = elapsed_ms / (100 * len(x_validation))

        validation[expert_name] = {
            "accuracy": float(accuracy_score(y_validation, validation_predictions)),
            "balanced_accuracy": float(
                balanced_accuracy_score(y_validation, validation_predictions)
            ),
            "class_recall": class_recall,
            "bootstrap_accuracy_mean": bootstrap_mean,
            "bootstrap_accuracy_std": bootstrap_std,
        }

        test_probabilities = model.predict_proba(x_test)  # type: ignore[attr-defined]
        protected_test[expert_name] = {
            "probabilities": test_probabilities,
            "predictions": np.argmax(test_probabilities, axis=1),
        }

    efficiency = normalised_efficiency(inference_latency)
    static_expert = max(
        EXPERTS,
        key=lambda expert: (
            validation[expert]["balanced_accuracy"],
            validation[expert]["accuracy"],
            efficiency[expert],
        ),
    )

    arm_ids = (
        "static_validation_expert",
        "random_router",
        "confidence_only_router",
        "oracle_router",
        "pgc_evidence_router",
        "pgc_without_coherence",
        "pgc_without_efficiency",
    )
    arm_results: list[ArmResult] = []

    for arm_id in arm_ids:
        rng = random.Random(seed + sum(ord(character) for character in arm_id))
        selected_labels: list[int] = []
        selected_probabilities: list[np.ndarray] = []
        selected_experts: list[str | None] = []
        oracle_experts: list[str] = []
        route_latencies: list[float] = []
        abstentions = 0

        for row_index in range(len(y_test)):
            predictions = {
                expert: int(protected_test[expert]["predictions"][row_index])
                for expert in EXPERTS
            }
            probabilities = {
                expert: protected_test[expert]["probabilities"][row_index]
                for expert in EXPERTS
            }
            correct_experts = [
                expert for expert in EXPERTS if predictions[expert] == int(y_test[row_index])
            ]
            oracle_expert = (
                max(
                    correct_experts,
                    key=lambda expert: (
                        validation[expert]["balanced_accuracy"],
                        efficiency[expert],
                    ),
                )
                if correct_experts
                else max(
                    EXPERTS,
                    key=lambda expert: float(np.max(probabilities[expert])),
                )
            )
            oracle_experts.append(oracle_expert)

            started = time.perf_counter()
            selected_expert: str | None
            if arm_id == "static_validation_expert":
                selected_expert = static_expert
            elif arm_id == "random_router":
                selected_expert = rng.choice(EXPERTS)
            elif arm_id == "confidence_only_router":
                selected_expert = max(
                    EXPERTS,
                    key=lambda expert: float(np.max(probabilities[expert])),
                )
            elif arm_id == "oracle_router":
                selected_expert = oracle_expert
            else:
                vote_counts = {
                    class_index: sum(
                        predictions[expert] == class_index for expert in EXPERTS
                    )
                    for class_index in range(3)
                }
                candidates: list[CandidateConfiguration] = []
                for expert in EXPERTS:
                    predicted_class = predictions[expert]
                    confidence = float(np.max(probabilities[expert]))
                    class_reliability = validation[expert]["class_recall"][predicted_class]
                    task_fitness = 0.55 * class_reliability + 0.45 * confidence
                    coherence = (
                        vote_counts[predicted_class] / len(EXPERTS)
                        if arm_id != "pgc_without_coherence"
                        else 0.75
                    )
                    robustness = max(
                        0.0,
                        min(
                            1.0,
                            validation[expert]["bootstrap_accuracy_mean"]
                            - validation[expert]["bootstrap_accuracy_std"],
                        ),
                    )
                    efficiency_value = (
                        efficiency[expert]
                        if arm_id != "pgc_without_efficiency"
                        else 0.75
                    )
                    candidates.append(
                        CandidateConfiguration(
                            candidate_id=expert,
                            task_fitness=task_fitness,
                            evidence_validity=validation[expert]["balanced_accuracy"],
                            coherence=coherence,
                            robustness=robustness,
                            uncertainty=entropy_uncertainty(probabilities[expert]),
                            safety=1.0,
                            efficiency=efficiency_value,
                        )
                    )
                selected_expert = route(
                    candidates,
                    minimum_score=0.55,
                ).selected_candidate_id
            route_latencies.append((time.perf_counter() - started) * 1000.0)
            selected_experts.append(selected_expert)

            if selected_expert is None:
                abstentions += 1
                selected_labels.append(-1)
                selected_probabilities.append(np.ones(3, dtype=float) / 3.0)
            else:
                selected_labels.append(predictions[selected_expert])
                selected_probabilities.append(probabilities[selected_expert])

        selected_array = np.asarray(selected_labels, dtype=int)
        selected_probability_array = np.asarray(selected_probabilities, dtype=float)
        oracle_success = float(
            np.mean(
                [
                    protected_test[expert]["predictions"][index] == y_test[index]
                    for index, expert in enumerate(oracle_experts)
                ]
            )
        )
        task_success = float(np.mean(selected_array == y_test))
        routing_accuracy = float(
            np.mean(
                [selected == oracle for selected, oracle in zip(selected_experts, oracle_experts)]
            )
        )

        arm_results.append(
            ArmResult(
                arm_id=arm_id,
                n_test=len(y_test),
                task_success=task_success,
                balanced_accuracy=float(balanced_accuracy_score(y_test, selected_array)),
                macro_f1=float(f1_score(y_test, selected_array, average="macro")),
                log_loss=float(log_loss(y_test, selected_probability_array, labels=[0, 1, 2])),
                routing_accuracy=routing_accuracy,
                routing_regret=max(0.0, oracle_success - task_success),
                abstention_rate=abstentions / len(y_test),
                mean_router_latency_ms=float(np.mean(route_latencies)),
                static_expert=(
                    static_expert if arm_id == "static_validation_expert" else None
                ),
            )
        )

    return {
        "seed": seed,
        "split": {
            "train": len(y_train),
            "validation": len(y_validation),
            "protected_test": len(y_test),
        },
        "validation_evidence": validation,
        "inference_latency_ms_per_sample": inference_latency,
        "efficiency": efficiency,
        "static_expert": static_expert,
        "arms": [asdict(result) for result in arm_results],
        "dataset_checksum_sha256": dataset_checksum(features, target),
    }


def run_experiment(seeds: list[int], bootstrap_resamples: int = 100) -> dict:
    seed_results = [run_seed(seed, bootstrap_resamples) for seed in seeds]
    arm_ids = [result["arm_id"] for result in seed_results[0]["arms"]]
    metric_names = (
        "task_success",
        "balanced_accuracy",
        "macro_f1",
        "log_loss",
        "routing_accuracy",
        "routing_regret",
        "abstention_rate",
        "mean_router_latency_ms",
    )
    aggregate: dict[str, dict[str, float]] = {}
    for arm_id in arm_ids:
        rows = [
            next(item for item in seed_result["arms"] if item["arm_id"] == arm_id)
            for seed_result in seed_results
        ]
        aggregate[arm_id] = {}
        for metric_name in metric_names:
            values = [float(row[metric_name]) for row in rows]
            aggregate[arm_id][f"{metric_name}_mean"] = float(statistics.fmean(values))
            aggregate[arm_id][f"{metric_name}_std"] = float(statistics.pstdev(values))

    strongest_non_oracle = max(
        ("static_validation_expert", "random_router", "confidence_only_router"),
        key=lambda arm_id: aggregate[arm_id]["task_success_mean"],
    )
    pgc = aggregate["pgc_evidence_router"]
    baseline = aggregate[strongest_non_oracle]

    return {
        "experiment_id": "PGC_EXPERIMENT_002",
        "state": "completed_trial",
        "dataset": {
            "name": "Iris",
            "source": "UCI Machine Learning Repository",
            "uci_id": 53,
            "doi": "10.24432/C56C76",
            "licence": "CC BY 4.0",
            "loader": "sklearn.datasets.load_iris",
            "samples": 150,
            "features": 4,
            "classes": 3,
            "checksum_sha256": seed_results[0]["dataset_checksum_sha256"],
        },
        "seeds": seeds,
        "split_policy": (
            "stratified 60% train, 20% validation and 20% protected test "
            "independently for each seed"
        ),
        "protected_test_used_for_routing": False,
        "aggregate": aggregate,
        "strongest_non_oracle_baseline": strongest_non_oracle,
        "promotion_candidate": (
            pgc["task_success_mean"] >= baseline["task_success_mean"]
            and pgc["routing_regret_mean"] <= baseline["routing_regret_mean"]
        ),
        "publication_evidence": False,
        "trial_evidence": True,
        "per_seed": seed_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="PGC/experiments/PGC_EXPERIMENT_002/results.json",
    )
    parser.add_argument("--seeds", default="11,23,37,53,71")
    parser.add_argument("--bootstrap-resamples", type=int, default=100)
    args = parser.parse_args()

    seeds = [int(value.strip()) for value in args.seeds.split(",") if value.strip()]
    if not seeds:
        raise ValueError("at least one seed is required")
    if args.bootstrap_resamples < 10:
        raise ValueError("bootstrap_resamples must be at least 10")

    result = run_experiment(seeds, args.bootstrap_resamples)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "strongest_non_oracle_baseline": result[
                    "strongest_non_oracle_baseline"
                ],
                "promotion_candidate": result["promotion_candidate"],
                "pgc": result["aggregate"]["pgc_evidence_router"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
