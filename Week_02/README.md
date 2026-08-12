# Week_02

## Bayesian Black Box Optimisation Portfolio
### Week 02 Analysis

## Contents

1. Introduction
2. Week 2 Results
3. Comparison with Week 1
4. Query Selection Strategy
5. Exploration and Exploitation
6. Reflection on Week 3 Selection
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

Week 02 was the first round in which I could use the response to my own submitted queries rather than relying only on the starter observations supplied by Imperial. That changed the decision process. I now had direct evidence of which first moves had helped and which had taken me into weaker regions.

My aim was not to apply one rule to all eight functions. I kept close to strong results where that seemed justified and moved further when the previous response gave little reason to stay.

## 2. Week 2 Results

The Week 1 outputs used to prepare this round were:

| Function | Week 1 output |
| --- | ---: |
| F1 | 0.000000 |
| F2 | 0.454942 |
| F3 | -0.101836 |
| F4 | -4.359875 |
| F5 | 1415.876394 |
| F6 | -0.700155 |
| F7 | 1.319994 |
| F8 | 9.580240 |

Week 2 showed that the functions were already behaving very differently. F5 offered the clearest reason to stay near a productive region. F8 and F7 were also positive. F3, F4 and F6 remained difficult, while F1 gave almost no useful separation from zero.

## 3. Comparison with Week 1

The main lesson from the comparison was that a strong result could justify a smaller move, but a weak result did not justify repeatedly sampling the same neighbourhood. F5 therefore moved towards exploitation, while the weaker functions retained a larger exploratory component.

## 4. Query Selection Strategy

I ranked the observed outputs, then considered the scale and direction of each function separately. Ranking was useful as a summary, but I did not treat it as a complete decision rule because the eight functions operate on very different numerical scales.

## 5. Exploration and Exploitation

F5 was the clearest exploitation candidate. F7 and F8 justified cautious local work because both were positive. F1, F3, F4 and F6 needed more exploration. F2 sat between these groups because its positive result was useful but not yet stable enough to assume that the surrounding region was consistently strong.

## 6. Reflection on Week 3 Selection

The Week 2 results made me less willing to move every function in the same way. For Week 3, I wanted to preserve the strong F5 direction while using the weaker functions to learn more about regions that had not yet produced useful outputs.

## 7. Functional Ranking

The ranking helped identify where the limited query budget was already producing a clear signal. It was most useful when read alongside the history of each function rather than as a direct comparison of raw magnitudes.

## 8. Promising Regions

F5 had the strongest evidence of a productive region. F8 and F7 also had positive areas worth retaining. At this stage I did not regard any of these as proven optima. They were simply the strongest regions observed so far.

## 9. Decision Matrix

| Function group | Week 2 interpretation | Next action |
| --- | --- | --- |
| F5 | Strongest response | Exploit carefully |
| F7, F8 | Positive response | Refine locally |
| F2 | Positive but less settled | Monitor and refine |
| F1, F3, F4, F6 | Weak or uninformative | Explore |

## 10. Information Gained

Week 2 was useful because it began separating the functions into different search problems. The value was not only in finding higher outputs. Poor responses also showed where another small move was unlikely to be informative.

## 11. Computational Analysis

Simple ranking and comparison code was used to organise the observations. The calculations supported the decision process, but the final query choices remained judgement based because the hidden functions and their gradients were unavailable.

## 12. Repository Record

This README records the reasoning used at the time. Numerical observations shown here are retained from the Week 2 record. Later rounds add more detailed CSV and reproducibility files as the repository structure develops.

## 13. Conclusion

Week 2 marked the move from an initial local search to a function specific strategy. F5 provided the strongest reason for exploitation, while the weaker functions still needed broader investigation. That distinction became the basis for the next round.

## 14. Automation Decision

No automated optimiser selected the Week 2 queries. Code was used to organise and compare the available observations, with the final choices made manually from the evidence available at that point.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.