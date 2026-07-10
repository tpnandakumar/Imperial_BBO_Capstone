# Week_08

## Bayesian Black Box Optimisation Portfolio

### Week 08 Analysis

## Contents

1. Introduction
2. Week 08 Results
3. Comparison of Week 07 and Week 08 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 09 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References


Agreed. This is closer to the tone you've been aiming for throughout the project.

---

# 1. Introduction

Week 08 marked another step forward in understanding the hidden objective functions within the Bayesian Black Box Optimisation (BBO) challenge. With seven previous optimisation rounds completed, the search process had moved beyond broad exploration and towards making decisions based on an increasingly reliable body of evidence. Each new set of results helped clarify which regions of the search space were consistently productive and which still required further investigation.

The query selections for Week 08 were based on the patterns that had emerged over the previous weeks rather than intuition alone. Functions showing sustained improvement continued to receive greater attention, while functions with uncertain or inconsistent behaviour remained under observation. This approach aimed to make the best use of the limited query budget by concentrating effort where it was most likely to improve optimisation performance, without losing the opportunity to discover new productive regions.

The results from Week 08 provided further confidence in the overall optimisation strategy. Function 5 once again delivered the strongest performance, reinforcing its position as the primary target for continued exploitation. Functions 3, 4 and 6 continued to show encouraging progress, while Functions 7 and 8 remained stable within productive regions of the search space. Function 2 improved compared with the previous week, although its behaviour still warranted careful observation. Function 1 remained close to zero and continued to provide little evidence of a productive region, making further exploration the most appropriate course of action.

This report documents the complete Week 08 analysis, including the optimisation results, comparisons with previous weeks, query selection strategy, computational analysis and repository development. The accompanying Python scripts, CSV datasets and visualisations provide a clear and reproducible record of the work completed during this optimisation round. Together, they support a consistent workflow that can be extended as the remaining optimisation rounds are completed and the understanding of the hidden objective functions continues to develop.



## 2. Week 08 Results

Week 08 provided additional evidence that the optimisation strategy was continuing to identify productive regions within the hidden search landscape. Although several functions exhibited only modest changes compared with Week 07, the additional observations strengthened confidence in the current understanding of their behaviour and provided a more reliable basis for selecting future queries.

Function 5 remained the strongest performing objective function, increasing from **4278.816638** in Week 07 to **4359.384134322703** in Week 08. This continued upward trend confirmed that the selected search region remained highly productive and supported continued exploitation in subsequent optimisation rounds.

Function 2 demonstrated the most notable positive change among the remaining positive functions, increasing from **0.239929** to **0.5672775862793291**. This improvement suggested that the revised query selection had identified a more favourable region of the search space, although additional optimisation would still be required before considering the region fully characterised.

Function 8 remained highly stable despite a small reduction from **9.494760** to **9.47621**, while Function 7 also showed only a modest decrease from **1.154336** to **1.3346391663186332**. Despite these minor fluctuations, both functions continued to occupy productive regions and remained suitable candidates for targeted refinement rather than broad exploration.

Among the negative objective functions, mixed behaviour was observed. Function 3 changed slightly from **−0.091169** to **−0.0991107637427902**, while Function 4 decreased from **−10.745961** to **−12.305008897187289**. Function 6 remained relatively stable, changing only from **−1.119713** to **−1.1197178425911847**. These observations suggested that the optimisation process was continuing to map these regions of the search landscape, although additional refinement would be required before stronger conclusions could be drawn.

Function 1 again produced a value effectively equal to zero (**−1.4546199699251391 × 10⁻⁵⁸**), providing little evidence that the current search region contained a productive optimum. Continued exploration therefore remained the most appropriate strategy for this function.

Overall, the Week 08 results strengthened confidence in the current optimisation framework. The evidence continued to support sustained exploitation of Function 5, targeted refinement of Functions 2, 3, 4, 6, 7 and 8, and continued exploration of Function 1. Each optimisation round contributed additional information, reducing uncertainty and improving the understanding of the hidden objective functions.

