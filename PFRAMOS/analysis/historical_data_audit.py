"""Audit Weeks 1 to 11 before any candidate modelling begins."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from PFRAMOS.adapters.imperial_bbo.dataset import DIMENSIONS, load_history


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "outputs" / "public" / "historical_data_audit.json"


def main() -> None:
    history = load_history(REPOSITORY_ROOT, 1, 11)
    report = {
        "weeks": [1, 11],
        "expected_observations_per_function": 11,
        "functions": {},
    }

    for function, observations in history.items():
        unique_points = {tuple(item.coordinates) for item in observations}
        report["functions"][str(function)] = {
            "dimension": DIMENSIONS[function],
            "observation_count": len(observations),
            "unique_point_count": len(unique_points),
            "observations_per_dimension": len(observations) / DIMENSIONS[function],
            "minimum_output": str(min(item.output for item in observations)),
            "maximum_output": str(max(item.output for item in observations)),
            "weeks": [item.week for item in observations],
        }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Historical audit written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
