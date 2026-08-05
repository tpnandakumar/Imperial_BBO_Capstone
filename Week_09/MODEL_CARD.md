# Model Card for the Bayesian Black Box Optimisation Workflow

**Author:** Dr N T Pisharam  
**Course module:** 21  
**Capstone week:** 09  
**Optimisation round:** 9  
**Model name:** Pisharam Bayesian Black Box Optimisation Workflow  
**Model type:** Human-supervised, LLM-assisted sequential optimisation workflow  
**Model version:** 0.9  
**Document version:** 1.0  
**Status:** Final Module 21 submission

## 1. Executive Summary

This model card describes the Bayesian Black Box Optimisation (BBO) workflow developed during the Imperial College London Machine Learning and Artificial Intelligence capstone project. The workflow was designed to support sequential optimisation of eight unknown objective functions by selecting one query vector for each function during every optimisation round. Since the analytical form of the functions remained unknown throughout the challenge, every recommendation was based entirely on previously observed evidence rather than mathematical models of the search landscape.

The workflow combines historical optimisation data, computational analysis and human judgement to guide query selection. As additional observations became available, the optimisation strategy evolved from broad exploration towards increasingly focused refinement and exploitation where the evidence supported those decisions. Throughout the project, transparency and reproducibility remained central principles, ensuring that every recommendation could be traced back to the observations that influenced it.

Rather than functioning as an autonomous optimisation system, the workflow provides structured decision support. Human review remained an essential part of every optimisation round, allowing analytical evidence to be interpreted within the wider context of the optimisation process before the final submissions were made.

## 2. Model Overview

The Bayesian Black Box Optimisation workflow was developed to support optimisation problems where the underlying objective functions are unknown and only the returned outputs from submitted query points are available for analysis. Unlike conventional optimisation methods that rely on gradients or explicit mathematical models, this workflow learns progressively from accumulated observations and adapts its search strategy as additional evidence becomes available.

Each optimisation round contributes new information that improves understanding of the behaviour of the hidden objective functions. Rather than treating every function in the same way, the workflow evaluates the optimisation history of each function independently, allowing different search strategies to emerge according to the available evidence. This adaptive approach enables exploration to continue where uncertainty remains high while concentrating refinement within regions that have demonstrated consistent improvement.

The workflow therefore acts as a structured decision support system that transforms historical optimisation evidence into informed query recommendations while preserving complete transparency throughout the optimisation process.

## 3. Model Purpose

The primary purpose of the workflow is to improve optimisation performance by selecting progressively more informative query points throughout successive optimisation rounds. Every recommendation aims to balance exploration of uncertain regions with refinement of areas that have already demonstrated promising performance, allowing the available query budget to be used as effectively as possible.

A second objective is to provide a transparent and reproducible record of the optimisation process. Rather than presenting only the submitted query vectors, the workflow documents the evidence, reasoning and assumptions that contributed to every optimisation decision. This makes it possible to understand how the optimisation strategy evolved and why particular query points were selected at different stages of the project.

The workflow also serves an educational purpose by demonstrating how adaptive optimisation develops under conditions of uncertainty. It provides a practical example of evidence based decision making within a sequential optimisation framework while illustrating the importance of careful documentation and reproducible analysis.

## 4. Model Description

The optimisation workflow combines historical observations, computational analysis and human interpretation to generate recommendations for each optimisation round. The workflow does not attempt to estimate the hidden mathematical functions directly. Instead, it analyses previously submitted query vectors together with their returned objective values to identify patterns that may support improved optimisation decisions.

Every optimisation round begins with a review of the cumulative optimisation history. Recent changes in objective values, longer term performance trends and the behaviour of neighbouring query points are considered before selecting new candidate queries. The available evidence is then interpreted to determine whether each function is more likely to benefit from continued exploration, cautious refinement, reassessment or controlled exploitation.

Throughout the project, the optimisation strategy remained adaptive rather than fixed. Decisions changed as new observations became available, allowing the workflow to respond to emerging patterns while recognising that the hidden objective functions could not be observed directly. Human judgement remained an important component of this process, ensuring that every recommendation was evaluated before submission rather than being accepted automatically.

## 5. Model Architecture

The workflow follows a sequential architecture in which every optimisation round builds directly upon the evidence collected during previous rounds. Historical query vectors and returned objective values form the foundation of the decision making process, providing the information required to evaluate performance trends and identify promising search directions.

