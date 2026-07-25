"""Auditable cognitive enhancement layer for PFRAMOS.

This module augments attention, working memory, hypothesis generation,
counterfactual reasoning, metacognitive checking and decision quality.
It does not replace human judgement or promote decisions automatically.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CognitiveState:
    task_id: str
    attention_load: float
    working_memory_load: float
    uncertainty: float
    conflict: float
    novelty: float
    evidence_quality: float
    time_pressure: float
    risk: float

    def __post_init__(self) -> None:
        for name in (
            "attention_load",
            "working_memory_load",
            "uncertainty",
            "conflict",
            "novelty",
            "evidence_quality",
            "time_pressure",
            "risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class CognitiveEnhancementPlan:
    task_id: str
    focus_strength: float
    memory_compression: float
    hypothesis_count: int
    counterfactual_depth: int
    verification_depth: int
    contradiction_scan: bool
    retrieval_required: bool
    human_review_required: bool
    allowed_actions: Tuple[str, ...]
    rationale: Tuple[str, ...]


def build_cognitive_plan(state: CognitiveState) -> CognitiveEnhancementPlan:
    reasons = []

    focus_strength = min(
        1.0,
        0.35 * state.attention_load
        + 0.25 * state.time_pressure
        + 0.20 * state.risk
        + 0.20 * state.conflict,
    )

    memory_compression = min(
        1.0,
        0.55 * state.working_memory_load
        + 0.25 * state.attention_load
        + 0.20 * state.time_pressure,
    )

    if state.novelty >= 0.75 or state.uncertainty >= 0.70:
        hypothesis_count = 5
        reasons.append("broad_hypothesis_search")
    elif state.conflict >= 0.55:
        hypothesis_count = 4
        reasons.append("conflicting_evidence")
    else:
        hypothesis_count = 3

    counterfactual_depth = 3 if state.risk >= 0.70 else 2 if state.uncertainty >= 0.45 else 1
    verification_depth = 3 if state.risk >= 0.65 or state.evidence_quality < 0.55 else 2

    contradiction_scan = state.conflict >= 0.35 or state.uncertainty >= 0.45
    retrieval_required = state.evidence_quality < 0.70 or state.novelty >= 0.60
    human_review_required = state.risk >= 0.50 or state.uncertainty >= 0.60

    actions = [
        "prioritise_relevant_evidence",
        "compress_working_memory",
        "generate_alternative_hypotheses",
        "test_counterfactuals",
        "calibrate_confidence",
    ]
    if contradiction_scan:
        actions.append("scan_for_contradictions")
    if retrieval_required:
        actions.append("retrieve_additional_evidence")
    if human_review_required:
        actions.append("request_human_review")

    if state.evidence_quality < 0.50:
        reasons.append("weak_evidence")
    if state.risk >= 0.70:
        reasons.append("high_risk_task")
    if state.working_memory_load >= 0.70:
        reasons.append("working_memory_pressure")

    return CognitiveEnhancementPlan(
        task_id=state.task_id,
        focus_strength=focus_strength,
        memory_compression=memory_compression,
        hypothesis_count=hypothesis_count,
        counterfactual_depth=counterfactual_depth,
        verification_depth=verification_depth,
        contradiction_scan=contradiction_scan,
        retrieval_required=retrieval_required,
        human_review_required=human_review_required,
        allowed_actions=tuple(actions),
        rationale=tuple(reasons),
    )
