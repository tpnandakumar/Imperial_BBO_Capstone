# Datasheet for the Bayesian Black Box Optimisation Capstone Dataset

**Author:** Dr N T Pisharam  
**Project:** Imperial BBO Optimisation  
**Course module:** 21  
**Capstone week:** 09  
**Optimisation round:** 9  
**Document status:** Full detailed datasheet

## 1. Executive Summary

This datasheet documents the Bayesian Black Box Optimisation (BBO) dataset developed during the Imperial College London Machine Learning and Artificial Intelligence capstone project. The dataset provides a complete record of the optimisation process up to Round 9, documenting the submitted query vectors, returned objective values and the analytical evidence used to guide each subsequent optimisation round. Rather than representing a static collection of observations, the dataset captures an evolving optimisation process in which every new submission builds upon the knowledge gained from previous rounds.

The dataset contains optimisation records for eight hidden objective functions with dimensionalities ranging from two to eight variables. By the completion of Round 9, each function had accumulated nine optimisation observations, resulting in a total of seventy two submitted query vectors and seventy two corresponding objective values. These observations form the evidence base from which optimisation strategies were developed, refined and evaluated throughout the project.

Alongside the raw optimisation data, the repository includes analytical summaries, computational scripts and supporting figures that reproduce the reported analyses without altering the original observations. Maintaining transparency and reproducibility was a fundamental objective throughout the project. Every optimisation decision can therefore be traced directly to the evidence available at the time it was made, allowing the reasoning behind each submission to be reviewed, understood and reproduced.

## 2. Motivation

The Bayesian Black Box Optimisation challenge requires participants to improve the performance of unknown objective functions using only the information returned after each submission. Since the mathematical form of each function is intentionally hidden, optimisation cannot rely on gradients, analytical equations or prior knowledge of the search landscape. Instead, every decision must be based on previously observed results and the interpretation of emerging patterns within the accumulated data.

This dataset was created to preserve that complete optimisation history. Rather than recording only the final submitted queries, it captures the gradual development of the optimisation strategy across successive rounds. Every submission contributed new evidence that influenced subsequent decisions, allowing the optimisation process to evolve from broad exploration during the early stages towards increasingly focused refinement and exploitation as confidence grew.

A second motivation was to ensure that the optimisation process remained fully transparent. Every submitted query, returned objective value and analytical interpretation has been retained so that the reasoning behind each optimisation decision can be examined in its original context. This provides an auditable record of the search process and allows both successful and unsuccessful optimisation decisions to be evaluated objectively.

The dataset also serves an educational purpose by demonstrating how sequential optimisation develops under conditions of uncertainty. It illustrates the practical challenges associated with balancing exploration, refinement and exploitation when only limited information is available, while highlighting how evidence accumulates over time to support increasingly informed decision making. Consequently, the dataset provides both a record of the capstone project and a practical resource for understanding adaptive optimisation strategies within complex search spaces.

## 3. Dataset Overview

The dataset represents the complete optimisation history available at the conclusion of Round 9 of the Bayesian Black Box Optimisation capstone. It contains observations for eight independent hidden objective functions, each requiring one submitted query vector during every optimisation round. Function dimensionality ranges from two to eight variables, with every submitted value constrained to the interval from zero to one.

Unlike conventional machine learning datasets, this dataset expands sequentially throughout the optimisation process. Every round contributes one new observation for each function, increasing the available evidence while preserving all previous records. By the completion of Round 9, nine observations had been collected for every function, allowing longer term optimisation trends to be examined alongside the behaviour of individual functions.

The repository contains both the original optimisation records and the supporting material required to reproduce the reported analyses. These include submitted query vectors, returned objective values, analytical summaries, ranking tables, computational scripts and graphical outputs. The original optimisation data remain unchanged throughout the project, while derived analyses are generated separately to preserve data integrity and maintain reproducibility.

The hidden objective functions remain unknown throughout the challenge. As a result, the dataset documents observed optimisation behaviour rather than the underlying mathematical relationships governing the search landscape. This distinction is central to interpreting the results and reflects the fundamental characteristics of black box optimisation.

## 4. Dataset Composition

The dataset contains optimisation records for eight hidden objective functions collected over nine successive optimisation rounds. Each function contributes one submitted query vector and one returned objective value during every round, producing a cumulative total of seventy two query vectors together with seventy two corresponding objective values.

