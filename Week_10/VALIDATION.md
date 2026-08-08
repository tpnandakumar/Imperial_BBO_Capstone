# Week 10 Validation Record

## Purpose

This document records the validation checks applied to the Week 10 optimisation evidence and separates data validation from interpretation of optimisation performance.

## Source validation

The Week 10 analysis uses the stored source files:

- [week_10_inputs.csv](week_10_inputs.csv)
- [week_10_results.csv](week_10_results.csv)

The input file contains one submitted vector for each of the eight functions. The result file contains one returned objective value for each function.

## Dimensionality checks

The required dimensions are:

| Function | Required dimensions |
| --- | ---: |
| Function 1 | 2 |
| Function 2 | 2 |
| Function 3 | 3 |
| Function 4 | 4 |
| Function 5 | 4 |
| Function 6 | 5 |
| Function 7 | 6 |
| Function 8 | 8 |

The Week 10 input vectors conform to these dimensionality requirements. Each coordinate is within the permitted interval from 0 to 1 and is stored using the submitted six decimal place representation.

## Exact numerical preservation

Returned objective values are retained exactly as stored in `week_10_results.csv`. No rounding or truncation is introduced into the authoritative record. Exact Week 09 to Week 10 differences are calculated using decimal arithmetic in the analysis workflow.

## Cross week validation

The Week 10 results were compared with the verified Week 09 results. The comparison produced three improvements, four declines and one unchanged result:

| Function | Week 09 | Week 10 | Exact change |
| --- | ---: | ---: | ---: |
| Function 1 | -1.4546199699251391e-58 | 2.8950706668499033e-23 | 2.895070666849903300000000000E-23 |
| Function 2 | 0.47297842839949866 | 0.5311818841205426 | 0.05820345572104394 |
| Function 3 | -0.1156707106126581 | -0.08697581687486715 | 0.02869489373779095 |
| Function 4 | -11.788939969158545 | -13.483642655031158 | -1.694702685872613 |
| Function 5 | 4394.868042481448 | 4394.868042481448 | 0 |
| Function 6 | -1.1733030029888645 | -1.2283806967341901 | -0.0550776937453256 |
| Function 7 | 1.314307996450604 | 1.285160161342515 | -0.029147835108089 |
| Function 8 | 9.4709436 | 9.4646525 | -0.0062911 |

## Repeatability check

Function 5 provides a direct Week 10 repeatability observation. The Week 09 input `0.120000,0.997000,0.999800,0.999800` was submitted again in Week 10 and returned `4394.868042481448` on both occasions.

This validates repeatability for that exact tested query under the observed competition conditions. It does not establish repeatability for neighbouring inputs or prove that the region contains the global optimum.

## Interpretation checks

The analytical labels used in the README are consistent with the verified observations:

- Function 1 remains an exploration target because its output remains effectively zero.
- Functions 2 and 3 support refinement because both improved.
- Functions 4 and 6 require reassessment because both declined.
- Function 5 supports precise exploitation because the leading value repeated at the same query.
- Functions 7 and 8 remain suitable for cautious refinement because both remain positive but declined slightly.

These labels are interpretations of the data and are not additional outputs from the black box platform.

## Reproducibility

The Week 10 analysis can be reproduced from the repository root using:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The first script validates and analyses the stored Week 10 evidence. The second generates the analytical figure data and visual outputs. The original input and result CSV files remain unchanged.

## Validation boundary

The checks above establish consistency of the stored record and reproducibility of the derived analysis. They do not validate the unknown mathematical functions, prove a global optimum, or establish that the Week 10 strategy will generalise to another optimisation problem.