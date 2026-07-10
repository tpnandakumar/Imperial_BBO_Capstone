# Week_07

## Bayesian Black Box Optimisation Portfolio
### Week 07 Analysis

## Contents

1. Introduction
2. Week 7 Results
3. Comparison of Week 6 and Week 7 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 7 Query Selection
7. Functional Ranking Evolution
8. High Performing Regions
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References

## 1. Introduction

Week 07 represented another important stage in the Bayesian Black Box Optimisation (BBO) challenge. By this point, six optimisation rounds had been completed, providing a richer collection of observations from which to evaluate the behaviour of the eight unknown objective functions. The additional data enabled more informed decision making, improved confidence in query selection and a clearer understanding of the underlying search landscape.

The optimisation strategy continued to balance exploration of uncertain regions with exploitation of previously identified high-performing areas. Rather than relying on intuition, query selection was guided by evidence accumulated across successive optimisation rounds. This progressive approach increased confidence as additional observations reduced uncertainty surrounding the hidden objective functions and identified regions with greater optimisation potential.

The Week 07 results provided an opportunity to compare performance with Week 06 and evaluate whether previous optimisation decisions continued to improve objective values. Particular attention was given to identifying functions demonstrating sustained improvement, stable behaviour or persistent uncertainty. These observations informed the allocation of future query resources and supported planning for the Week 08 optimisation round.

This repository documents the complete Week 07 optimisation workflow, including performance analysis, comparison with previous weeks, query selection strategy, exploration versus exploitation analysis, functional ranking, computational implementation and repository organisation. Together, these analyses provide a transparent and reproducible record of the optimisation process while supporting continued refinement of the Bayesian Black Box Optimisation strategy.


## 2. Week 7 Results

Week 07 provided further evidence regarding the behaviour of the eight unknown objective functions. The additional optimisation round expanded the available dataset and strengthened understanding of the hidden search landscape. While several functions demonstrated continued improvement, others remained stable or exhibited greater uncertainty, providing valuable guidance for future query selection.

Function 5 continued to produce the highest objective value, increasing from 3922.765223 in Week 06 to 4278.816638 in Week 07. This sustained improvement reinforced confidence that the optimisation strategy had identified a productive search region suitable for continued exploitation. In contrast, Function 2 decreased from 0.571248 in Week 06 to 0.239929 in Week 07, suggesting that the previous search region did not consistently maintain its earlier performance and should be reassessed.

Function 8 remained highly stable despite a slight decrease from 9.514800 in Week 06 to 9.494760 in Week 07, while Function 7 maintained positive performance despite declining from 1.352949 to 1.154336. These results suggested that both functions continued to occupy relatively stable regions of the search space where limited local refinement remained appropriate.

Conversely, Functions 3, 4 and 6 remained negative. Function 3 improved substantially from -0.307182 in Week 06 to -0.091169 in Week 07, moving much closer to zero. Function 4 improved markedly from -31.203478 to -10.745961, although it remained the lowest-performing function overall. Function 6 also showed modest improvement, changing from -1.379227 to -1.119713, indicating gradual progress despite remaining within a negative region of the search landscape.

Overall, the Week 07 results demonstrated continued progress in understanding the hidden objective functions. The evidence obtained from this optimisation round strengthened confidence in exploiting high-performing regions, particularly for Function 5, supported continued refinement of Functions 3, 4 and 6, confirmed the stability of Functions 7 and 8, and highlighted the need to reassess Function 2 before the next optimisation round.

| Function   |          Week 07 Output | Interpretation                                                 |
| ---------- | ----------------------: | -------------------------------------------------------------- |
| Function 1 | -1.4546199699251391e-58 | Remained close to zero, indicating continued uncertainty       |
| Function 2 |                0.239929 | Declined from Week 06, requiring reassessment                  |
| Function 3 |               -0.091169 | Significant improvement, moving closer to zero                 |
| Function 4 |              -10.745961 | Largest improvement among the negative functions               |
| Function 5 |             4278.816638 | Highest performing function, supporting continued exploitation |
| Function 6 |               -1.119713 | Continued improvement within a negative region                 |
| Function 7 |                1.154336 | Stable positive performance despite a small reduction          |
| Function 8 |                9.494760 | Stable high performance with only a minor decrease             |


