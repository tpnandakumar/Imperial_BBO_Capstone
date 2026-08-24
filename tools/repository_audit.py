from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "Module_25_Final_BBO_Submission" / "README.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_1_Retrospective" / "EVIDENCE_MAP.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_2_Successful_Optimisation_Strategies" / "EVIDENCE_MAP.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_CAPSTONE_DATASHEET.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_CAPSTONE_MODEL_CARD.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_REPRODUCIBILITY.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "REPOSITORY_AUDIT.md",
    ROOT / "Module_25_Final_BBO_Submission" / "Final_13_Round_Evidence" / "FINAL_RESULTS_SUMMARY.csv",
    ROOT / "Week_13" / "week_13_inputs.csv",
    ROOT / "Week_13" / "week_13_results.csv",
    ROOT / "Week_13" / "week_13_analysis.py",
    ROOT / "Week_13" / "generate_week_13_figures.py",
]

PLACEHOLDER_TERMS = (
    "TODO",
    "TBD",
    "PLACEHOLDER",
    "YOUR CODE HERE",
    "INSERT HERE",
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def iter_markdown_files() -> list[Path]:
    ignored = {".git", ".venv", "venv", "node_modules"}
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored for part in path.parts)
    ]


def check_required_paths() -> list[str]:
    return [str(path.relative_to(ROOT)) for path in REQUIRED_PATHS if not path.exists()]


def check_week_navigation() -> list[str]:
    missing = []
    for week in range(1, 14):
        path = ROOT / f"Week_{week:02d}" / "README.md"
        if not path.exists():
            missing.append(str(path.relative_to(ROOT)))
    return missing


def clean_link_target(raw: str) -> str:
    target = raw.strip().split()[0].strip("<>")
    target = target.split("#", 1)[0]
    return unquote(target)


def check_internal_links() -> list[str]:
    broken = []
    for md_file in iter_markdown_files():
        text = md_file.read_text(encoding="utf-8", errors="replace")
        for raw in MARKDOWN_LINK.findall(text):
            target = clean_link_target(raw)
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (md_file.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                broken.append(f"{md_file.relative_to(ROOT)} -> {target}")
    return sorted(set(broken))


def check_placeholders() -> list[str]:
    hits = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        upper = text.upper()
        for term in PLACEHOLDER_TERMS:
            if term in upper:
                hits.append(f"{path.relative_to(ROOT)}: {term}")
    for path in ROOT.rglob("*.py"):
        if "tools/repository_audit.py" in path.as_posix():
            continue
        text = path.read_text(encoding="utf-8", errors="replace").upper()
        for term in PLACEHOLDER_TERMS:
            if term in text:
                hits.append(f"{path.relative_to(ROOT)}: {term}")
    return sorted(set(hits))


def print_section(title: str, items: list[str]) -> None:
    print(f"\n{title}")
    if items:
        for item in items:
            print(f"  FAIL: {item}")
    else:
        print("  PASS")


def main() -> int:
    missing_required = check_required_paths()
    missing_weeks = check_week_navigation()
    broken_links = check_internal_links()
    placeholders = check_placeholders()

    print("Imperial BBO Capstone repository audit")
    print_section("Required final-assessment files", missing_required)
    print_section("Week 01 to Week 13 navigation", missing_weeks)
    print_section("Internal Markdown links", broken_links)
    print_section("Unfinished placeholder markers", placeholders)

    failures = missing_required + missing_weeks + broken_links + placeholders
    print(f"\nTotal findings: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
