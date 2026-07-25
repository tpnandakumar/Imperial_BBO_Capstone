"""Execute PGC Experiment 001 with deterministic synthetic tasks."""

from __future__ import annotations

import argparse
import json
import random
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from PGC.architecture.cognitive_router import CandidateConfiguration, route

TASK_FAMILIES = (
    "alternating_state",
    "parity",
    "modular_arithmetic",
    "delayed_induction",
    "bounded_optimisation",
)
EXPERTS = (
    "sequence_state_expert",
    "arithmetic_expert",
    "retrieval_expert",
    "optimisation_expert",
)


@dataclass(frozen=True)
class TrialCase:
    case_id: str
    task_family: str
    oracle_expert: str
    difficulty: float
    signal_quality: float


@dataclass(frozen=True)
class ArmSummary:
    arm_id: str
    cases: int
    routing_accuracy: float
    task_success: float
    routing_regret: float
    abstention_rate: float
    mean_latency_ms: float


def oracle_for(task_family: str) -> str:
    return {
        "alternating_state": "sequence_state_expert",
        "parity": "sequence_state_expert",
        "modular_arithmetic": "arithmetic_expert",
        "delayed_induction": "retrieval_expert",
        "bounded_optimisation": "optimisation_expert",
    }[task_family]


def generate_cases(seed: int, per_family: int) -> list[TrialCase]:
    rng = random.Random(seed)
    cases: list[TrialCase] = []
    for family in TASK_FAMILIES:
        for index in range(per_family):
            cases.append(
                TrialCase(
                    case_id=f"{family}-{seed}-{index:03d}",
                    task_family=family,
                    oracle_expert=oracle_for(family),
                    difficulty=rng.uniform(0.15, 0.95),
                    signal_quality=rng.uniform(0.55, 0.98),
                )
            )
    rng.shuffle(cases)
    return cases


def expert_success_probability(case: TrialCase, expert_id: str) -> float:
    base = 0.86 - 0.42 * case.difficulty
    if expert_id == case.oracle_expert:
        advantage = 0.20
    elif {expert_id, case.oracle_expert} <= {"sequence_state_expert", "retrieval_expert"}:
        advantage = 0.04
    else:
        advantage = -0.18
    return min(0.99, max(0.01, base + advantage))


def candidate_for(
    case: TrialCase,
    expert_id: str,
    *,
    use_coherence: bool = True,
    use_efficiency: bool = True,
) -> CandidateConfiguration:
    is_oracle = expert_id == case.oracle_expert
    related = {expert_id, case.oracle_expert} <= {"sequence_state_expert", "retrieval_expert"}
    fitness = 0.86 if is_oracle else (0.63 if related else 0.43)
    evidence = 0.82 if is_oracle else (0.66 if related else 0.55)
    coherence_value = (0.84 if is_oracle else 0.61) if use_coherence else 0.70
    robustness = 0.82 if is_oracle else 0.59
    uncertainty = 0.13 if is_oracle else (0.32 if related else 0.52)
    safety = 0.92
    efficiency_value = {
        "sequence_state_expert": 0.82,
        "arithmetic_expert": 0.91,
        "retrieval_expert": 0.76,
        "optimisation_expert": 0.68,
    }[expert_id]
    if not use_efficiency:
        efficiency_value = 0.70
    quality = case.signal_quality
    return CandidateConfiguration(
        candidate_id=expert_id,
        task_fitness=min(1.0, fitness * quality + 0.08),
        evidence_validity=min(1.0, evidence * quality + 0.10),
        coherence=min(1.0, coherence_value * quality + 0.08),
        robustness=min(1.0, robustness * quality + 0.10),
        uncertainty=min(1.0, uncertainty + (1.0 - quality) * 0.25),
        safety=safety,
        efficiency=efficiency_value,
    )


def choose(case: TrialCase, arm_id: str, rng: random.Random) -> str | None:
    if arm_id == "static_single_expert":
        return "sequence_state_expert"
    if arm_id == "random_router":
        return rng.choice(EXPERTS)
    if arm_id == "confidence_only_router":
        candidates = [candidate_for(case, expert) for expert in EXPERTS]
        return min(candidates, key=lambda item: item.uncertainty).candidate_id
    if arm_id == "oracle_router":
        return case.oracle_expert

    use_coherence = arm_id != "pgc_without_coherence"
    use_efficiency = arm_id != "pgc_without_efficiency"
    candidates = [
        candidate_for(
            case,
            expert,
            use_coherence=use_coherence,
            use_efficiency=use_efficiency,
        )
        for expert in EXPERTS
    ]
    decision = route(candidates, minimum_score=0.50)
    return decision.selected_candidate_id