The optimisation process begins by reviewing the cumulative dataset and assessing the behaviour of each hidden objective function individually. Candidate query vectors are then generated using the available evidence and evaluated within the context of the existing optimisation history. Following human review, the selected queries are submitted to the optimisation platform and the returned objective values are incorporated into the cumulative dataset. The updated observations then become the starting point for the following optimisation round.

This cyclical architecture allows the optimisation strategy to evolve naturally as new evidence becomes available. Rather than relying on predetermined search rules, the workflow continuously adapts its recommendations according to the observed behaviour of the hidden objective functions while maintaining a complete record of the reasoning that supports every optimisation decision.

<img width="1536" height="1024" alt="model_workflow" src="https://github.com/user-attachments/assets/f9007ac9-ee63-4e3d-91fb-0411e6f4c68e" />

**Figure 1. Bayesian Black Box Optimisation model workflow used throughout the project.**

## 6. Model Inputs

The optimisation workflow relies on information accumulated throughout the project rather than a single optimisation round. The primary inputs consist of the submitted query vectors and the corresponding objective values returned by the hidden optimisation functions. Together, these observations provide the evidence used to guide future optimisation decisions.

In addition to the numerical data, the workflow considers the dimensionality of each function, the permitted search boundaries and the historical behaviour of every optimisation pathway. Changes in objective values across successive rounds, the stability of neighbouring query points and the overall direction of previous optimisation decisions all contribute to the assessment of each function.

Rather than treating recent observations in isolation, the workflow evaluates the complete optimisation history before generating new recommendations. This cumulative approach allows every optimisation round to benefit from all previously collected evidence while reducing the likelihood that decisions are influenced by short term fluctuations alone.

## 7. Model Outputs

The primary output of the workflow is one recommended query vector for each hidden objective function during every optimisation round. Each recommendation represents the most appropriate query point based on the evidence available at that stage of the optimisation process.

Alongside the submitted query vectors, the workflow produces analytical outputs that help explain and evaluate the optimisation strategy. These include function rankings, comparisons between optimisation rounds, performance summaries, graphical visualisations and descriptive classifications that indicate whether a function is best approached through exploration, refinement, reassessment or exploitation.

These outputs are intended to support interpretation rather than replace independent judgement. They provide a structured explanation of the optimisation process while ensuring that the underlying observations remain the principal source of evidence.

## 8. Model Development

The workflow developed progressively as additional optimisation rounds increased the amount of available evidence. During the earliest stages of the project, limited knowledge of the hidden objective functions required broad exploration across the search space. The primary objective at this stage was to gather sufficient information to identify regions that appeared more promising than others.

As further observations became available, recurring patterns began to emerge. Productive regions could be recognised with greater confidence, allowing the optimisation strategy to move gradually towards more focused refinement while maintaining exploration where uncertainty remained high. Individual functions also began to display distinct behaviour, making it increasingly appropriate to optimise each one independently rather than applying a common strategy across the entire problem.

By Round 9, the workflow had developed into an evidence driven optimisation system in which every recommendation reflected the accumulated history of previous observations. This gradual development illustrates how adaptive optimisation improves as additional information becomes available and demonstrates the value of preserving the complete optimisation history throughout the project.

## 9. Optimisation Strategy

The optimisation strategy was designed to balance the competing objectives of improving current performance while continuing to learn about the hidden search landscape. Rather than concentrating exclusively on the highest performing regions, the workflow maintained a balance between exploration, refinement, reassessment and exploitation according to the evidence available for each function.

Functions that consistently produced favourable objective values were refined cautiously in order to determine whether additional improvement remained possible. Stable, high performing regions became candidates for controlled exploitation, while functions showing inconsistent or declining behaviour were reassessed before further refinement was attempted. Functions that continued to provide little useful information remained exploration targets so that alternative regions of the search space could be investigated.

This adaptive strategy allowed each function to follow its own optimisation pathway while ensuring that the overall search process remained responsive to newly acquired evidence. As confidence increased, optimisation decisions became progressively more focused, but sufficient exploration was retained throughout the project to reduce the risk of overlooking potentially productive regions.

## 10. Decision Making Framework

