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
Week 4 query selection was based on accumulated evidence from the first three optimisation rounds. Rather than treating all functions equally, resources were allocated according to observed performance patterns. High-performing functions such as F5 were assigned exploitative queries intended to maximise performance gains. Stable positive functions such as F2, F7 and F8 were refined locally to improve performance while simultaneously increasing understanding of their surrounding search landscapes.

Functions exhibiting poor or unstable behaviour, including F3, F4 and F6, were assigned exploratory movements to increase information gain and identify alternative regions of interest. This approach reflected a Bayesian optimisation mindset in which query selection seeks both improved performance and improved knowledge of the objective function.

# 5. Exploration vs Exploitation Analysis

# Figure 2. Exploration vs Exploitation Matrix

<img width="1402" height="1122" alt="Figure2_Exploration_Exploitation_Matrix" src="https://github.com/user-attachments/assets/a32bb202-4912-4cf9-899b-44fd4692de61" />

The Week 4 optimisation strategy reflected a deliberate balance between exploration and exploitation. Exploitation was prioritised for functions that had demonstrated consistent positive performance in previous rounds, while exploration was reserved for functions whose behaviour remained uncertain or unstable.

Function 5 represented the strongest exploitation candidate. Its output increased from 1415.88 in Week 1 to 2308.15 in Week 2, 2840.99 in Week 3 and 3238.33 in Week 4. This sustained upward trend provided strong evidence that the search process had identified a highly productive region of the landscape. Consequently, query selection focused on local refinement rather than broad exploration.

Functions 2, 7 and 8 were classified as moderate exploitation candidates. These functions consistently produced positive outputs and therefore justified further refinement. However, their growth patterns were less pronounced than Function 5, suggesting that a combination of local exploitation and limited exploration remained appropriate.

Functions 1, 3, 4 and 6 were assigned a higher exploratory priority. These functions either produced low outputs, negative outputs or inconsistent behaviour across optimisation rounds. Exploratory queries were therefore used to maximise information gain and improve understanding of the surrounding search landscape.

The resulting allocation of search effort demonstrates the central Bayesian optimisation trade-off between expected improvement and uncertainty reduction. High-performing regions received exploitative refinement, while uncertain regions were explored to improve knowledge of the objective functions.

# 6. Reflection on Week 5 Query Selection

The Week 5 query strategy was informed by the cumulative evidence generated throughout Weeks 1–4. As more observations became available, confidence in the structure of each function increased, allowing query selection to become progressively more targeted.

Function 5 remained the primary exploitation target because it consistently produced the highest outputs observed during the challenge. The sustained increase from 1415.88 in Week 1 to 3238.33 in Week 4 suggested that the optimisation process had identified a highly productive region worthy of continued refinement.

Functions 2 and 7 also demonstrated stable positive performance and therefore remained suitable candidates for local refinement. Function 8 continued to occupy a relatively stable high-performing region and was therefore treated as a monitoring and refinement candidate rather than a target for aggressive exploration.
In contrast, Functions 1, 3, 4 and 6 continued to exhibit uncertainty regarding the underlying structure of their objective landscapes. These functions therefore remained appropriate targets for exploratory sampling designed to maximise information gain and improve future optimisation decisions.

Overall, the Week 5 query strategy reflected a transition from broad exploratory search toward increasingly evidence-driven optimisation. Each query was selected based on observed behaviour from previous rounds rather than intuition alone, demonstrating a systematic approach to optimisation under uncertainty.

## 7. Functional Ranking Evolution

Throughout the first four optimisation rounds, clear differences emerged between the eight objective functions. Early exploratory sampling suggested that several functions were capable of producing positive outputs, while others consistently generated low or negative values. As additional observations accumulated, a stable ranking hierarchy began to emerge, allowing optimisation resources to be allocated more effectively.

Function 5 rapidly established itself as the dominant performer. Its output increased from approximately 1415.88 in Week 1 to 2308.15 in Week 2, 2840.99 in Week 3 and 3238.33 in Week 4. This sustained upward trajectory maintained Function 5 as the highest-ranked objective throughout the optimisation process and provided strong evidence that a highly productive region of the search landscape had been identified.

Function 8 consistently occupied second position, producing remarkably stable outputs near 9.5 across all four optimisation rounds. Although its absolute improvement was considerably smaller than that of Function 5, its consistency suggested that the search process had located a reliable high-performing region with relatively low uncertainty.

Functions 7 and 2 formed a secondary performance tier. Both functions maintained positive outputs throughout most of the optimisation process and demonstrated sufficient stability to justify continued refinement. Function 7 recovered strongly during Week 4, while Function 2 demonstrated a substantial improvement following a weaker Week 3 result, reinforcing their status as viable optimisation targets.

