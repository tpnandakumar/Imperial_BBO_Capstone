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


## 4. Query Selection Strategy

The Week 06 query selection strategy was guided by evidence accumulated from the previous optimisation rounds. With six optimisation cycles completed, sufficient information had been collected to distinguish between functions that required continued exploitation, local refinement or broader exploration. This evidence based approach improved allocation of the limited query budget while increasing confidence in subsequent optimisation decisions.

Function 5 remained the highest priority for exploitation because it continued to produce the strongest objective values throughout the optimisation process. The increase from 3682.211062 in Week 05 to 3922.765223 in Week 06 confirmed that the selected search region remained highly productive. Consequently, only small local adjustments were considered to maximise further performance while remaining close to the established optimum.

Function 2 demonstrated substantial improvement during Week 06, suggesting that the surrounding search region contained additional optimisation potential. Functions 7 and 8 continued to produce stable positive outputs and therefore remained suitable candidates for local refinement. Maintaining queries close to these regions increased the likelihood of obtaining incremental improvements while confirming the consistency of previous observations.

In contrast, Functions 1, 3, 4 and 6 continued to demonstrate greater uncertainty. Function 1 remained close to zero, while Functions 3, 4 and 6 continued to produce negative objective values. These observations indicated that the corresponding search regions had not yet converged towards favourable solutions. Continued exploratory sampling therefore remained the most appropriate strategy for these functions.

Overall, the Week 06 query selection strategy reflected a balanced optimisation framework that allocated computational resources according to observed performance, confidence and expected information gain. This evidence based allocation supported continued improvement while maintaining an appropriate balance between exploitation of productive regions and exploration of uncertain areas.

**Figure 2. Week 06 Query Selection Strategy**

<img width="1536" height="1024" alt="Figure 2  Week 06 Query Selection Strategy" src="https://github.com/user-attachments/assets/8c99dc13-7568-46fe-9063-2ef583ee607f" />


## 5. Exploration vs Exploitation Analysis

A successful Bayesian Black Box Optimisation strategy requires an appropriate balance between exploration and exploitation. Exploration focuses on sampling uncertain regions of the search space to identify previously undiscovered high performing solutions, whereas exploitation concentrates on refining known productive regions to maximise objective values. Maintaining this balance remained a key objective throughout the Week 06 optimisation process.

The Week 06 results demonstrated that Function 5 continued to outperform all other functions, increasing from 3682.211062 to 3922.765223. This sustained improvement provided strong evidence that the surrounding search region remained highly productive. Consequently, Function 5 continued to receive the highest exploitation priority through small local adjustments designed to maximise further performance while remaining close to the identified optimum.

Function 2 demonstrated the greatest improvement among the remaining positive functions, increasing from 0.280168 to 0.571248. Functions 7 and 8 continued to demonstrate stable positive behaviour and therefore remained suitable candidates for local refinement. Maintaining search activity within these regions increased confidence while providing opportunities for incremental optimisation gains.

Conversely, Functions 1, 3, 4 and 6 continued to exhibit greater uncertainty. Function 1 remained close to zero, while Functions 3, 4 and 6 produced negative objective values throughout Week 06. These observations indicated that the current query locations had not yet identified favourable regions of the search landscape. Continued exploratory sampling therefore remained the most appropriate strategy for these functions.

Overall, Week 06 demonstrated that optimisation performance improves when computational resources are allocated according to observed evidence rather than uniformly across all functions. Exploiting productive regions while continuing to explore uncertain areas increased both optimisation performance and understanding of the hidden objective functions.

**Figure 3. Exploration vs Exploitation Analysis**

<img width="1536" height="1024" alt="Figure 3  Exploration vs Exploitation Analysis" src="https://github.com/user-attachments/assets/da215e8b-c1da-4232-a270-250410c66fda" />

Week 06 Strategy

Explore:
F1, F3, F4, F6

Refine:
F2, F7, F8

Exploit:
F5

Goal:
Maximise optimisation performance while increasing information gain.



## 6. Reflection on Week 7 Query Selection

The Week 06 query selection process was guided by evidence accumulated throughout six optimisation rounds. Rather than selecting query locations randomly, each decision was supported by observed objective values, functional rankings and confidence assessments derived from previous optimisation results. This evidence based approach increased confidence in allocating computational resources towards functions most likely to improve optimisation performance.

Function 5 remained the strongest candidate for continued exploitation. The increase from 3682.211062 in Week 05 to 3922.765223 in Week 06 demonstrated that the selected search region continued to generate higher objective values. This consistent upward trend justified maintaining local refinement around the current optimum while avoiding unnecessary movement into less productive regions.