Every optimisation decision followed the same structured process throughout the project. The workflow began by reviewing the complete history of submitted queries and returned objective values before examining recent changes in performance and longer term optimisation trends. The available evidence was then interpreted to determine which optimisation strategy was most appropriate for each function.

Once candidate query vectors had been generated, they were assessed within the context of previous optimisation rounds rather than being accepted solely on the basis of recent results. This broader perspective reduced the influence of isolated observations and encouraged decisions that reflected the cumulative optimisation history.

Human review formed the final stage of the decision making process. Candidate recommendations were examined before submission to ensure that they remained consistent with the available evidence, satisfied the search constraints and reflected the overall objectives of the optimisation strategy. This combination of computational analysis and human judgement provided a balanced framework that supported transparent, evidence based optimisation while recognising the uncertainty inherent in black box search problems.

## 11. Model Performance

Model performance was assessed by examining how effectively each optimisation round improved understanding of the hidden objective functions while maintaining steady progress towards stronger objective values. Since the mathematical form of the optimisation landscape remained unknown, performance could not be measured against a known optimum. Instead, evaluation focused on the quality of the optimisation decisions and the consistency of the improvements achieved across successive rounds.

As the project progressed, the optimisation strategy became increasingly selective because more evidence was available to guide decision making. Productive regions were identified with greater confidence, allowing local refinement where appropriate while preserving broader exploration for functions that remained poorly understood. This adaptive approach produced a more balanced optimisation strategy than would have been achieved through either unrestricted exploration or exclusive exploitation alone.

By Round 9, individual functions displayed distinct optimisation behaviour. Some functions showed consistent improvement and supported cautious refinement, while others continued to require exploration or reassessment. This demonstrated that the workflow had progressed beyond a uniform search strategy and had developed into an evidence driven optimisation process that responded to the observed behaviour of each function independently.

## 12. Performance Evaluation

Performance was evaluated continuously throughout the project rather than at a single point in time. Every optimisation round was compared with the previous rounds to determine whether new query points contributed useful information or improved objective values. This allowed the optimisation strategy to evolve gradually as additional evidence became available.

Several complementary measures were considered when assessing performance. Changes in objective values provided direct evidence of improvement or deterioration, while longer term trends helped determine whether a function continued to benefit from local refinement or required a change in direction. The stability of neighbouring query points, consistency of the optimisation strategy and the balance between exploration and exploitation were also considered when interpreting the results.

Evaluation was therefore based on the overall development of the optimisation process rather than isolated numerical improvements. This broader perspective reduced the influence of individual observations and provided a more reliable assessment of whether the optimisation strategy was progressing in a meaningful direction.

## 13. Strengths of the Model

One of the principal strengths of the workflow is its ability to adapt as new evidence becomes available. Rather than relying on fixed optimisation rules, the strategy develops progressively by learning from the accumulated optimisation history. This allows the search process to respond naturally to changing evidence while remaining flexible enough to investigate alternative regions whenever necessary.

Another important strength is the transparency of the decision making process. Every recommendation is supported by documented evidence derived from previous optimisation rounds, allowing the reasoning behind each submission to be understood and reviewed. Maintaining this level of documentation improves reproducibility and makes it possible to evaluate how individual optimisation decisions contributed to the overall development of the project.

The workflow also performs well in situations where little information is available about the underlying optimisation landscape. By combining careful exploration with targeted refinement, it makes effective use of a limited query budget while continuing to gather new information throughout the search process. This balance between learning and optimisation allows the workflow to remain effective despite the uncertainty that characterises black box optimisation problems.

## 14. Intended Uses

The workflow has been developed specifically to support sequential Bayesian Black Box Optimisation within the Imperial College London capstone project. Its primary purpose is to assist with selecting informative query points, interpreting optimisation behaviour and documenting the reasoning behind each optimisation decision.

It is intended for educational and research applications where the objective functions remain unknown and optimisation must rely on previously observed evidence rather than explicit mathematical models. The workflow is particularly suited to studying adaptive optimisation, evidence based decision making and the practical challenges associated with balancing exploration and exploitation in complex search spaces.

The accompanying documentation also makes the workflow suitable for teaching transparent research practice by demonstrating how optimisation decisions can be recorded, justified and reproduced using a structured analytical framework.

## 15. Unsuitable Uses

The workflow should not be used to identify the mathematical form of the hidden objective functions or to claim that a global optimum has been reached. Because the optimisation process relies entirely on observed behaviour, all recommendations remain dependent upon the available evidence and should be interpreted within that context.

