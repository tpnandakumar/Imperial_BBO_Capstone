# Week_10

## Bayesian Black Box Optimisation Portfolio

### Week 10 Analysis

## Documentation

- [Datasheet for the Bayesian Black Box Optimisation Capstone Dataset](DATASHEET.md)
- [Model Card for the Bayesian Black Box Optimisation Workflow](MODEL_CARD.md)
- [Dataset Record](DATASET.md)
- [Assumptions](ASSUMPTIONS.md)
- [Validation Record](VALIDATION.md)
- [Decision Card](DECISION_CARD.md)
- [Documentation Changelog](CHANGELOG.md)
- [Research Note](RESEARCH_NOTE.md)

The submitted inputs and returned results remain the authoritative numerical record for Week 10.

## Contents

1. Introduction
2. Week 10 Results
3. Comparison of Week 09 and Week 10 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 11 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References

## 1. Introduction

Week 10 continued the evidence based optimisation process developed across the earlier rounds of the Imperial Black Box Optimisation challenge. By this stage, the accumulated observations allowed each function to be treated according to its own recent behaviour rather than applying the same search strategy to every objective.

The Week 10 submission combined local refinement of productive regions with broader or redirected searches where the evidence remained weak. Function 5 was held at the established best input to test whether the result was reproducible. Functions 2, 3, 7 and 8 received controlled refinements. Functions 4 and 6 were moved to alternative local regions after mixed earlier results, while Function 1 was explored more broadly because its recent outputs remained effectively zero.

This folder records the exact Week 10 inputs and outputs, the comparison with Week 09, the ranking and strategy classification, and the reproducible Python workflow used to generate the analytical summaries and figures. All source values are retained at their original precision.

## 2. Week 10 Results

The Week 10 results were mixed but informative. Function 5 remained the leading objective with an output of **4394.868042481448**, exactly matching its Week 09 result. This repeat confirmed that the submitted point produced a stable result, although it did not provide a further gain.

Function 2 improved from **0.47297842839949866** to **0.5311818841205426**. Function 3 also improved, moving from **-0.1156707106126581** to **-0.08697581687486715**. Function 1 changed from a very small negative value to **2.8950706668499033e-23**, but the result remained within the near zero range and did not yet establish a productive region.

Functions 4, 6, 7 and 8 declined. Function 4 showed the largest deterioration, moving to **-13.483642655031158**. The reductions for Functions 6, 7 and 8 were smaller, but they indicated that the latest local movements had not improved performance.

| Function | Week 10 input | Week 10 output | Interpretation |
| --- | --- | ---: | --- |
| Function 1 | 0.450000,0.650000 | 2.8950706668499033e-23 | Near zero, broader exploration still required |
| Function 2 | 0.700000,0.955000 | 0.5311818841205426 | Improved positive result |
| Function 3 | 0.280000,0.875000,0.315000 | -0.08697581687486715 | Improved within the negative region |
| Function 4 | 0.290000,0.730000,0.690000,0.210000 | -13.483642655031158 | Declined and requires reassessment |
| Function 5 | 0.120000,0.997000,0.999800,0.999800 | 4394.868042481448 | Stable leading result |
| Function 6 | 0.260000,0.780000,0.260000,0.840000,0.300000 | -1.2283806967341901 | Small decline and requires reassessment |
| Function 7 | 0.060000,0.500000,0.250000,0.220000,0.430000,0.740000 | 1.285160161342515 | Positive but slightly lower |
| Function 8 | 0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000 | 9.4646525 | Stable positive region with a small decline |

The figure generation script creates the following Week 10 figures in this folder:

- `week_10_figure_1_output_evolution.png`
- `week_10_figure_2_performance_ranking.png`
- `week_10_figure_3_weekly_change.png`
- `week_10_figure_4_strategy_allocation.png`
- `week_10_figure_5_function_5_progress.png`

## 3. Comparison of Week 09 and Week 10 Performance

The comparison with Week 09 shows three improvements, four declines and one unchanged result. Decimal arithmetic was used to calculate every change without rounding or truncation.

| Function | Week 09 output | Week 10 output | Exact change | Direction |
| --- | ---: | ---: | ---: | --- |
| Function 1 | -1.4546199699251391e-58 | 2.8950706668499033e-23 | 2.895070666849903300000000000E-23 | Improved, but still near zero |
| Function 2 | 0.47297842839949866 | 0.5311818841205426 | 0.05820345572104394 | Improved |
| Function 3 | -0.1156707106126581 | -0.08697581687486715 | 0.02869489373779095 | Improved |
| Function 4 | -11.788939969158545 | -13.483642655031158 | -1.694702685872613 | Declined |
| Function 5 | 4394.868042481448 | 4394.868042481448 | 0 | Unchanged |
| Function 6 | -1.1733030029888645 | -1.2283806967341901 | -0.0550776937453256 | Declined |
| Function 7 | 1.314307996450604 | 1.285160161342515 | -0.029147835108089 | Declined |
| Function 8 | 9.4709436 | 9.4646525 | -0.0062911 | Declined |

