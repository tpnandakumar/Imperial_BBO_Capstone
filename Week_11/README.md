# Week_11

## Bayesian Black Box Optimisation Portfolio

### Week 11 Analysis

## Contents

1. Introduction
2. Week 11 Results
3. Comparison of Week 10 and Week 11 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 12 Query Selection
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

Week 11 marked a stronger transition from general evidence based search towards function specific strategic optimisation. The submission used the complete verified history from Weeks 01 to 10 and selected a different action for each objective according to its observed behaviour. Confirmed high performing points were reused where earlier evidence justified exploitation, while local probes, recovery moves and one controlled boundary directed test were used elsewhere.

The resulting round was the first in which every function improved relative to the preceding week. This outcome does not prove that the selected methods are universally optimal, nor does it reveal the hidden objective landscapes. It does, however, provide clear evidence that the Week 11 decision process was effective within this competition and at this stage of the available history.

This folder records the exact Week 11 inputs and outputs, the comparison with Week 10, the ranking and strategy classification, and the reproducible Python workflow used to create the analytical summaries and figures. Every numerical source value is preserved exactly as supplied. No value has been rounded, shortened or reconstructed from an estimate.

## 2. Week 11 Results

Week 11 produced improvements across all eight objective functions. Function 5 remained the leading objective and reached a new verified best output of **4411.0387356061765**. The change from Week 10 was **16.1706931247285**, confirming that the controlled boundary directed probe improved upon the stable point used in the preceding round.

Function 4 recorded the largest recovery relative to its own recent result, increasing from **-13.483642655031158** to **-4.868852987697114**. Function 6 also recovered substantially, moving from **-1.2283806967341901** to **-0.7268715077444687**. Both values remained negative, but the direction of travel showed that recovery towards previously stronger regions was more productive than continuing the Week 10 movement.

Functions 2, 3 and 7 improved through local refinement or trust region probes. Function 8 returned to **9.58024**, matching its verified Week 01 value and exceeding its Week 10 result. Function 1 improved from a value close to zero to **0.025559285339829783**, reproducing the verified narrow peak first observed in Week 03.

| Function | Week 11 input | Week 11 output | Interpretation |
| --- | --- | ---: | --- |
| Function 1 | 0.600000,0.600000 | 0.025559285339829783 | Confirmed recovery of the narrow positive peak |
| Function 2 | 0.695000,0.950000 | 0.5848554940277205 | Improved through a local trust region probe |
| Function 3 | 0.840000,0.160000,0.840000 | -0.06542982421105416 | Improved through local refinement |
| Function 4 | 0.620000,0.420000,0.440000,0.250000 | -4.868852987697114 | Strong recovery from the Week 10 decline |
| Function 5 | 0.110000,0.998000,0.999900,0.999900 | 4411.0387356061765 | New verified best following a boundary directed probe |
| Function 6 | 0.720000,0.190000,0.700000,0.710000,0.150000 | -0.7268715077444687 | Recovered towards the strongest known basin |
| Function 7 | 0.045000,0.485000,0.255000,0.220000,0.420000,0.745000 | 1.3579108517237013 | Improved through tight trust region refinement |
| Function 8 | 0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000 | 9.58024 | Confirmed return to the best verified value |

The figure generation script creates the following Week 11 figures directly in this folder:

- `week_11_figure_1_output_evolution.png`
- `week_11_figure_2_performance_ranking.png`
- `week_11_figure_3_weekly_change.png`
- `week_11_figure_4_strategy_allocation.png`
- `week_11_figure_5_function_5_progress.png`

## 3. Comparison of Week 10 and Week 11 Performance

Every Week 11 output was higher than its Week 10 counterpart. Decimal arithmetic was used to calculate each change without rounding or truncation.