Functions 1, 3, 6 and 4 occupied the lower portion of the ranking hierarchy. Function 1 remained close to zero throughout the challenge, suggesting either a flat landscape or limited optimisation potential. Functions 3 and 6 consistently produced negative outputs despite exploratory movements, while Function 4 remained the weakest-performing function overall, generating the most negative values observed during the optimisation process.

The evolution of these rankings demonstrates how repeated observations gradually transformed an initially uncertain search problem into a structured optimisation landscape with clearly differentiated performance tiers. By Week 4, the hierarchy of functions was sufficiently stable to support increasingly targeted and evidence-driven query selection.

# Figure 1. Function Output Evolution (Weeks 1–4)

<img width="1536" height="1024" alt="Figure1_Function_Output_Evolution_With_Caption" src="https://github.com/user-attachments/assets/28a9b6b7-93cf-463f-a8f1-ac80b26d6c71" />

Figure 1 illustrates the evolution of the highest-performing functions across the four optimisation rounds and demonstrates the emergence of distinct performance tiers.

**Figure 1C. Functional Ranking Evolution Across Weeks 1–4**
<img width="1536" height="1024" alt="Figure1C_F5_Growth_Curve" src="https://github.com/user-attachments/assets/f2e01e78-f032-4957-a6da-0fb85d43d965" />

### Current Week 4 Ranking

| Rank | Function | Output                    |
| ---- | -------- | ------------------------- |
| 1    | F5       | 3238.333368768757         |
| 2    | F8       | 9.539439999999999         |
| 3    | F7       | 1.1968303712356705        |
| 4    | F2       | 0.5228458934672892        |
| 5    | F1       | 0.00000014754580129542488 |
| 6    | F3       | -0.06037987403160633      |
| 7    | F6       | -0.8733671274789931       |
| 8    | F4       | -22.55187651826871        |



## 8. High-Performing Region Identification

The Week 4 results allowed the strongest regions of the search landscape to be identified with greater confidence. Across the first four optimisation rounds, Function 5 emerged as the clearest high-performing region. Its output increased consistently from 1415.8763939603884 in Week 1 to 2308.1487028593933 in Week 2, 2840.9903787629305 in Week 3 and 3238.333368768757 in Week 4. This pattern suggested that successive query points were moving within, or close to, a highly productive area of the objective landscape.

<img width="1536" height="1024" alt="Figure1C_F5_Growth_Curve" src="https://github.com/user-attachments/assets/8b4a22da-742b-4f05-b650-31f3dcd8ca48" />

Function 8 also represented a high-performing region, although with a different pattern. Rather than showing strong growth, it remained consistently positive and stable across the optimisation rounds. Its Week 4 output of 9.539439999999999 confirmed that this function continued to provide reliable performance, suggesting a stable plateau rather than a rapidly improving region.

Functions 2 and 7 showed moderate high-performing potential. Function 2 recovered to 0.5228458934672892 in Week 4, while Function 7 improved to 1.1968303712356705. These results suggested that both functions may contain useful local regions requiring further refinement, although neither demonstrated the same strong growth pattern as Function 5.

<img width="1536" height="1024" alt="Figure1B_Zoomed_F2_F7_F8" src="https://github.com/user-attachments/assets/d65a5e0f-0430-4ff8-9fdc-b391fa62449f" />

In contrast, Functions 1, 3, 4 and 6 did not provide strong evidence of high-performing regions by Week 4. Function 1 remained close to zero, while Functions 3, 4 and 6 continued to produce negative outputs. These functions were therefore better interpreted as exploratory targets rather than exploitation candidates.

Overall, the strongest high-performing region was associated with Function 5, while Function 8 represented a stable high-output region. Functions 2 and 7 remained secondary refinement candidates. This evidence directly informed later query selection by distinguishing functions suitable for exploitation from those requiring further exploration.


## 9. Decision Matrix and Resource Allocation

<img width="1402" height="1122" alt="Figure 2 Decission matrix for week 5 resource allocation" src="https://github.com/user-attachments/assets/c9a55aa6-0f78-45d6-b12e-f1dc77482477" />

<img width="1536" height="1024" alt="Figure 2 1  Confidence–Performance Decision Matrix" src="https://github.com/user-attachments/assets/989590fe-07ea-4791-be36-20fe39e1044a" />


By Week 4, sufficient information had been collected to support a structured allocation of optimisation effort across the eight functions. Rather than treating all functions equally, observed performance trends enabled the classification of functions according to their expected value for future optimisation.

