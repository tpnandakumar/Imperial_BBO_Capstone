# Week_04

## Contents


1. Introduction
2. Week 4 Results
3. Comparison of Week 3 and Week 4 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 5 Query Selection
7. Functional Ranking Evolution
8. High-Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Conclusion


## Introduction

The Week 4 optimisation round built on the accumulated evidence from Weeks 1–3. By this stage, the search process had moved beyond broad exploratory sampling and had become increasingly evidence driven. Previous outputs had identified clear differences between functions, including strong exploitation candidates, stable positive performers, declining functions requiring monitoring, and uncertain low-output regions requiring further exploration.

The main objective of Week 4 was to use this evidence to select query points that balanced exploitation, monitoring and targeted exploration. Strong-performing functions were prioritised for local refinement, while unstable or poorly understood functions were assigned exploratory movements to improve understanding of the search landscape. This reflected the broader principle of Bayesian optimisation, where query selection should maximise both expected improvement and information gain.

## Week 4 Results

The Week 4 optimisation round produced mixed outcomes across the eight functions. Function 5 remained the strongest performer and achieved its highest value to date (3238.33), confirming that the exploitation strategy continued to identify highly productive regions of the search space. Functions 2 and 7 also demonstrated positive performance, while Function 8 remained a stable high-value performer despite a slight fluctuation from previous weeks.

Functions 3, 4 and 6 remained negative, indicating that these search regions continue to present challenges and require further investigation. Function 1 returned a value extremely close to zero, suggesting either a flat landscape or a region with very limited optimisation potential. Overall, the Week 4 results reinforced the distinction between strong exploitation candidates and functions requiring continued exploration.

Table 1. Week 4 Function Outputs

The Week 4 optimisation round produced mixed outcomes across the eight functions. Function 5 remained the strongest performer and achieved its highest value to date (3238.33), confirming that the exploitation strategy continued to identify highly productive regions of the search space. Functions 2 and 7 also demonstrated positive performance, while Function 8 remained a stable high-value performer despite a slight fluctuation from previous weeks.

Functions 3, 4 and 6 remained negative, indicating that these search regions continue to present challenges and require further investigation. Function 1 returned a value extremely close to zero, suggesting either a flat landscape or a region with very limited optimisation potential. Overall, the Week 4 results reinforced the distinction between strong exploitation candidates and functions requiring continued exploration.

# Table 1. Week 4 Function Outputs

| Function | Output       |
| -------- | ------------ |
| F1       | 0.0000001475 |
| F2       | 0.522846     |
| F3       | -0.060380    |
| F4       | -22.551877   |
| F5       | 3238.333369  |
| F6       | -0.873367    |
| F7       | 1.196830     |
| F8       | 9.539440     |

# 3. Comparison of Week 3 and Week 4 Performance

Comparison between Weeks 3 and 4 demonstrates the effectiveness of evidence-driven query refinement. Function 5 increased from 2840.99 to 3238.33, representing another substantial improvement and confirming that the selected region remained highly productive. Function 7 improved from 0.897 to 1.197, while Function 2 increased from 0.141 to 0.523, indicating successful refinement of previously promising regions.

Function 8 remained relatively stable, changing from 9.443 to 9.539. This suggests that the optimisation process has likely located a plateau of consistently high performance. Function 3 improved slightly towards zero, while Function 6 deteriorated modestly. Function 4 declined further into a strongly negative region, indicating that the current search area remains suboptimal.

Overall, the Week 4 results support the transition from broad exploratory sampling toward targeted exploitation and refinement. The strongest gains were achieved in functions where previous evidence had already identified promising regions.


# 4. Query Selection Strategy
Week 4 query selection was based on accumulated evidence from the first three optimisation rounds. Rather than treating all functions equally, resources were allocated according to observed performance patterns. High-performing functions such as F5 were assigned exploitative queries intended to maximise performance gains. Stable positive functions such as F2, F7 and F8 were refined locally to improve understanding of their surrounding landscapes.

Functions exhibiting poor or unstable behaviour, including F3, F4 and F6, were assigned exploratory movements to increase information gain and identify alternative regions of interest. This approach reflected a Bayesian optimisation mindset in which query selection seeks both improved performance and improved knowledge of the objective function.



