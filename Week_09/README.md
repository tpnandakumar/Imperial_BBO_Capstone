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


## 3. Comparison of Week 08 and Week 09 Performance

Comparison of the Week 08 and Week 09 results showed that the overall performance ranking remained stable, although several functions moved within their established search regions. Function 5 continued to improve, Function 4 moved towards a less negative value, and the remaining functions either declined slightly or remained unchanged. These changes provided useful evidence for refining the Week 10 query strategy.

Function 5 remained the strongest performer. Its output increased from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09, giving an exact increase of **35.483908158745**. The improvement was smaller than those achieved during earlier rounds, but it confirmed that the current region continued to produce higher objective values. This supported continued exploitation through cautious local adjustment.

Function 4 recorded the main improvement among the negative functions. Its output changed from **-12.305008897187289** to **-11.788939969158545**, an exact improvement of **0.516068928028744**. Although the value remained negative, the movement towards zero suggested that the revised query had identified a more favourable neighbouring region.

Function 2 declined from **0.5672775862793291** to **0.47297842839949866**, an exact change of **-0.09429915787983044**. The output remained positive, but the reduction showed that the strong Week 08 result had not been maintained. Further refinement was still justified, although the next query needed to remain close to the better performing region rather than continuing in the same direction without adjustment.

Functions 7 and 8 remained stable positive performers. Function 7 changed from **1.3346391663186332** to **1.314307996450604**, a reduction of **0.0203311698680292**. Function 8 decreased from **9.47621** to **9.4709436**, a reduction of **0.0052664**. These small declines did not alter their relative positions and continued to support careful local refinement.

Function 3 decreased from **-0.0991107637427902** to **-0.1156707106126581**, giving an exact change of **-0.0165599468698679**. Function 6 also declined from **-1.1197178425911847** to **-1.1733030029888645**, an exact change of **-0.0535851603976798**. Both functions remained within negative regions and required further investigation before a reliable improvement path could be identified.

Function 1 returned exactly the same output as in Week 08, remaining at **-1.4546199699251391e-58**. The absence of change confirmed that the current region continued to provide little useful evidence of optimisation potential. Broader exploration remained the most appropriate strategy.

Overall, Week 09 produced a mixed but informative result. Function 5 continued to improve and Function 4 moved in a favourable direction, while Functions 2, 3, 6, 7 and 8 declined by varying amounts. Function 1 remained unchanged. These observations supported continued exploitation of Function 5, cautious refinement of the stable positive functions, reassessment of the declining negative functions and broader exploration of Function 1.

**Figure 1C. Week 08 vs Week 09 Comparison Dashboard**

<img width="1536" height="1024" alt="Figure 1C  Week 08 vs Week 09 Comparison Dashboard" src="https://github.com/user-attachments/assets/1803e28e-8dd3-402c-b53a-65405fe16330" />

## 4. Query Selection Strategy

The Week 09 query selection strategy was based on the performance patterns observed across the first eight optimisation rounds. By this stage, several functions had shown consistent behaviour, while others still required further investigation. The available query budget was therefore allocated according to the strength of the current evidence, the direction of recent change and the likelihood of gaining useful information from each new query.

Function 5 remained the main exploitation target. Its output increased again, from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09. This confirmed that the current search region continued to produce the strongest results in the portfolio. The most appropriate strategy was therefore to continue with small, controlled adjustments around the existing best-known input rather than move to a different part of the search space.

Functions 7 and 8 remained suitable for local refinement. Both continued to produce strong positive outputs, although each declined slightly in Week 09. Their overall stability suggested that the surrounding regions remained productive, but the next queries needed to be more cautious and focused on preserving performance while testing nearby alternatives.

Function 2 also remained a refinement target. Its Week 09 output of **0.47297842839949866** was lower than the Week 08 result, but the function remained positive and continued to perform better than in several earlier rounds. The decline indicated that the search should remain close to the stronger Week 08 region rather than continue moving in the same direction without adjustment.

Function 4 showed the most encouraging movement among the negative functions. Its output improved from **-12.305008897187289** to **-11.788939969158545**, suggesting that the revised query had moved towards a more favourable region. Further local refinement remained justified, although progress was still gradual and the function continued to require careful monitoring.

