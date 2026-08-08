# Week 10 Reproducibility Checklist

## Assessment status

| Check | Status | Evidence |
| --- | --- | --- |
| Eight submitted query vectors are present | Complete | `week_10_inputs.csv` |
| Eight returned objective values are present | Complete | `week_10_results.csv` |
| Function dimensionality is documented | Complete | `DATASET.md`, `VALIDATION.md` |
| Submitted coordinates remain within 0 to 1 | Complete | `VALIDATION.md`, `week_10_analysis.py` |
| Submitted coordinates retain six decimal place representation | Complete | `week_10_inputs.csv` |
| Returned numerical precision is preserved | Complete | `week_10_results.csv` |
| Week 09 comparison is documented | Complete | `README.md`, `VALIDATION.md` |
| Exact changes are calculated without rounding or truncation | Complete | `week_10_analysis.py`, `week_10_analysis_summary.csv` |
| Analysis is reproducible from stored files | Complete | `week_10_analysis.py` |
| Figure data are reproducible | Complete | `generate_week_10_figures.py`, `week_10_figure_data_summary.csv` |
| Assumptions are explicit | Complete | `ASSUMPTIONS.md` |
| Validation boundaries are explicit | Complete | `VALIDATION.md` |
| Decision rationale is recorded | Complete | `DECISION_CARD.md` |
| Evidence provenance is traceable | Complete | `EVIDENCE_PROVENANCE.md` |
| Negative evidence is documented | Complete | `NEGATIVE_EVIDENCE.md` |
| Datasheet is present | Complete | `DATASHEET.md` |
| Model card is present | Complete | `MODEL_CARD.md` |

## Reproduction commands

From the repository root:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The scripts operate on the stored Week 10 evidence. The original input and output CSV files should not be overwritten manually.

## Interpretation

A completed checklist confirms that the Week 10 record is internally documented and that its derived analyses can be traced to stored evidence. It does not prove that the optimisation strategy is globally optimal, that the hidden functions are known, or that the workflow will generalise to another problem.