| Function   |          Week 08 Output | Interpretation                                             |
| ---------- | ----------------------: | ---------------------------------------------------------- |
| Function 1 | -1.4546199699251391e-58 | Remained close to zero, supporting continued exploration   |
| Function 2 |      0.5672775862793291 | Improved from Week 07, indicating a more productive region |
| Function 3 |     -0.0991107637427902 | Small change, continued refinement appropriate             |
| Function 4 |     -12.305008897187289 | Remained negative, further refinement required             |
| Function 5 |       4359.384134322703 | Highest objective value, continued exploitation justified  |
| Function 6 |     -1.1197178425911847 | Stable behaviour within a negative region                  |
| Function 7 |      1.3346391663186332 | Stable positive performance, suitable for refinement       |
| Function 8 |                 9.47621 | Continued strong performance despite a small reduction     |

**Figure 1A. Function Output Evolution (Weeks 1–8)**

<img width="1149" height="1369" alt="Figure 1A  Function Output Evolution (Weeks 1–8)" src="https://github.com/user-attachments/assets/22c651d8-0b2d-4f75-9b2b-54f36bef4994" />


**Figure 1B. Week 08 Function Performance Ranking**

<img width="1024" height="1536" alt="Figure 1B  Week 08 Function Performance Ranking" src="https://github.com/user-attachments/assets/b19f9170-957c-4b04-a62f-54de0c690d43" />

## 3. Comparison of Week 07 and Week 08 Performance

## 3. Comparison of Week 07 and Week 08 Performance

A comparison of the Week 07 and Week 08 results showed that the optimisation process continued to produce useful evidence across the eight hidden objective functions. Some functions improved clearly, while others remained stable or moved into less favourable regions. These changes helped distinguish between functions suitable for continued exploitation, functions requiring targeted refinement and functions that still needed broader exploration.

Function 5 remained the strongest performer. Its output increased from 4278.816638076986 in Week 07 to 4359.384134322703 in Week 08, an absolute increase of 80.567496245717. This continued improvement confirmed that the selected search region remained productive and supported further exploitation through small, controlled adjustments around the current best-performing region.

Function 2 showed the largest relative improvement, increasing from 0.2399291698606551 to 0.5672775862793291. The absolute increase was 0.3273484164186740, representing an improvement of 136.43543909595895579217187763774038426525282470407 per cent relative to the Week 07 value. This result suggested that the revised query had moved into a more favourable region and that further local refinement could be worthwhile.

Function 7 also improved, rising from 1.1543358123792982 in Week 07 to 1.3346391663186332 in Week 08. The increase of 0.1803033539393350 indicated that the function remained within a productive region and continued to respond positively to local refinement. Function 8 remained highly stable, although its output decreased slightly from 9.49476 to 9.47621. The reduction of 0.01855 was small and did not alter its position as the second highest-performing function.

The negative functions showed less favourable movement. Function 3 decreased from -0.09116928906376276 to -0.0991107637427902, while Function 4 decreased from -10.745961383135121 to -12.305008897187289. Function 6 changed only slightly from -1.119713499832813 to -1.1197178425911847, indicating near stability within a negative region. These results suggested that the Week 08 queries for Functions 3, 4 and 6 did not identify stronger locations and that their future search strategy should be reviewed carefully.

Function 1 produced exactly the same output as in Week 07, remaining at -1.4546199699251391e-58. This confirmed that the current search region continued to provide almost no measurable improvement. Further exploration remained necessary to determine whether more productive regions existed elsewhere in the search space.

Overall, the Week 08 comparison strengthened confidence in continued exploitation of Function 5 and refinement of Functions 2 and 7. Function 8 remained suitable for monitoring and limited refinement because of its stable high performance. Functions 3, 4 and 6 required reassessment following their negative or unchanged movement, while Function 1 remained the principal exploration target.

**Figure 1C. Week 07 vs Week 08 Comparison Dashboard**