**Figure 1A. Function Output Evolution (Weeks 1 to 7)**


<img width="1536" height="1024" alt="Figure 1A  Function Output Evolution (Weeks 1–7)" src="https://github.com/user-attachments/assets/af939cec-956b-44a0-bceb-df2e94b94bce" />

**Figure 1B  Function Performance Ranking**

<img width="1536" height="1024" alt="Figure 1B  Function Performance Ranking" src="https://github.com/user-attachments/assets/bc06ae31-5d24-4096-832d-cd43018805e0" />


## 3. Comparison of Week 6 and Week 7 Performance

A comparison between the Week 06 and Week 07 results demonstrated that the optimisation strategy continued to improve understanding of the hidden search landscape while refining the balance between exploration and exploitation. The most significant improvement was observed in Function 5, which increased from 3922.765223 in Week 06 to 4278.816638 in Week 07. This sustained upward trend provided strong evidence that the selected query region contained a highly productive optimum and justified continued exploitation.

Functions 3, 4 and 6 also demonstrated meaningful improvement. Function 3 improved from -0.307182 to -0.091169, moving considerably closer to zero. Function 4 improved substantially from -31.203478 to -10.745961, indicating that the revised query identified a more favourable region despite remaining the lowest-performing function. Function 6 improved from -1.379227 to -1.119713, suggesting gradual progress within a previously difficult search region.

In contrast, Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous optimisation gains were not maintained. Function 7 also declined from 1.352949 to 1.154336, while Function 8 remained highly stable despite a slight reduction from 9.514800 to 9.494760. These observations suggested that Functions 7 and 8 continued to occupy productive regions of the search space where only limited local refinement was required.

Overall, the comparison between Week 06 and Week 07 demonstrated increasing confidence in the optimisation strategy. The results supported continued exploitation of Function 5, targeted refinement of Functions 3, 4 and 6, reassessment of Function 2 following its decline, and continued monitoring of the stable high-performing regions represented by Functions 7 and 8. These observations provided a stronger evidence base for planning the Week 08 optimisation strategy.

**Figure 1C. Comparison of Week 6 and Week 7 Performance**


<img width="1536" height="1024" alt="Figure 1C  Week 06 vs Week 07 Comparison Dashboard" src="https://github.com/user-attachments/assets/9c45c6bc-cfe9-4e49-a8d0-bc6950666436" />



## 4. Query Selection Strategy

The Week 07 query selection strategy was guided by evidence accumulated during the previous six optimisation rounds. Sufficient information had been collected to distinguish between functions that required continued exploitation, targeted refinement or broader exploration. This evidence-based approach improved allocation of the limited query budget while increasing confidence in subsequent optimisation decisions.

Function 5 remained the highest priority for exploitation because it had consistently produced the strongest objective values throughout the optimisation process. The sustained improvement observed during previous optimisation rounds indicated that the selected search region remained highly productive. Consequently, only small local adjustments were selected to maximise further performance while remaining close to the established optimum.

Functions 2, 7 and 8 demonstrated stable positive performance during the previous optimisation rounds and were therefore selected for local refinement. Their objective values suggested that the surrounding search regions remained productive and that carefully controlled adjustments could produce additional optimisation gains while confirming the stability of the identified regions.

Functions 1, 3, 4 and 6 continued to exhibit greater uncertainty before Week 07. Function 1 remained close to zero, while Functions 3, 4 and 6 continued to produce negative objective values after Week 06. These observations indicated that broader exploration remained appropriate in order to improve understanding of the hidden search landscape and identify alternative productive regions.

