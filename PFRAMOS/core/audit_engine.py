"""Append-only JSON Lines audit engine for PFRAMOS."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


@dataclass(frozen=True)
class AuditEvent:
    run_id: str
    event_type: str
    node_id: str
    payload: Mapping[str, Any]
    timestamp_utc: str


class AuditEngine:
    def __init__(self, output_file: Path) -> None:
        self.output_file = output_file
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

    def record(
        self,
        *,
        run_id: str,
        event_type: str,
        node_id: str,
        payload: Mapping[str, Any],
    ) -> AuditEvent:
        event = AuditEvent(
            run_id=run_id,
            event_type=event_type,
            node_id=node_id,
            payload=payload,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
        )
        with self.output_file.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(event), sort_keys=True, default=str))
            handle.write("\n")
        return event