Function 5 was assigned the highest priority for exploitation. Its sustained growth from 1415.8763939603884 in Week 1 to 3238.333368768757 in Week 4 provided strong evidence that highly productive regions of the search landscape had been identified. Additional optimisation resources directed toward Function 5 were therefore expected to produce the greatest potential gains.

Function 8 was classified as a stable exploitation candidate. Although it did not demonstrate rapid growth, it consistently generated positive outputs throughout all optimisation rounds. This stability suggested that the optimisation process had identified a reliable high-performing region with relatively low uncertainty.

Functions 2 and 7 were assigned to a refinement category. Both functions maintained positive outputs and demonstrated evidence of recoverable performance after periods of weaker results. These functions warranted continued investigation through targeted local exploration and moderate exploitation.

Functions 1, 3, 4 and 6 remained exploratory candidates. Function 1 consistently produced outputs near zero, while Functions 3, 4 and 6 generated negative outputs throughout most optimisation rounds. Although these functions were unlikely to outperform the leading candidates, selective exploration remained valuable for reducing uncertainty and avoiding premature convergence.

This decision matrix enabled optimisation effort to be distributed according to observed evidence rather than intuition, reflecting a progressively more systematic and data-driven optimisation strategy.


## 10. Information Gain Analysis

<img width="1536" height="1024" alt="Figure 3  Information Gain Across Functions" src="https://github.com/user-attachments/assets/d20c8076-970b-4848-9a7f-7a457588cbaa" />


A central objective of Bayesian optimisation is the efficient acquisition of information about the underlying search landscape. Each optimisation round not only seeks improved objective values but also increases understanding of the underlying function behaviour.

During the early rounds, uncertainty was high across all eight functions. Query selections therefore prioritised exploration to gather information about function behaviour and identify potentially promising regions. The outputs obtained from these exploratory queries revealed substantial differences between functions, allowing increasingly informed decisions in subsequent rounds.

By Week 4, information gain was evident in several forms. First, a clear ranking hierarchy had emerged, distinguishing strong performers from weaker functions. Second, repeated observations reduced uncertainty surrounding the most promising regions, particularly for Function 5. Third, stable behaviour observed in Functions 2, 7 and 8 improved confidence regarding their likely future performance.

The optimisation process therefore demonstrated the transition from uncertainty-driven exploration toward evidence-driven exploitation. As information accumulated, optimisation decisions became increasingly focused, reducing wasted evaluations and improving overall search efficiency.

The progressive reduction of uncertainty represents one of the most important outcomes of the optimisation process, as improved understanding of the search landscape ultimately drives more effective query selection.

## 11. Computational Analysis and Coding Implementation

The optimisation workflow was supported by a structured computational framework implemented using Python. Numerical calculations were performed using NumPy, while data organisation and analysis were supported through Pandas. Visualisations were generated using Matplotlib to communicate performance trends, optimisation progress and comparative function behaviour.

The computational workflow consisted of several stages. Weekly query inputs and optimisation outputs were recorded and organised into structured datasets. These datasets were then analysed to calculate performance changes, ranking positions and comparative trends across optimisation rounds.

Visualisation scripts were used to generate figures illustrating function growth, ranking evolution and optimisation trajectories. These graphical outputs provided an effective means of identifying patterns that were less obvious from numerical tables alone.

The use of computational tools improved consistency, reproducibility and transparency throughout the optimisation process. By automating calculations and visualisation generation, the likelihood of manual error was reduced while enabling efficient analysis of increasingly complex optimisation behaviour.

This computational framework also forms the foundation for future extensions involving Bayesian optimisation libraries, machine learning workflows and automated decision-support systems.

##  12. Conclusion

The Week 4 optimisation results demonstrated a clear progression from exploratory search toward evidence-driven optimisation. Repeated observations enabled increasingly accurate assessment of function behaviour, leading to the identification of distinct performance tiers and high-performing regions within the search landscape.

Function 5 emerged as the dominant optimisation target, displaying sustained growth across all four optimisation rounds. Functions 2, 7 and 8 provided additional positive performance signals, while Functions 1, 3, 4 and 6 remained primarily exploratory candidates.

The analysis highlighted the importance of balancing exploration and exploitation throughout the optimisation process. Early exploratory queries generated critical information regarding function behaviour, while later rounds increasingly leveraged this information to focus resources on the most promising regions.

Overall, the optimisation challenge demonstrated how systematic data collection, quantitative analysis and evidence-based decision making can progressively transform an initially unknown search problem into a structured and interpretable optimisation landscape. The resulting repository provides a transparent record of this process and establishes a reproducible framework for future Bayesian optimisation investigations.

These four sections fit naturally after Section 8 and complete the GitHub narrative from optimisation results → resource allocation → information gain → computational implementation → final conclusions.



