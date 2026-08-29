from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_1_Retrospective" / "DETAILED_EXECUTIVE_SUMMARY.md",
    ROOT / "Module_25_Final_BBO_Submission" / "SECTION_GUIDE.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_1_Retrospective" / "EVIDENCE_MAP.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_2_Successful_Optimisation_Strategies" / "EVIDENCE_MAP.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_CAPSTONE_DATASHEET.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "SECTION_GUIDE.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_CAPSTONE_MODEL_CARD.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_CAPSTONE_NOTEBOOK.ipynb",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "FINAL_REPRODUCIBILITY.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "REPOSITORY_AUDIT.md",
    ROOT / "Module_25_Final_BBO_Submission" / "25_3_GitHub_Final_Submission" / "DISCUSSION_BOARD_SUBMISSION.md",
    ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv",
    ROOT / "Module_25_Final_BBO_Submission" / "Final_13_Round_Evidence" / "FINAL_RESULTS_SUMMARY.csv",
    ROOT / "Module_25_Final_BBO_Submission" / "Final_13_Round_Evidence" / "INFOGRAPHIC_SOURCE_MAP.md",
    ROOT / "Module_25_Final_BBO_Submission" / "Final_13_Round_Evidence" / "FIGURE_STATUS.md",
    ROOT / "Week_13" / "week_13_inputs.csv",
    ROOT / "Week_13" / "week_13_results.csv",
    ROOT / "Week_13" / "week_13_analysis.py",
    ROOT / "Week_13" / "generate_week_13_figures.py",
    ROOT / "tools" / "validate_final_notebook.py",
    ROOT / "BBO_Visual_Book_Shiny" / "app.py",
    ROOT / "BBO_Visual_Book_Shiny" / "NARRATION_SCRIPTS.md",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration-player.js",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "01_welcome_and_project_purpose.m4a",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "02_imperial_bbo_journey.m4a",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "03_results_and_interpretation.m4a",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "04_delta_signature_of_change.m4a",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "05_black_box_resolution.m4a",
    ROOT / "BBO_Visual_Book_Shiny" / "www" / "narration" / "06_pdhis_and_conclusion.m4a",
]

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
UNFINISHED_MARKER = re.compile(
    r"(?:^|\s)(?:TODO|TBD|YOUR CODE HERE|INSERT HERE|PLACEHOLDER)\s*(?::|$)",
    re.IGNORECASE,
)


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
        path = ROOT / f"Week_{week:02d}" / "SECTION_GUIDE.md"
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


def check_unfinished_markers() -> list[str]:
    hits = []
    candidate_files = iter_markdown_files() + list(ROOT.rglob("*.py"))
    for path in candidate_files:
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        in_fence = False
        for number, line in enumerate(text.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if UNFINISHED_MARKER.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    return sorted(set(hits))


def check_complete_dataset() -> list[str]:
    """Verify the final dataset contains the declared starter and query record."""
    path = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
    if not path.exists():
        return ["Complete capstone dataset is missing"]

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    findings = []
    if len(rows) != 279:
        findings.append(f"Complete dataset has {len(rows)} rows, expected 279")

    starter = sum(row["source"] == "starter" for row in rows)
    weekly = len(rows) - starter
    if starter != 175:
        findings.append(f"Starter record has {starter} rows, expected 175")
    if weekly != 104:
        findings.append(f"Prospective query record has {weekly} rows, expected 104")

    expected_sources = {"starter"} | {f"week_{week:02d}" for week in range(1, 14)}
    observed_sources = {row["source"] for row in rows}
    if observed_sources != expected_sources:
        findings.append(
            "Dataset sources differ from starter plus week_01 to week_13"
        )

    if {int(row["function"]) for row in rows} != set(range(1, 9)):
        findings.append("Dataset does not contain exactly Functions 1 to 8")
    return findings


def check_nontechnical_summary() -> list[str]:
    """Confirm that the root README contains the requested 100-word summary."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(
        r"## NON-TECHNICAL EXPLANATION OF (?:MY|YOUR) PROJECT\s+(.*?)\s+### EXECUTIVE SUMMARY",
        text,
        flags=re.DOTALL,
    )
    if not match:
        return ["Non-technical README summary section was not found"]
    words = re.findall(r"\b[\w]+(?:['’][\w]+)?\b", match.group(1))
    return [] if len(words) == 100 else [f"Non-technical summary has {len(words)} words, expected 100"]


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
    unfinished = check_unfinished_markers()
    dataset_findings = check_complete_dataset()
    summary_findings = check_nontechnical_summary()

    print("Imperial BBO Capstone repository audit")
    print_section("Required final-assessment files", missing_required)
    print_section("Week 01 to Week 13 navigation", missing_weeks)
    print_section("Internal Markdown links", broken_links)
    print_section("Unfinished work markers", unfinished)
    print_section("Complete 279-observation dataset", dataset_findings)
    print_section("100-word non-technical summary", summary_findings)

    failures = (
        missing_required
        + missing_weeks
        + broken_links
        + unfinished
        + dataset_findings
        + summary_findings
    )
    print(f"\nTotal findings: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