Overall, the Week 07 query selection strategy reflected a balanced optimisation framework that allocated computational resources according to observed performance, confidence and expected information gain. The strategy prioritised exploitation of the strongest performing region, refinement of stable positive regions and continued exploration of uncertain regions, providing a structured foundation for the Week 07 optimisation round.

**Figure 2 – Exploration, Refinement and Exploitation Strategy**

<img width="1536" height="1024" alt="Figure 2  Exploration, Refinement and Exploitation Strategy" src="https://github.com/user-attachments/assets/3080ebab-4a52-4799-8b58-75bec6ca13cd" />


## 5. Exploration vs Exploitation Analysis

A successful Bayesian Black Box Optimisation strategy requires an appropriate balance between exploration and exploitation. Exploration focuses on sampling uncertain regions of the search space to identify previously undiscovered high-performing solutions, whereas exploitation concentrates on refining known productive regions to maximise objective values. Maintaining this balance remained a central objective throughout the Week 07 optimisation process.

The Week 07 results demonstrated that Function 5 continued to outperform all other functions, increasing from 3922.765223 in Week 06 to 4278.816638 in Week 07. This sustained improvement provided strong evidence that the surrounding search region remained highly productive. Consequently, Function 5 continued to receive the highest exploitation priority through small local adjustments designed to maximise further performance while remaining close to the identified optimum.

Functions 3, 4 and 6 also demonstrated encouraging improvement during Week 07. Function 3 improved from -0.307182 to -0.091169, moving considerably closer to zero. Function 4 improved substantially from -31.203478 to -10.745961, while Function 6 improved from -1.379227 to -1.119713. These observations suggested that refinement within previously uncertain regions was beginning to identify more favourable areas of the search landscape while reducing uncertainty.

Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous optimisation gains were not maintained and that the corresponding search region required reassessment. Functions 7 and 8 remained stable despite small reductions in objective value. Function 7 decreased from 1.352949 to 1.154336, while Function 8 changed only slightly from 9.514800 to 9.494760. These observations suggested that both functions remained within productive regions where only limited local refinement was likely to be beneficial.

Overall, the Week 07 results demonstrated that optimisation performance improved when computational resources were allocated according to observed evidence rather than uniformly across all functions. Continued exploitation of the highly productive region identified for Function 5, targeted refinement of improving functions, reassessment of declining performance and exploration of uncertain regions increased both optimisation performance and understanding of the hidden objective functions.

**Figure 2A – Exploration vs Exploitation Balance**

<img width="1536" height="1024" alt="Figure 2A  Exploration vs Exploitation Balance" src="https://github.com/user-attachments/assets/5206164f-2d57-46de-b77f-78e8251fa850" />


Week 07 Strategy


Exploit:
F5

Refine:
F3, F4, F6

Monitor:
F7, F8

Reassess:
F2

Explore:
F1

Goal:
Maximise optimisation performance while balancing exploitation, targeted refinement and information gain.



## 6. Reflection on Week 7 Query Selection

The Week 07 query selection process was guided by evidence accumulated throughout the previous six optimisation rounds. Rather than selecting query locations randomly, each decision was informed by observed objective values, functional rankings, performance trends and confidence assessments derived from earlier optimisation results. This evidence-based strategy aimed to allocate the limited query budget towards regions most likely to improve optimisation performance while continuing to reduce uncertainty within the hidden search landscape.

Function 5 remained the highest priority for continued exploitation. The objective value increased from 3922.765223 in Week 06 to 4278.816638 in Week 07, representing the strongest performance among all eight functions. This sustained improvement confirmed that the selected search region continued to contain a highly productive optimum and justified maintaining only small local refinements around the current solution.

Functions 3, 4 and 6 also demonstrated encouraging progress. Function 3 improved from -0.307182 to -0.091169, moving substantially closer to zero. Function 4 improved from -31.203478 to -10.745961, representing the largest improvement among the negative functions despite remaining the lowest-performing objective. Function 6 improved from -1.379227 to -1.119713, indicating that refinement within previously uncertain regions was producing measurable progress.

