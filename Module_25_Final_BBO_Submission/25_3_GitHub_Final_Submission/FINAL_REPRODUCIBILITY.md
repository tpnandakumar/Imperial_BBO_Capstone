# Final Reproducibility Guide

## Scope

This guide provides a short assessor-facing route for reproducing the closing Week 13 analysis from committed evidence. It does not attempt to rerun the hidden Imperial objective functions, which are not available in the repository.

## Authoritative evidence used by the final script

The early exact numerical history for Weeks 1 to 11 is stored in:

`PFRAMOS/data/recovered_exact_history.csv`

The final two rounds are read directly from their verified source files:

- `Week_12/week_12_inputs.csv`
- `Week_12/week_12_results.csv`
- `Week_13/week_13_inputs.csv`
- `Week_13/week_13_results.csv`

The historical Week 01 to Week 11 READMEs remain the chronological narrative record. The consolidated exact-history CSV provides the machine-readable early numerical evidence needed for the final reproducibility script.

## Final analysis

From the repository root, run:

```bash
python Week_13/week_13_analysis.py
```

The script reconstructs the complete thirteen-round history from the committed sources above, calculates exact Week 12 to Week 13 changes with Python `Decimal`, identifies each function's strongest observed output and associated week or weeks, and reports repeated coordinates that returned non-identical outputs.

The principal derived table is:

`Week_13/week_13_analysis_summary.csv`

## Figures

Run:

```bash
python Week_13/generate_week_13_figures.py
```

The figure script uses the same history loader as the numerical analysis. It generates the final-round change plot, within-function normalised progress, the F5 trajectory and the latest round in which each best value was observed.

The supporting source table is:

`Week_13/week_13_figure_data_summary.csv`

## Dependencies

The numerical Week 13 analysis uses Python's standard library. Figure generation requires `matplotlib`.

Earlier analytical stages use additional libraries where documented in their weekly files, including clustering and PCA workflows. Their committed source files and documentation remain in the relevant weekly folders.

## Numerical integrity

Objective values remain stored in their supplied textual representation. Exact Week 12 to Week 13 changes are calculated with decimal arithmetic. Plotting converts values to floating point only for visual display.

## Reproducibility boundary

The repository can reproduce analyses derived from the recorded inputs and outputs. It cannot independently regenerate the hidden objective values because the Imperial black-box evaluator is external to the repository.

The Advanced Extension Series and SOC are post-capstone research and have separate dependencies and reproducibility instructions. They are not required to reproduce the official Week 01 to Week 13 record.