<img width="1536" height="1024" alt="Figure 1C  Week 07 vs Week 08 Comparison Dashboard" src="https://github.com/user-attachments/assets/5e6492b2-8326-4a61-8630-b2c3c6d5ec5e" />

## 4. Query Selection Strategy

The Week 08 query selection strategy was guided by the evidence gathered during the previous seven optimisation rounds. By this stage of the challenge, enough information had been collected to distinguish between functions that consistently produced strong objective values, functions that continued to improve gradually, and functions that remained uncertain. Rather than distributing the available queries evenly across all functions, greater emphasis was placed on those most likely to provide useful optimisation gains.

Function 5 remained the highest priority because it had consistently produced the strongest objective values throughout the optimisation process. The increase from **4278.816638076986** in Week 07 to **4359.384134322703** in Week 08 confirmed that the selected search region continued to contain a productive optimum. As a result, continued exploitation using carefully controlled local adjustments remained the most appropriate strategy for maximising further improvement.

Functions 2, 7 and 8 remained within productive regions of the search landscape and therefore continued to receive targeted refinement. Function 2 showed a substantial improvement compared with Week 07, suggesting that the revised query had identified a more favourable location. Functions 7 and 8 remained stable despite relatively small changes in objective value, indicating that these regions continued to perform reliably while still offering opportunities for incremental optimisation.

Functions 3, 4 and 6 continued to require refinement despite remaining within negative regions of the objective space. Although their outputs did not yet approach the highest-performing functions, continued sampling within neighbouring regions remained appropriate because previous optimisation rounds had demonstrated gradual improvement. Controlled refinement offered the best opportunity to identify more favourable local regions without abandoning potentially informative areas of the search space.

Function 1 again produced an output effectively equal to zero and continued to provide little evidence of a productive search region. Rather than investing additional exploitation effort, continued exploration remained the preferred strategy. Sampling new regions of the search space offered the greatest opportunity to reduce uncertainty and determine whether undiscovered productive regions remained available.

Overall, the Week 08 query selection strategy reflected a balanced and evidence-based optimisation approach. Continued exploitation of Function 5 was combined with targeted refinement of Functions 2, 3, 4, 6, 7 and 8, while Function 1 remained the primary exploration target. This allocation of the available query budget aimed to maximise optimisation performance while continuing to improve understanding of the hidden objective functions.

**Figure 2. Exploration, Refinement and Exploitation Strategy**

<img width="1536" height="1024" alt="Figure 2  Exploration, Refinement and Exploitation Strategy" src="https://github.com/user-attachments/assets/b5ec6ce2-6e4a-4aca-842d-dbb6b00eee82" />

## 5. Exploration vs Exploitation Analysis

Maintaining an appropriate balance between exploration and exploitation remained a central objective throughout Week 08. As more information became available from successive optimisation rounds, confidence in several search regions continued to increase, allowing greater emphasis to be placed on functions that consistently produced strong objective values while still reserving part of the available query budget for reducing uncertainty.

Function 5 continued to justify an exploitative strategy. Its objective value increased from **4278.816638076986** in Week 07 to **4359.384134322703** in Week 08, extending its position as the strongest performing function. The continued improvement suggested that the surrounding search region remained highly productive and that further local refinement was more likely to generate additional gains than broad exploration elsewhere.

Refinement remained appropriate for Functions 2, 3, 4, 6, 7 and 8. Function 2 produced the largest relative improvement of the week, demonstrating that careful adjustment of the query location could reveal more productive regions. Functions 7 and 8 remained stable within positive regions, supporting continued local refinement rather than extensive exploration. Although Functions 3, 4 and 6 remained negative, previous optimisation rounds had demonstrated gradual changes in their behaviour, indicating that further targeted refinement could continue to improve understanding of these regions.

Exploration continued to focus primarily on Function 1. Despite repeated sampling, the function again returned an output effectively equal to zero. Rather than abandoning the function, continued exploration remained appropriate because the current evidence suggested that productive regions had not yet been identified. Exploring alternative areas of the search space offered the greatest opportunity to reduce uncertainty and improve future optimisation performance.

