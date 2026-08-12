# Week_08

## Bayesian Black Box Optimisation Portfolio
### Week 08 Analysis

## 1. Introduction

Week 08 gave me a clearer split between functions that were responding to local refinement and functions that still needed a change of direction. F5 improved again, F2 recovered strongly and F7 also moved up. F3 and F4 moved backwards, while F6 was almost unchanged. That mixture was more useful than a simple statement that the round had improved overall.

## 2. Week 08 Results

| Function | Week 08 output |
| --- | ---: |
| F1 | -1.4546199699251391e-58 |
| F2 | 0.5672775862793291 |
| F3 | -0.0991107637427902 |
| F4 | -12.305008897187289 |
| F5 | 4359.384134322703 |
| F6 | -1.1197178425911847 |
| F7 | 1.3346391663186332 |
| F8 | 9.47621 |

F5 increased from the Week 07 value of `4278.816638`. F2 recovered from `0.239929` to `0.5672775862793291`. F7 also improved from `1.154336` to `1.3346391663186332`. F8 remained positive but declined slightly. F3 and F4 deteriorated, while F6 changed very little.

## 3. Comparison with Week 07

The F2 recovery was particularly useful because it showed that the Week 07 decline had not destroyed the productive region. F7's increase supported continued local refinement. F3 and F4, however, did not maintain their Week 07 recoveries, which weakened the case for continuing those movements without adjustment.

## 4. Query Selection Strategy

The next round needed to keep F5 close to its leading region while avoiding unnecessary movement in F8. F2 and F7 had earned another controlled refinement. F3 and F4 required reassessment because their latest moves reversed some of the previous gain. F1 remained unresolved.

## 5. Exploration and Exploitation

F5 remained the clearest exploitation target. F2, F7 and F8 were refinement candidates. F3, F4 and F6 required more cautious investigation, and F1 still needed exploration because repeated near zero values had not revealed a useful direction.

## 6. Reflection on Week 09 Query Selection

Week 08 made me more interested in stability as well as peak value. F5 had both a high value and a sustained upward trajectory. F8 had a stable positive region but little reason for a large move. F3 and F4 showed why a single recovery should not be treated as proof of a settled direction.

## 7. Functional Ranking

The broad ordering remained F5, F8, F7 and F2 at the top, followed by F1 near zero and the negative functions. The more important change was within that ordering: F2 and F7 strengthened, while F3 and F4 lost ground.

## 8. High Performing Regions

F5 remained the strongest identified region. F8 continued to show stability on its own scale. F7 strengthened its positive region and F2 recovered into a stronger local area. No equivalent stable region had yet been established for F1, F3, F4 or F6.

## 9. Decision Matrix

| Function | Week 08 reading | Week 09 approach |
| --- | --- | --- |
| F1 | Effectively zero | Explore |
| F2 | Strong recovery | Refine |
| F3 | Small deterioration | Reassess |
| F4 | Deteriorated after recovery | Reassess |
| F5 | Continued gain | Exploit |
| F6 | Almost unchanged and negative | Explore selectively |
| F7 | Improved | Refine |
| F8 | Small decline in stable positive region | Refine cautiously |

## 10. Information Gained

Week 08 separated repeatable progress from temporary recovery. F2 recovered after a poor Week 07 result, whereas F3 and F4 failed to continue their recoveries. This made the recent trajectory and the size of each change more useful than a fixed label applied for several rounds.

## 11. Computational Analysis

`week_08_analysis.py` and `generate_week_08_figures.py` support the numerical analysis and visualisation. Derived summaries are kept separate from the source inputs and outputs.

## 12. Repository Files and Reproducibility

The Week 08 folder contains the source CSV files, analysis code, figure generation code, dataset record and datasheet. `week_08_results.csv` is the numerical reference for the outputs shown above.

## 13. Conclusion

Week 08 strengthened F5, F2 and F7 but weakened the case for continuing the same F3 and F4 directions. The result supported a more selective Week 09 strategy rather than a uniform move across all functions.

## 14. Automation Decision

Computational tools were used to organise and check the observations. The final query choices remained manually supervised.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.