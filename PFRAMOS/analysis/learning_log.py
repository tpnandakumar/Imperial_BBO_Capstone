"""Append-only learning log for PFRAMOS harmony and optimisation stages."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


DEFAULT_LOG = Path(__file__).resolve().parents[1] / "outputs" / "public" / "learning_log.jsonl"


@dataclass(frozen=True)
class LearningEntry:
    stage: str
    finding: str
    evidence: Mapping[str, Any]
    action_taken: str
    outcome: str
    reusable_rule: str
    timestamp_utc: str


def append_learning(
    *,
    stage: str,
    finding: str,
    evidence: Mapping[str, Any],
    action_taken: str,
    outcome: str,
    reusable_rule: str,
    output_file: Path = DEFAULT_LOG,
) -> LearningEntry:
    entry = LearningEntry(
        stage=stage,
        finding=finding,
        evidence=evidence,
        action_taken=action_taken,
        outcome=outcome,
        reusable_rule=reusable_rule,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
    )
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(asdict(entry), sort_keys=True, default=str))
        handle.write("\n")
    return entry
