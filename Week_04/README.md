# Week_04

## Bayesian Black Box Optimisation Portfolio
### Week 04 Analysis

## Contents

1. Introduction
2. Week 4 Results
3. Comparison with Week 3
4. Query Selection Strategy
5. Exploration and Exploitation
6. Reflection on Week 5 Selection
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

Week 04 tested whether the directions suggested by the first three rounds would hold after another set of deliberate moves. I was particularly interested in whether F5 could continue improving and whether the weaker functions would respond to larger changes in position.

## 2. Week 4 Results

| Function | Week 4 output |
| --- | ---: |
| F1 | 0.00000014754580129542488 |
| F2 | 0.5228458934672892 |
| F3 | -0.06037987403160633 |
| F4 | -22.55187651826871 |
| F5 | 3238.333368768757 |
| F6 | -0.8733671274789931 |
| F7 | 1.1968303712356705 |
| F8 | 9.539439999999999 |

F5 improved again. F2 recovered strongly from Week 3, F3 moved closer to zero and F8 recovered above its Week 3 value. F4 deteriorated again, while F6 remained negative. F1 returned to a value extremely close to zero.

## 3. Comparison with Week 3

The round confirmed that the same type of movement did not work equally well across functions. F2 and F3 benefited from their Week 4 changes, whereas F4 did not. F5 continued its upward progression, which made it increasingly reasonable to keep its next query close to the current region.

## 4. Query Selection Strategy

The submitted vectors are preserved in `week_04_inputs.csv`. They included a tight boundary oriented move for F5 and more substantial changes for functions where the previous evidence was weaker. The choices were based on the observed history rather than a single common step size.

## 5. Exploration and Exploitation

F5 remained the main exploitation target. F2, F7 and F8 had positive outputs and could be refined with care. F1, F3, F4 and F6 still needed more information, although F3's improvement suggested that its current direction deserved attention.

## 6. Reflection on Week 5 Selection

The Week 4 response made two points clear. First, protecting the F5 region was working. Second, F4 could not be treated as though every move towards a new area would automatically improve it. Week 5 therefore needed to preserve the strong functions while accepting that the difficult functions might require several changes of direction.

## 7. Functional Ranking

F5 remained first by a wide margin, followed by F8, F7 and F2. F1 was numerically close to zero. F3, F6 and F4 remained negative. The ranking was useful for orientation, but the week to week movement remained central to the next decision.

## 8. Promising Regions

The strongest evidence remained around F5. F8 also showed a stable positive region, while F7 remained positive despite some variation. F2's recovery restored confidence in local refinement. The remaining functions were still too inconsistent to label as settled regions.

## 9. Decision Matrix

| Function | Week 4 reading | Next action |
| --- | --- | --- |
| F1 | Near zero again | Explore |
| F2 | Strong recovery | Refine |
| F3 | Improved but negative | Refine cautiously |
| F4 | Deteriorated | Change direction |
| F5 | Continued strong improvement | Exploit |
| F6 | Negative | Explore |
| F7 | Positive | Refine |
| F8 | Stable positive | Refine cautiously |

## 10. Information Gained

F4 supplied useful negative evidence because the latest move did not support the direction tested. F2 provided the opposite result by showing that a previous decline could be recovered. Together these results reduced the value of using simple momentum as a decision rule.

## 11. Computational Analysis

`week_04_analysis.py` and `week_04_analysis_summary.csv` support the numerical comparison. The raw submitted vectors and returned outputs remain separate in `week_04_inputs.csv` and `week_04_results.csv`.

## 12. Repository Record

The Week 4 folder preserves the source inputs, returned results and derived analysis. The source CSV files are the numerical reference for this round.

## 13. Conclusion

Week 4 strengthened the F5 exploitation case but also showed why the weaker functions needed independent treatment. The mixed response was useful because it narrowed the directions worth pursuing in Week 5.

## 14. Automation Decision

Code was used to check and summarise the observations. The final interpretation and next query choices remained manually supervised.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.