The functions differ in dimensionality, allowing optimisation behaviour to be examined across search spaces of varying complexity. Functions 1 and 2 each contain two variables, Function 3 contains three variables, Functions 4 and 5 each contain four variables, Function 6 contains five variables, Function 7 contains six variables and Function 8 contains eight variables. This variation provides opportunities to examine how optimisation strategies perform as the dimensionality of the search space increases.

| Function | Dimensions | Observations by Round 9 |
|---|---:|---:|
| Function 1 | 2 | 9 |
| Function 2 | 2 | 9 |
| Function 3 | 3 | 9 |
| Function 4 | 4 | 9 |
| Function 5 | 4 | 9 |
| Function 6 | 5 | 9 |
| Function 7 | 6 | 9 |
| Function 8 | 8 | 9 |

<img width="1536" height="1024" alt="Dataset composition infographic" src="https://github.com/user-attachments/assets/d236414e-32c1-4ca8-bb2b-30a4739573d3" />

**Figure 1. Dataset composition of the Bayesian Black Box Optimisation dataset at the end of Round 9.**

In addition to the raw optimisation records, the repository contains derived analytical summaries that classify optimisation strategies, rank function performance and compare successive optimisation rounds. Supporting Python scripts reproduce every reported analysis and generate the accompanying figures directly from the stored data. These derived files extend the analytical value of the dataset while ensuring that the original observations remain unchanged.

Together, the raw observations, analytical summaries and supporting computational material provide a comprehensive record of the optimisation process from the first submission through to the completion of Round 9. The resulting dataset supports transparent analysis, reproducible research and objective evaluation of the optimisation strategies developed throughout the capstone project.

## 5. Dataset Structure

The dataset is organised using a weekly structure that records each stage of the optimisation process in chronological order. Every optimisation round is stored within its own folder, preserving the submitted query vectors, returned objective values, analytical summaries, figures and supporting code. This organisation provides a clear record of how the optimisation strategy developed over time and allows previous decisions to be revisited whenever further analysis is required.

Within each weekly folder, the original optimisation records are stored separately from the derived analytical outputs. Raw input vectors and returned objective values remain unchanged throughout the project, while ranking tables, performance summaries, visualisations and computational analyses are generated as independent files. This separation protects the integrity of the original observations while allowing additional analyses to be performed without altering the underlying dataset.

The dataset also follows a cumulative structure. Each optimisation round adds new observations while retaining every previous submission, creating a complete historical record of the search process. This approach allows individual optimisation rounds to be examined in isolation while also supporting longer term analyses of performance, strategy development and changes in decision making across the project.

This structure provides a reliable foundation for the next stage of the datasheet by explaining how the data were collected and incorporated into the optimisation workflow.

## 6. Data Collection Methodology

The data were collected through a sequential optimisation process carried out over successive rounds of the Bayesian Black Box Optimisation challenge. During each round, one query vector was submitted for every hidden objective function using the official optimisation platform. Once the submitted queries had been evaluated, the returned objective values were recorded and added to the cumulative dataset before the next optimisation round began.

The collection process followed the same procedure throughout the project. Historical observations were reviewed first, after which new query vectors were generated for each function. Following submission, the returned outputs were recorded exactly as received and stored without modification. These verified observations then became part of the evidence available for future optimisation decisions.

Maintaining a consistent collection methodology was important because it ensured that every optimisation round could be compared directly with previous rounds. The resulting dataset therefore represents a continuous record of the optimisation process, allowing changes in performance, strategy and search behaviour to be examined using a consistent and reproducible approach.

This systematic method also ensured that the optimisation history remained complete, providing a dependable evidence base for generating new query vectors and evaluating the effectiveness of different optimisation strategies.

## 7. Query Generation Strategy

The strategy used to generate new query vectors evolved steadily as more optimisation evidence became available. During the early stages of the project, very little was known about the behaviour of the hidden objective functions, so the emphasis was placed on exploring different regions of the search space. As additional observations accumulated, clearer patterns began to emerge, allowing future queries to be selected with greater confidence.

Rather than applying the same strategy to every function, each objective was assessed independently using its own optimisation history. Functions showing consistent improvement were refined cautiously to determine whether additional gains could be achieved. Functions producing stable, high objective values were treated as exploitation targets, while functions displaying inconsistent or declining behaviour were reassessed before further local refinement was attempted. Functions that continued to produce little useful information remained exploration targets in an effort to identify more productive regions elsewhere within the search space.

