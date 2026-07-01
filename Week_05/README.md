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

Function 7 also demonstrated continued improvement, increasing from 1.333900 to 1.380300, while Function 8 remained highly stable despite a small reduction from 9.602900 to 9.511300. The stability of these functions suggested that the optimisation process had identified productive regions of the search space where only minor refinements were required.

In contrast, Functions 3, 4 and 6 remained negative and showed little evidence of approaching favourable regions. Function 4 continued to produce the lowest output, indicating that the selected query location was unlikely to be close to an optimum. These functions therefore remained candidates for continued exploration rather than exploitation.

Overall, the comparison demonstrated a gradual transition from broad exploratory sampling towards evidence based optimisation. The Week 5 results increased confidence in exploiting high performing functions while continuing to investigate uncertain regions of the search space through carefully selected exploratory queries.

**Figure 1B.1 Comparison of Week 4 and Week 5 Performance**


<img width="1536" height="1024" alt="Week 4 vs Week 5 performance comparison 2" src="https://github.com/user-attachments/assets/dd64911d-df72-43bc-9640-031ba42c791f" />

...

## 4. Query Selection Strategy

The Week 05 query selection strategy was guided by evidence accumulated from previous optimisation rounds rather than random exploration. Results from Weeks 1 to 4 revealed which functions were responding positively to incremental refinement and which continued to exhibit high uncertainty. This information was used to allocate the limited query budget more effectively across the eight unknown objective functions.

Function 5 remained the highest priority for continued exploitation because it had demonstrated consistent improvement throughout successive optimisation rounds. Small adjustments were made around the previously successful query region to maximise the likelihood of further performance gains while avoiding unnecessary movement away from the promising optimum.

Functions 7 and 8 demonstrated stable positive behaviour and therefore required only modest refinement. Maintaining exploration close to these established regions balanced the potential for incremental improvement with the need to confirm the consistency of previous observations.

In contrast, Functions 1, 3, 4 and 6 continued to produce weaker or negative outputs. These functions remained candidates for exploratory sampling because their search landscapes were still poorly understood. Broader exploration increased the likelihood of identifying previously undiscovered high performing regions while reducing uncertainty surrounding the underlying objective functions.

Overall, the Week 05 query selection strategy reflected a balanced optimisation approach that combined exploitation of high performing functions with continued exploration of uncertain regions. This evidence based allocation of queries maximised information gain while supporting steady improvement across successive optimisation rounds.

**Figure 2. Week 05 Query Selection Strategy**


<img width="1536" height="1024" alt="Figure 2 Week 05 query selection strategy diagram" src="https://github.com/user-attachments/assets/f7cd7b17-db1d-43fd-a05c-de6abb38eb48" />


...

## 5. Exploration vs Exploitation Analysis

A successful Bayesian Black Box Optimisation strategy requires an appropriate balance between exploration and exploitation. Exploration focuses on sampling uncertain regions of the search space to discover potentially better solutions, whereas exploitation concentrates on refining known high performing regions to maximise objective values. Achieving an effective balance between these competing objectives was central to the Week 05 optimisation strategy.

The Week 05 results demonstrated that Function 5 continued to outperform all other functions. Its consistent improvement over successive optimisation rounds provided strong evidence that the surrounding search region contained a high quality solution. Consequently, additional query resources were allocated to exploitation through small incremental adjustments designed to maximise further performance gains while remaining close to the established optimum.

Functions 7 and 8 also demonstrated stable positive behaviour. Rather than performing broad exploration, these functions benefited from local refinement to confirm the consistency of previous observations and identify possible incremental improvements within neighbouring regions of the search space.

Conversely, Functions 1, 3, 4 and 6 continued to exhibit greater uncertainty. Their outputs suggested that the current query locations had not yet identified favourable regions, making continued exploration the most appropriate strategy. Sampling alternative areas of the search space increased the probability of discovering previously unidentified optima while reducing uncertainty surrounding the underlying objective functions.

Overall, Week 05 demonstrated that effective optimisation depends not only on maximising exploitation but also on allocating limited queries according to the confidence associated with each function. This evidence based balance between exploration and exploitation improved both optimisation performance and understanding of the hidden search landscape.

**Figure 3. Exploration versus Exploitation Analysis**

<img width="1536" height="1024" alt="Figure 3 Exploration vs exploitation analysis overview" src="https://github.com/user-attachments/assets/f3960ef2-5bb0-439f-a774-2aebb88987f4" />

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
