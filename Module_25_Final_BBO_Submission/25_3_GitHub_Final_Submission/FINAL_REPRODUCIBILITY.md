# Final Reproducibility Guide

## Scope

This guide provides a short assessor-facing route for reproducing the closing Week 13 analysis from committed evidence. It does not attempt to rerun the hidden Imperial objective functions, which are not available in the repository.

## Recommended assessor route

Open [`FINAL_CAPSTONE_NOTEBOOK.ipynb`](FINAL_CAPSTONE_NOTEBOOK.ipynb). The notebook verifies the complete 279-row dataset, separates the 175 starter observations from the 104 participant-selected queries, compares their within-function maxima, checks the final participant-query winner table and plots all thirteen query trajectories.

The canonical complete dataset is:

`BBO_Dashboard/data/complete_internal_evidence.csv`

## Authoritative evidence used by the final script

The early exact numerical history for Weeks 1 to 11 is read from the canonical complete dataset:

`BBO_Dashboard/data/complete_internal_evidence.csv`

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

## Week 13 RL-informed decision experiment

Run:

```bash
python Week_13/RL_DECISION_EXPERIMENT/run_rl_decision_experiment.py
```

The experiment uses the verified Week 1 to Week 12 record to select the final action type for each function, then adds the returned Week 13 outputs to evaluate what followed those actions. It writes a state-action-reward CSV and two assessment-ready PNG figures to `Week_13/RL_DECISION_EXPERIMENT/outputs/`.

## Dependencies

The numerical Week 13 analysis uses Python's standard library. Figure generation requires `matplotlib`. The RL decision experiment also uses `pandas` and `numpy`. These packages are recorded in `requirements-final.txt`.

Earlier analytical stages use additional libraries where documented in their weekly files, including clustering and PCA workflows. Their committed source files and documentation remain in the relevant weekly folders.

To execute the final notebook locally after installing Jupyter, run:

```bash
jupyter nbconvert --to notebook --execute \
  Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb \
  --output FINAL_CAPSTONE_NOTEBOOK.executed.ipynb
```

## Numerical integrity

Objective values remain stored in their supplied textual representation. Exact Week 12 to Week 13 changes are calculated with decimal arithmetic. Plotting converts values to floating point only for visual display.

## Reproducibility boundary

The repository can reproduce analyses derived from the recorded inputs and outputs. It cannot independently regenerate the hidden objective values because the Imperial black-box evaluator is external to the repository. The final winner table refers to the strongest participant-query outputs. Starter-data maxima are retained and compared separately rather than being attributed to the optimisation rounds.

The Advanced Extension Series and SOC are post-capstone research and have separate dependencies and reproducibility instructions. They are not required to reproduce the official Week 01 to Week 13 record.