| Function | Week 10 output | Week 11 output | Exact change | Direction |
| --- | ---: | ---: | ---: | --- |
| Function 1 | 2.8950706668499033e-23 | 0.025559285339829783 | 0.02555928533982978299997104929 | Improved |
| Function 2 | 0.5311818841205426 | 0.5848554940277205 | 0.0536736099071779 | Improved |
| Function 3 | -0.08697581687486715 | -0.06542982421105416 | 0.02154599266381299 | Improved |
| Function 4 | -13.483642655031158 | -4.868852987697114 | 8.614789667334044 | Improved |
| Function 5 | 4394.868042481448 | 4411.0387356061765 | 16.1706931247285 | Improved |
| Function 6 | -1.2283806967341901 | -0.7268715077444687 | 0.5015091889897214 | Improved |
| Function 7 | 1.285160161342515 | 1.3579108517237013 | 0.0727506903811863 | Improved |
| Function 8 | 9.4646525 | 9.58024 | 0.1155875 | Improved |

The broad improvement matters because the selected actions were not uniform. Function 5 benefited from a controlled movement towards the upper boundary, Functions 4 and 6 benefited from recovery towards previously stronger regions, and Functions 2, 3 and 7 improved through smaller local adjustments. Functions 1 and 8 demonstrated the value of recovering confirmed historical points rather than assuming the latest local neighbourhood was always preferable.

The rank order remained unchanged, but the underlying evidence strengthened. Function 5 extended its lead, Function 8 regained its best verified value, and Function 7 moved closer to its strongest earlier result. Function 2 reached its best observed output in the recorded history. Although Functions 3, 4 and 6 remained negative, each moved in a favourable direction.

## 4. Query Selection Strategy

The Week 11 query set was produced by treating each function according to its own evidence rather than applying one optimiser or one step size across the portfolio.

Function 1 used the confirmed input **0.600000,0.600000**, which had previously produced the strongest verified value for that objective. The Week 11 result reproduced **0.025559285339829783** exactly and confirmed that the narrow positive response was recoverable.

Function 2 used a local trust region probe around the productive region identified in Week 10. The output increased to **0.5848554940277205**, supporting the local direction while leaving open the question of how wide the productive neighbourhood may be.

Function 3 used a local refinement based on the stronger earlier region. The output improved to **-0.06542982421105416**. It remained negative, but the change supplied useful directional evidence.

Function 4 used a recovery probe after the substantial Week 10 deterioration. The move increased the output by **8.614789667334044**, demonstrating that a clear change of region was preferable to continuing the failed Week 10 direction.

Function 5 used a deliberately small boundary directed probe. The first coordinate moved from **0.120000** to **0.110000**, while the remaining coordinates moved closer to their upper bounds. The resulting value of **4411.0387356061765** established a new verified best.

Function 6 returned towards the strongest known basin and improved by **0.5015091889897214**. Function 7 used tight trust region refinement and improved by **0.0727506903811863**. Function 8 reused the confirmed best input and returned to **9.58024**.

## 5. Exploration vs Exploitation Analysis

Week 11 used a selective balance between exploitation, refinement, recovery and controlled probing.

- **Confirmed exploitation:** Functions 1 and 8 returned to previously verified best points.
- **Local refinement:** Functions 2, 3 and 7 used limited movements around regions supported by recent evidence.
- **Recovery:** Functions 4 and 6 moved away from unproductive Week 10 directions and towards stronger historical basins.
- **Controlled boundary probing:** Function 5 tested a small movement near the edge of the search space.

This allocation was more precise than a simple exploration versus exploitation split. Recovery was not equivalent to broad exploration because it used known historical evidence. The Function 5 probe was not unrestricted exploitation because it tested a new point near, but not identical to, the established best region. The local refinements also differed in purpose, with Function 2 probing a productive positive region, Function 3 seeking a less negative response, and Function 7 refining an already positive basin.

The round therefore used the available query budget to answer different questions for different functions. Some queries tested reproducibility, some tested local direction, and others corrected movements that had performed poorly in Week 10.

## 6. Reflection on Week 12 Query Selection

The Week 11 results provide a strong evidence base for the next round, but no verified Week 12 input set is currently stored in the repository. Exact Week 12 coordinates are therefore not included here.

