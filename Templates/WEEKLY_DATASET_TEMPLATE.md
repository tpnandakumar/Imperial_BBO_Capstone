# Week XX Dataset

**Week:** XX  
**Optimisation round:** XX  
**Status:** Draft / Submitted / Processed / Final  
**Maintainer:** Dr N T Pisharam

## 1. Dataset purpose

Briefly state what this weekly dataset records and how it supports the next optimisation decision.

## 2. Dataset files

| File | Role | Raw or derived | Status |
|---|---|---|---|
| `week_XX_inputs.csv` | Submitted query points | Raw |  |
| `week_XX_results.csv` | Returned objective values | Raw |  |
| `week_XX_analysis_summary.csv` | Derived analytical summary | Derived |  |
| `week_XX_figure_data_summary.csv` | Data used to generate figures | Derived |  |
| `week_XX_analysis.py` | Analysis code | Reproducibility |  |
| `generate_week_XX_figures.py` | Figure generation code | Reproducibility |  |

## 3. Scope and size

- Functions represented: F1 to F8
- Number of weekly query records:
- Number of returned outputs:
- Missing or pending records:

## 4. Input dimensions

| Function | Dimensions |
|---|---:|
| F1 | 2 |
| F2 | 2 |
| F3 | 3 |
| F4 | 4 |
| F5 | 4 |
| F6 | 5 |
| F7 | 6 |
| F8 | 8 |

All query coordinates must be in `[0,1]` and recorded to six decimal places.

## 5. Schemas

Document every column in each CSV file, including data type, meaning, units and whether it is raw or derived.

## 6. Relationships between files

Explain how inputs become portal outputs, how outputs feed analysis, and how summaries feed figures and the weekly README.

## 7. Gaps and quality notes

Record missing values, corrections, unusual outputs, scale differences, pending portal results and any deviations from the standard workflow.

## 8. Reproduction

Provide the commands needed to run the weekly analysis and regenerate figures.

## 9. Companion datasheet

When this template is instantiated in a weekly folder, the companion provenance and limitations record should be stored as `DATASHEET.md` in that same folder.
