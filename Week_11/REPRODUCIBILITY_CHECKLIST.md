# Week 11 Reproducibility Checklist

| Check | Status | Evidence |
| --- | --- | --- |
| Eight Week 11 query vectors present | Complete | `week_11_inputs.csv` |
| Eight Week 11 returned values present | Complete | `week_11_results.csv` |
| Function dimensionality checked | Complete | `week_11_analysis.py`, `VALIDATION.md` |
| Input bounds checked | Complete | `week_11_analysis.py`, `VALIDATION.md` |
| Six decimal submission formatting preserved | Complete | `week_11_inputs.csv` |
| Returned numerical precision preserved | Complete | `week_11_results.csv` |
| Week 10 comparison reproduced | Complete | `week_11_analysis.py`, `week_11_analysis_summary.csv` |
| Historical best comparison recorded | Complete | `README.md`, `EVIDENCE_PROVENANCE.md` |
| PCA calculation reproducible | Complete | `week_11_analysis.py` |
| PCA limitations documented | Complete | `DATASHEET.md`, `MODEL_CARD.md`, `VALIDATION.md` |
| Figure data reproducible | Complete | `generate_week_11_figures.py`, `week_11_figure_data_summary.csv` |
| Week 12 strategy comparison documented | Complete | `PCA_STRATEGY_COMPARISON.md` |
| Week 12 decision trail documented | Complete | `WEEK_12_DECISION_RECORD.md` |
| Exact submitted Week 12 inputs preserved | Complete | `../Week_12/week_12_inputs.csv` |

## Reproduction commands

From the repository root:

```bash
python Week_11/week_11_analysis.py
python Week_11/generate_week_11_figures.py
```

The original Week 11 input and result files remain the source record. Reproduction of the derived analysis does not require altering those files.

## Scope

This checklist confirms that the Week 11 analytical record is traceable and reproducible from the stored evidence. It does not establish the hidden functions or guarantee the performance of the submitted Week 12 queries.