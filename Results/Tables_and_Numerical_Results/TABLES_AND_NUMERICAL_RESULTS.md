# Tables and Numerical Results

## Summary

Round 13 produced new participant-query best values for Functions 3, 5 and 6. Function 5 showed the clearest sustained improvement, rising from `1415.876394` in Week 1 to `4440.957217` in Week 13. Functions 1, 4, 7 and 8 retained or reconfirmed strong earlier values, while Function 2 showed that another small move can reduce performance. The table below reports the strongest participant-selected result for each function. These values do not establish the unknown global optima.

## Final participant-query results

| Function | Best output | Best query week or weeks | Numerical interpretation |
| --- | ---: | --- | --- |
| F1 | `0.025559285339829783` | 3, 11, 12 and 13 | The strongest value was found early and reproduced later |
| F2 | `0.7335252043269003` | 12 | A further small move in Week 13 reduced performance |
| F3 | `-0.05685061601567621` | 13 | The final adjustment produced a new participant-query best |
| F4 | `-4.359874926582439` | 1, 12 and 13 | Recovery returned to the earlier strongest point |
| F5 | `4440.957216598753` | 13 | Sustained refinement produced the clearest continuing improvement |
| F6 | `-0.6071562248604215` | 13 | The final round improved the observed best, with repeatability still relevant |
| F7 | `1.3809299933612855` | 5, 12 and 13 | Recovery and repetition confirmed an earlier strong point |
| F8 | `9.58024` | 1, 11, 12 and 13 | Repetition confirmed the retained result within the observed record |

## Numerical evidence and reproduction

| Evidence | What it reports | Reproduction route |
| --- | --- | --- |
| [Verified final result summary](../../Module_25_Final_BBO_Submission/Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv) | Strongest participant-query output and winning week for F1 to F8 | [Final numerical analysis code](../../Week_13/week_13_analysis.py) |
| [Week 13 analysis summary](../../Week_13/week_13_analysis_summary.csv) | Final-round change, strongest observed output and repeatability findings | [Final numerical analysis code](../../Week_13/week_13_analysis.py) |
| [Final figure data summary](../../Week_13/week_13_figure_data_summary.csv) | Source values used in the four assessment figures | [Figure-generation code](../../Week_13/generate_week_13_figures.py) |
| [Complete 279-observation evidence](../../BBO_Dashboard/data/complete_internal_evidence.csv) | All 175 starter observations and 104 participant-selected queries | [Executable capstone notebook](../../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb) |

The [final reproducibility guide](../../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md) provides the assessor-facing execution route.

[Return to the Results summary](../SECTION_GUIDE.md).

