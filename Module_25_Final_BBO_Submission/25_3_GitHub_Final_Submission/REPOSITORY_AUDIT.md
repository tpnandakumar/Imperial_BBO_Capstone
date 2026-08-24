# Component 25.3: Final GitHub Repository Audit

## Purpose

This audit is based on the grading information currently available for the final GitHub submission. It must be checked again against the live Component 25.3 page when the assignment unlocks.

## Known grading criteria and current readiness

| Criterion | Evidence now prepared | Remaining check |
| --- | --- | --- |
| Code is clear, well commented and easy to run, with reproducible results | Week 13 analysis and figure scripts now reconstruct the thirteen-round history from committed evidence; final reproducibility guide added | Run once in the final submission environment and confirm generated files match committed summaries |
| Datasheet is complete and included | `FINAL_CAPSTONE_DATASHEET.md` added and linked from the root README | Compare against the unlocked 25.3 rubric wording |
| Model card is complete and included | `FINAL_CAPSTONE_MODEL_CARD.md` added and linked from the root README | Compare against the unlocked 25.3 rubric wording |
| README contains an approximately 100-word non-technical explanation | Plain-language project summary added near the top of the root README | Final word-count and readability check |
| Repository is well organised and contains all relevant project files | Module 25 assessment hub, Weeks 01 to 13 navigation, final winner summary and post-capstone boundary are explicit | Final broken-link, placeholder and file-presence audit |

## Checks already completed in this preparation stage

- Week 13 verified inputs and outputs are preserved unchanged.
- Final strongest verified coordinates are recorded for F1 to F8.
- Module 25 is separated from the thirteen optimisation rounds.
- The superseded `Week_25_Final_BBO_Submission` structure has been removed to avoid incorrect round numbering.
- The root README links directly to the Module 25 evidence hub, final datasheet, model card and reproducibility guide.
- The final Week 13 analysis no longer expects non-existent Week 01 to Week 11 CSV files. It reads the committed exact early-history file and the verified Week 12 and Week 13 source files.
- Final infographic sources are mapped without pre-writing the locked 25.1 or 25.2 responses.
- Advanced Extension Series and SOC remain explicitly identified as post-capstone research.

## Final audit sequence before 25.3 submission

1. Capture the unlocked Component 25.3 prompt and full rubric.
2. Run `python Week_13/week_13_analysis.py` from the repository root.
3. Run `python Week_13/generate_week_13_figures.py` from the repository root in an environment with `matplotlib` installed.
4. Compare regenerated `week_13_analysis_summary.csv` with the committed version.
5. Confirm final datasheet and model card address every rubric field.
6. Count and review the non-technical root README summary.
7. Verify every assessment-navigation link.
8. Check that all final figures referenced in Module 25 exist and have correct captions.
9. Search for unfinished placeholders, obsolete instructions and accidental conversational text.
10. Confirm public assessor access and branch protection remain appropriate.

## Submission principle

The assessor should not need to search the repository to establish that a criterion has been met. Each required item should be directly visible from the root README and traceable to the underlying evidence.