This adaptive approach allowed the optimisation strategy to develop naturally as knowledge increased. Decisions became progressively more selective because they were supported by a growing body of evidence rather than by isolated observations. The strategy therefore reflected the behaviour of each individual function instead of following a fixed optimisation rule across the entire problem.

## 8. Optimisation Workflow

The optimisation workflow followed a structured sequence that remained consistent throughout the project. Each round began with a review of the complete optimisation history, including previously submitted query vectors, returned objective values and recent performance trends. This information was used to assess the current behaviour of each function before selecting the next set of candidate query vectors.

Once candidate queries had been generated, they were checked to ensure that every function satisfied its dimensionality requirements and that all submitted values remained within the permitted search boundaries. The validated queries were then submitted through the optimisation platform, where the hidden objective functions returned a new set of objective values. These results were recorded without modification before being incorporated into the cumulative dataset.

Following each optimisation round, the new observations were analysed alongside the existing optimisation history to determine whether exploration, refinement, reassessment or exploitation remained the most appropriate strategy for each function. Updated analytical summaries, computational scripts and supporting figures were then produced to document the results and preserve a complete record of the optimisation process.

Repeating this workflow throughout the project ensured that every optimisation decision was supported by the strongest available evidence while maintaining a transparent and reproducible record of how the search strategy developed from one round to the next.

<img width="1402" height="1122" alt="optimisation_workflow" src="https://github.com/user-attachments/assets/d40f148e-b82d-4396-9117-7e1c5903531a" />


## 9. Data Preprocessing

The original optimisation records were preserved throughout the project to ensure that the dataset remained an accurate representation of every submitted query and returned objective value. No scaling, normalisation or numerical transformation was applied to the raw data. Instead, preprocessing focused on preparing the dataset for analysis while preserving the integrity of the original observations.

Each submitted query vector was checked to confirm that it contained the correct number of variables for the corresponding objective function. Every coordinate was then verified to ensure that it remained within the permitted search interval from zero to one and that all submitted values were recorded using the required six decimal places. Once the objective values had been returned, each output was matched with its corresponding query to confirm that every submission produced a complete optimisation record.

Following these checks, the verified observations were organised into structured datasets for analysis. The raw optimisation records remained unchanged, while analytical summaries, rankings and visualisations were generated separately. Maintaining this separation ensured that every reported result could be traced directly to the original optimisation data without introducing unnecessary modification of the source records.

This approach provided a consistent and reliable foundation for the analytical stages that followed while preserving the authenticity of the original optimisation history.

## 10. Data Validation and Quality Assurance

Maintaining data quality was essential because every optimisation decision depended upon the accuracy of the observations collected during previous rounds. Validation was therefore carried out throughout the project to confirm that the recorded data remained complete, consistent and suitable for analysis.

Each optimisation round was examined to verify that all eight hidden objective functions contained one submitted query vector and one corresponding objective value. Query dimensionality was checked against the published specification for each function, while numerical values were confirmed to lie within the permitted submission range. Returned objective values were then matched with the original queries to ensure that every observation had been recorded correctly before being added to the cumulative dataset.

Quality assurance continued beyond the raw optimisation records. Ranking tables, optimisation strategies, summary statistics and graphical outputs were all generated directly from the validated source data. This ensured that every analytical result could be reproduced while leaving the original observations unchanged. By separating the raw dataset from the derived analyses, the project maintained a clear audit trail that supports transparency and reproducibility.

Although the recorded data were carefully validated, uncertainty remains an inherent feature of the optimisation challenge because the mathematical form of the hidden objective functions is unknown. Consequently, validation confirms the accuracy of the recorded observations rather than the correctness of the underlying optimisation landscape.

## 11. Feature Description

The dataset consists of numerical input variables together with the objective values returned by the hidden optimisation functions. Each function has a fixed dimensionality that remains constant throughout the project. Functions 1 and 2 each contain two input variables, Function 3 contains three variables, Functions 4 and 5 each contain four variables, Function 6 contains five variables, Function 7 contains six variables and Function 8 contains eight variables.

Every input variable represents a continuous numerical coordinate within the permitted search interval from zero to one. Together, these coordinates define the position of the submitted query within the search space for the corresponding function. The returned output is a single continuous numerical value that represents the performance of that query within the hidden optimisation landscape.