Functions 3 and 6 declined during Week 09 and remained within negative regions. Their next queries needed to be selected cautiously, with the aim of testing nearby alternatives rather than making large changes. The purpose of these queries was not only to improve the objective value but also to better understand the local search landscape and avoid repeating unproductive directions.

Function 1 again produced an output effectively equal to zero. Repeated sampling around the current region had provided little evidence of optimisation potential. Broader exploration remained necessary, with the next query directed towards a clearly different part of the search space.

Overall, the Week 09 query selection strategy maintained a clear distinction between exploitation, refinement and exploration. Function 5 remained the strongest exploitation target, Functions 2, 4, 7 and 8 required local refinement, Functions 3 and 6 required cautious reassessment, and Function 1 remained the principal exploration target. This approach provided the basis for the Week 10 input selection.

**Figure 2. Exploration, Refinement and Exploitation Strategy**

<img width="1536" height="1024" alt="Figure 2  Exploration, Refinement and Exploitation Strategy" src="https://github.com/user-attachments/assets/96af14a8-091e-4f77-a5c9-ce8221e51d6c" />


## 5. Exploration vs Exploitation Analysis

Maintaining an effective balance between exploration and exploitation remained central to the Week 09 optimisation strategy. As the optimisation process progressed, confidence in several search regions continued to increase, allowing greater emphasis to be placed on functions with established optimisation potential while preserving sufficient exploration to identify previously undiscovered productive regions. This balance ensured that computational resources were directed efficiently without limiting opportunities for future improvement.

Function 5 remained the primary exploitation target throughout Week 09. Its objective value increased from **4359.384134322703** in Week 08 to **4394.868042481448**, confirming that the surrounding search region continued to generate the strongest optimisation results. The relatively small but consistent improvement suggested that the optimum had not yet been reached and that further gains were likely to come from careful local refinement rather than large changes in the query values.

Refinement remained appropriate for Functions 2, 4, 7 and 8. Function 4 continued to improve, moving from **-12.305008897187289** to **-11.788939969158545**, while Functions 7 and 8 remained stable despite small reductions in objective value. Function 2 declined compared with Week 08 but continued to produce a positive output, indicating that the underlying search region remained promising even though the most recent query produced a less favourable result. Collectively, these functions continued to justify local refinement because they provided useful optimisation information without requiring broad exploration.

Functions 3 and 6 remained within negative regions of the search landscape and therefore required a more cautious approach. The small reductions observed during Week 09 suggested that neighbouring regions had not yet been fully explored. Rather than abandoning these functions, carefully selected local adjustments remained appropriate to improve understanding of the surrounding search space while avoiding unnecessary computational effort.

Function 1 again produced an output effectively equal to zero and remained the least informative objective function. Repeated sampling within the current region continued to provide little evidence of optimisation potential. Broader exploration therefore remained the preferred strategy, with future queries directed towards substantially different regions of the search space in an effort to identify previously undiscovered areas of higher performance.

Overall, the Week 09 optimisation strategy continued to balance exploitation, refinement and exploration according to the evidence accumulated throughout the project. Concentrating computational effort on proven high-performing regions while maintaining targeted investigation of uncertain regions provided the strongest opportunity to improve optimisation performance and further reduce uncertainty before the next optimisation round.

**Figure 2A. Exploration vs Exploitation Balance (Week 09)**

<img width="1536" height="1024" alt="Figure 2A  Exploration vs Exploitation Balance (Week 09)" src="https://github.com/user-attachments/assets/4e098082-9d43-44b8-9695-40c6bd26b639" />

## 6. Reflection on Week 10 Query Selection

The Week 09 results provided additional evidence to guide the selection of queries for Week 10. After nine optimisation rounds, the behaviour of the eight hidden objective functions had become increasingly well understood, allowing future decisions to be based on observed performance rather than broad exploration. The emphasis therefore shifted towards confirming productive search regions while continuing to investigate functions that still exhibited uncertainty.