Function 2 demonstrated the largest positive improvement among the remaining positive functions. This substantial increase suggested that the surrounding search region retained further optimisation potential. Functions 7 and 8 continued to produce stable objective values, supporting continued local refinement to improve performance while confirming the reliability of previously identified productive regions.

Functions 1, 3, 4 and 6 remained associated with greater uncertainty. Function 1 continued to produce values close to zero, while Functions 3, 4 and 6 remained negative throughout Week 06. These observations suggested that additional exploratory sampling remained necessary to improve understanding of these regions and reduce uncertainty within the hidden search landscape.

Overall, the Week 06 analysis strengthened confidence in the strategy selected for Week 07. Evidence accumulated throughout successive optimisation rounds supported continued exploitation of the highest performing function, selective refinement of stable regions and targeted exploration of uncertain areas. This balanced strategy aimed to maximise information gain while maintaining steady optimisation progress.

**Figure 4. Reflection on Week 7 Query Selection**

<img width="1536" height="1024" alt="Figure 4  Reflection on Week 7 Query Selection" src="https://github.com/user-attachments/assets/9e961372-f275-4ab5-9649-e90165b9c4f2" />




Week 07 Strategy

Exploit:
F5

Refine:
F2, F7, F8

Explore:
F1, F3, F4, F6

Objective:
Improve optimisation performance while maximising information gain.



## 7. Functional Ranking Evolution

Ranking the objective functions after six optimisation rounds provided a comprehensive measure of optimisation progress and revealed how the relative performance of the eight unknown objective functions changed as additional evidence became available. Monitoring ranking stability assisted in identifying functions suitable for continued exploitation, local refinement or broader exploration.

Function 5 retained the highest ranking throughout Week 06. The objective value increased from 3682.211062 in Week 05 to 3922.765223 in Week 06, reinforcing confidence that the optimisation process had identified a productive search region. This sustained improvement justified continued exploitation through carefully controlled local refinement.

Function 8 remained the second highest ranked function with a stable objective value of 9.514800. Although only a small improvement was observed, the consistency of its performance indicated that the surrounding search region remained reliable and suitable for continued refinement. Function 7 maintained third position despite a slight reduction in objective value, demonstrating continued positive performance across successive optimisation rounds.

Function 2 moved closer to the leading functions following a substantial increase from 0.280168 to 0.571248. This improvement suggested that additional optimisation opportunities remained within the current search region and justified continued refinement during subsequent optimisation rounds.

Functions 1, 3, 4 and 6 continued to occupy the lower rankings. Function 1 remained close to zero, while Functions 3, 4 and 6 continued to produce negative objective values. These functions remained priorities for exploratory sampling because additional evidence was required to improve understanding of their hidden response surfaces.

Overall, the Week 06 functional rankings demonstrated increasing separation between consistently productive regions and uncertain regions of the search space. The ranking evolution provided an objective framework for allocating optimisation resources while balancing exploitation, refinement and exploration.

**Figure 5. Functional Ranking Evolution**

<img width="1536" height="1024" alt="Figure 5  Functional Ranking Evolution" src="https://github.com/user-attachments/assets/24d24661-8fd7-43d6-b1df-efac72ecde0d" />


Week 06 Functional Ranking

Exploit:
F5

Refine:
F2, F7, F8

Explore:
F1, F3, F4, F6

Ranking stability increased confidence in optimisation decisions while identifying functions requiring continued exploration.


## 8. High Performing Region Identification

Identifying high performing regions remained one of the primary objectives of the Bayesian Black Box Optimisation process. After six optimisation rounds, sufficient evidence had been accumulated to distinguish between productive search regions that consistently generated strong objective values and uncertain regions requiring further investigation. This information provided the foundation for efficient allocation of future query resources.

Function 5 continued to represent the strongest high performing region within the search landscape. The objective value increased from 3682.211062 in Week 05 to 3922.765223 in Week 06, confirming that the selected query region remained highly productive. The sustained improvement observed across multiple optimisation rounds indicated that local refinement continued to be the most appropriate strategy for maximising objective values.

Functions 2, 7 and 8 also demonstrated favourable optimisation behaviour. Function 2 showed substantial improvement during Week 06, while Functions 7 and 8 continued to produce stable positive objective values. These observations suggested that the surrounding search regions remained reliable and suitable for continued local refinement to achieve incremental performance improvements.

Conversely, Functions 1, 3, 4 and 6 continued to exhibit limited optimisation success. Function 1 remained close to zero, while Functions 3, 4 and 6 continued to generate negative objective values. These functions remained associated with uncertain search regions where broader exploration was required to improve understanding of the hidden objective functions.

