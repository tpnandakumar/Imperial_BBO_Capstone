# Week_06

## Bayesian Black Box Optimisation Portfolio
### Week 06 Analysis

## Contents

1. Introduction
2. Week 6 Results
3. Comparison of Week 5 and Week 6 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 7 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. References

## 1. Introduction

Week 06 represented another important stage in the Bayesian Black Box Optimisation (BBO) challenge. By this point, six optimisation rounds had been completed, providing a richer collection of observations from which to evaluate the behaviour of the eight unknown objective functions. The additional data enabled more informed decision making, improved confidence in query selection and a clearer understanding of the underlying search landscape.

The optimisation strategy continued to balance exploration of uncertain regions with exploitation of previously identified high performing areas. Rather than relying on intuition, query selection was guided by evidence accumulated across successive optimisation rounds. This progressive approach allowed confidence to increase as additional observations reduced uncertainty surrounding the hidden objective functions.

The Week 06 results also provided an opportunity to compare performance with Week 05 and evaluate whether previous optimisation decisions had continued to improve objective values. Particular attention was given to identifying functions demonstrating sustained improvement, stable behaviour or persistent uncertainty. These observations informed the allocation of future query resources and supported preparation for the Week 07 optimisation round.

This repository documents the complete Week 06 optimisation workflow, including performance analysis, comparison with previous weeks, query selection strategy, exploration versus exploitation analysis, functional ranking, computational implementation and repository organisation. Together, these analyses provide a transparent and reproducible record of the optimisation process while supporting continued refinement of the Bayesian optimisation strategy.


## 2. Week 6 Results

Week 06 provided further evidence regarding the behaviour of the eight unknown objective functions. The additional optimisation round expanded the available dataset and strengthened understanding of the hidden search landscape. While some functions demonstrated continued improvement, others remained stable or exhibited greater uncertainty, providing valuable guidance for future query selection.

Function 5 continued to produce the highest objective value, increasing from 3682.211062 in Week 05 to 3922.765223 in Week 06. This consistent improvement reinforced confidence that the optimisation strategy had identified a productive search region suitable for continued exploitation. Function 2 also demonstrated a notable increase, improving from 0.280168 to 0.571248, indicating that further refinement of this region may be beneficial.

Function 8 remained highly stable with a slight increase from 9.511300 to 9.514800, while Function 7 maintained positive performance despite a small reduction from 1.380930 to 1.352949. These results suggested that both functions occupied relatively stable regions of the search space where local refinement continued to be appropriate.

Conversely, Functions 3, 4 and 6 remained negative. Function 4 produced the lowest objective value at -31.203478, confirming that the current search region continued to provide limited optimisation benefit. These functions therefore remained priorities for continued exploration during the next optimisation round.

Overall, the Week 06 results demonstrated continued progress in understanding the hidden objective functions. The evidence obtained from this optimisation round strengthened confidence in exploiting high performing regions while supporting continued exploration of uncertain areas to maximise future optimisation performance.

| Function | Week 06 Output | Interpretation |
|----------|---------------:|----------------|
| Function 1 | 0.000000003 | Near zero with minimal improvement |
| Function 2 | 0.571248 | Strong positive improvement |
| Function 3 | -0.307182 | Negative response requiring continued exploration |
| Function 4 | -31.203478 | Lowest output indicating persistent uncertainty |
| Function 5 | 3922.765223 | Highest performing function supporting continued exploitation |
| Function 6 | -1.379227 | Negative response requiring additional exploration |
| Function 7 | 1.352949 | Stable positive performance |
| Function 8 | 9.514800 | Stable high performance |

**Figure 1A. Function Output Evolution (Weeks 1 to 6)**

<img width="1536" height="1024" alt="Figure 1A  Function Output Evolution (Weeks 1 to 6)" src="https://github.com/user-attachments/assets/e67c8132-0b96-46f0-86e2-4562203228ca" />


## 3. Comparison of Week 5 and Week 6 Performance

A comparison between the Week 05 and Week 06 results demonstrated that the optimisation strategy continued to improve understanding of the hidden search landscape while identifying functions suitable for continued exploitation. The most significant improvement was observed in Function 5, which increased from 3682.211062 in Week 05 to 3922.765223 in Week 06. This sustained upward trend provided further evidence that the selected query region contained a highly productive optimum.

Function 2 also demonstrated substantial improvement, increasing from 0.280168 to 0.571248. This represented the largest relative improvement among the lower performing positive functions and suggested that additional refinement of the surrounding search region may continue to generate higher objective values.

Function 8 remained remarkably stable, increasing slightly from 9.511300 to 9.514800. Function 7 maintained a positive output despite a small reduction from 1.380930 to 1.352949. The stability of these functions indicated that the optimisation process had successfully identified productive regions requiring only minor local adjustments.

Conversely, Functions 3, 4 and 6 remained negative throughout Week 06. Function 4 continued to produce the lowest objective value at -31.203478, while Function 3 decreased further into negative territory. These observations suggested that the corresponding search regions remained poorly understood and continued to require exploratory sampling.

Overall, the Week 06 comparison demonstrated increasing confidence in the optimisation strategy. The results supported continued exploitation of Function 5, selective refinement of Functions 2, 7 and 8, and continued exploration of Functions 1, 3, 4 and 6 to maximise information gain and improve future optimisation performance.

**Figure 1B.1. Comparison of Week 5 and Week 6 Performance**

<img width="1536" height="1024" alt="Figure 1B 1  Comparison of Week 5 and Week 6 Performance" src="https://github.com/user-attachments/assets/e19ca9fe-0802-402d-841d-c16d2b0378cc" />