Not all optimisation decisions produced improved outcomes. Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous search region had not consistently maintained its earlier performance. Functions 7 and 8 remained comparatively stable despite small reductions in objective value. Function 7 decreased from 1.352949 to 1.154336, while Function 8 changed only slightly from 9.514800 to 9.494760. These results suggested that both functions remained close to productive regions where only limited local refinement was required.

Overall, the Week 07 results reinforced the value of an evidence-based optimisation strategy. The observations supported continued exploitation of the highly productive region identified for Function 5, targeted refinement of improving functions, reassessment of Function 2 following its decline, and continued exploration of uncertain regions. This balanced allocation of computational resources strengthened understanding of the hidden objective functions while improving optimisation performance.

**Figure 3 – Function Classification Matrix**

<img width="1536" height="1024" alt="Figure 3  Function Classification Matrix" src="https://github.com/user-attachments/assets/bca78aaa-0ebc-4f16-8379-f9e9c1f9771a" />


Week 07 Strategy

This better matches the Week 7 results:

F5 improved strongly.
F3, F4 and F6 all improved.
F7 and F8 remained stable with small declines.
F2 regressed and therefore required reassessment rather than simple refinement.
F1 remained close to zero and contributed little new information.

Objective:
Maximise optimisation performance while balancing exploitation, targeted refinement and information gain.

## 7. Functional Ranking Evolution

Ranking the objective functions after seven completed optimisation rounds provided a comprehensive measure of optimisation progress and revealed how the relative performance of the eight unknown objective functions evolved as additional evidence became available. Monitoring ranking stability assisted in identifying functions suitable for continued exploitation, targeted refinement and broader exploration.

Function 5 retained the highest ranking throughout Week 07. The objective value increased from 3922.765223 in Week 06 to 4278.816638 in Week 07, reinforcing confidence that the optimisation process had identified a highly productive search region. This sustained improvement justified continued exploitation through carefully controlled local refinement.

Function 8 remained the second highest-ranked function despite a slight decrease from 9.514800 in Week 06 to 9.494760 in Week 07. The small reduction demonstrated excellent stability and indicated that the surrounding search region remained reliable and suitable for continued refinement. Function 7 maintained third position despite decreasing from 1.352949 to 1.154336, continuing to demonstrate consistently positive performance across successive optimisation rounds.

Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07. Although this reduced its relative performance, the function remained positive and continued to warrant further investigation. In contrast, Functions 3, 4 and 6 all demonstrated measurable improvement. Function 3 improved from -0.307182 to -0.091169, Function 4 improved substantially from -31.203478 to -10.745961, and Function 6 improved from -1.379227 to -1.119713, indicating that refinement within these regions was producing meaningful progress.

Function 1 remained close to zero throughout Week 07 and continued to provide limited evidence regarding the underlying search landscape. Although it neither improved nor deteriorated substantially, continued exploratory sampling remained appropriate to determine whether more productive regions existed elsewhere within the search space.

Overall, the Week 07 functional rankings demonstrated increasing separation between consistently productive regions and more uncertain regions of the search landscape. The ranking evolution provided an objective framework for allocating optimisation resources while maintaining an effective balance between exploitation, targeted refinement and exploration.

**Figure 3A – Functional Ranking Evolution**

<img width="1536" height="1024" alt="Figure 3A  Functional Ranking Evolution" src="https://github.com/user-attachments/assets/13b77be7-8ed3-424f-b0d7-84f4970487a4" />

Week 07 Functional Ranking

Exploit:
F5

Refine:
F2, F7, F8

Explore:
F1, F3, F4, F6

Ranking stability increased confidence in optimisation decisions while identifying functions requiring continued exploration.


## 8. High Performing Regions

Identifying high-performing regions remained one of the primary objectives of the Bayesian Black Box Optimisation process. After six completed optimisation rounds, sufficient evidence had been accumulated to distinguish between productive search regions that consistently generated strong objective values and uncertain regions requiring further investigation. This information provided the foundation for selecting the Week 07 queries and allocating the limited query budget more efficiently.

