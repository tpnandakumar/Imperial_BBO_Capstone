"""PGC Experiment 005: Dynamic Live Accuracy Honing.

Reuses Experiment 004's deterministic generator. Validation selects threshold
changes; protected-test labels are used only for final evaluation.
"""
from __future__ import annotations

import importlib.util
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXP4 = ROOT / "PGC/experiments/PGC_EXPERIMENT_004/run_experiment.py"
spec = importlib.util.spec_from_file_location("pgc_exp4", EXP4)
exp4 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(exp4)

SEEDS = [11, 23, 37, 53, 71]
BASE = [0.78, 0.55, 0.58, 0.62, 0.45]
STEPS = [0.08, 0.04, 0.02, 0.01, 0.005]
AI = exp4.AI


def predict(case, p):
    _, factual, emotional, disagreement, _, _, _, _ = exp4.coh(case)
    urgent_f, urgent_e, caution_f, support_need, uncertainty_t = p
    uncertainty = max(case.u, disagreement)
    if factual >= urgent_f:
        return "urgent_response" if emotional >= urgent_e else "caution"
    if factual >= caution_f:
        return "caution"
    if case.en >= support_need and factual < caution_f:
        return "support"
    if uncertainty >= uncertainty_t or (emotional >= 0.75 and factual < 0.50):
        return "clarify"
    return "observe"


def utility(cases, p):
    accuracy = statistics.fmean(float(predict(c, p) == c.truth) for c in cases)
    urgent = [c for c in cases if c.truth == "urgent_response"]
    recall = statistics.fmean(float(predict(c, p) == "urgent_response") for c in urgent)
    return accuracy + 0.02 * recall


def hone(validation):
    p = BASE.copy()
    best = utility(validation, p)
    trace = []
    for grade, step in enumerate(STEPS, start=1):
        improved = True
        while improved:
            improved = False
            for index in range(len(p)):
                for direction in (-1.0, 1.0):
                    candidate = p.copy()
                    candidate[index] = min(1.0, max(0.0, candidate[index] + direction * step))
                    score = utility(validation, candidate)
                    if score > best + 1e-12:
                        p, best, improved = candidate, score, True
            trace.append({"grade": grade, "step": step, "parameters": p.copy(), "utility": best})
    base_correct = sum(predict(c, BASE) == c.truth for c in validation)
    tuned_correct = sum(predict(c, p) == c.truth for c in validation)
    accepted = tuned_correct - base_correct >= 2
    return (p if accepted else BASE.copy()), accepted, base_correct, tuned_correct, trace


def evaluate(cases, p):
    predictions = [predict(c, p) for c in cases]
    truth = [c.truth for c in cases]
    urgent = [i for i, value in enumerate(truth) if value == "urgent_response"]
    benign = [i for i, c in enumerate(cases) if c.family in {"benign_misleading_emotion", "distress_no_danger"}]
    return {
        "cases": len(cases),
        "action_accuracy": statistics.fmean(float(a == b) for a, b in zip(predictions, truth)),
        "urgent_threat_recall": statistics.fmean(float(predictions[i] == "urgent_response") for i in urgent),
        "false_escalation_rate": statistics.fmean(float(predictions[i] in {"caution", "urgent_response"}) for i in benign),
        "emotional_proportionality": statistics.fmean(max(0.0, 1.0 - abs(AI[a] - AI[b])) for a, b in zip(predictions, truth)),
    }


def run():
    rows = []
    for seed in SEEDS:
        train, validation, protected_test = exp4.split(exp4.gen(seed))
        tuned, accepted, base_correct, tuned_correct, trace = hone(validation)
        rows.append({
            "seed": seed,
            "split_sizes": {"train": len(train), "validation": len(validation), "protected_test": len(protected_test)},
            "validation_base_correct": base_correct,
            "validation_tuned_correct": tuned_correct,
            "honing_accepted": accepted,
            "final_parameters": tuned,
            "honing_trace": trace,
            "fusion_anchor": evaluate(protected_test, BASE),
            "dlah_sdvgtc": evaluate(protected_test, tuned),
        })
    metrics = ["action_accuracy", "urgent_threat_recall", "false_escalation_rate", "emotional_proportionality"]
    aggregate = {}
    for arm in ("fusion_anchor", "dlah_sdvgtc"):
        aggregate[arm] = {m + "_mean": statistics.fmean(row[arm][m] for row in rows) for m in metrics}
    return {
        "experiment_id": "PGC_EXPERIMENT_005",
        "state": "completed_trial",
        "evidence_status": "trial_not_publication",
        "method": "fusion_anchored_dynamic_live_accuracy_honing_with_sequential_variable_grade_threshold_convergence",
        "seeds": SEEDS,
        "split": "60_train_20_validation_20_protected_test",
        "protected_test_label_feedback": False,
        "minimum_validation_gain_for_honing": 2,
        "grade_steps": STEPS,
        "aggregate": aggregate,
        "accuracy_gain": aggregate["dlah_sdvgtc"]["action_accuracy_mean"] - aggregate["fusion_anchor"]["action_accuracy_mean"],
        "per_seed": rows,
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["aggregate"], indent=2))
