# Week_09

## Bayesian Black Box Optimisation Portfolio

### Week 09 Analysis

## Contents

1. Introduction
2. Week 09 Results
3. Comparison of Week 08 and Week 09 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 10 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References


## 1. Introduction

Week 09 represented another important stage in the Bayesian Black Box Optimisation (BBO) challenge. By this point, eight optimisation rounds had been completed, providing a substantial body of evidence on the behaviour of the hidden objective functions. As understanding of the search landscape continued to improve, optimisation decisions became increasingly focused on building upon previous results while continuing to investigate areas where uncertainty remained.

The aim of Week 09 was to determine whether the productive regions identified during earlier optimisation rounds continued to deliver improved objective values. At the same time, the remaining query budget was used to gather additional evidence from functions that had shown inconsistent or limited progress. This balanced approach allowed strong-performing regions to be refined while ensuring that less well understood areas of the search space continued to be investigated.

The results from Week 09 reinforced several of the patterns observed during previous weeks. Function 5 remained the strongest performer and achieved another increase in objective value, strengthening confidence that the current search region remained the most productive identified so far. Functions 7 and 8 continued to produce stable positive outputs, while Function 2 remained within a productive region despite a small reduction compared with Week 08. Function 4 showed further improvement within the negative objective region, whereas Functions 3 and 6 continued to require careful refinement. Function 1 again returned an output effectively equal to zero, indicating that broader exploration remained necessary to determine whether more productive regions existed elsewhere in the search space.

This repository documents the complete Week 09 optimisation process, including the optimisation results, comparison with previous weeks, query selection strategy, computational analysis and repository organisation. The accompanying Python scripts, structured CSV datasets and supporting figures provide a clear and reproducible record of the work completed during this optimisation round. Together, these components maintain a consistent analytical framework while supporting the continued development of the Bayesian Black Box Optimisation project.

## 2. Week 09 Results

Week 09 provided further evidence that the optimisation strategy continued to identify productive regions within the hidden search landscape. While the overall ranking of the objective functions remained largely unchanged, several functions exhibited meaningful changes that helped refine understanding of their behaviour. These observations provided additional guidance for selecting future queries and improving the balance between exploitation, refinement and exploration.

Function 5 once again produced the highest objective value, increasing from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09. This continued upward trend reinforced confidence that the optimisation process remained centred on a highly productive region of the search landscape. The consistent improvement observed over successive optimisation rounds supported continued local exploitation while maintaining only small adjustments to the query values.

Function 7 remained one of the strongest positive functions despite a slight reduction from **1.3346391663186332** to **1.314307996450604**. Function 8 also remained highly stable, changing only from **9.47621** to **9.4709436**. Although both functions declined slightly, the changes were small and did not alter their overall interpretation as reliable and productive regions suitable for continued refinement.

Function 2 declined from **0.5672775862793291** in Week 08 to **0.47297842839949866** in Week 09. While this represented a reduction in objective value, the function remained positive and continued to perform substantially better than during earlier optimisation rounds. Continued refinement therefore remained appropriate while further evidence was gathered.

The remaining functions continued to occupy negative regions of the objective space. Function 4 improved from **-12.305008897187289** to **-11.788939969158545**, providing further evidence that gradual refinement within this region continued to improve performance. Function 3 declined slightly from **-0.0991107637427902** to **-0.1156707106126581**, while Function 6 decreased marginally from **-1.1197178425911847** to **-1.1733030029888645**. These changes suggested that the search landscape surrounding these functions remained complex and required continued investigation.

Function 1 again returned an output effectively equal to zero, remaining at **-1.4546199699251391e-58**. This repeated observation suggested that the current search region continued to provide little useful optimisation information and that broader exploration remained the most appropriate strategy.

Overall, the Week 09 results strengthened confidence in the current optimisation framework. Function 5 continued to justify sustained exploitation, Functions 2, 7 and 8 remained suitable for targeted refinement, Functions 3, 4 and 6 continued to improve understanding of the negative search regions, and Function 1 remained the principal exploration target. Together, these observations provided a stronger evidence base for planning the Week 10 optimisation strategy.

| Function   |          Week 09 Output | Interpretation                                            |
| ---------- | ----------------------: | --------------------------------------------------------- |
| Function 1 | -1.4546199699251391e-58 | Remained close to zero, supporting continued exploration  |
| Function 2 |     0.47297842839949866 | Positive output with a small decline from Week 08         |
| Function 3 |     -0.1156707106126581 | Slight decline, continued refinement required             |
| Function 4 |     -11.788939969158545 | Continued improvement within a negative region            |
| Function 5 |       4394.868042481448 | Highest objective value, continued exploitation justified |
| Function 6 |     -1.1733030029888645 | Small decline within a negative region                    |
| Function 7 |       1.314307996450604 | Stable positive performance despite a slight reduction    |
| Function 8 |               9.4709436 | Stable high performance with minimal change               |

**Figure 1A. Function Output Evolution (Weeks 1–9)**

<img width="1693" height="929" alt="Figure 1A  Function Output Evolution (Weeks 1–9)" src="https://github.com/user-attachments/assets/130e7734-c3c8-49b9-a6d5-f31a28715c78" />


**Figure 1B. Week 09 Function Performance Ranking**

<img width="1536" height="1024" alt="Figure 1B  Week 09 Function Performance Ranking" src="https://github.com/user-attachments/assets/1c9e05e5-c3d6-479c-a18f-f943643fc42e" />




