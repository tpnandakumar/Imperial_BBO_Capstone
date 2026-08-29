# Component 25.3: Final GitHub Repository Audit

## Rubric outcome

This audit maps the public repository directly to the five criteria shown on the live Component 25.3 page.

| Criterion | Direct evidence | Verification |
| --- | --- | --- |
| Code is clear, commented, easy to run and reproducible | [`FINAL_CAPSTONE_NOTEBOOK.ipynb`](FINAL_CAPSTONE_NOTEBOOK.ipynb), [`FINAL_REPRODUCIBILITY.md`](FINAL_REPRODUCIBILITY.md), `Week_13/week_13_analysis.py`, `Week_13/generate_week_13_figures.py` | Notebook executes from committed evidence; scripts regenerate the final summaries and figures |
| Dataset is complete and included | [`complete_internal_evidence.csv`](../../BBO_Dashboard/data/complete_internal_evidence.csv) and [`FINAL_CAPSTONE_DATASHEET.md`](FINAL_CAPSTONE_DATASHEET.md) | Automated audit confirms 175 starter rows, 104 weekly-query rows, 279 total rows and Functions 1 to 8 |
| Model card is complete and included | [`FINAL_CAPSTONE_MODEL_CARD.md`](FINAL_CAPSTONE_MODEL_CARD.md) | Covers input, output, architecture, performance, limitations, trade-offs, intended use and safeguards |
| README contains an approximately 100-word non-technical explanation | [Root README](../../README.md) | Automated audit confirms exactly 100 words using the repository word-count rule |
| Repository is organised and contains relevant files | [Root assessment quick start](../../README.md), [Module 25 hub](../SECTION_GUIDE.md), Week 01 to Week 13 folders | Automated audit checks required paths, weekly navigation, internal links and unfinished markers |

## Numerical and provenance checks

- The complete dataset contains 279 observations across eight functions.
- Starter observations and participant-selected queries are explicitly separated.
- The final winner table is verified against the strongest participant-query output, not silently combined with starter maxima.
- F3, F4 and F8 retain stronger starter observations than the best participant query, and this is reported in the notebook.
- Week 13 inputs and outputs remain unchanged.
- Exact Week 12 to Week 13 comparisons use decimal arithmetic.
- Repeated-coordinate variability in F2, F3 and F6 is preserved rather than corrected or averaged away; F6 has the largest observed range.
- Post-capstone Black Box Resolution work is labelled separately and does not alter the official record.

## Automated final check

From the repository root:

```bash
python tools/repository_audit.py
```

The audit checks:

1. every required Component 25.3 file;
2. Week 01 to Week 13 navigation;
3. internal Markdown links;
4. unfinished placeholders;
5. the 279-row dataset composition; and
6. the 100-word non-technical README summary.

The continuous-integration workflow repeats this audit, regenerates the Week 13 analysis and verifies the final figures.

## Submission boundary

The repository contains additional research undertaken after the capstone. The official assessed experiment is confined to the course-supplied starter observations and the thirteen authorised query rounds. Black Box Resolution and PDHIS material is clearly separated and did not generate or alter the official portal results.