The workflow has been developed specifically for this optimisation challenge and should not be transferred directly to unrelated optimisation problems without further validation. Differences in search landscapes, objective functions or optimisation constraints may require alternative strategies that fall outside the scope of the present model.

It is also unsuitable for applications where optimisation decisions have direct consequences for safety, healthcare, finance or other high risk environments. In such situations, substantially stronger evidence, formal validation and independent verification would be required before the workflow could be considered appropriate for operational use.

## 16. Model Assumptions

The workflow is built upon several practical assumptions that support optimisation under conditions of uncertainty. The most important assumption is that information gathered during previous optimisation rounds provides useful guidance when selecting future query points. Although the hidden objective functions remain unknown, the accumulated observations are assumed to contain meaningful patterns that can be used to improve subsequent decisions.

A second assumption is that neighbouring query points may demonstrate related behaviour, making cautious local refinement appropriate when repeated observations indicate consistent improvement. At the same time, the workflow recognises that this relationship may not always hold, particularly within complex or irregular optimisation landscapes. For this reason, local refinement is balanced with continued exploration to reduce the risk of relying too heavily on a single region of the search space.

The workflow also assumes that optimisation is an iterative learning process rather than a sequence of isolated events. Every optimisation round contributes additional evidence that improves understanding of the search landscape, allowing future recommendations to become progressively more informed. These assumptions provide a practical framework for decision making while recognising that they remain open to revision as new evidence becomes available.

## 17. Known Limitations

The workflow operates within several important constraints that influence the interpretation of its recommendations. The most significant limitation is that the mathematical form of the hidden objective functions is never revealed. As a result, optimisation decisions are based entirely on observed behaviour rather than complete knowledge of the search landscape.

The limited query budget also restricts the amount of information that can be collected during each optimisation round. With only one new observation available for each function, large areas of the search space remain unexplored, particularly for functions with higher dimensionality. Consequently, recommendations are based on the strongest available evidence rather than complete coverage of the optimisation landscape.

Another limitation is that later optimisation decisions depend upon earlier observations. While this sequential approach reflects the nature of adaptive optimisation, it also means that incorrect interpretations during the early stages of the project may influence later search directions until sufficient evidence becomes available to support an alternative strategy.

These limitations do not reduce the value of the workflow but provide important context when interpreting the optimisation results.

## 18. Potential Failure Modes

Like any optimisation approach operating under uncertainty, the workflow may perform less effectively under certain conditions. One possible failure mode is premature convergence, where repeated refinement within a productive region discourages exploration of other areas that may contain stronger solutions. Closely related to this is the possibility of becoming trapped within a local optimum, particularly when neighbouring observations consistently suggest only small improvements.

The workflow may also encounter difficulties when the hidden objective functions contain abrupt changes, irregular local structure or substantial stochastic variation. Under these conditions, neighbouring query points may behave very differently, reducing the effectiveness of local refinement and making optimisation decisions less predictable.

Another potential limitation arises when the available observations remain too sparse to distinguish genuine optimisation trends from random variation. In these situations, additional exploration becomes necessary to improve understanding of the search landscape before stronger optimisation decisions can be made.

Recognising these potential failure modes encourages a balanced optimisation strategy and reinforces the importance of continual reassessment as new evidence becomes available.

## 19. Sources of Bias

Several sources of bias naturally arise during sequential optimisation because every new query is influenced by previous observations. The most important is adaptive sampling bias. Regions that demonstrate encouraging performance receive more attention during later optimisation rounds, while areas producing weaker results are explored less frequently. Although this improves optimisation efficiency, it also creates uneven coverage of the search space.

A second source of bias is local refinement bias. Once productive regions have been identified, neighbouring query points are often sampled repeatedly in an effort to achieve incremental improvements. This increases confidence within those regions but reduces opportunities to discover alternative solutions elsewhere in the search landscape.

The workflow may also exhibit boundary bias because high performing query points occasionally occur close to the limits of the permitted search interval. Continued refinement around these regions increases the concentration of observations near the search boundaries and may reduce exploration of the central regions of the search space.

Finally, the optimisation history itself introduces temporal bias. Early decisions were made using limited evidence, whereas later recommendations benefited from substantially more information. Consequently, optimisation behaviour changes naturally throughout the project as knowledge of the search landscape increases.

