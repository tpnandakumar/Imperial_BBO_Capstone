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
14. References

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

The Week 06 query selection was developed directly from the evidence obtained during the Week 05 optimisation cycle. Rather than relying on intuition, each query was selected according to the observed performance of the corresponding objective function. This ensured that the limited query budget was allocated to maximise both optimisation performance and information gain.

Function 5 remained the primary candidate for exploitation because it consistently produced the highest objective values throughout successive optimisation rounds. The Week 05 results strengthened confidence that the selected search region contained a high quality solution. Consequently, only small adjustments were introduced to maintain progress while reducing the risk of moving away from the most promising region.

Functions 7 and 8 continued to demonstrate stable positive performance and therefore remained suitable for local refinement. Minor modifications around previously successful query locations provided an opportunity to confirm the stability of these regions while identifying any incremental improvements that might further increase performance.

In contrast, Functions 1, 3, 4 and 6 continued to exhibit greater uncertainty. Their outputs suggested that the search process had not yet identified favourable regions of the search landscape. Additional exploratory sampling was therefore retained to improve understanding of these functions and increase the likelihood of locating more productive areas for future optimisation.

Overall, the Week 06 query selection reflected a progressive learning process in which each optimisation round built upon knowledge obtained from previous observations. This evidence based approach improved confidence in decision making, strengthened the balance between exploration and exploitation, and provided a more systematic framework for continuing optimisation in subsequent weeks.

**Figure 4. Reflection on Week 06 Query Selection**

<img width="1024" height="1536" alt="Figure 4 Week 06 query selection process flow" src="https://github.com/user-attachments/assets/a67f0606-01c6-43bd-a05a-1934d5d5b6e5" />

...

## 7. Functional Ranking Evolution

Ranking the objective functions after each optimisation round provided a simple method for monitoring performance trends throughout the Black Box Optimisation process. Rather than considering each function independently, the ranking system enabled direct comparison of relative performance across all eight functions and highlighted changes in optimisation priorities over successive weeks.

By Week 05, Function 5 had clearly established itself as the highest performing objective function. Its continued improvement across successive optimisation rounds demonstrated that the selected query region consistently produced superior objective values, supporting the decision to prioritise exploitation. Function 8 remained the second highest performing function, while Function 7 continued to show gradual but consistent improvement, strengthening confidence in local refinement.

Function 2 demonstrated moderate performance but exhibited greater variability than Functions 7 and 8. Although it remained a positive contributor, additional observations were required before allocating further exploitation resources. In contrast, Functions 1, 3, 4 and 6 continued to occupy the lower positions in the ranking because their outputs remained close to zero or negative, indicating that favourable search regions had not yet been identified.

Monitoring the evolution of functional rankings also provided valuable insight into the effectiveness of the optimisation strategy. Functions that consistently improved gradually moved towards higher rankings, whereas functions producing weaker responses remained candidates for continued exploration. This ranking system therefore served as an additional decision support tool for allocating future query resources.

Overall, the Week 05 functional rankings confirmed that optimisation decisions should be driven by observed performance rather than fixed assumptions. Combining functional rankings with evidence from previous optimisation rounds improved confidence in balancing exploitation of high performing functions with exploration of uncertain regions.

**Figure 5. Functional Ranking Evolution**

<img width="1536" height="1024" alt="Figure 5 Functional ranking evolution analysis" src="https://github.com/user-attachments/assets/35f09ac4-3850-46c6-9860-47021eb0cc06" />

...
## 8. High Performing Region Identification

One of the primary objectives of Bayesian Black Box Optimisation is to identify regions of the search space that consistently produce favourable objective values. Rather than focusing solely on individual outputs, the optimisation process seeks to recognise patterns that indicate where high quality solutions are most likely to be located. By Week 05, sufficient observations had been collected to begin identifying these high performing regions with greater confidence.

Function 5 provided the strongest evidence of a productive search region. Successive optimisation rounds demonstrated consistent improvements in objective value, indicating that the surrounding query space contained a promising optimum. This justified continued local exploitation through carefully controlled adjustments while maintaining proximity to the most successful query locations.

Functions 7 and 8 also demonstrated stable positive performance, suggesting that useful regions of the search landscape had been identified. Although their objective values were substantially lower than those of Function 5, their consistency indicated that further local refinement could provide incremental improvements while reducing unnecessary exploration.

Conversely, Functions 1, 3, 4 and 6 continued to exhibit greater uncertainty because their outputs remained close to zero or negative. These observations suggested that the corresponding search regions had not yet revealed favourable objective values. Continued exploration therefore remained necessary to improve understanding of these functions and identify alternative regions with greater optimisation potential.

