"""Execute PGC Experiment 003 with deterministic multimodal scenarios."""

from __future__ import annotations

import argparse
import json
import random
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from PGC.perception_emotion.emotional_balance_regulator import BalanceInput, regulate_balance
from PGC.perception_emotion.emotional_coherence_controller import (
    EmotionalCognitiveState,
    assess_coherence,
)
from PGC.perception_emotion.emotional_signal_interpreter import interpret_emotional_signal
from PGC.perception_emotion.multimodal_fusion import (
    PerceptualObservation,
    fuse_observations,
)


SCENARIO_BASES = {
    "genuine_threat": (0.98, 0.90, 0.35, 0.12, "urgent_response"),
    "ambiguous_alarm": (0.34, 0.90, 0.30, 0.62, "clarify"),
    "distress_no_danger": (0.20, 0.82, 0.95, 0.30, "support"),
    "hidden_risk_calm": (0.86, 0.22, 0.20, 0.22, "caution"),
    "benign_misleading_emotion": (0.10, 0.62, 0.20, 0.18, "observe"),
    "conflicting_modalities": (0.52, 0.58, 0.35, 0.72, "clarify"),
}
MODALITIES = ("language", "vision", "audio", "temporal")
ACTIONS = ("observe", "clarify", "support", "caution", "urgent_response", "abstain_and_review")
ACTION_INTENSITY = {
    "observe": 0.10,
    "clarify": 0.30,
    "support": 0.45,
    "caution": 0.65,
    "urgent_response": 1.00,
    "abstain_and_review": 0.00,
}


@dataclass(frozen=True)
class ScenarioCase:
    case_id: str
    family: str
    factual_risk: float
    emotional_intensity: float
    empathy_need: float
    uncertainty: float
    ground_truth_action: str
    observations: tuple[PerceptualObservation, ...]


@dataclass(frozen=True)
class ArmSummary:
    arm_id: str
    cases: int
    action_accuracy: float
    urgent_threat_recall: float
    missed_threat_rate: float
    false_escalation_rate: float
    emotional_proportionality: float
    factual_override_accuracy: float
    coherence_pass_rate: float
    abstention_rate: float
    mean_latency_ms: float


def _clip(value: float) -> float:
    return min(1.0, max(0.0, value))


def generate_cases(seed: int, per_family: int) -> list[ScenarioCase]:
    rng = random.Random(seed)
    cases: list[ScenarioCase] = []
    for family, base in SCENARIO_BASES.items():
        factual, emotional, empathy, uncertainty, action = base
        for index in range(per_family):
            observations: list[PerceptualObservation] = []
            for modality_index, modality in enumerate(MODALITIES):
                reliability = rng.uniform(0.56, 0.96)
                confidence = rng.uniform(0.62, 0.97)
                factual_noise = rng.gauss(0.0, 0.07 + 0.04 * (1.0 - reliability))
                emotional_noise = rng.gauss(0.0, 0.07 + 0.04 * (1.0 - reliability))
                modality_factual = factual
                modality_emotional = emotional

                if family == "conflicting_modalities":
                    if modality_index % 2 == 0:
                        modality_factual = 0.78
                        modality_emotional = 0.28
                    else:
                        modality_factual = 0.24
                        modality_emotional = 0.88
                elif family == "hidden_risk_calm" and modality in {"language", "audio"}:
                    modality_factual = 0.58
                    modality_emotional = 0.18
                elif family == "benign_misleading_emotion" and modality == "audio":
                    modality_emotional = 0.85

                observations.append(
                    PerceptualObservation(
                        modality_id=modality,
                        factual_signal=_clip(modality_factual + factual_noise),
                        emotional_signal=_clip(modality_emotional + emotional_noise),
                        confidence=confidence,
                        reliability=reliability,
                        provenance=f"synthetic:{family}:{seed}:{index}:{modality}",
                    )
                )

            cases.append(
                ScenarioCase(
                    case_id=f"{family}-{seed}-{index:03d}",
                    family=family,
                    factual_risk=factual,
                    emotional_intensity=emotional,
                    empathy_need=empathy,
                    uncertainty=uncertainty,
                    ground_truth_action=action,
                    observations=tuple(observations),
                )
            )
    rng.shuffle(cases)
    return cases