Function 5 continued to represent the strongest high-performing region within the search landscape. The objective value increased from 3922.765223 in Week 06 to 4278.816638 in Week 07, confirming that the selected query region remained highly productive. The sustained improvement observed across successive optimisation rounds indicated that local refinement remained the most appropriate strategy for maximising objective values while remaining close to the identified optimum.

Functions 3, 4 and 6 also demonstrated encouraging optimisation behaviour during Week 07. Function 3 improved from -0.307182 to -0.091169, moving considerably closer to zero. Function 4 improved substantially from -31.203478 to -10.745961, while Function 6 improved from -1.379227 to -1.119713. These observations suggested that refinement within previously uncertain regions was identifying more favourable areas of the hidden search landscape while reducing uncertainty.

In contrast, Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous improvement had not been maintained and that the corresponding search region required reassessment. Functions 7 and 8 remained stable despite small reductions in objective value. Function 7 decreased from 1.352949 to 1.154336, while Function 8 changed only slightly from 9.514800 to 9.494760. These observations suggested that both functions remained within productive regions where only limited local refinement was likely to be beneficial.

Overall, the identification of high-performing regions provided an evidence-based framework for guiding future optimisation decisions. Concentrating computational effort on the most productive regions, refining improving search areas, reassessing declining performance and continuing to investigate uncertain regions increased optimisation efficiency while maximising the information gained from the available query budget.

**Figure 4 – Function 5 Optimisation Progress**

<img width="1536" height="1024" alt="Figure 4  Function 5 Optimisation Progress" src="https://github.com/user-attachments/assets/ec289f3d-20e4-4aca-b4fd-a0c238d19169" />

**Best Function: F5**
<img width="1024" height="1536" alt="Best Function F5" src="https://github.com/user-attachments/assets/04b78bd6-abf4-4845-807e-2a994eb876b1" />

**Highest Output: 4278.816638**

<img width="1086" height="1448" alt="Highest Output 4278 816638" src="https://github.com/user-attachments/assets/bf8026ab-c2bb-488f-83dc-5b7a11e4ebf1" />

**Most Improved: F4**
<img width="1149" height="1369" alt="Most Improved F4" src="https://github.com/user-attachments/assets/0b776a4b-2044-49ad-adf7-c517e5d02adf" />

**Stable High Performance: F7, F8
<img width="1198" height="1313" alt="Stable High Performance F7, F8" src="https://github.com/user-attachments/assets/94d55bdc-4424-41ad-8768-ffbadb684395" />

**Needs Reassessment: F2**

<img width="1149" height="1369" alt="Needs Reassessment F2" src="https://github.com/user-attachments/assets/7b2049d5-8b93-4301-a961-37d27b9e9273" />

**Continue Exploration: F1**

<img width="1024" height="1536" alt="Continue Exploration F1" src="https://github.com/user-attachments/assets/81314370-188f-4a03-9171-4253547741cd" />

**Continue Refinement: F3, F4, F6**

<img width="1536" height="1024" alt="Continue Refinement F3, F4, F6" src="https://github.com/user-attachments/assets/13098fb8-7273-4655-972e-083c9989ef4d" />


Week 07 High Performing Regions

Exploit:
F5

Refine:
F3, F4, F6

Monitor:
F7, F8

Reassess:
F2

Explore:
F1

High-performing regions became increasingly well defined following the Week 07 optimisation results. Function 5 remained the dominant region for continued exploitation, while Functions 3, 4 and 6 demonstrated encouraging improvement through targeted refinement. Functions 7 and 8 remained stable high-performing regions requiring only limited local adjustment, whereas Function 2 required reassessment following a reduction in objective value. Function 1 remained suitable for continued exploration because the search landscape surrounding this function remained largely uninformative.


## 9. Decision Matrix and Resource Allocation