The evidence supports several principles for the next decision. Function 5 warrants careful treatment because the latest boundary directed movement produced a new best, but the response near the boundary has not been mapped densely enough to justify an unsupported larger step. Functions 2 and 7 have productive local regions that may support further controlled refinement. Function 8 has confirmed a repeatable best point, so any departure from that location should have a clear information objective.

Functions 4 and 6 improved through recovery, which suggests that continued work should remain anchored to the stronger historical basins rather than returning to the unsuccessful Week 10 directions. Function 3 improved but remains negative, so further movement should be assessed against both recent direction and the best earlier observations. Function 1 reproduced its narrow peak, confirming the point but not yet defining the surrounding surface.

A final Week 12 submission should only be recorded once its eight input vectors have been verified. The same rule applies to the returned outputs and any subsequent analysis files.

## 7. Functional Ranking Evolution

The Week 11 rank order remained the same as Week 10, although every output improved.

| Rank | Function | Week 11 output | Strategy |
| ---: | --- | ---: | --- |
| 1 | Function 5 | 4411.0387356061765 | Boundary directed probe |
| 2 | Function 8 | 9.58024 | Exploit confirmed best |
| 3 | Function 7 | 1.3579108517237013 | Tight trust region refinement |
| 4 | Function 2 | 0.5848554940277205 | Local trust region probe |
| 5 | Function 1 | 0.025559285339829783 | Exploit confirmed narrow peak |
| 6 | Function 3 | -0.06542982421105416 | Local refinement |
| 7 | Function 6 | -0.7268715077444687 | Best basin recovery |
| 8 | Function 4 | -4.868852987697114 | Local recovery probe |

Cross function ranking is descriptive because the objectives operate on different numerical scales. The more meaningful comparison is the change within each function over time. On that basis, Week 11 was uniformly favourable.

Function 5 continued to dominate the numerical ranking. Functions 8, 7, 2 and 1 were positive. Functions 3, 6 and 4 remained negative, but their improvements showed that rank alone would understate the value of the Week 11 recovery decisions.

## 8. High Performing Region Identification

The strongest verified Function 5 region is now represented by **0.110000,0.998000,0.999900,0.999900**, with an output of **4411.0387356061765**. The result extends the sequence of strong values observed as the second, third and fourth coordinates approached their upper limits. The first coordinate remains slightly away from zero, and the available history does not establish the precise shape of the local surface.

Function 8 has a confirmed high performing point at **0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000**, returning **9.58024**. Function 1 also has a repeatable positive point at **0.600000,0.600000**, although the surrounding region remains poorly characterised.

Function 7 strengthened its productive basin with **1.3579108517237013**, while Function 2 established a new best recorded value of **0.5848554940277205**. Function 3 identified a more favourable negative region at **-0.06542982421105416**. Functions 4 and 6 recovered substantially, but neither Week 11 point can yet be treated as an established optimum because stronger historical values exist for both functions.

## 9. Decision Matrix and Resource Allocation

The Week 11 evidence supports differentiated allocation of the remaining query budget.

| Function | Evidence from Week 11 | Decision basis | Priority |
| --- | --- | --- | --- |
| Function 1 | Confirmed narrow positive peak | Preserve the verified point and investigate only with a clear local objective | Medium |
| Function 2 | New best through a local probe | Continue controlled local assessment | High |
| Function 3 | Improved but remained negative | Refine cautiously using the full history | Medium |
| Function 4 | Large recovery after Week 10 decline | Keep attention on the recovered basin | High |
| Function 5 | New verified best near the boundary | Protect the gain and test only defensible small movements | High |
| Function 6 | Strong recovery towards the best basin | Continue evidence led basin assessment | Medium |
| Function 7 | Improved within a productive region | Use conservative trust region refinement | Medium |
| Function 8 | Reproduced the confirmed best value | Preserve or test only for specific information gain | Medium |

The highest priorities are Function 5, because it remains the dominant source of portfolio performance, Function 2, because the local probe reached a new best, and Function 4, because the recovery move produced a large correction. The remaining functions still require attention, but their next actions should be proportionate to the evidence and the limited number of remaining rounds.

## 10. Information Gain Analysis

