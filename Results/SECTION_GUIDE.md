# Results

This folder is the assessment-facing results chapter for the Imperial BBO Capstone. It brings the final tables, graphs and discussion together while linking to the authoritative data and code used to reproduce them.

## 1. Tables

| Results table | What it reports | Reproduction route |
| --- | --- | --- |
| [Verified final result summary](../Module_25_Final_BBO_Submission/Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv) | Strongest participant-query output and winning week for F1 to F8 | [Final numerical analysis code](../Week_13/week_13_analysis.py) |
| [Week 13 analysis summary](../Week_13/week_13_analysis_summary.csv) | Final-round change, strongest observed output and repeatability findings | [Final numerical analysis code](../Week_13/week_13_analysis.py) |
| [Final figure data summary](../Week_13/week_13_figure_data_summary.csv) | Source values used in the four assessment figures | [Figure-generation code](../Week_13/generate_week_13_figures.py) |
| [Complete 279-observation evidence](../BBO_Dashboard/data/complete_internal_evidence.csv) | All 175 starter observations and 104 participant-selected queries | [Executable capstone notebook](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb) |

## 2. Graphs

The four figures below are assessment-facing copies. Their reproducible source figures remain in `Week_13`, where the automated workflow regenerates and verifies them.

| Figure | Interpretation | Reproducible source |
| --- | --- | --- |
| [Final-round change](figure_01_final_round_change.png) | Compares the movement from Week 12 to Week 13 for all eight functions | [`Week_13/week_13_figure_1_final_change.png`](../Week_13/week_13_figure_1_final_change.png) |
| [Normalised progress](figure_02_normalised_progress.png) | Shows the timing and direction of progress within each function across thirteen rounds | [`Week_13/week_13_figure_2_normalised_progress.png`](../Week_13/week_13_figure_2_normalised_progress.png) |
| [Function 5 trajectory](figure_03_function_5_trajectory.png) | Shows the clearest sustained improvement in the participant-query record | [`Week_13/week_13_figure_3_function_5_trajectory.png`](../Week_13/week_13_figure_3_function_5_trajectory.png) |
| [Latest best round](figure_04_latest_best_round.png) | Shows when each function's strongest participant-query result was last observed | [`Week_13/week_13_figure_4_latest_best_round.png`](../Week_13/week_13_figure_4_latest_best_round.png) |

The normalised progress figure compares each function only with its own observed range. It does not make raw objective values comparable across functions. All four figures can be regenerated with [`generate_week_13_figures.py`](../Week_13/generate_week_13_figures.py) after installing [`requirements-final.txt`](../requirements-final.txt).

## 3. Discussion

### Summary

No single search behaviour suited all eight hidden functions. Function 5 benefited from sustained directional refinement. Functions 1, 4, 7 and 8 showed the value of retaining or recovering strong earlier points. Function 2 demonstrated that a small additional move can reduce performance, while Function 6 showed why repeated-coordinate checks matter when returned outputs vary. Overall, the evidence supports an adaptive sequential strategy that balances exploration, refinement, recovery, replication and stopping.

[Read the detailed Results Discussion](../Discussion/RESULTS_DISCUSSION.md) for the full interpretation of F1 to F8, what the model taught us, the limitations of the evidence and the practical conclusions.

- [Final strategy outcome](../Week_13/FINAL_STRATEGY_OUTCOME.md)
- [Final capstone synthesis](../Week_13/FINAL_CAPSTONE_SYNTHESIS.md)
- [Successful optimisation strategies evidence](../Module_25_Final_BBO_Submission/25_2_Successful_Optimisation_Strategies/EVIDENCE_MAP.md)
- [Final model card](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_MODEL_CARD.md)