Overall, identifying high performing regions enabled optimisation resources to be allocated more efficiently. Concentrating exploitation around proven search regions while continuing exploration in uncertain areas improved both optimisation performance and the overall understanding of the hidden search landscape.

**Figure 6. High Performing Region Identification**

<img width="1536" height="1024" alt="figure 6 High-performing region identification after Week 05" src="https://github.com/user-attachments/assets/5ac4353c-e21c-4b61-863a-5d1f50320854" />

...

## 9. Decision Matrix and Resource Allocation

The allocation of query resources during Week 05 was guided by a structured decision matrix that combined observed performance with confidence in the underlying search regions. Rather than distributing queries equally across all objective functions, resources were prioritised according to the evidence collected during previous optimisation rounds. This approach ensured that the limited query budget was used efficiently while maintaining an appropriate balance between exploration and exploitation.

Function 5 received the highest priority because it consistently produced the strongest objective values across successive weeks. The evidence indicated that the surrounding search region contained a productive optimum, making continued exploitation the most effective use of available resources. Small local refinements were therefore prioritised to maximise further improvements while maintaining stability.

Functions 7 and 8 demonstrated stable positive performance and moderate confidence. These functions were allocated sufficient resources for local refinement to confirm the consistency of previous observations while identifying opportunities for incremental improvement. This strategy reduced unnecessary exploration while continuing to strengthen confidence in these regions.

In contrast, Functions 1, 3, 4 and 6 remained associated with greater uncertainty. Their weaker objective values suggested that favourable regions had not yet been identified. Consequently, a larger proportion of exploratory queries was directed towards these functions to improve understanding of their search landscapes and identify alternative regions with greater optimisation potential.

Overall, the decision matrix provided a systematic framework for allocating resources according to observed evidence rather than fixed assumptions. This structured approach improved optimisation efficiency, increased information gain and supported progressive refinement of the Bayesian Black Box Optimisation strategy.

**Figure 7. Decision Matrix and Resource Allocation**

<img width="1536" height="1024" alt="Figure 7  Decision Matrix and Resource Allocation analysis" src="https://github.com/user-attachments/assets/e3af9e59-673d-4b91-b936-0ae90a3e3d15" />

...

## 10. Information Gain Analysis

Information gain is a fundamental objective of Bayesian Black Box Optimisation because each query contributes not only to improving objective values but also to increasing knowledge of the hidden search landscape. During Week 05, every submitted query was evaluated according to the amount of new information it provided about the corresponding objective function. This approach ensured that the limited query budget was used to maximise both learning and optimisation performance.

Function 5 generated the greatest practical information gain by confirming that the previously identified search region continued to produce progressively higher objective values. This reinforced confidence in the current optimisation strategy and justified continued exploitation through carefully controlled local refinement. The consistent improvement also reduced uncertainty regarding the location of a productive search region.

Functions 7 and 8 contributed moderate information gain by confirming the stability of their respective search regions. Although their improvements were smaller, repeated positive results increased confidence that these regions could continue to benefit from incremental refinement while maintaining reliable performance.

Conversely, Functions 1, 3, 4 and 6 produced valuable information despite weaker objective values. Their continued negative or uncertain responses helped eliminate less productive areas of the search space and guided future exploration towards alternative regions. In Bayesian optimisation, identifying where favourable solutions are unlikely to exist is as valuable as identifying successful regions because it reduces uncertainty and improves future decision making.

Overall, the Week 05 information gain analysis demonstrated that optimisation progress should be evaluated using both objective performance and the knowledge obtained from each query. Combining these two perspectives strengthened the evidence based optimisation strategy and improved the efficiency of future query selection.

**Figure 8. Information Gain Analysis**

<img width="1536" height="1024" alt="Figure 8  Information Gain Analysis" src="https://github.com/user-attachments/assets/251596e8-a313-48f0-9716-6f0ded3241a3" />

...

## 11. Computational Analysis and Coding Implementation

The computational analysis for Week 05 combined structured data processing with automated performance evaluation to support evidence based optimisation decisions. Python scripts were developed to organise the weekly inputs and outputs, calculate performance metrics and generate summary tables that assisted interpretation of the optimisation results. Automating these tasks improved consistency, reduced manual errors and ensured that each optimisation round could be reproduced accurately.

NumPy provided efficient numerical operations for handling the optimisation data, while Pandas was used to manage tabular datasets, perform comparisons between optimisation rounds and export structured CSV files. These libraries simplified the processing of multiple objective functions and enabled rapid analysis of performance trends across successive weeks.

The Week 05 analysis script also generated summary statistics that supported ranking, comparison and decision making. These computational outputs complemented the graphical visualisations presented throughout the repository and provided an objective foundation for selecting future query locations. The use of automated analysis reduced subjective interpretation and strengthened the reproducibility of the optimisation workflow.