Week 11 delivered both performance gain and information gain. Functions 1 and 8 confirmed that their earlier best points were reproducible. This reduced uncertainty about whether those values were isolated recording anomalies or stable responses at the submitted coordinates.

Functions 4 and 6 demonstrated that recovery towards stronger historical regions could reverse the Week 10 declines. Their outputs remained below their best recorded values, so the new observations do not complete the search, but they rule against simply extending the Week 10 movement.

Functions 2, 3 and 7 supplied local directional evidence. Each improved after a targeted adjustment, although one observation does not define the wider neighbourhood. Function 5 provided the most important combined result. The new boundary directed point improved the objective while also showing that the Week 09 and Week 10 plateau was not the final verified limit of the observed region.

The round also highlighted the value of retaining the complete history. Several successful Week 11 decisions depended on earlier strong observations rather than only the immediately preceding result.

## 11. Computational Analysis and Coding Implementation

The Week 11 computational workflow uses two Python scripts.

`week_11_analysis.py` validates the dimensions and bounds of the input vectors, reads the Week 10 and Week 11 results, calculates exact changes with `Decimal`, ranks the functions and exports `week_11_analysis_summary.csv`. It also checks for missing, unexpected or duplicate function rows.

`generate_week_11_figures.py` stores the verified historical outputs from Weeks 01 to 11 as exact strings, constructs the Week 10 to Week 11 comparison, exports `week_11_figure_data_summary.csv` and generates five analytical figures in the Week 11 folder. Decimal values are converted to floating point numbers only when required by Matplotlib. The stored CSV values remain unchanged.

The scripts follow the established flat structure and do not create a separate figures directory. This keeps the source data, analysis, summaries and generated visual outputs together.

## 12. Repository Files and Reproducibility

The Week 11 folder contains the following core files:

- `README.md`
- `week_11_inputs.csv`
- `week_11_results.csv`
- `week_11_analysis_summary.csv`
- `week_11_figure_data_summary.csv`
- `week_11_analysis.py`
- `generate_week_11_figures.py`

The analysis can be reproduced from the repository root with:

```bash
python Week_11/week_11_analysis.py
python Week_11/generate_week_11_figures.py
```

The analysis script requires `Week_10/week_10_results.csv` for the exact weekly comparison. The figure script uses the verified historical output series stored within the script and writes all generated files directly into `Week_11`.

The CSV source files remain authoritative. If a future correction is made to any verified input or output, both scripts should be rerun so that the analytical summaries and figures remain aligned with the source data.

## 13. Conclusion

Week 11 was the strongest uniformly improving round in the verified record. Every function produced a higher output than in Week 10. Function 5 reached a new verified best of **4411.0387356061765**, Functions 4 and 6 recovered substantially, and Functions 1 and 8 reproduced confirmed historical best values. Functions 2, 3 and 7 also improved through targeted local work.

The result supports a function specific strategy built from the complete optimisation history. It does not establish a global optimum or prove universal superiority over established optimisation methods. Its value lies in the transparent connection between observed evidence, selected action and returned result.

The next weekly folder should follow the same standard. It should be created only after both the submitted inputs and returned outputs have been verified, with every numerical value preserved exactly.

## 14. Automation Decision

The Week 11 folder uses a repeatable computational workflow while retaining manual verification as the controlling step. The scripts check structure, dimensions, bounds, exact changes, rankings and output files, but they do not infer missing observations.

This balance is important. Routine calculations and figure generation can be automated reliably once the source data are complete. Strategic interpretation still requires review of the full history, particularly where a recovery move, boundary probe or return to an earlier point may carry a different meaning from an ordinary local refinement.

Future weekly updates should retain the established seven core files and the flat folder structure. An incomplete week should not be finalised merely to maintain a timetable. Verified data remain the prerequisite for any committed weekly analysis.

## 15. References

Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. Nature, 585, 357-362.

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science and Engineering, 9(3), 90-95.

McKinney, W. (2010). Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference, 56-61.

Python Software Foundation. (2026). Python language reference, version 3.

Imperial BBO Capstone repository. Verified Week 10 and Week 11 input, output and experiment records.