## 20. Human Oversight

Human judgement remained an essential part of the optimisation workflow throughout the project. Although computational analysis provided evidence to support query selection, every recommendation was reviewed before submission to ensure that it remained consistent with the available observations and the overall objectives of the optimisation strategy.

Human oversight also provided an opportunity to question analytical results rather than accepting them automatically. Unexpected changes in objective values, conflicting evidence or unusually large movements within the search space were examined carefully before decisions were finalised. This review process helped reduce the risk of overinterpreting individual observations while encouraging a more balanced assessment of the available evidence.

Maintaining human involvement throughout the optimisation process also strengthened transparency and accountability. Every submitted query represented a considered decision supported by both computational analysis and independent review. This combination allowed the workflow to benefit from systematic analysis while retaining the flexibility and critical judgement that remain important when working with incomplete information and unknown optimisation landscapes.

## 21. Transparency and Interpretability

Transparency and interpretability were fundamental principles throughout the development of the optimisation workflow. Every recommendation was supported by the evidence available at the time rather than being presented as an unexplained outcome. Historical query vectors, returned objective values and analytical summaries were preserved so that the reasoning behind each optimisation decision could be examined and understood.

Interpretability was achieved by documenting how the optimisation strategy changed as new evidence became available. Instead of producing recommendations through an opaque process, the workflow recorded why particular functions were explored, refined, reassessed or exploited. This made it possible to understand how the optimisation strategy evolved and how individual observations influenced later decisions.

Maintaining this level of transparency strengthened confidence in the optimisation process because every recommendation could be traced back to the observations that supported it. The workflow therefore provides not only the optimisation results but also a clear explanation of how those results were obtained.

## 22. Reproducibility

Reproducibility formed an important objective throughout the project. The original optimisation records were preserved together with the computational scripts used to generate analytical summaries and figures. This allows the reported analyses to be repeated directly from the stored data without modifying the original observations.

The repository also maintains a complete record of the optimisation history, allowing every optimisation round to be reproduced using the evidence available at that stage of the project. Because the analytical summaries are generated from the validated source data, the reported findings remain consistent with the original optimisation records.

Comprehensive documentation accompanies the dataset and computational workflow, enabling other researchers to understand the methodology and repeat the analytical process. This combination of preserved data, reproducible analysis and detailed documentation provides a reliable foundation for future investigation and independent verification.

The accompanying [Datasheet](DATASHEET.md) documents the provenance, composition, preprocessing, quality controls, limitations and governance of the data used by this workflow.

## 23. Ethical Considerations

The workflow was developed solely for educational and research purposes within the Bayesian Black Box Optimisation capstone project. It was designed to encourage responsible research practice by documenting every stage of the optimisation process and by presenting both the strengths and limitations of the resulting recommendations.

The optimisation data contain no personal information or sensitive records. All observations relate exclusively to numerical optimisation tasks generated within the capstone challenge, avoiding the ethical concerns commonly associated with datasets containing identifiable individuals or confidential information.

Responsible interpretation of the results remained an important consideration throughout the project. Recommendations were presented as evidence based decisions rather than definitive solutions, and uncertainty was acknowledged whenever the available observations did not support stronger conclusions. This balanced approach encourages appropriate use of the workflow while recognising the limitations inherent in optimisation under uncertainty.

## 24. Distribution and Accessibility

The optimisation workflow is maintained within the Imperial_BBO_Capstone GitHub repository together with the supporting dataset, computational scripts, analytical summaries and documentation. Organising the project within a structured repository provides a single location from which the optimisation process can be examined, reproduced and maintained.

The repository has been arranged so that users can move easily between the raw optimisation records, analytical outputs and supporting documentation. This structure improves accessibility while ensuring that the relationship between the original observations and the derived analyses remains clear.

The workflow has been prepared primarily for educational and research purposes. Future users should preserve the accompanying documentation whenever the repository is shared so that the optimisation process continues to be interpreted within its intended context.

## 25. Version Control

Version control has been maintained throughout the project to preserve the complete development history of the optimisation workflow. Every optimisation round represents a new stage in the evolution of the model, allowing earlier recommendations and analytical results to remain available for comparison with later developments.

Each repository update records newly submitted query vectors, returned objective values, revised analyses and supporting documentation. Maintaining this chronological record provides a transparent account of how the optimisation strategy developed as additional evidence became available.