Function 2 delivered the strongest useful improvement among the moderate scale functions. Function 3 also moved in the correct direction and produced its best result since Week 07. Function 5 demonstrated reproducibility at the tested point, while the decline in Function 4 showed that its Week 10 movement was not beneficial. The small changes in Functions 7 and 8 were consistent with relatively stable local regions, although the direction was unfavourable.

## 4. Query Selection Strategy

The Week 10 query selection strategy was based on the observed Week 09 behaviour and the amount of uncertainty remaining around each function.

Function 5 was treated as the main exploitation target. The exact Week 09 input was retained because it had produced the highest observed value. This repeat tested stability before any further movement near the boundary.

Function 2 received a controlled local refinement and improved. Function 3 also received a local adjustment and moved closer to zero, supporting continued refinement. Functions 7 and 8 remained in established positive regions, so only limited local movements were used. Their slight declines suggest that future changes should remain cautious.

Function 4 was moved within the previously explored local region but deteriorated substantially. Function 6 also declined after a local movement. Both functions therefore require reassessment rather than automatic continuation in the same direction.

Function 1 was moved to a different two dimensional location. Although the sign changed, the magnitude remained extremely small, so the result did not justify local exploitation.

## 5. Exploration vs Exploitation Analysis

The Week 10 allocation maintained a deliberate separation between exploitation, refinement, reassessment and exploration.

- **Exploit:** Function 5, because it remained the clear leading function and repeated the highest known output.
- **Refine:** Functions 2, 3, 7 and 8, because they retained interpretable local structure and either improved or remained within productive regions.
- **Reassess:** Functions 4 and 6, because the Week 10 movements reduced performance.
- **Explore:** Function 1, because the output remained effectively zero despite a substantial change in input.

This classification avoids treating a positive result as sufficient evidence for unrestricted exploitation. Function 2 improved, but one successful movement still requires confirmation. Functions 7 and 8 remain productive, but their small declines support conservative refinement rather than larger steps. Function 5 is the only objective with enough repeated evidence to justify direct exploitation.

## 6. Reflection on Week 11 Query Selection

The Week 10 evidence supported a more differentiated Week 11 submission. Function 5 could be moved only slightly from the stable Week 10 point to test whether a marginal boundary refinement produced an additional gain. Function 2 could remain close to its improved region. Functions 7 and 8 required cautious adjustment because their latest changes were small but negative.

The deterioration in Functions 4 and 6 justified a clearer change of direction rather than another minor continuation. Function 3 had improved and therefore supported one further targeted refinement. Function 1 still required broad exploration because the Week 10 result remained near zero.

The verified Week 11 query set reflected these conclusions:

| Function | Week 11 query |
| --- | --- |
| Function 1 | 0.600000,0.600000 |
| Function 2 | 0.695000,0.950000 |
| Function 3 | 0.840000,0.160000,0.840000 |
| Function 4 | 0.620000,0.420000,0.440000,0.250000 |
| Function 5 | 0.110000,0.998000,0.999900,0.999900 |
| Function 6 | 0.720000,0.190000,0.700000,0.710000,0.150000 |
| Function 7 | 0.045000,0.485000,0.255000,0.220000,0.420000,0.745000 |
| Function 8 | 0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000 |

## 7. Functional Ranking Evolution

The Week 10 ranking remained unchanged from Week 09. Stability in rank does not mean that every function was stable in value, but it confirms that the broad ordering of the objective scales remained consistent.

| Rank | Function | Week 10 output | Strategy |
| ---: | --- | ---: | --- |
| 1 | Function 5 | 4394.868042481448 | Exploit |
| 2 | Function 8 | 9.4646525 | Refine |
| 3 | Function 7 | 1.285160161342515 | Refine |
| 4 | Function 2 | 0.5311818841205426 | Refine |
| 5 | Function 1 | 2.8950706668499033e-23 | Explore |
| 6 | Function 3 | -0.08697581687486715 | Refine |
| 7 | Function 6 | -1.2283806967341901 | Reassess |
| 8 | Function 4 | -13.483642655031158 | Reassess |