def _simple_action(factual: float, emotional: float, empathy: float, uncertainty: float) -> str:
    if factual >= 0.78:
        return "urgent_response" if emotional >= 0.55 else "caution"
    if factual >= 0.58:
        return "caution"
    if empathy >= 0.62 and factual < 0.55:
        return "support"
    if uncertainty >= 0.45 or (emotional >= 0.75 and factual < 0.50):
        return "clarify"
    return "observe"


def _select(case: ScenarioCase, arm_id: str) -> tuple[str, float, bool]:
    observations = case.observations
    factual_average = statistics.fmean(item.factual_signal for item in observations)
    emotional_average = statistics.fmean(item.emotional_signal for item in observations)

    if arm_id == "factual_only":
        action = "urgent_response" if factual_average >= 0.80 else ("caution" if factual_average >= 0.58 else "observe")
        return action, 0.55, True
    if arm_id == "emotional_only":
        action = "urgent_response" if emotional_average >= 0.80 else ("support" if emotional_average >= 0.58 else "observe")
        return action, 0.35, False
    if arm_id == "unweighted_fusion":
        action = _simple_action(factual_average, emotional_average, case.empathy_need, case.uncertainty)
        return action, 0.60, True
    if arm_id == "oracle":
        return case.ground_truth_action, 1.0, True

    fused = fuse_observations(observations)
    appraisal = interpret_emotional_signal(
        fused,
        social_significance=case.empathy_need,
        stated_distress=case.empathy_need,
        trust_signal=0.75,
    )

    if arm_id == "reliability_weighted_fusion":
        action = _simple_action(
            fused.factual_estimate,
            fused.emotional_estimate,
            case.empathy_need,
            max(case.uncertainty, appraisal.uncertainty),
        )
        return action, 0.70, True

    expected_intensity = _clip(0.62 * appraisal.factual_support + 0.38 * appraisal.urgency)
    factual_accuracy = _clip(1.0 - abs(fused.factual_estimate - case.factual_risk))
    proportionality = _clip(1.0 - abs(expected_intensity - ACTION_INTENSITY[case.ground_truth_action]))
    uncertainty_awareness = _clip(1.0 - abs(appraisal.uncertainty - case.uncertainty))

    provisional = EmotionalCognitiveState(
        perceived_significance=_clip(0.55 * fused.factual_estimate + 0.45 * fused.emotional_estimate),
        appraisal_intensity=expected_intensity,
        reasoning_intensity=fused.factual_estimate,
        memory_intensity=0.50,
        expression_intensity=expected_intensity,
        action_intensity=expected_intensity,
        factual_accuracy=factual_accuracy,
        safety=0.92,
        proportionality=proportionality,
        uncertainty_awareness=uncertainty_awareness,
    )
    coherence = assess_coherence(provisional)
    phcs_value = _clip((coherence.coherence_index + 1.0) / 2.0)
    if arm_id == "pgc_without_coherence":
        phcs_value = 0.75

    decision = regulate_balance(
        BalanceInput(
            factual_support=appraisal.factual_support,
            threat=appraisal.threat,
            urgency=appraisal.urgency,
            empathy_need=appraisal.empathy_need,
            uncertainty=max(case.uncertainty, appraisal.uncertainty),
            factual_accuracy=factual_accuracy,
            safety=0.92,
            proportionality=proportionality,
            phcs_coherence=phcs_value,
        )
    )
    return decision.action, decision.balance_score, coherence.passed