The allocation of query resources during Week 07 was determined by objective performance, confidence assessment and expected information gain. After six completed optimisation rounds, sufficient evidence had been collected to distinguish between functions requiring continued exploitation, targeted refinement and broader exploration. This evidence based allocation improved the efficiency of the limited query budget while supporting continued optimisation progress.

Function 5 remained the highest priority for exploitation because it consistently produced the strongest objective values. The increase from 3922.765223 in Week 06 to 4278.816638 in Week 07 confirmed that the current search region continued to provide the greatest optimisation potential. Query allocation therefore focused on small local adjustments designed to maximise further performance while maintaining convergence within this highly productive region.

Functions 3, 4 and 6 demonstrated encouraging improvement during Week 07 and therefore became priorities for continued refinement. Function 3 improved from -0.307182 to -0.091169, Function 4 improved substantially from -31.203478 to -10.745961, and Function 6 improved from -1.379227 to -1.119713. These improvements suggested that continued refinement within these regions could further increase optimisation performance while reducing uncertainty.

Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous optimisation gains were not maintained and that the search strategy required reassessment. Functions 7 and 8 remained stable despite small reductions in objective value. Function 7 decreased from 1.352949 to 1.154336, while Function 8 changed only slightly from 9.514800 to 9.494760. These observations suggested that both functions remained within productive regions where only limited local refinement was necessary. Function 1 remained close to zero throughout the optimisation process and continued to require exploratory sampling to improve understanding of the underlying search landscape.

Overall, the Week 07 decision matrix demonstrated that effective optimisation depended upon allocating computational resources according to observed evidence rather than distributing queries equally across all functions. Continued exploitation of Function 5, targeted refinement of improving functions, reassessment of declining performance and exploration of uncertain regions maintained an effective balance between optimisation performance and information gain.

**Figure 4A – Resource Allocation Decision Matrix**


<img width="1536" height="1024" alt="Figure 4A  Resource Allocation Decision Matrix" src="https://github.com/user-attachments/assets/6e35bec0-0b85-425f-9d1e-a66a40a6cf31" />


Week 07 Resource Allocation

Highest Priority:
F5

Refinement Priority:
F3, F4, F6

Monitoring Priority:
F7, F8

Reassessment Priority:
F2

Exploration Priority:
F1

Objective:
Allocate computational effort according to observed performance, optimisation progress, confidence and expected information gain while maintaining an appropriate balance between exploitation, refinement and exploration.


## 10. Information Gain Analysis

Information gain remained a key objective throughout the Week 07 optimisation process because every query contributed additional knowledge about the hidden objective functions. Rather than evaluating optimisation progress solely through objective values, Week 07 also considered how each query reduced uncertainty and improved understanding of the underlying search landscape. This evidence supported more effective query selection and increased confidence in subsequent optimisation decisions.

Function 5 continued to provide the greatest information gain by consistently producing higher objective values within the same productive search region. The increase from 3922.765223 in Week 06 to 4278.816638 in Week 07 confirmed that the surrounding landscape remained favourable for continued local refinement. This strengthened confidence in exploiting the current optimum while reducing uncertainty regarding the behaviour of this region.

Functions 3, 4 and 6 also generated valuable information through measurable improvement during Week 07. Function 3 moved substantially closer to zero, Function 4 demonstrated the largest improvement among the negative functions, and Function 6 improved from -1.379227 to -1.119713. These observations indicated that refinement within previously uncertain regions was improving understanding of the hidden search landscape while identifying more favourable search locations.

Function 2 declined from 0.571248 in Week 06 to 0.239929 in Week 07, indicating that the previous optimisation gains were not maintained. This outcome provided valuable information by identifying a less reliable region of the search landscape and highlighting the need for reassessment. Functions 7 and 8 remained stable despite small reductions in objective value. Their consistent performance confirmed that these regions remained reliable and required only limited local refinement.