The Week 08 optimisation strategy therefore reflected a measured balance between exploiting well-established productive regions and continuing to gather information where uncertainty remained. This approach maximised the likelihood of improving the overall optimisation objective while ensuring that computational effort was not concentrated exclusively on a single function. As the search progressed, each additional optimisation round contributed new evidence that refined the understanding of the hidden objective functions and strengthened confidence in future query selection.

**Figure 2A. Exploration vs Exploitation Balance (Week 08)**

<img width="1536" height="1024" alt="Figure 2A  Exploration vs Exploitation Balance (Week 08)" src="https://github.com/user-attachments/assets/9387d32f-37a5-460b-b73c-78067b3a852e" />

## 6. Reflection on Week 09 Query Selection

The Week 08 optimisation results provided a stronger evidence base for planning the next round of query selection. With eight optimisation rounds completed, the behaviour of several functions had become increasingly consistent, allowing future queries to be selected with greater confidence. The emphasis was no longer on broad exploration across all functions but on allocating the limited query budget according to the observed performance and expected information gain of each objective function.

Function 5 remained the highest priority for Week 09. Its continued improvement, reaching **4359.384134322703**, confirmed that the current search region continued to produce the strongest objective values. Further local refinement around the existing optimum offered the greatest opportunity for additional improvement while carrying relatively low uncertainty.

Function 2 demonstrated a substantial improvement during Week 08, suggesting that the revised query had successfully identified a more productive region. This function therefore became a strong candidate for continued refinement during Week 09. Functions 7 and 8 also remained within stable, productive regions and continued to justify carefully controlled local refinement rather than extensive exploration.

Functions 3, 4 and 6 remained below zero despite previous improvements. Although their current performance was less favourable, the gradual changes observed over successive optimisation rounds suggested that useful information could still be obtained through targeted refinement. Careful adjustment of future queries within neighbouring regions may reveal more productive areas while improving understanding of these parts of the search landscape.

Function 1 continued to produce values effectively equal to zero and remained the least understood objective function. The lack of measurable progress suggested that the current search region was unlikely to contain a productive optimum. For this reason, broader exploration remained the most appropriate strategy during Week 09. Sampling alternative regions offered the greatest opportunity to reduce uncertainty and potentially identify previously undiscovered areas of higher performance.

Overall, the Week 08 results reinforced the value of an evidence-based optimisation strategy. Continued exploitation of Function 5, targeted refinement of Functions 2, 3, 4, 6, 7 and 8, and continued exploration of Function 1 provided a balanced approach that aimed to maximise optimisation performance while continuing to improve understanding of the hidden objective functions.

**Figure 3. Function Classification Matrix (Week 08)**

<img width="1536" height="1024" alt="Figure 3  Function Classification Matrix (Week 08)" src="https://github.com/user-attachments/assets/76e380fd-24e1-4cf3-86f6-0475d2bbc3b1" />

## 7. Functional Ranking Evolution

The Week 08 results provided a clearer view of how the relative performance of the eight objective functions had changed after eight optimisation rounds. Ranking the functions by their current objective values helped separate consistently productive regions from areas that remained uncertain or difficult to optimise.

Function 5 retained first position with an output of **4359.384134322703**. Its continued dominance confirmed that the current search region remained the strongest identified area within the optimisation landscape. The function had now produced the highest output across successive rounds, supporting continued exploitation through small local adjustments.

Function 8 remained in second position with an output of **9.47621**. Although its value decreased slightly from Week 07, the change was small and did not affect its ranking. Function 7 retained third place and improved from **1.1543358123792982** to **1.3346391663186332**, reinforcing its position as a stable positive performer.

Function 2 remained in fourth position but showed a marked improvement, increasing from **0.2399291698606551** to **0.5672775862793291**. This increase strengthened confidence that the revised query had identified a more productive local region and supported continued refinement during the next optimisation round.

