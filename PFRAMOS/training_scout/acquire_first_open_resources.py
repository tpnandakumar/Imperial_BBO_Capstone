"""Acquire the first approved open-resource bundle into a trial cache.

This script is deliberately conservative. It clones approved public code and
retrieves metadata from open registries. It does not download arbitrary Google
Research datasets or apply parameter updates.
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


def run(command: list[str], cwd: Path | None = None) -> None:
    completed = subprocess.run(command, cwd=cwd, check=False, text=True)
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

    records = []

    coco_dir = output_dir / "coco"
    clone_shallow("https://github.com/numbbo/coco.git", coco_dir)
    records.append({"resource_id": "coco_bbob", "local_path": str(coco_dir), "state": "acquired"})

    nvbench_dir = output_dir / "nvbench"
    clone_shallow("https://github.com/NVIDIA/nvbench.git", nvbench_dir)
    records.append({"resource_id": "nvidia_nvbench", "local_path": str(nvbench_dir), "state": "acquired"})

    openml_meta = fetch_json("https://www.openml.org/api/v1/json/data/list/limit/20")
    openml_path = output_dir / "openml_first_20_metadata.json"
    openml_path.write_text(json.dumps(openml_meta, indent=2), encoding="utf-8")
    records.append({"resource_id": "openml_registry", "local_path": str(openml_path), "state": "metadata_acquired"})

    google_record = {
        "resource_id": "google_research_dataset_catalogue",
        "state": "discovery_only",
        "official_source": "https://research.google/resources/datasets/",
        "parameter_updates_allowed": False,
        "next_gate": "dataset_specific_licence_and_privacy_clearance"
    }
    google_path = output_dir / "google_research_catalogue_record.json"
    google_path.write_text(json.dumps(google_record, indent=2), encoding="utf-8")
    records.append({"resource_id": "google_research_dataset_catalogue", "local_path": str(google_path), "state": "recorded"})

    acquisition_record = {
        "manifest_id": manifest["manifest_id"],
        "state": "trial_resources_acquired",
        "parameter_updates_applied": False,
        "resources": records,
    }
    record_path = output_dir / "acquisition_record.json"
    record_path.write_text(json.dumps(acquisition_record, indent=2), encoding="utf-8")
    return acquisition_record


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
