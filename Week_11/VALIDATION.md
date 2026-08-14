# Week 11 Validation Record

## Purpose

This document records the checks used to validate the Week 11 evidence and the transition from Week 11 analysis to the submitted Week 12 query set.

## Source validation

The authoritative Week 11 files are:

- [week_11_inputs.csv](week_11_inputs.csv)
- [week_11_results.csv](week_11_results.csv)

Each file contains one record for Functions 1 to 8.

## Dimensionality and bounds

The expected dimensions are 2, 2, 3, 4, 4, 5, 6 and 8. The Week 11 vectors conform to those dimensions. Every coordinate lies within the interval from 0 to 1.

## Numerical preservation

The submitted vectors retain their six decimal place representation. Returned values are stored exactly as supplied. Week 10 to Week 11 changes are derived from the verified source values rather than from rounded display values.

## Outcome validation

All eight Week 11 outputs improved relative to Week 10. The direction of change is therefore consistent across the portfolio, although the magnitude differs by function.

Functions 2 and 5 produced new verified best values. Functions 1 and 8 reproduced earlier best values exactly. Functions 3, 4 and 6 recovered towards stronger historical regions, while Function 7 remained in a productive positive region.

## Strategy validation

The Week 11 results provide an outcome test of the Week 10 strategy. Because every objective improved from Week 10, the regional recovery and refinement choices were supported by the returned evidence.

This does not prove that the Week 10 method was globally optimal. It shows that the selected Week 11 queries performed better than the immediately preceding Week 10 queries.

## PCA validation boundary

PCA was applied after the Week 11 results were available. The calculation used centred query coordinates for Functions 3 to 8. The resulting explained variance ratios describe concentration in the submitted query trajectories.

These ratios were not treated as direct evidence of objective importance. The Week 12 decision compared PCA structure with verified objective performance before choosing the stronger source of evidence for each function.

## Reproducibility

The Week 11 analytical workflow can be reproduced from the repository root with:

```bash
python Week_11/week_11_analysis.py
python Week_11/generate_week_11_figures.py
```

The analysis script validates the Week 11 source data, calculates exact comparisons and performs the PCA calculation. The figure script uses the derived summary to prepare the Week 11 visual evidence.

## Decision validation

The submitted Week 12 coordinates are recorded in [WEEK_12_DECISION_RECORD.md](WEEK_12_DECISION_RECORD.md) and in `../Week_12/week_12_inputs.csv`.

The Week 12 input set was checked for:

- correct dimensionality;
- values within the permitted interval;
- six decimal place submission formatting;
- consistency with the documented function specific strategy.

## Limitation

Validation establishes consistency between the stored evidence, calculations and decision record. It does not establish the hidden form of the objective functions, prove a global optimum or predict the Week 12 outcomes.