Function 5 continued to dominate the portfolio. Functions 8, 7 and 2 remained the other positive performers. Function 1 ranked above the negative functions numerically, but its near zero output still represented a lack of useful signal rather than a strong optimisation result.

## 8. High Performing Region Identification

The strongest identified region remained the Function 5 boundary region represented by **0.120000,0.997000,0.999800,0.999800**. The repeated output of **4394.868042481448** confirmed that the result was stable at this point.

Function 8 continued to occupy a high and stable positive region, although the Week 10 output declined slightly to **9.4646525**. Function 7 also remained positive at **1.285160161342515**. Function 2 strengthened its productive region by increasing to **0.5311818841205426**.

Function 3 showed evidence of a more favourable local region because it improved to **-0.08697581687486715**. The result remained negative, but the movement provided a clearer direction for further refinement. No high performing region was established for Function 1, and the Week 10 movements for Functions 4 and 6 did not identify improved locations.

## 9. Decision Matrix and Resource Allocation

The Week 10 decision matrix assigns effort according to current evidence rather than raw rank alone.

| Function | Evidence from Week 10 | Decision | Priority |
| --- | --- | --- | --- |
| Function 1 | Near zero after broad movement | Continue exploration | Medium |
| Function 2 | Clear improvement | Confirm and refine | High |
| Function 3 | Improved within negative region | Continue targeted refinement | Medium |
| Function 4 | Largest decline | Change direction and reassess | High |
| Function 5 | Stable highest output | Continue precise exploitation | High |
| Function 6 | Small decline | Reassess local direction | Medium |
| Function 7 | Small decline in positive region | Conservative refinement | Medium |
| Function 8 | Very small decline in stable region | Monitor and refine cautiously | Medium |

Resource allocation should therefore concentrate on preserving the Function 5 result, confirming the Function 2 improvement and correcting the unproductive movements in Functions 4 and 6. Function 1 still requires enough search breadth to identify a meaningful signal.

## 10. Information Gain Analysis

Week 10 provided valuable information even where objective values did not improve. The unchanged Function 5 output confirmed repeatability at the tested point. The improvement in Function 2 strengthened confidence in its local search direction, while the Function 3 result identified a more favourable region.

The decline in Function 4 was also informative because it ruled out the Week 10 direction as an immediate continuation path. Function 6 supplied similar, though smaller, evidence. The limited declines in Functions 7 and 8 suggested that both were operating on relatively flat local surfaces where large movements would carry unnecessary risk.

Function 1 remained the least resolved objective. Its change from a minute negative value to a minute positive value did not provide evidence of a practically useful region. Its main information contribution was therefore confirmation that further exploration was still required.

## 11. Computational Analysis and Coding Implementation

The Week 10 computational workflow uses two Python scripts.

`week_10_analysis.py` validates the dimensions and bounds of the input vectors, reads the Week 09 and Week 10 results, calculates exact changes with `Decimal`, ranks the functions and exports `week_10_analysis_summary.csv`.

`generate_week_10_figures.py` stores the verified historical outputs as exact strings, constructs the Week 09 to Week 10 comparison, exports `week_10_figure_data_summary.csv` and generates five analytical figures in the Week 10 folder. Decimal values are converted to floating point numbers only when required by Matplotlib for plotting. The stored CSV values remain unchanged.

The scripts use a flat structure and do not create a separate figures directory. This keeps the Week 10 artefacts together and follows the established repository convention.

## 12. Repository Files and Reproducibility

The Week 10 folder contains the following assessment and reproducibility files:

- `README.md`
- [`DATASHEET.md`](DATASHEET.md)
- [`MODEL_CARD.md`](MODEL_CARD.md)
- [`DATASET.md`](DATASET.md)
- [`ASSUMPTIONS.md`](ASSUMPTIONS.md)
- [`VALIDATION.md`](VALIDATION.md)
- [`DECISION_CARD.md`](DECISION_CARD.md)
- [`CHANGELOG.md`](CHANGELOG.md)
- [`RESEARCH_NOTE.md`](RESEARCH_NOTE.md)
- `week_10_inputs.csv`
- `week_10_results.csv`
- `week_10_analysis_summary.csv`
- `week_10_figure_data_summary.csv`
- `week_10_analysis.py`
- `generate_week_10_figures.py`

The analysis can be reproduced from the repository root with:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The analysis script requires `Week_09/week_09_results.csv` for the exact weekly comparison. The figure script uses the verified historical output series stored within the script and writes all generated files directly into `Week_10`.

## 13. Conclusion

Week 10 strengthened the evidence base for the remaining optimisation rounds. Function 2 and Function 3 improved, Function 5 reproduced its