Alongside the original optimisation records, the repository contains several derived variables that support interpretation of the optimisation process. These include function rankings, optimisation strategies, week to week performance changes and summary statistics generated from the cumulative optimisation history. These derived variables provide additional analytical context while preserving the original optimisation records as the primary source of information.

The combination of raw observations and derived analytical information allows the dataset to support both quantitative analysis and transparent reporting without compromising the integrity of the original optimisation data.

## 12. Data Labelling and Derived Variables

The original optimisation records consist only of the submitted query vectors and their corresponding objective values. To improve interpretation of the optimisation process, additional descriptive labels and derived variables were generated during the analytical stage of the project. These additions explain the optimisation strategy without altering the original observations.

Each function was assigned a strategy according to the evidence available at the time of analysis. Depending on recent performance and longer term behaviour, functions were classified as exploration, refinement, reassessment or exploitation targets. These labels describe the optimisation strategy adopted during that round and should not be interpreted as permanent characteristics of the hidden objective functions.

Further derived variables include function rankings, changes in objective values between optimisation rounds, cumulative performance summaries and graphical representations of optimisation progress. Together, these variables provide a clearer understanding of how the optimisation strategy evolved as additional evidence became available.

All derived variables were generated directly from the validated optimisation records using reproducible analytical procedures. The original query vectors and returned objective values remain the authoritative dataset, while the derived labels and summaries provide an additional layer of interpretation that supports transparent analysis, informed decision making and reproducible reporting.

## 13. Exploratory Data Characteristics

The dataset reflects the progressive nature of sequential black box optimisation rather than a conventional independently sampled dataset. Each optimisation round builds upon the observations collected previously, meaning that later query points are influenced by the evidence accumulated during earlier rounds. As a result, the distribution of observations changes naturally over time as the optimisation strategy becomes increasingly informed.

During the early rounds, query points were distributed more widely because very little was known about the behaviour of the hidden objective functions. This broad exploration provided the initial evidence needed to identify potentially productive regions within each search space. As additional observations became available, the search gradually became more focused, with greater attention directed towards regions demonstrating consistent improvement while still preserving sufficient exploration to investigate areas that remained uncertain.

The dataset therefore contains a combination of exploratory and exploitative observations. Some functions show clusters of query points around productive regions, reflecting increasing confidence in local optimisation, while others continue to display broader coverage because reliable improvement has not yet been established. This changing pattern is an expected characteristic of adaptive optimisation and provides valuable insight into how evidence influences decision making throughout the project.

Although the dataset does not represent uniform coverage of the search space, it provides a realistic record of how optimisation develops when decisions are driven by progressively accumulating evidence rather than random sampling.

## 14. Intended Uses

The dataset has been developed primarily to support analysis of sequential Bayesian Black Box Optimisation within the Imperial College London capstone project. It provides a transparent record of the optimisation process and enables the progression of individual functions to be examined across successive rounds.

It is intended to support evaluation of optimisation strategies, comparison of exploration and exploitation behaviour, reproduction of analytical results and investigation of how evidence influences future query selection. The dataset also provides an educational resource for understanding optimisation under uncertainty, demonstrating how decisions evolve when only limited information is available about the underlying search landscape.

Beyond the immediate requirements of the capstone project, the dataset may be useful for teaching adaptive optimisation techniques, demonstrating transparent research practice and illustrating the importance of reproducible computational workflows. The combination of raw observations, analytical summaries and supporting documentation allows future users to understand not only the optimisation results but also the reasoning that produced them.

The dataset is intended to encourage careful interpretation of optimisation behaviour rather than simply reporting numerical performance, making it suitable for educational and research purposes where transparency and reproducibility are important objectives.

## 15. Unsuitable Uses

The dataset should not be used to infer the mathematical form of the hidden objective functions or to claim that a global optimum has been identified. The optimisation challenge intentionally conceals the analytical structure of each function, meaning that all conclusions are based solely on observed behaviour rather than complete knowledge of the search landscape.

The dataset should also not be treated as a statistically representative sample of the entire optimisation space. Query points were selected adaptively using evidence gathered during previous rounds rather than through independent or random sampling. Consequently, the observations reflect the optimisation strategy employed during the project rather than the full distribution of possible solutions.