Function 5 remained the strongest optimisation target throughout the project. Its objective value increased again, from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09, confirming that the current search region continued to produce the highest objective values. Rather than making large adjustments, the evidence supported repeating or making only very small refinements around the best-performing input in order to determine whether the optimum had been reached or whether further improvement remained possible.

Function 4 continued to show gradual improvement despite remaining within the negative objective region. The movement from **-12.305008897187289** to **-11.788939969158545** suggested that the revised query had moved towards a more favourable region of the search space. Continued refinement therefore remained appropriate, although progress was expected to be gradual.

Function 2 remained positive despite a reduction compared with Week 08. This decline indicated that the strong improvement observed during the previous optimisation round required further confirmation before the surrounding region could be considered stable. Functions 7 and 8 remained reliable positive performers, with only small reductions in objective value. These functions continued to justify careful local refinement because their behaviour remained consistent across successive optimisation rounds.

Functions 3 and 6 remained within negative regions and continued to provide limited improvement. The evidence suggested that further investigation should concentrate on nearby regions rather than making substantial changes to the search direction. Maintaining continuity in the refinement process offered the greatest opportunity to improve understanding of these parts of the optimisation landscape.

Function 1 again returned an output effectively equal to zero and remained the least informative objective function. Repeated observations confirmed that the current region was unlikely to contain a productive optimum. Future queries therefore continued to prioritise broader exploration in an effort to identify previously untested regions with greater optimisation potential.

Overall, the Week 09 results reinforced the value of an evidence-based optimisation strategy. Continued exploitation of Function 5, targeted refinement of Functions 2, 4, 7 and 8, cautious reassessment of Functions 3 and 6, and broad exploration of Function 1 provided the most balanced approach for preparing the Week 10 optimisation round.

**Figure 3. Function Classification Matrix (Week 09)**

<img width="1536" height="1024" alt="Figure 3  Function Classification Matrix (Week 09)" src="https://github.com/user-attachments/assets/a7139d16-e325-4a99-bce6-bad74188752d" />



## 7. Functional Ranking Evolution

The Week 09 results provided a clearer picture of how the relative performance of the eight objective functions had evolved after nine optimisation rounds. Although the overall ranking remained unchanged from Week 08, the latest results provided additional evidence regarding the stability of the leading functions and the behaviour of those requiring further investigation. This continuing record of performance helped guide future optimisation decisions by distinguishing consistently productive regions from those that remained uncertain.

Function 5 retained first position with an output of **4394.868042481448**. The continued increase confirmed that the identified search region remained highly productive and that the optimisation process continued to move in a favourable direction. After nine optimisation rounds, Function 5 had established itself as the dominant objective function, supporting continued local exploitation rather than broad exploratory sampling.

Function 8 remained in second position with an output of **9.4709436**. Although the objective value decreased slightly from Week 08, the reduction was minimal and did not affect its ranking. Function 7 also maintained third position, producing **1.314307996450604**. The small decline compared with the previous week suggested that the surrounding search region remained stable while indicating that future refinement should proceed cautiously.

Function 2 remained in fourth position with an output of **0.47297842839949866**. Despite the reduction from Week 08, the function continued to produce a positive objective value and remained substantially stronger than the negative functions. Continued refinement therefore remained appropriate while gathering further evidence regarding the surrounding search region.

Function 1 remained in fifth position because its output continued to lie close to zero. Although this ranking placed it above the negative functions, the result reflected the absence of a productive response rather than genuine optimisation progress. Continued exploration therefore remained the preferred strategy.

Functions 3, 6 and 4 occupied the lower positions in the ranking. Function 3 produced **-0.1156707106126581**, Function 6 produced **-1.1733030029888645**, and Function 4 produced **-11.788939969158545**. Although Function 4 improved compared with Week 08, it remained the lowest-ranked objective function and continued to require careful investigation.

Overall, the Week 09 ranking demonstrated that the leading functions remained remarkably stable throughout the optimisation process. Function 5 continued to strengthen its position, Functions 7 and 8 remained reliable positive performers, Function 2 retained a productive search region despite a modest decline, and the remaining functions continued to provide useful information for refining the understanding of the hidden optimisation landscape.

**Figure 3A. Functional Ranking Evolution (Weeks 1–9)**

