# Week_03

## Bayesian Black Box Optimisation Portfolio
### Week 03 Analysis

## Contents

1. Introduction
2. Week 3 Results
3. Comparison with Week 2
4. Query Selection Strategy
5. Exploration and Exploitation
6. Reflection on Week 4 Selection
7. Functional Ranking
8. Promising Regions
9. Decision Matrix
10. Information Gained
11. Computational Analysis
12. Repository Record
13. Conclusion
14. Automation Decision
15. References

## 1. Introduction

By Week 03, three rounds were available for comparison. I could now see that a good result in one round did not necessarily persist after the next move. That made the direction of change as important as the latest value itself.

## 2. Week 3 Results

| Function | Week 1 | Week 2 | Week 3 |
| --- | ---: | ---: | ---: |
| F1 | 0.000000 | 0.000000 | 0.025559 |
| F2 | 0.454942 | 0.412137 | 0.140988 |
| F3 | -0.101836 | -0.133256 | -0.127870 |
| F4 | -4.359875 | -23.120154 | -14.554029 |
| F5 | 1415.876000 | 2308.149000 | 2840.990000 |
| F6 | -0.700155 | -2.070246 | -0.648848 |
| F7 | 1.319994 | 1.069658 | 0.896603 |
| F8 | 9.580240 | 9.524100 | 9.442960 |

F5 improved again and remained the clearest productive direction. F1 produced its first visible positive value. F6 recovered sharply from Week 2. F4 also recovered but remained poor. F2, F7 and F8 moved down, which made continued movement in the same direction less attractive.

## 3. Comparison with Week 2

The strongest gains were F6 and F4 in relative terms, although both remained negative. F5 gained another `532.841000`. F2 fell by `-0.271149`, F7 by `-0.173055` and F8 by `-0.081140`. Those declines mattered because they showed that previously positive regions could still be overshot.

## 4. Query Selection Strategy

I separated the functions according to what the latest movement had taught me. F5 justified continued exploitation. F1, F3, F4 and F6 still needed exploration. F2, F7 and F8 needed smaller, more cautious moves rather than automatic continuation.

## 5. Exploration and Exploitation

The balance was now asymmetric. More of the query budget could be spent protecting the F5 gain while the uncertain functions were used to search for a clearer signal. This was preferable to forcing all eight functions into the same exploration or exploitation rule.

## 6. Reflection on Week 4 Selection

The Week 3 results made me more cautious about assuming that a local trend would continue. The next round therefore needed to test whether the F5 improvement could be extended while changing direction where the recent move had weakened performance.

## 7. Functional Ranking

The Week 3 ranking was F5, F8, F7, F2, F1, F3, F6 and F4. The ranking helped organise attention, but the change from the previous week remained the more useful guide for deciding how far to move.

## 8. Promising Regions

F5 was the only function showing a strong repeated upward trend. F8 remained high on its own scale despite a small decline. F7 remained positive but was weakening. The remaining functions did not yet provide enough evidence to define a reliable local region.

## 9. Decision Matrix

| Function | Week 3 reading | Week 4 approach |
| --- | --- | --- |
| F1 | First visible positive response | Explore |
| F2 | Declined | Monitor and refine |
| F3 | Slight recovery but negative | Explore |
| F4 | Recovered but still weak | Explore |
| F5 | Third consecutive strong gain | Exploit |
| F6 | Strong recovery but negative | Explore |
| F7 | Positive but declining | Monitor and refine |
| F8 | High but slightly declining | Cautious refinement |

## 10. Information Gained

The main gain in Week 3 was learning where not to continue mechanically. The declines in F2, F7 and F8 were useful warnings. The recovery in F6 showed that changing direction could be worthwhile even before the output became positive.

## 11. Computational Analysis

The stored analysis summary records the Week 1 to Week 3 values, weekly changes, ranking and proposed Week 4 strategy. It provides a reproducible numerical check on the narrative above.

## 12. Repository Record

Supporting files include `week3_analysis.py` and `week3_analysis_summary.csv`. The summary values are retained as recorded for this round.

## 13. Conclusion

Week 3 strengthened the case for treating each function separately. F5 continued to reward exploitation, while several other functions showed that local movement could easily reverse a previous gain. That shaped a more cautious Week 4 strategy.

## 14. Automation Decision

The calculations were used to compare rounds and organise the evidence. Query selection remained manually supervised rather than being delegated to an automated optimiser.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.
