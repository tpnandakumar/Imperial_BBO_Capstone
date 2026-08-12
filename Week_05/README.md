# Week_05

## Bayesian Black Box Optimisation Portfolio
### Week 05 Analysis

## 1. Introduction

Week 05 produced a useful contrast between a very strong F5 result and several functions that moved in the wrong direction. That contrast mattered more than the overall ranking because it showed where local refinement was earning its query cost and where it was not.

## 2. Week 5 Results

| Function | Week 5 output |
| --- | ---: |
| F1 | 0.012779642669914939 |
| F2 | 0.28016822307722516 |
| F3 | -0.11392206377710448 |
| F4 | -27.44051496086922 |
| F5 | 3682.2110623386798 |
| F6 | -1.073875453695542 |
| F7 | 1.3809299933612855 |
| F8 | 9.5113 |

F5 rose substantially again. F7 also improved and F1 produced a measurable positive result. F2, F3, F4, F6 and F8 were lower than in Week 4, although F8 remained within a narrow positive range.

## 3. Comparison with Week 4

F5 increased from `3238.333368768757` to `3682.2110623386798`, reinforcing the decision to remain close to that region. F7 improved from `1.1968303712356705` to `1.3809299933612855`. F2 lost much of its Week 4 recovery and F4 deteriorated further. The mixed outcome argued against assuming that one successful local move would persist.

## 4. Query Selection Strategy

The next strategy needed to protect the clear F5 gain while reducing commitment to directions that had just weakened. F7 could continue with local refinement. F8 remained stable enough for cautious movement. F2 required reassessment rather than another automatic step in the same direction.

## 5. Exploration and Exploitation

Exploitation was concentrated on F5 because it had repeated evidence of improvement. F7 and F8 justified refinement, but not the same level of commitment. F1, F3, F4 and F6 still needed broader investigation.

## 6. Reflection on Week 6 Selection

The Week 5 results made me more selective about where to spend a small query budget. A strong trajectory such as F5 deserved another local test. A deterioration such as F4's was a reason to change direction rather than defend the previous choice.

## 7. Functional Ranking

F5 remained the dominant result, followed by F8, F7, F2 and F1. F3, F6 and F4 remained negative. Because the scales differ greatly between functions, I used this ranking mainly to organise the portfolio rather than to compare absolute difficulty.

## 8. Promising Regions

F5 had the clearest high performing region. F7 had recovered to a stronger positive value, while F8 remained consistently high on its own scale. F2 was positive but unstable. The negative functions had not yet shown enough consistency to justify a narrow search.

## 9. Decision Matrix

| Function | Week 5 reading | Week 6 approach |
| --- | --- | --- |
| F1 | Positive but small | Explore |
| F2 | Fell after Week 4 recovery | Reassess and refine |
| F3 | Negative and lower | Explore |
| F4 | Further deterioration | Change direction |
| F5 | Strong continued gain | Exploit |
| F6 | Negative and lower | Explore |
| F7 | Improved positive result | Refine |
| F8 | Small decline in stable region | Refine cautiously |

## 10. Information Gained

F2 showed that a recovery could be temporary, while F4 showed that repeated movement in an unproductive region could consume queries without reward. These results pushed the strategy towards more explicit reassessment after deterioration.

## 11. Computational Analysis

`week_05_analysis.py` and `week_05_analysis_summary.csv` support the comparison and strategy summary. Source values are stored separately in `week_05_inputs.csv` and `week_05_results.csv`.

## 12. Repository Record

The Week 5 folder keeps source observations separate from derived interpretation, allowing the narrative to be checked against the submitted and returned values.

## 13. Conclusion

Week 5 strengthened the F5 direction while exposing instability elsewhere. The next round therefore needed careful exploitation where the evidence was strong and active reassessment where recent moves had failed.

## 14. Automation Decision

The analysis scripts organised the evidence and reduced arithmetic error. Final query selection remained manually supervised.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.