def evaluate_arm(cases: list[TrialCase], arm_id: str, seed: int) -> ArmSummary:
    rng = random.Random(seed + sum(ord(ch) for ch in arm_id))
    routing_correct: list[float] = []
    successes: list[float] = []
    regrets: list[float] = []
    abstentions = 0
    latencies: list[float] = []

    for case in cases:
        started = time.perf_counter()
        selected = choose(case, arm_id, rng)
        latencies.append((time.perf_counter() - started) * 1000.0)
        if selected is None:
            abstentions += 1
            routing_correct.append(0.0)
            successes.append(0.0)
            regrets.append(expert_success_probability(case, case.oracle_expert))
            continue

        routing_correct.append(float(selected == case.oracle_expert))
        selected_p = expert_success_probability(case, selected)
        oracle_p = expert_success_probability(case, case.oracle_expert)
        successes.append(float(rng.random() < selected_p))
        regrets.append(max(0.0, oracle_p - selected_p))

    return ArmSummary(
        arm_id=arm_id,
        cases=len(cases),
        routing_accuracy=statistics.fmean(routing_correct),
        task_success=statistics.fmean(successes),
        routing_regret=statistics.fmean(regrets),
        abstention_rate=abstentions / len(cases),
        mean_latency_ms=statistics.fmean(latencies),
    )


def run_experiment(seeds: list[int], per_family: int) -> dict:
    arms = (
        "static_single_expert",
        "random_router",
        "confidence_only_router",
        "oracle_router",
        "pgc_evidence_router",
        "pgc_without_coherence",
        "pgc_without_efficiency",
    )
    per_seed: list[dict] = []
    for seed in seeds:
        cases = generate_cases(seed, per_family)
        summaries = [evaluate_arm(cases, arm, seed) for arm in arms]
        per_seed.append({"seed": seed, "arms": [asdict(item) for item in summaries]})

    aggregate: dict[str, dict[str, float]] = {}
    for arm in arms:
        rows = [
            next(item for item in seed_row["arms"] if item["arm_id"] == arm)
            for seed_row in per_seed
        ]
        aggregate[arm] = {
            "routing_accuracy_mean": statistics.fmean(row["routing_accuracy"] for row in rows),
            "task_success_mean": statistics.fmean(row["task_success"] for row in rows),
            "routing_regret_mean": statistics.fmean(row["routing_regret"] for row in rows),
            "abstention_rate_mean": statistics.fmean(row["abstention_rate"] for row in rows),
            "mean_latency_ms": statistics.fmean(row["mean_latency_ms"] for row in rows),
        }

    pgc = aggregate["pgc_evidence_router"]
    strongest_non_oracle = max(
        (arm for arm in ("static_single_expert", "random_router", "confidence_only_router")),
        key=lambda arm: aggregate[arm]["task_success_mean"],
    )
    baseline = aggregate[strongest_non_oracle]
    promotion_candidate = (
        pgc["task_success_mean"] >= baseline["task_success_mean"]
        and pgc["routing_regret_mean"] <= baseline["routing_regret_mean"]
    )

    return {
        "experiment_id": "PGC_EXPERIMENT_001",
        "state": "completed_trial",
        "seeds": seeds,
        "cases_per_family": per_family,
        "total_cases_per_seed": per_family * len(TASK_FAMILIES),
        "aggregate": aggregate,
        "strongest_non_oracle_baseline": strongest_non_oracle,
        "promotion_candidate": promotion_candidate,
        "publication_evidence": False,
        "per_seed": per_seed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="PGC/experiments/PGC_EXPERIMENT_001/results.json")
    parser.add_argument("--per-family", type=int, default=100)
    parser.add_argument("--seeds", default="11,23,37,53,71")
    args = parser.parse_args()

    seeds = [int(value.strip()) for value in args.seeds.split(",") if value.strip()]
    if not seeds or args.per_family < 1:
        raise ValueError("at least one seed and one case per family are required")

    result = run_experiment(seeds, args.per_family)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["aggregate"], indent=2))
    print(f"promotion_candidate={result['promotion_candidate']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
