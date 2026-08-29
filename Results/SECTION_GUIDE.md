# Results

This folder provides the assessment-facing final figures linked from the single repository README. The reproducible source figures remain in `Week_13`, where the automated workflow regenerates and verifies them.

| Figure | Interpretation | Reproducible source |
| --- | --- | --- |
| [Final-round change](figure_01_final_round_change.png) | Compares the movement from Week 12 to Week 13 for all eight functions | [`Week_13/week_13_figure_1_final_change.png`](../Week_13/week_13_figure_1_final_change.png) |
| [Normalised progress](figure_02_normalised_progress.png) | Shows the timing and direction of progress within each function across thirteen rounds | [`Week_13/week_13_figure_2_normalised_progress.png`](../Week_13/week_13_figure_2_normalised_progress.png) |
| [Function 5 trajectory](figure_03_function_5_trajectory.png) | Shows the clearest sustained improvement in the participant-query record | [`Week_13/week_13_figure_3_function_5_trajectory.png`](../Week_13/week_13_figure_3_function_5_trajectory.png) |
| [Latest best round](figure_04_latest_best_round.png) | Shows when each function's strongest participant-query result was last observed | [`Week_13/week_13_figure_4_latest_best_round.png`](../Week_13/week_13_figure_4_latest_best_round.png) |

The normalised progress figure compares each function only with its own observed range. It does not make raw objective values comparable across functions.

## Reproduction code

| Code | Purpose |
| --- | --- |
| [`week_13_analysis.py`](../Week_13/week_13_analysis.py) | Reconstructs the full thirteen-round record and verifies the final function-level results |
| [`generate_week_13_figures.py`](../Week_13/generate_week_13_figures.py) | Regenerates the four final assessment figures from committed evidence |
| [`FINAL_CAPSTONE_NOTEBOOK.ipynb`](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb) | Runs the assessor-facing data checks, comparisons, repeatability analysis and trajectory plots without path editing |
| [`requirements-final.txt`](../requirements-final.txt) | Records the required plotting dependency for reproducible execution |

