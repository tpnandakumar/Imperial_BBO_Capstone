from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = (
    ROOT
    / "Module_25_Final_BBO_Submission"
    / "25_3_GitHub_Final_Submission"
    / "FINAL_CAPSTONE_NOTEBOOK.ipynb"
)


def main() -> None:
    """Execute every code cell from the two common assessor locations."""
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    previous_directory = Path.cwd()
    try:
        for working_directory in (ROOT, NOTEBOOK.parent):
            os.chdir(working_directory)
            namespace: dict[str, object] = {"__name__": "__main__"}
            for number, cell in enumerate(notebook["cells"], start=1):
                if cell.get("cell_type") != "code":
                    continue
                source = "".join(cell.get("source", []))
                exec(compile(source, f"{NOTEBOOK.name}:cell-{number}", "exec"), namespace)
    finally:
        os.chdir(previous_directory)
    print(f"PASS: executed all code cells from the repository root and the notebook folder")


if __name__ == "__main__":
    main()

