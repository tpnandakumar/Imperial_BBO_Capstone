"""Acquire the minimal first open-resource bundle into a trial cache.

Phase 1 acquires only COCO/BBOB and OpenML metadata. This gives immediate,
reproducible optimisation evidence with low storage and licensing risk.
GPU-specific resources and large external datasets remain deferred.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "PFRAMOS" / "training_scout" / "FIRST_RESOURCE_ACQUISITION_MANIFEST.json"


def run(command: list[str]) -> None:
    completed = subprocess.run(command, check=False, text=True)
    if completed.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(command)}")


def clone_shallow(url: str, destination: Path) -> None:
    if destination.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    run(["git", "clone", "--depth", "1", url, str(destination)])


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "PACC-Scout/0.1"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def acquire(output_dir: Path) -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)

    coco_dir = output_dir / "coco"
    clone_shallow("https://github.com/numbbo/coco.git", coco_dir)
    coco_revision = subprocess.check_output(
        ["git", "-C", str(coco_dir), "rev-parse", "HEAD"],
        text=True,
    ).strip()

    openml_meta = fetch_json("https://www.openml.org/api/v1/json/data/list/limit/20")
    openml_path = output_dir / "openml_first_20_metadata.json"
    openml_path.write_text(json.dumps(openml_meta, indent=2), encoding="utf-8")

    record = {
        "manifest_id": manifest["manifest_id"],
        "state": "minimal_trial_resources_acquired",
        "parameter_updates_applied": False,
        "deferred": ["nvidia_nvbench", "google_research_datasets", "large_external_datasets"],
        "resources": [
            {
                "resource_id": "coco_bbob",
                "local_path": str(coco_dir),
                "revision": coco_revision,
                "state": "acquired_for_benchmark_trial",
            },
            {
                "resource_id": "openml_registry",
                "local_path": str(openml_path),
                "state": "metadata_acquired_for_screening",
            },
        ],
    }
    (output_dir / "acquisition_record.json").write_text(
        json.dumps(record, indent=2),
        encoding="utf-8",
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        default="PFRAMOS/trial_runs/resource_cache",
        help="Trial cache directory",
    )
    args = parser.parse_args()

    try:
        record = acquire(ROOT / args.output_dir)
    except Exception as exc:
        print(f"acquisition failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