Because the dataset was created for a specific educational optimisation challenge, it should not be applied directly to unrelated optimisation problems without appropriate validation. Likewise, it should not be used to support safety critical, financial or clinical decision making where stronger guarantees regarding performance, reliability and generalisability would be required.

The analytical summaries and optimisation strategies included within the repository represent informed interpretations of the available evidence rather than definitive descriptions of the hidden objective functions. They should therefore be considered within the context of the optimisation process for which they were developed.

## 16. Strengths of the Dataset

One of the principal strengths of the dataset is that it preserves the complete optimisation history rather than recording only the final solution. Every optimisation round contributes additional evidence, allowing the development of the search strategy to be followed from the earliest exploratory submissions through to the more targeted optimisation decisions made during the later stages of the project. This provides valuable insight into the reasoning process that underpins successful sequential optimisation.

A further strength is the transparency of the dataset. The original optimisation records remain unchanged throughout the project, while analytical summaries, computational scripts and supporting figures are generated separately. This clear separation between raw observations and derived analyses allows every reported result to be reproduced directly from the original data while preserving a complete audit trail of the optimisation process.

The dataset also captures optimisation behaviour across objective functions with different dimensionalities, providing opportunities to examine how search strategies adapt as the complexity of the optimisation problem increases. Recording both successful and unsuccessful optimisation decisions contributes to a more balanced understanding of the search process by demonstrating that progress is achieved through continuous evaluation and refinement rather than through isolated improvements.

Finally, the dataset combines numerical observations with comprehensive supporting documentation, creating a resource that explains not only what happened during the optimisation process but also why particular decisions were made. This combination of data, analysis and documented reasoning enhances reproducibility, supports future investigation and increases the educational value of the dataset beyond the immediate requirements of the capstone project.

## 17. Dataset Limitations

Although the dataset provides a detailed record of the optimisation process, several limitations should be recognised when interpreting the results. The most important limitation is that the underlying objective functions remain unknown throughout the challenge. As a result, the dataset records observed optimisation behaviour rather than describing the true mathematical characteristics of the search landscape. This means that improvements in objective values cannot be confirmed as movements towards a global optimum and should instead be viewed as evidence supporting the current optimisation strategy.

A further limitation arises from the restricted number of observations. Each optimisation round contributes only one new query for each function, meaning that the search space is sampled gradually over time. While this reflects the practical constraints of the challenge, it also means that large areas of the search landscape remain unexplored. Functions with higher dimensionality present an additional challenge because the number of possible query locations increases substantially as the number of variables grows.

The dataset is also influenced by the sequential nature of the optimisation process. Later observations depend directly on earlier results because every new query is selected using the accumulated evidence from previous rounds. This dependency is an expected feature of adaptive optimisation, but it means that the observations cannot be regarded as independent samples.

Despite these limitations, the dataset provides a reliable and well documented record of the optimisation process, making it suitable for evaluating optimisation strategies, analysing decision making and supporting reproducible research.

## 18. Sources of Bias

The dataset contains several sources of bias that arise naturally from the optimisation strategy rather than from errors in data collection. The most significant is adaptive sampling bias. Query points were selected according to the evidence available at the time, meaning that functions showing encouraging results received greater attention than regions that appeared less promising. This produced a deliberate concentration of observations within areas believed to have the greatest optimisation potential.

Another source of bias is local search bias. Once a productive region had been identified, subsequent optimisation rounds often focused on neighbouring query points in an effort to achieve incremental improvement. While this approach is effective for local refinement, it reduces exploration of more distant regions that may also contain favourable solutions.

The dataset may also contain boundary bias because several optimisation rounds investigated regions close to the limits of the permitted search space. This reflects the behaviour of the optimisation process rather than a weakness in the dataset itself, but it should be recognised when interpreting the distribution of query points.

Finally, the dataset contains temporal bias because later optimisation decisions benefited from considerably more evidence than those made during the earliest rounds. Early submissions were necessarily exploratory, whereas later rounds reflected a progressively stronger understanding of the optimisation landscape. This changing evidence base is an inherent characteristic of sequential optimisation and should be considered when comparing different stages of the project.

## 19. Assumptions

The optimisation strategy is based on several practical assumptions that supported decision making throughout the project. One important assumption is that historical observations provide useful guidance when selecting future query points. Although the hidden objective functions remain unknown, repeated improvements within a local region were treated as evidence that cautious refinement could continue to produce useful results.