def evaluate_arm(cases: list[ScenarioCase], arm_id: str) -> ArmSummary:
    correct: list[float] = []
    proportionality: list[float] = []
    override_correct: list[float] = []
    coherence_passes: list[float] = []
    urgent_true = 0
    urgent_detected = 0
    missed_threats = 0
    benign_cases = 0
    false_escalations = 0
    abstentions = 0
    latencies: list[float] = []

    override_families = {"ambiguous_alarm", "hidden_risk_calm", "benign_misleading_emotion"}

    for case in cases:
        started = time.perf_counter()
        action, _, coherence_passed = _select(case, arm_id)
        latencies.append((time.perf_counter() - started) * 1000.0)
        correct.append(float(action == case.ground_truth_action))
        proportionality.append(
            max(0.0, 1.0 - abs(ACTION_INTENSITY[action] - ACTION_INTENSITY[case.ground_truth_action]))
        )
        coherence_passes.append(float(coherence_passed))

        if case.family in override_families:
            override_correct.append(float(action == case.ground_truth_action))
        if case.ground_truth_action == "urgent_response":
            urgent_true += 1
            if action == "urgent_response":
                urgent_detected += 1
            else:
                missed_threats += 1
        if case.family in {"benign_misleading_emotion", "distress_no_danger"}:
            benign_cases += 1
            if action in {"caution", "urgent_response"}:
                false_escalations += 1
        if action == "abstain_and_review":
            abstentions += 1

    return ArmSummary(
        arm_id=arm_id,
        cases=len(cases),
        action_accuracy=statistics.fmean(correct),
        urgent_threat_recall=urgent_detected / urgent_true if urgent_true else 0.0,
        missed_threat_rate=missed_threats / urgent_true if urgent_true else 0.0,
        false_escalation_rate=false_escalations / benign_cases if benign_cases else 0.0,
        emotional_proportionality=statistics.fmean(proportionality),
        factual_override_accuracy=statistics.fmean(override_correct),
        coherence_pass_rate=statistics.fmean(coherence_passes),
        abstention_rate=abstentions / len(cases),
        mean_latency_ms=statistics.fmean(latencies),
    )


def run_experiment(seeds: list[int], per_family: int) -> dict:
    arms = (
        "factual_only",
        "emotional_only",
        "unweighted_fusion",
        "reliability_weighted_fusion",
        "pgc_perception_emotion",
        "pgc_without_coherence",
        "oracle",
    )
    per_seed: list[dict] = []
    for seed in seeds:
        cases = generate_cases(seed, per_family)
        summaries = [evaluate_arm(cases, arm) for arm in arms]
        per_seed.append({"seed": seed, "arms": [asdict(summary) for summary in summaries]})

    aggregate: dict[str, dict[str, float]] = {}
    metric_names = (
        "action_accuracy",
        "urgent_threat_recall",
        "missed_threat_rate",
        "false_escalation_rate",
        "emotional_proportionality",
        "factual_override_accuracy",
        "coherence_pass_rate",
        "abstention_rate",
        "mean_latency_ms",
    )
    for arm in arms:
        rows = [next(item for item in seed_row["arms"] if item["arm_id"] == arm) for seed_row in per_seed]
        aggregate[arm] = {}
        for metric in metric_names:
            values = [float(row[metric]) for row in rows]
            aggregate[arm][f"{metric}_mean"] = statistics.fmean(values)
            aggregate[arm][f"{metric}_std"] = statistics.pstdev(values)

    strongest_non_oracle = max(
        (arm for arm in arms if arm not in {"oracle", "pgc_perception_emotion", "pgc_without_coherence"}),
        key=lambda arm: (
            aggregate[arm]["action_accuracy_mean"],
            aggregate[arm]["emotional_proportionality_mean"],
        ),
    )
    pgc = aggregate["pgc_perception_emotion"]
    baseline = aggregate[strongest_non_oracle]
    promotion_candidate = (
        pgc["action_accuracy_mean"] >= baseline["action_accuracy_mean"]
        and pgc["false_escalation_rate_mean"] <= baseline["false_escalation_rate_mean"]
        and pgc["emotional_proportionality_mean"] >= baseline["emotional_proportionality_mean"]
    )

    return {
        "experiment_id": "PGC_EXPERIMENT_003",
        "state": "completed_trial",
        "dataset": {
            "type": "deterministic_synthetic_multimodal_emotional_scenarios",
            "scenario_families": list(SCENARIO_BASES),
            "modalities": list(MODALITIES),
        },
        "seeds": seeds,
        "cases_per_family": per_family,
        "total_cases_per_seed": per_family * len(SCENARIO_BASES),
        "factual_accuracy_precedence": True,
        "safety_precedence": True,
        "phcs_coherence_enabled": True,
        "aggregate": aggregate,
        "strongest_non_oracle_baseline": strongest_non_oracle,
        "promotion_candidate": promotion_candidate,
        "publication_evidence": False,
        "trial_evidence": True,
        "per_seed": per_seed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="PGC/experiments/PGC_EXPERIMENT_003/results.json")
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