<img width="1536" height="1024" alt="Figure 3A  Functional Ranking Evolution (Weeks 1–9)" src="https://github.com/user-attachments/assets/6dc97ab2-62e6-42f9-a42f-24b294d6cde5" />

## 8. High Performing Region Identification

Identifying productive regions within the hidden search landscape remained one of the main objectives of the Bayesian Black Box Optimisation process. After nine optimisation rounds, the accumulated evidence provided a clearer picture of which regions consistently produced strong objective values and which continued to require further investigation. This growing understanding allowed future queries to focus increasingly on regions with the greatest optimisation potential while continuing to reduce uncertainty elsewhere in the search space.

Function 5 remained the strongest high-performing region identified during the project. Its objective value increased from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09, continuing the steady upward trend observed throughout the optimisation process. This consistent improvement suggested that the current search region remained highly productive and supported continued local exploitation rather than broad exploratory sampling.

Function 8 remained the second strongest performing function despite a very small reduction from **9.47621** to **9.4709436**. The change was minimal and did not alter the overall interpretation of the surrounding search region, which continued to demonstrate stable performance and low uncertainty. Function 7 also remained within a productive region, changing only slightly from **1.3346391663186332** to **1.314307996450604**. Although the objective value declined marginally, the function continued to demonstrate reliable behaviour and remained suitable for careful local refinement.

Function 2 remained within a productive positive region despite declining from **0.5672775862793291** to **0.47297842839949866**. While this reduction indicated that the previous improvement had not been fully maintained, the function continued to produce positive objective values and remained considerably stronger than the remaining negative functions. Continued refinement therefore remained appropriate while gathering additional evidence from the surrounding search region.

The remaining functions continued to provide valuable information despite producing lower objective values. Function 4 moved closer to zero, improving from **-12.305008897187289** to **-11.788939969158545**, while Functions 3 and 6 declined slightly but continued to improve understanding of their respective search regions. Function 1 again returned an output effectively equal to zero, indicating that the current search region remained unproductive and that broader exploration continued to offer the greatest opportunity for discovering new areas of optimisation potential.

Overall, the Week 09 results strengthened confidence in the productive regions identified during previous optimisation rounds while continuing to refine the understanding of less productive areas. Sustained exploitation of Function 5, careful refinement of Functions 2, 7 and 8, continued investigation of Functions 3, 4 and 6, and broad exploration of Function 1 provided the most balanced strategy for future optimisation rounds.

**Figure 4. Function 5 Optimisation Progress (Weeks 1–9)**

<img width="1536" height="1024" alt="Figure 4  Function 5 Optimisation Progress (Weeks 1–9)" src="https://github.com/user-attachments/assets/dc513168-d3d2-4cd0-89fa-ee263e88dbd9" />


**Best Function: F5**

<img width="1536" height="1024" alt="week_09 Best function F5" src="https://github.com/user-attachments/assets/98a092f2-e59b-41ec-bfc1-3848ed90d0dc" />


**Highest Output: 4394.868042481448**

<img width="1536" height="1024" alt="Week_09 Highest Output" src="https://github.com/user-attachments/assets/28ae2f98-5379-4ace-a066-782e1dfeadee" />

## 9. Decision Matrix and Resource Allocation

The Week 09 optimisation strategy continued to allocate computational resources according to observed performance, recent optimisation trends and expected information gain. After nine optimisation rounds, the hidden search landscape had become more clearly defined, allowing greater confidence when deciding which functions should receive further exploitation, targeted refinement or broader exploration. This evidence-based approach ensured that the available query budget was used efficiently while continuing to improve understanding of the underlying optimisation problem.

Function 5 remained the highest priority for resource allocation. Its objective value increased from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09, extending its position as the strongest performing function. The consistent improvement suggested that the current search region continued to offer the greatest opportunity for additional optimisation. Consequently, the majority of exploitation effort remained focused on carefully controlled local refinement around the existing best-performing solution.

Functions 2, 7 and 8 continued to receive a high refinement priority. Although each function showed a small reduction in objective value during Week 09, all three remained within productive regions of the search landscape. Their stability suggested that neighbouring regions still offered potential for incremental improvement while carrying relatively low optimisation risk. Function 4 also remained a refinement candidate because its movement towards zero indicated that the surrounding search region continued to improve.