A second assumption is that neighbouring query points may display related optimisation behaviour. This assumption encouraged gradual local refinement around productive regions while maintaining broader exploration where little useful information had been obtained. At the same time, the strategy recognised that neighbouring observations do not guarantee similar objective values, particularly within complex or highly irregular search spaces.

The optimisation process also assumes that preserving the complete history of submitted queries and returned objective values provides a stronger basis for future decisions than relying solely on recent observations. Consequently, every optimisation round considered the cumulative evidence rather than interpreting individual results in isolation.

These assumptions guided the optimisation strategy but were never regarded as established facts. Instead, they provided a practical framework for making informed decisions while recognising that new evidence could challenge earlier interpretations at any stage of the project.

## 20. Ethical Considerations

Although the dataset was developed for an educational optimisation challenge, responsible research practice remained an important consideration throughout the project. The optimisation workflow was designed to promote transparency by preserving the original observations and documenting the reasoning behind each optimisation decision. Maintaining this level of documentation allows other researchers to understand how conclusions were reached and to reproduce the analytical process using the same underlying data.

The dataset contains no personal information, sensitive data or identifiable records. All observations relate exclusively to numerical optimisation tasks generated within the capstone challenge, avoiding the privacy concerns that often accompany real world datasets.

The analytical summaries and optimisation strategies included within the repository are intended to support interpretation rather than replace independent judgement. Every optimisation decision was reviewed in the context of the available evidence, while uncertainty was acknowledged whenever the observations remained insufficient to justify stronger conclusions.

Finally, the dataset is presented with the expectation that it will be used responsibly. It should be interpreted within the context of the optimisation challenge for which it was created and not applied beyond that setting without appropriate validation. Presenting both the strengths and limitations of the dataset encourages balanced interpretation and supports the principles of transparent, reproducible and responsible research.

## 21. Transparency and Reproducibility

Transparency was a guiding principle throughout the development of this dataset. Every optimisation round was documented from the initial query selection through to the returned objective values and subsequent analysis. Rather than presenting only the final optimisation results, the repository preserves the complete sequence of observations, allowing the reasoning behind each decision to be examined in its original context.

Reproducibility was supported by retaining the original optimisation records alongside the computational scripts used to generate the analytical summaries and figures. The raw input vectors and returned objective values remain unchanged throughout the project, while the analytical outputs are produced independently from these source records. This approach allows the reported results to be reproduced directly from the original dataset without introducing unnecessary modification of the underlying observations.

Supporting documentation forms an integral part of the repository and provides additional context for interpreting the optimisation process. Together with the computational workflow, these records allow other researchers to understand not only the reported results but also the sequence of decisions that produced them. Maintaining this level of documentation strengthens confidence in the reported findings and supports future investigation of alternative optimisation strategies.

The combination of preserved source data, reproducible analysis and comprehensive documentation ensures that the dataset remains both transparent and verifiable throughout the life of the project.

The accompanying [Model Card](MODEL_CARD.md) explains how this dataset is used within the optimisation workflow, including the model architecture, evaluation approach, assumptions, limitations and human oversight.

## 22. Distribution and Accessibility

The dataset is maintained within the Imperial_BBO_Capstone GitHub repository, where each optimisation round is organised into its own folder together with the associated analysis, figures and supporting documentation. This structure provides a clear record of the project's development while allowing individual optimisation rounds to be examined independently or as part of the cumulative optimisation history.

The repository has been organised to ensure that users can move easily between the raw optimisation records, analytical summaries and supporting computational material. This arrangement simplifies navigation and provides direct access to the information required to understand or reproduce the reported analyses.

The dataset has been prepared primarily for educational and research purposes within the Bayesian Black Box Optimisation capstone project. Any future distribution beyond the scope of the course should preserve the complete documentation accompanying the dataset so that the optimisation process can continue to be interpreted correctly. Separating the raw observations from the analytical summaries also helps ensure that future users can distinguish between the recorded optimisation data and the interpretations derived from them.

## 23. Version Control

Version control has been maintained throughout the project to preserve the complete development history of the dataset. Every optimisation round represents a new stage in the evolution of the repository, with previous observations retained rather than replaced. This approach ensures that the optimisation history remains complete and that earlier decisions can be reviewed whenever required.