Overall, the Week 07 information gain analysis demonstrated that optimisation success depended upon both improving objective values and reducing uncertainty across the hidden search landscape. Continued exploitation of productive regions, targeted refinement of improving search areas, reassessment of declining performance and exploration of uncertain regions increased both optimisation performance and understanding of the underlying objective functions.
**Figure 5 – Information Gain Summary**


<img width="1536" height="1024" alt="Figure 5  Information Gain Summary" src="https://github.com/user-attachments/assets/199eb012-ce90-49c1-a9a9-b313e06e91c7" />


Week 07 Information Gain

Highest Learning:
F5

Increasing Confidence:
F3, F4, F6

Stable Knowledge:
F7, F8

Reassessment Required:
F2

Reducing Uncertainty:
F1

Objective:
Maximise knowledge while improving optimisation performance through evidence based exploitation, targeted refinement and continued exploration.


## 11. Computational Analysis and Coding Implementation

The computational analysis performed during Week 07 transformed optimisation data into structured evidence that supported objective decision making. Python scripts were developed to process input queries and optimisation results, calculate performance rankings, classify optimisation strategies and support the generation of summary outputs suitable for documentation and future analysis. This workflow improved reproducibility while reducing manual processing and providing a consistent analytical framework.

The Week 07 analysis script imported the optimisation inputs and objective values from structured CSV files before performing ranking and classification. Each function was ranked according to its objective value, classified according to the optimisation strategy adopted during Week 07, and evaluated according to whether the objective value was positive or negative. The resulting analysis provided a consistent framework for interpreting optimisation performance and comparing results across successive optimisation rounds.

Although the Week 07 analysis summary was prepared manually for this repository, the computational framework was designed so that future optimisation rounds could be analysed using the same Python implementation. Updating the input and result CSV files would allow the analytical workflow to be repeated while preserving a consistent computational methodology. This approach simplified repository maintenance and improved long term reproducibility.

The Python implementation also demonstrated the practical application of data analysis libraries for optimisation research. Pandas provided efficient handling of structured datasets, while standard Python functions supported data processing, ranking, classification and summary generation. The resulting workflow provided a reusable analytical foundation that supported the accompanying visualisations and written analysis.

Overall, the Week 07 computational framework demonstrated how structured computational analysis can improve the transparency, reproducibility and efficiency of Bayesian Black Box Optimisation studies. Combining structured datasets, reusable Python scripts and comprehensive documentation created a reliable foundation for analysing future optimisation rounds while maintaining a consistent analytical methodology.

**Figure 5A – Python Computational Workflow**


<img width="1024" height="1536" alt="Figure 5A  Python Computational Workflow" src="https://github.com/user-attachments/assets/cff082b9-42c6-49e7-8120-b7ab44c33c5d" />


Week 07 Computational Workflow

Inputs:
week_07_inputs.csv

Results:
week_07_results.csv

Processing:
week_07_analysis.py

Output:
week_07_analysis_summary.csv

Objective:
Create a reproducible and automated optimisation analysis workflow.



## 12. Repository Files and Reproducibility

Maintaining a well organised repository remained an important objective throughout Week 07 because it supported transparency, reproducibility and efficient project development. The repository structure was designed to separate raw optimisation data, computational analysis, documentation and visualisations into clearly defined components, allowing each stage of the optimisation workflow to be independently verified and reproduced.

The Week 07 repository contained structured input and output datasets together with reusable Python analysis scripts and comprehensive documentation. The optimisation inputs and objective values were stored as CSV files, while the accompanying Python implementation provided a consistent framework for ranking functions, classifying optimisation strategies and supporting future automated analysis. The analytical workflow was designed to produce consistent and reproducible outputs while maintaining compatibility with future automation as the repository continued to develop.

Repository documentation was expanded through a detailed README file describing each stage of the optimisation process. Written analysis was supported by figures, tables and infographics that presented optimisation trends, decision making strategies and computational workflows in a clear and reproducible format. This documentation improved the accessibility of the repository for future development, independent review and reproducibility.