Functions 3 and 6 remained within negative regions and therefore received a lower allocation of computational resources. Rather than abandoning these functions, targeted local refinement continued because successive optimisation rounds had gradually improved understanding of their behaviour. Carefully selected queries within nearby regions offered the best opportunity to identify more favourable directions without unnecessarily increasing exploration.

Function 1 remained the primary exploration target. After repeated optimisation rounds, its objective value continued to remain effectively equal to zero, providing little evidence that the current region contained a productive optimum. Future computational effort therefore remained directed towards exploring substantially different regions of the search space in an attempt to identify previously undiscovered optimisation opportunities.

Overall, the Week 09 decision matrix reflected a balanced optimisation strategy. Computational resources remained concentrated on proven high-performing regions while maintaining sufficient refinement and exploration to improve understanding of the remaining objective functions. This approach continued to strengthen optimisation performance while reducing uncertainty and supporting evidence-based decision making for future optimisation rounds.

**Figure 4A. Resource Allocation Decision Matrix (Week 09)**

<img width="1536" height="1024" alt="Week_09 Highest Output" src="https://github.com/user-attachments/assets/a08d7b39-da77-4cad-8921-53e33aa86be3" />


## 10. Information Gain Analysis

Information gain remained one of the principal objectives throughout Week 09 because each optimisation round contributed new evidence about the behaviour of the hidden objective functions. While improvements in objective values remained important, the optimisation process also depended upon reducing uncertainty and strengthening confidence in the search regions identified during previous weeks. After nine optimisation rounds, the accumulated evidence provided a clearer understanding of where future computational effort was most likely to produce meaningful improvement.

Function 5 continued to provide the greatest overall information gain. Its objective value increased from **4359.384134322703** in Week 08 to **4394.868042481448** in Week 09, confirming that the current search region remained highly productive. Although the increase was smaller than those observed during earlier optimisation rounds, it strengthened confidence that the optimisation process was approaching a stable optimum while continuing to benefit from carefully controlled local refinement.

Function 4 also contributed useful information despite remaining within the negative objective region. Its improvement from **-12.305008897187289** to **-11.788939969158545** suggested that neighbouring regions continued to contain opportunities for incremental improvement. This movement increased confidence in the current refinement strategy and supported further investigation of nearby regions.

Functions 2, 7 and 8 produced smaller amounts of information gain. Although each function declined slightly compared with Week 08, all three remained within productive regions of the search landscape. These observations confirmed that the identified regions continued to perform reliably while indicating that future refinement should proceed cautiously to avoid moving away from favourable locations.

Functions 3 and 6 continued to provide useful information despite remaining negative. The small reductions observed during Week 09 improved understanding of their local search landscapes by identifying regions that were less productive than expected. This knowledge remained valuable because it reduced uncertainty and helped avoid unproductive search directions in future optimisation rounds.

Function 1 again produced an output effectively equal to zero. While the objective value itself remained unchanged, repeated observations continued to strengthen confidence that the current search region contained little optimisation potential. This reinforced the decision to prioritise broader exploration rather than further refinement within the existing region.

Overall, the Week 09 information gain demonstrated that optimisation success depended upon combining improvements in objective value with continued reduction in uncertainty. The evidence accumulated over nine optimisation rounds provided a stronger foundation for future decision making and supported increasingly targeted optimisation strategies as the project progressed.

**Figure 5. Information Gain Summary (Week 09)**

<img width="1536" height="1024" alt="Figure 5A  Python Computational Workflow (Week 09)" src="https://github.com/user-attachments/assets/7bc2ac93-f4c3-4ea6-928d-d918ad72cfc5" />

## 12. Repository Files and Reproducibility

Maintaining a structured and well organised repository remained an important objective throughout Week 09 because it ensured that every stage of the optimisation process could be reproduced, reviewed and extended. The repository continued to separate optimisation inputs, objective function outputs, computational analysis, summary datasets and documentation into clearly defined files. This organisation provided a transparent workflow in which every result could be traced directly to its source.