Function 1 remained close to zero and occupied fifth position because its output was still greater than the three negative functions. Its rank did not indicate meaningful optimisation progress. The result instead reflected its near-zero value and the absence of a stronger response from the current search region.

Functions 3, 6 and 4 remained in the lower positions. Function 3 ranked sixth with **-0.0991107637427902**, Function 6 ranked seventh with **-1.1197178425911847**, and Function 4 ranked eighth with **-12.305008897187289**. Function 4 showed the weakest Week 08 output and required careful reassessment of the surrounding search region.

Overall, the Week 08 ranking remained stable at the top, with Functions 5, 8 and 7 continuing to lead. Function 2 showed the most encouraging upward movement in performance, while Functions 3, 4 and 6 remained priorities for further refinement. Function 1 continued to require broad exploration because its near-zero output provided little information about potentially productive regions elsewhere in the search space.

**Figure 3A. Functional Ranking Evolution (Weeks 1–8)**

<img width="1536" height="1024" alt="Figure 3A  Functional Ranking Evolution (Weeks 1–8)" src="https://github.com/user-attachments/assets/6beb06b3-dc34-4379-9ab9-f507adcdd0e2" />


## 8. High Performing Region Identification

Identifying productive regions within the hidden search landscape remained one of the primary objectives of the Bayesian Black Box Optimisation process. After eight optimisation rounds, the accumulated evidence provided a clearer picture of where the highest objective values were being generated and where additional investigation was still required. This growing understanding enabled future queries to be directed towards regions with the greatest optimisation potential while reducing unnecessary exploration.

Function 5 continued to represent the strongest high-performing region identified during the project. Its objective value increased from **4278.816638076986** in Week 07 to **4359.384134322703** in Week 08, extending the consistent upward trend observed over previous optimisation rounds. The continued improvement indicated that the surrounding search region remained highly productive and justified continued exploitation using carefully controlled local adjustments.

Function 8 remained the second strongest region despite a small reduction in objective value from **9.494760** to **9.47621**. This minor change did not alter the overall interpretation of the function, which continued to demonstrate stable performance and low uncertainty. Function 7 also remained within a productive region, improving from **1.1543358123792982** to **1.3346391663186332**, suggesting that neighbouring areas continued to provide reliable optimisation opportunities.

Function 2 demonstrated a marked improvement during Week 08, increasing from **0.2399291698606551** to **0.5672775862793291**. This improvement suggested that the revised query had identified a more favourable part of the search space and that additional local refinement could produce further gains. Although its objective value remained considerably lower than those of Functions 5 and 8, the positive trend strengthened confidence in the surrounding region.

The remaining functions continued to provide valuable information despite producing lower objective values. Functions 3, 4 and 6 remained within negative regions but contributed to a better understanding of the underlying search landscape through continued refinement. Function 1 again returned an output effectively equal to zero, indicating that the current search region remained unproductive and that broader exploration continued to be the most appropriate strategy.

Overall, the Week 08 results strengthened confidence in the high-performing regions already identified while providing further evidence to guide future optimisation decisions. Continued exploitation of Function 5, local refinement around Functions 2, 7 and 8, and careful investigation of the remaining functions represented a balanced strategy for improving optimisation performance while expanding knowledge of the hidden objective functions.

**Figure 4. Function 5 Optimisation Progress (Weeks 1–8)**

<img width="1536" height="1024" alt="Figure 4  Function 5 Optimisation Progress (Weeks 1–8)" src="https://github.com/user-attachments/assets/efa7f2ae-2ee4-4185-92ba-f6ac7f0d1608" />


**Best Function: F5**

<img width="1086" height="1448" alt="Best Function F5" src="https://github.com/user-attachments/assets/44f75f79-c76c-4eba-b89a-ab803a1d1ca9" />


**Highest Output: 4359.384134322703**

<img width="1024" height="1536" alt="Highest Output 4359 384134322703" src="https://github.com/user-attachments/assets/934e5eaf-51aa-49d8-a2f3-9c3e81aa972e" />