Version control also strengthens reproducibility by allowing individual optimisation rounds to be revisited whenever required. Earlier recommendations can therefore be examined using the evidence available at that time, providing a reliable audit trail for both the optimisation process and the accompanying documentation.

## 26. Maintenance

The optimisation workflow will continue to develop as additional optimisation rounds are completed. After each new round, the repository will be updated with the latest query vectors, returned objective values, revised analytical summaries and supporting documentation. Earlier records will remain unchanged so that the complete optimisation history is preserved.

Routine maintenance includes checking the consistency of the optimisation records, confirming that analytical summaries agree with the source data and ensuring that all supporting documentation reflects the latest evidence. This ongoing review helps maintain the reliability of the workflow while preserving a transparent record of every stage of its development.

By combining regular updates with careful version control and comprehensive documentation, the workflow is able to evolve without losing the historical evidence that supports its recommendations. This ensures that the optimisation process remains transparent, reproducible and straightforward to maintain throughout the remainder of the capstone project.

## 27. Future Development

The optimisation workflow will continue to develop as additional optimisation rounds provide new evidence. Each successive round will strengthen understanding of the hidden objective functions, allowing the optimisation strategy to become progressively more informed while preserving the flexibility to respond to unexpected changes within the search landscape.

Future work will focus on refining the balance between exploration and exploitation as the amount of available evidence increases. Longer optimisation histories will provide opportunities to examine performance trends over extended periods, compare alternative optimisation strategies and assess how individual functions respond to different search approaches. These developments will improve understanding of the optimisation process while maintaining the adaptive principles on which the workflow is based.

The supporting documentation will also continue to evolve. Future versions of the workflow may include additional performance measures, expanded validation procedures and more detailed analytical visualisations. These enhancements will strengthen interpretation of the optimisation process without changing the original optimisation records that form the foundation of the repository.

Although the workflow has been developed for the current capstone challenge, the underlying documentation framework has wider potential. The combination of transparent decision making, reproducible analysis and comprehensive reporting provides a practical model that could be adapted for other optimisation studies where clear documentation and responsible research practice are important.

## 28. Conclusion

This model card describes the optimisation workflow developed for the Bayesian Black Box Optimisation capstone project and explains how historical observations were transformed into evidence based optimisation decisions. Rather than relying on explicit mathematical models of the hidden objective functions, the workflow progressively improved its recommendations by interpreting the optimisation history accumulated across successive rounds.

A key strength of the workflow is its ability to adapt as new evidence becomes available. Exploration, refinement, reassessment and exploitation were applied according to the observed behaviour of each function, allowing the optimisation strategy to become increasingly focused while maintaining sufficient flexibility to investigate areas that remained uncertain. Human review remained an important part of every optimisation round, ensuring that computational analysis supported rather than replaced informed judgement.

Transparency and reproducibility formed the foundation of the workflow. Every optimisation recommendation can be traced back to the observations that supported it, while the accompanying documentation provides a complete record of how the optimisation strategy evolved throughout the project. This makes the workflow straightforward to understand, review and reproduce.

Although the hidden objective functions and limited query budget impose unavoidable constraints, the workflow demonstrates that careful interpretation of accumulated evidence can support effective optimisation under uncertainty. The result is not simply a sequence of submitted query vectors, but a structured and well documented optimisation process that records both the decisions made and the reasoning that guided them.

## 29. References

Frazier, P. I. (2018). A Tutorial on Bayesian Optimization. arXiv:1807.02811.

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., and Crawford, K. (2021). Datasheets for Datasets. Communications of the ACM, 64(12), 86-92.

Imperial College London. (2026). Module 21: Transparency, Interpretability and Responsible AI. Professional Certificate in Machine Learning and Artificial Intelligence. Course materials.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. (2019). Model Cards for Model Reporting. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220-229.

Nocedal, J., and Wright, S. J. (2006). Numerical Optimization (2nd ed.). Springer.

Pisharam, N. T. (2026). Imperial_BBO_Capstone: Bayesian Black Box Optimisation Repository. GitHub project documentation.

Snoek, J., Larochelle, H., and Adams, R. P. (2012). Practical Bayesian Optimization of Machine Learning Algorithms. Advances in Neural Information Processing Systems, 25, 2951-2959.