The Week 09 repository contained the complete optimisation inputs and outputs together with reusable Python analysis scripts and supporting documentation. The `week_09_inputs.csv` file stored the exact query values submitted during Week 09, while `week_09_results.csv` contained the objective values returned by the optimisation system. These datasets formed the foundation of the computational analysis and ensured that every optimisation result remained fully reproducible.

The `week_09_analysis.py` script processed the structured datasets, calculated changes relative to Week 08, ranked the objective functions, classified optimisation strategies and generated the analytical summary. The resulting `week_09_analysis_summary.csv` provided a concise overview of optimisation performance and supplied the data used throughout the figures and discussion. Using the same analytical workflow each week maintained consistency while reducing manual processing.

Documentation continued to play a central role within the repository. The Week 09 `README.md` recorded the complete optimisation workflow, including methodology, results, discussion, figures and conclusions. Combining structured datasets, reusable Python scripts and detailed documentation created a reproducible research framework that could be extended easily during future optimisation rounds.

The repository structure also supported long-term maintenance and scalability. Future optimisation rounds required only updated input and output CSV files while the existing analysis script and documentation framework remained unchanged. This modular organisation reduced duplication of effort, improved consistency across optimisation rounds and simplified continued development of the Bayesian Black Box Optimisation project.

Overall, the Week 09 repository demonstrated the value of combining structured datasets, reusable computational tools and comprehensive documentation within a reproducible research environment. This organisation strengthened transparency, improved reproducibility and provided a robust framework for analysing future optimisation rounds.

**Figure 5B. Week 09 Repository Structure and Workflow**

<img width="1536" height="1024" alt="Figure 5B  Week 09 Repository Structure and Workflow" src="https://github.com/user-attachments/assets/472575ae-02da-4ef3-84e0-369003c3f9e8" />

## 13. Conclusion

Week 09 marked another significant stage in the Bayesian Black Box Optimisation challenge by providing further evidence about the behaviour of the hidden objective functions. After nine optimisation rounds, the optimisation process had become increasingly focused, with a clearer distinction between productive regions, stable regions and areas that continued to require further investigation. The growing body of evidence allowed optimisation decisions to be guided by observed performance rather than broad exploratory sampling.

Function 5 again demonstrated the strongest performance, achieving a new highest objective value of **4394.868042481448**. This continued improvement confirmed that the current search region remained highly productive and justified continued local exploitation. Functions 7 and 8 remained stable within positive regions despite small reductions in objective value, while Function 2 continued to produce positive outputs even though it declined compared with Week 08. Function 4 provided encouraging evidence by moving closer to zero, indicating gradual improvement within the negative objective region.

Functions 3 and 6 continued to occupy negative regions of the search landscape and required further refinement before stronger conclusions could be drawn. Function 1 again produced an output effectively equal to zero, reinforcing the need for continued exploration of alternative regions rather than additional refinement of the current search location.

The Week 09 analysis demonstrated the value of allocating computational effort according to accumulated evidence rather than treating all objective functions equally. Continued exploitation of Function 5 remained the most appropriate strategy, while targeted refinement of Functions 2, 4, 7 and 8 strengthened understanding of productive regions. Functions 3 and 6 continued to provide useful information despite lower objective values, and Function 1 remained the principal exploration target.

The computational workflow also continued to demonstrate the value of structured and reproducible analysis. Standardised CSV datasets, reusable Python scripts and comprehensive documentation provided a consistent analytical framework that could be repeated for every optimisation round. This approach improved transparency, reduced manual processing and strengthened the long-term maintainability of the repository.

Overall, the Week 09 results strengthened confidence in the current optimisation strategy while continuing to improve understanding of the hidden search landscape. The evidence gathered during this optimisation round provided a stronger basis for selecting the Week 10 queries and further reinforced the value of a systematic, evidence-based approach to Bayesian Black Box Optimisation.

**Figure 5C. Week 09 Conclusions and Strategic Outlook**

<img width="1024" height="1536" alt="Figure 5C  Week 09 Conclusions and Strategic Outlook" src="https://github.com/user-attachments/assets/029506e1-966a-4075-ba7a-4c87326f7582" />

