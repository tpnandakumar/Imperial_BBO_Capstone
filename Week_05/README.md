# Week_05

## Contents

1. Introduction
2. Week 5 Results
3. Comparison of Week 4 and Week 5 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 6 Query Selection
7. Functional Ranking Evolution
8. High-Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion

## 1. Introduction

Week 05 represents a transition from broad exploratory optimisation to more evidence based query refinement. By this stage, the optimisation process had accumulated sufficient information from previous rounds to identify stable functions, promising search regions and functions requiring continued exploration.

The main objective of Week 05 was to use the results from earlier submissions to refine the Week 06 query strategy. Particular attention was given to Function 5, which had shown sustained improvement across previous rounds, and Function 8, which appeared relatively stable. Functions with weaker or more uncertain performance remained candidates for exploratory sampling.

This week therefore focused on three linked objectives. First, to analyse the Week 05 results. Second, to compare performance with Week 04. Third, to use the observed patterns to develop a more structured and evidence based strategy for the Week 06 query selection..

...

## 2. Week 5 Results

Week 05 produced further evidence regarding the behaviour of the eight unknown objective functions. The results demonstrated that not all functions responded equally to the selected query points. Some functions showed continued improvement, whereas others remained relatively stable or exhibited little evidence of convergence. These observations were used to determine which functions should be exploited further and which required continued exploration during Week 06.

| Function | Week 5 Output | Interpretation |
|----------|--------------:|----------------|
| Function 1 | 0.012780 | Near zero with limited improvement |
| Function 2 | 0.280168 | Moderate improvement observed |
| Function 3 | -0.113922 | Negative response requiring further exploration |
| Function 4 | -27.440515 | Large negative value indicating high uncertainty |
| Function 5 | 3682.211062 | Highest performing function supporting continued exploitation |
| Function 6 | -1.073875 | Slight improvement but remains negative |
| Function 7 | 1.380300 | Stable positive performance |
| Function 8 | 9.511300 | Stable high performance |

**Figure 1A. Function Output Evolution (Weeks 1 to 5)**

<img width="1536" height="1024" alt="Function output evolution across weeks" src="https://github.com/user-attachments/assets/d9eb3c68-b715-45c8-8969-832a5844e458" />

The Week 05 results confirmed that Function 5 remained the strongest candidate for continued exploitation, while Functions 7 and 8 maintained stable performance. In contrast, Functions 3, 4 and 6 continued to exhibit greater uncertainty and required further exploration to improve understanding of their underlying response surfaces. These observations provided the evidence used to guide the Week 06 query selection.

...


## 3. Comparison of Week 4 and Week 5 Performance

A comparison between the Week 4 and Week 5 results demonstrated that the optimisation strategy continued to improve overall performance while providing additional information about the unknown search landscape. The most significant improvement occurred in Function 5, which increased from 3238.000000 in Week 4 to 3682.211062 in Week 5. This confirmed that the selected query region continued to produce higher objective values and justified further exploitation during the following optimisation round.

Function 7 also demonstrated continued improvement, increasing from 1.333900 to 1.380300, while Function 8 remained highly stable with only a small reduction from 9.602900 to 9.511300. The stability of these functions suggested that the optimisation process had identified productive regions of the search space where only minor refinements were required.

In contrast, Functions 3, 4 and 6 remained negative and showed little evidence of approaching favourable regions. Function 4 continued to produce the lowest output, indicating that the selected query location was unlikely to be close to an optimum. These functions therefore remained candidates for continued exploration rather than exploitation.

Overall, the comparison demonstrated a gradual transition from broad exploratory sampling towards evidence based optimisation. The Week 5 results increased confidence in exploiting high performing functions while continuing to investigate uncertain regions of the search space using carefully selected exploratory queries.

**Figure 1B. Comparison of Week 4 and Week 5 Performance**


<img width="1536" height="1024" alt="Week 4 vs Week 5 performance comparison" src="https://github.com/user-attachments/assets/2ab1f749-1443-40df-aed6-39e31d6e59c6" />


<img width="1536" height="1024" alt="Week 4 vs Week 5 performance comparison 2" src="https://github.com/user-attachments/assets/d0fe9402-8032-45ce-a47b-fea4cac2154c" />



...

## 4. Query Selection Strategy

...

## 5. Exploration vs Exploitation Analysis

...

## 6. Reflection on Week 6 Query Selection

...

## 7. Functional Ranking Evolution

...

## 8. High-Performing Region Identification

...

## 9. Decision Matrix and Resource Allocation

...

## 10. Information Gain Analysis

...

## 11. Computational Analysis and Coding Implementation

...

## 12. Repository Files and Reproducibility


...

## 13. Conclusion