CSV files were used to store both the submitted query values and the corresponding objective function outputs. This structured data format ensured compatibility with future analysis scripts and allowed results from different optimisation rounds to be compared efficiently. Maintaining organised datasets also simplified verification and future expansion of the repository.

Overall, the computational implementation transformed raw optimisation results into structured evidence that supported systematic decision making. Combining automated coding, numerical analysis and reproducible data management strengthened the technical foundation of the Bayesian Black Box Optimisation project and prepared the repository for continued development in subsequent weeks.

**Figure 9. Computational Analysis and Coding Implementation**

<img width="1536" height="1024" alt="Figure 9  Computational Analysis and Coding Implementation" src="https://github.com/user-attachments/assets/e76b90ae-9643-4e3a-887b-887e70a349ff" />

...

## 12. Repository Files and Reproducibility

Maintaining a well organised repository is essential for ensuring transparency, reproducibility and long term project development. The Week 05 repository has been structured so that all optimisation inputs, outputs, analysis scripts and documentation are stored in clearly defined files. This organisation enables every stage of the optimisation process to be reviewed, verified and reproduced from the available records.

The repository contains the submitted query values, returned objective function outputs, automated analysis scripts and summary tables generated during the computational workflow. Each file has a specific purpose within the optimisation pipeline and contributes to a complete record of the decision making process. Organising these resources into a consistent directory structure improves accessibility and simplifies future development.

The README document provides a comprehensive narrative describing the objectives, methodology, computational analysis and interpretation of the Week 05 optimisation results. Supporting figures, tables and visualisations are integrated throughout the documentation to provide a clear explanation of the optimisation strategy and the evidence supporting each decision.

Maintaining reproducible computational workflows also allows future optimisation rounds to build directly upon previous work. New results can be incorporated into the existing repository without changing the underlying analytical framework. This approach supports continuous development while preserving the complete history of the optimisation process.

Overall, the repository structure provides a reliable foundation for documenting the Bayesian Black Box Optimisation project. Combining organised data management, reproducible computational analysis and comprehensive documentation strengthens both the scientific quality and the professional presentation of the repository.

**Figure 10. Repository Files and Reproducibility**

<img width="1536" height="1024" alt="Figure 10  Repository Files and Reproducibility" src="https://github.com/user-attachments/assets/275dfa90-b896-4d84-94e6-8ff28452bea4" />

...

## 13. Conclusion

Week 05 represented another important stage in the progressive development of the Bayesian Black Box Optimisation strategy. The results demonstrated that evidence accumulated across successive optimisation rounds can be used to guide increasingly informed query selection and improve overall optimisation performance. Rather than relying on intuition, optimisation decisions were supported by objective analysis, computational evidence and systematic interpretation of the returned function values.

The analyses presented throughout this repository demonstrated how performance comparisons, functional rankings, high performing region identification, decision matrices and information gain assessments collectively contributed to a structured optimisation framework. These complementary analyses strengthened confidence in the continued exploitation of Function 5 while supporting selective refinement of Functions 7 and 8 and continued exploration of the remaining objective functions.

The computational workflow further reinforced the reproducibility of the project through automated analysis, structured data management and comprehensive documentation. Python scripts, CSV datasets, visualisations and repository organisation combined to create a transparent and repeatable optimisation process that can be extended throughout the remaining weeks of the competition.

Overall, Week 05 demonstrated measurable progress towards understanding the hidden objective functions while maintaining an appropriate balance between exploration and exploitation. The knowledge gained during this optimisation round provides a stronger foundation for Week 06 and subsequent iterations, supporting continual refinement of both the optimisation strategy and the technical framework documented throughout this repository.

## 14 References

1. Jones, D. R., Schonlau, M., & Welch, W. J. (1998). Efficient Global Optimisation of Expensive Black Box Functions. *Journal of Global Optimization*, 13(4), 455–492.

2. Shahriari, B., Swersky, K., Wang, Z., Adams, R. P., & De Freitas, N. (2016). Taking the Human Out of the Loop: A Review of Bayesian Optimization. *Proceedings of the IEEE*, 104(1), 148–175.

3. Snoek, J., Larochelle, H., & Adams, R. P. (2012). Practical Bayesian Optimization of Machine Learning Algorithms. *Advances in Neural Information Processing Systems (NeurIPS)*, 25.

4. Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.

5. Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array Programming with NumPy. *Nature*, 585, 357–362.

6. McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 56–61.

7. Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17, 261–272.

8. Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. *Computing in Science & Engineering*, 9(3), 90–95.

---
**Next Repository:** Week_06