Each weekly update records the newly submitted query vectors, returned objective values, revised analytical summaries and supporting documentation. By maintaining separate versions of the dataset across optimisation rounds, the repository provides a permanent record of how both the optimisation strategy and the supporting analyses developed over time.

This version controlled approach also supports reproducibility by allowing future users to identify the exact dataset, analysis and documentation associated with any particular optimisation round. Preserving earlier versions reduces the risk of losing valuable optimisation evidence while providing a reliable audit trail for future review and verification.

## 24. Maintenance

Responsibility for maintaining the dataset remains with the project author throughout the capstone. Following each optimisation round, the repository is updated with the newly submitted query vectors, returned objective values and the analytical material generated from those observations. Existing records are preserved to maintain the continuity of the optimisation history and to provide a complete record of the project's development.

Routine maintenance includes checking the consistency of the stored data, confirming that the analytical summaries agree with the original optimisation records and updating the supporting documentation whenever new evidence becomes available. Any future corrections will preserve the original observations wherever possible while documenting the reason for the revision so that the history of the dataset remains transparent.

As additional optimisation rounds are completed, the dataset will continue to expand while retaining the same organisational structure and documentation standards established during the earlier stages of the project. This consistent approach will allow the repository to remain reliable, reproducible and straightforward to maintain, while preserving a complete record of the optimisation process from the first submission through to the final round.

## 25. Future Development

The dataset will continue to expand as additional optimisation rounds are completed, providing a progressively richer record of the search process and the evidence supporting future decisions. Each new round will contribute further observations, allowing optimisation strategies to be evaluated over a longer period while improving understanding of the behaviour of the hidden objective functions.

Future updates will maintain the same documentation standards established during this project. New optimisation records will be incorporated alongside revised analytical summaries, computational scripts and supporting figures, ensuring that the repository continues to provide a complete and reproducible account of the optimisation process. As the dataset grows, additional analyses may be introduced to examine longer term optimisation trends, compare alternative search strategies and evaluate how decision making changes as more evidence becomes available.

There is also scope to extend the dataset by incorporating more comprehensive validation methods, additional performance metrics and enhanced visualisation techniques. These developments would improve interpretation of the optimisation process while preserving the integrity of the original observations. Although the dataset has been developed specifically for the current capstone challenge, the documentation framework established here may also provide a useful foundation for future optimisation projects requiring transparent and reproducible reporting.

## 26. Conclusion

This datasheet documents the Bayesian Black Box Optimisation dataset developed during the Imperial College London capstone project and provides a detailed account of how the data were collected, organised, validated and maintained. Rather than representing a static collection of observations, the dataset captures the gradual development of an optimisation strategy as new evidence became available across successive rounds.

A key strength of the dataset lies in the way it preserves both the original optimisation records and the analytical process used to interpret them. This allows every optimisation decision to be understood within the context of the evidence available at the time, while supporting reproducibility through carefully documented computational workflows and supporting documentation.

Although the hidden objective functions remain unknown and the search space cannot be explored exhaustively, the dataset provides a reliable and transparent record of the optimisation process. Its value extends beyond the numerical observations themselves by demonstrating how evidence, interpretation and careful decision making contribute to successful optimisation under conditions of uncertainty.

By combining complete historical records with reproducible analysis and comprehensive documentation, the dataset provides a robust foundation for evaluating optimisation strategies while supporting the principles of transparency, responsible research and continuous improvement. It therefore represents not only the outcome of the optimisation challenge but also the process through which those outcomes were achieved.

## 27. References

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., and Crawford, K. (2021). *Datasheets for Datasets*. Communications of the ACM, 64(12), 86-92.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. (2019). *Model Cards for Model Reporting*. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220-229.

Snoek, J., Larochelle, H., and Adams, R. P. (2012). *Practical Bayesian Optimization of Machine Learning Algorithms*. Advances in Neural Information Processing Systems, 25, 2951-2959.

Frazier, P. I. (2018). *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.

Nocedal, J., and Wright, S. J. (2006). *Numerical Optimization* (2nd ed.). Springer.

Imperial College London. (2026). *Module 21: Transparency, Interpretability and Responsible AI*. Professional Certificate in Machine Learning and Artificial Intelligence. Course materials.

Pisharam, N. T. (2026). *Imperial_BBO_Capstone: Bayesian Black Box Optimisation Repository*. GitHub project documentation.