Overall, the identification of high performing regions provided an evidence based framework for guiding future optimisation decisions. Concentrating computational effort around productive regions while continuing to investigate uncertain areas improved optimisation efficiency and maximised information gained from the available query budget.

**Figure 6. High Performing Region Identification**

<img width="1536" height="1024" alt="Figure 6  High Performing Region Identification" src="https://github.com/user-attachments/assets/307d4b75-4d1f-4fd6-a36b-9444b173cfaf" />


Week 06 High Performing Regions

Exploit:
F5

Refine:
F2, F7, F8

Explore:
F1, F3, F4, F6

High performing regions became increasingly well defined after six optimisation rounds, supporting evidence based query selection.


## 9. Decision Matrix and Resource Allocation

The allocation of query resources during Week 06 was determined by objective performance, confidence assessment and expected information gain. After six optimisation rounds, sufficient evidence had been collected to distinguish between functions requiring continued exploitation, local refinement or broader exploration. This evidence based allocation improved the efficiency of the limited query budget while supporting continued optimisation progress.

Function 5 remained the highest priority for exploitation because it consistently produced the strongest objective values. The increase from 3682.211062 in Week 05 to 3922.765223 in Week 06 confirmed that the current search region continued to provide the greatest optimisation potential. Query allocation therefore focused on small local adjustments designed to maximise further performance while preserving convergence within this productive region.

Functions 2, 7 and 8 were assigned medium priority for local refinement. Function 2 demonstrated substantial improvement during Week 06, while Functions 7 and 8 maintained stable positive objective values. These functions represented reliable search regions where incremental optimisation could be achieved through carefully controlled refinement rather than broad exploration.

Functions 1, 3, 4 and 6 remained associated with greater uncertainty. Function 1 continued to produce objective values close to zero, while Functions 3, 4 and 6 remained negative throughout Week 06. These observations indicated that the current search locations had not yet identified favourable regions, making continued exploratory sampling the most appropriate allocation strategy.

Overall, the Week 06 decision matrix demonstrated that effective optimisation depends upon allocating computational resources according to observed evidence rather than distributing queries equally across all functions. This structured allocation maximised expected information gain while maintaining an effective balance between exploitation, refinement and exploration.

**Figure 7. Decision Matrix and Resource Allocation**

<img width="1536" height="1024" alt="Figure 7  Decision Matrix and Resource Allocation" src="https://github.com/user-attachments/assets/85e6b87c-ece3-49f1-9317-98c1ace5ea66" />

Week 06 Resource Allocation

High Priority:
F5

Medium Priority:
F2, F7, F8

Exploration Priority:
F1, F3, F4, F6

Objective:
Allocate computational effort according to observed performance, confidence and expected information gain.


## 10. Information Gain Analysis

Information gain remained a key objective throughout the Week 06 optimisation process because every query contributed additional knowledge about the hidden objective functions. Rather than evaluating optimisation progress solely through objective values, Week 06 also considered how each query reduced uncertainty and improved understanding of the underlying search landscape. This evidence supported more effective query selection and increased confidence in subsequent optimisation decisions.

Function 5 continued to provide the greatest information gain by consistently producing higher objective values within the same productive search region. The increase from 3682.211062 in Week 05 to 3922.765223 in Week 06 confirmed that the surrounding landscape remained favourable for continued local refinement. This strengthened confidence in exploiting the current optimum while reducing uncertainty regarding the behaviour of this region.

Function 2 produced one of the largest improvements during Week 06 and therefore generated valuable additional information regarding a previously developing search region. Functions 7 and 8 continued to demonstrate stable positive behaviour, confirming that these regions remained reliable and suitable for incremental optimisation through local refinement.

Conversely, Functions 1, 3, 4 and 6 continued to provide valuable information despite producing limited objective improvements. Continued exploration of these functions reduced uncertainty surrounding poorly understood regions of the search landscape and increased the probability of identifying alternative productive areas during future optimisation rounds.

Overall, the Week 06 information gain analysis demonstrated that optimisation success depends upon both improving objective values and reducing uncertainty across the hidden search landscape. Combining exploitation, refinement and exploration produced a balanced optimisation strategy that maximised knowledge while supporting continued performance improvement.

**Figure 8. Information Gain Analysis**

<img width="1536" height="1024" alt="Figure 8  Information Gain Analysis" src="https://github.com/user-attachments/assets/06f51a8a-9ca3-4c77-a65f-181adf02f723" />


Week 06 Information Gain

Highest Learning:
F5

Increasing Confidence:
F2, F7, F8

Reducing Uncertainty:
F1, F3, F4, F6

Objective:
Maximise knowledge while improving optimisation performance.









