"""Validate quarantined technology-sweep candidates for nodal recruitment.

Validation is stricter than discovery screening. It may recommend promotion to
an experimental node, continued quarantine, deferral or rejection. It never
integrates a technique automatically.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from PFRAMOS.analysis.learning_log import append_learning


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = PFRAMOS_ROOT / "outputs" / "public" / "tech_sweep"
PRIVATE_DIR = PFRAMOS_ROOT / "outputs" / "private" / "tech_sweep"
INPUT_FILE = PRIVATE_DIR / "recruitment_candidates.json"
PUBLIC_OUTPUT = PUBLIC_DIR / "validation_summary.json"
PRIVATE_OUTPUT = PRIVATE_DIR / "validation_decisions.json"


def _decision(candidate: Dict[str, object]) -> Dict[str, object]:
    score = float(candidate["recruitment_score"])
    evidence = float(candidate["evidence_quality"])
    reproducibility = float(candidate["reproducibility"])
    maturity = float(candidate["maturity"])
    safety = float(candidate["safety"])
    transferability = float(candidate["transferability"])
    efficiency = 0.5 * (
        float(candidate["compute_efficiency"])
        + float(candidate["energy_efficiency"])
    )

    reasons: List[str] = []
    if evidence < 0.50:
        reasons.append("insufficient evidence quality")
    if reproducibility < 0.50:
        reasons.append("insufficient reproducibility signal")
    if safety < 0.50:
        reasons.append("insufficient safety or failure-mode evidence")
    if maturity < 0.45:
        reasons.append("technical maturity remains limited")

    if evidence < 0.40 or safety < 0.40:
        state = "rejected"
    elif (
        score >= 0.78
        and evidence >= 0.65
        and reproducibility >= 0.60
        and maturity >= 0.55
        and safety >= 0.60
        and transferability >= 0.60
    ):
        state = "promote_to_experimental_node_review"
    elif score >= 0.62 and not reasons:
        state = "continue_quarantine_for_replication"
    elif score >= 0.55:
        state = "defer_pending_evidence"
    else:
        state = "screened_no_recruitment"

    return {
        "candidate_id": candidate["candidate_id"],
        "title": candidate["title"],
        "source": candidate["source"],
        "source_url": candidate["source_url"],
        "recruitment_score": score,
        "validation_state": state,
        "validation_reasons": reasons,
        "transferability": transferability,
        "efficiency": efficiency,
        "human_approval_required": True,
        "automatic_integration": False,
    }


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Recruitment candidates are missing. Run the technology sweep first."
        )

    payload = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    candidates = payload.get("candidates", [])
    decisions = [_decision(candidate) for candidate in candidates]
    decisions.sort(key=lambda item: float(item["recruitment_score"]), reverse=True)

    generated_at = datetime.now(timezone.utc).isoformat()
    counts: Dict[str, int] = {}
    for item in decisions:
        state = str(item["validation_state"])
        counts[state] = counts.get(state, 0) + 1

    public_summary = {
        "generated_at": generated_at,
        "validated_candidates": len(decisions),
        "decision_counts": counts,
        "promoted_to_review": sum(
            item["validation_state"] == "promote_to_experimental_node_review"
            for item in decisions
        ),
        "automatically_integrated": 0,
        "human_approval_required": True,
        "validation_notice": (
            "Validation remains metadata-based until papers, code and experiments "
            "receive deeper human and retrospective assessment."
        ),
        "top_decisions": [
            {
                "candidate_id": item["candidate_id"],
                "title": item["title"],
                "source_url": item["source_url"],
                "recruitment_score": item["recruitment_score"],
                "validation_state": item["validation_state"],
            }
            for item in decisions[:20]
        ],
    }

    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_OUTPUT.write_text(json.dumps(public_summary, indent=2), encoding="utf-8")
    PRIVATE_OUTPUT.write_text(
        json.dumps(
            {
                "generated_at": generated_at,
                "status": "validation_only_no_automatic_integration",
                "decisions": decisions,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    append_learning(
        stage="technology_recruitment_validation",
        finding="Technology sweep candidates underwent stricter Sunday validation.",
        evidence=public_summary,
        action_taken="Applied evidence, reproducibility, maturity, safety, transferability and efficiency gates.",
        outcome="Candidates were promoted to review, quarantined, deferred or rejected; none were integrated automatically.",
        reusable_rule="Separate discovery from validation and separate validation from integration approval.",
    )
    print(json.dumps(public_summary, indent=2))


if __name__ == "__main__":
    main()
