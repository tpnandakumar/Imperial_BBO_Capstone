# Component 25.3: Final GitHub Submission

This folder is the assessor-facing entry point for the completed repository submission.

## Required deliverables

1. [Final Capstone Notebook](FINAL_CAPSTONE_NOTEBOOK.ipynb)
2. [Final Capstone Datasheet](FINAL_CAPSTONE_DATASHEET.md)
3. [Final Capstone Model Card](FINAL_CAPSTONE_MODEL_CARD.md)
4. [Final Reproducibility Guide](FINAL_REPRODUCIBILITY.md)
5. [Completed Repository Audit](REPOSITORY_AUDIT.md)
6. [Exact Discussion Board Submission](DISCUSSION_BOARD_SUBMISSION.md)

The complete dataset is [`BBO_Dashboard/data/complete_internal_evidence.csv`](../../BBO_Dashboard/data/complete_internal_evidence.csv). It contains 175 course-supplied starter observations and 104 participant-selected portal queries across thirteen rounds.

## Verification

From the repository root:

```bash
python -m pip install -r requirements-final.txt
python tools/repository_audit.py
python tools/validate_final_notebook.py
python Week_13/week_13_analysis.py
python Week_13/generate_week_13_figures.py
```

These commands verify the repository structure, dataset composition, notebook calculations, final participant-query results and analytical figures. They cannot rerun the hidden Imperial objective functions because the evaluator is external.

