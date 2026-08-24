# Final Repository Forensic Audit Findings

## Scope

This record documents the pre-submission forensic review undertaken before Module 25 unlocks. It focuses on issues that could affect assessor navigation, reproducibility or confidence in the repository.

## Findings and actions

### 1. Incorrect Week 25 framing

A previous assessment-facing folder was labelled `Week_25_Final_BBO_Submission`. That name could imply that the optimisation experiment continued to Week 25.

**Action:** removed the obsolete structure and replaced it with `Module_25_Final_BBO_Submission`. The official optimisation record remains Week 01 to Week 13.

### 2. Week 13 reproducibility dependency on non-existent early weekly CSV files

The first version of the closing Week 13 analysis expected `week_01_inputs.csv`, `week_01_results.csv` and equivalent files for all earlier weeks. Early folders do not contain those CSV files.

**Action:** repaired `Week_13/week_13_analysis.py` so Weeks 1 to 11 are reconstructed from the committed exact-history dataset, while Weeks 12 and 13 are read from their verified weekly CSV files. The figure script uses the same common loader.

### 3. Final assessment dependencies were not explicit

The closing numerical analysis uses the Python standard library, while the final figures require matplotlib.

**Action:** added `requirements-final.txt` and a concise final reproducibility route.

### 4. No automated repository-wide final audit

The repository contained strong weekly evidence but no single automated check for final assessment file presence, Week 01 to Week 13 navigation, broken internal Markdown links or common unfinished placeholder markers.

**Action:** added `tools/repository_audit.py` and `.github/workflows/final_repository_audit.yml`. The workflow also executes the final Week 13 analysis and figure-generation sequence.

### 5. Obsolete conversational or instruction-like wording

Targeted searches were made for common unfinished or conversational markers, including `TODO`, `placeholder`, `YOUR CODE HERE`, `please`, the obsolete `Week_25_Final_BBO_Submission` path and the earlier phrase `should not be rewritten`.

**Current search result:** no matches were returned for those targeted terms after the Module 25 restructuring.

This does not replace the automated final audit, which should still be run immediately before submission.

## Remaining checks when Module 25 unlocks

- Compare the final datasheet and model card directly against the live 25.3 rubric.
- Confirm the approximately 100-word non-technical README summary remains within the requested range.
- Confirm the automated final repository audit completes successfully on the submission commit.
- Confirm final reflection infographics exist, are linked correctly and use verified source data.
- Confirm public assessor access and branch protection remain appropriate.

## Assessment boundary

The Advanced Extension Series and SOC remain explicitly post-capstone. They are not presented as methods used to generate the Week 01 to Week 13 Imperial outputs.