Using a consistent repository structure also simplified long term maintenance. Future optimisation rounds could be incorporated by updating the input and result datasets while retaining the same computational framework and documentation structure. This approach improved scalability and supported continued development throughout the Bayesian Black Box Optimisation project.

Overall, the Week 07 repository demonstrated the importance of combining structured datasets, reusable computational tools and comprehensive documentation within a reproducible research framework. This organisation strengthened the transparency, reproducibility and long term maintainability of t

**Figure 5B – Repository Architecture**


<img width="1024" height="1536" alt="Figure 5B  Repository Architecture" src="https://github.com/user-attachments/assets/d59685f0-b7c0-4439-ab9d-edf1a2daded5" />


Week 07 Repository

Structured Data

Reusable Python

Automated Analysis

Comprehensive Documentation

Objective

Create a transparent and reproducible optimisation repository suitable for future development.


## 13. Conclusion

Week 07 represented another significant stage in the Bayesian Black Box Optimisation challenge by strengthening understanding of the hidden objective functions through evidence based optimisation. Following the completion of six optimisation rounds, the Week 07 queries provided additional evidence that further refined understanding of the hidden search landscape and increased confidence in subsequent optimisation decisions.

Function 5 continued to demonstrate exceptional optimisation performance and remained the strongest candidate for continued exploitation, achieving the highest objective value observed during the project to date. Functions 3, 4 and 6 demonstrated encouraging improvement, indicating that refinement within previously uncertain regions was producing measurable progress. Functions 7 and 8 remained stable despite small reductions in objective value, while Function 2 required reassessment following its decline in performance. Function 1 remained close to zero and continued to require exploratory sampling.

The computational workflow developed during Week 07 further improved the transparency and reproducibility of the optimisation process. Structured CSV datasets, reusable Python analysis scripts and comprehensive documentation provided a consistent framework for analysing optimisation performance while supporting future automation and continued repository development.

Overall, the Week 07 repository demonstrated that successful Bayesian Black Box Optimisation depends upon balancing exploitation, targeted refinement and exploration according to accumulated evidence rather than intuition alone. The knowledge gained during Week 07 provided a stronger foundation for planning the Week 08 optimisation strategy while continuing to improve understanding of the hidden optimisation landscape and guiding subsequent optimisation decisions.


**Overall Strategy Wheel**


<img width="1254" height="1254" alt="Overall Strategy Wheel" src="https://github.com/user-attachments/assets/1075bf5a-e9b3-4b93-b5d8-797c349091d7" />

**Key Week 07 Takeaways**


<img width="1024" height="1536" alt="Key Week 07 Takeaways" src="https://github.com/user-attachments/assets/75cd54f0-560c-4a6e-98db-addb7faa13b8" />


## 14 Automation Decision

For Week 07, the analysis summary was generated manually using week_07_analysis.py rather than through GitHub Actions. This decision was made to maintain a simple, transparent and easily verifiable workflow while the weekly Bayesian Black Box Optimisation analysis framework continued to mature.

GitHub Actions remains a planned enhancement for future development. Once the analysis script, CSV structure and repository workflow have been fully standardised across multiple optimisation rounds, automated generation of the analysis summary and associated outputs can be implemented to improve efficiency while maintaining reproducibility.


## 15. References

Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array Programming with NumPy. Nature, 585, 357–362.

Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering, 9(3), 90–95.

Jones, D. R., Schonlau, M., & Welch, W. J. (1998). Efficient Global Optimisation of Expensive Black Box Functions. Journal of Global Optimization, 13(4), 455–492.

McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, 56–61.

Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

Shahriari, B., Swersky, K., Wang, Z., Adams, R. P., & De Freitas, N. (2016). Taking the Human Out of the Loop: A Review of Bayesian Optimization. Proceedings of the IEEE, 104(1), 148–175.

Snoek, J., Larochelle, H., & Adams, R. P. (2012). Practical Bayesian Optimization of Machine Learning Algorithms. Advances in Neural Information Processing Systems, 25.

Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17, 261–272.
