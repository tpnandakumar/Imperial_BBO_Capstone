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

## 1. Model Overview

This Model Card describes the Bayesian Black Box Optimisation workflow developed for the Imperial College London Machine Learning and Artificial Intelligence capstone project. The workflow supports sequential optimisation of eight hidden objective functions using only submitted query vectors and returned objective values. Because the analytical form, gradients, noise properties and true optima of the functions remain unknown, recommendations are based on the evidence accumulated during earlier rounds.

The workflow combines historical optimisation data, computational analysis and human judgement. It recommends one query vector for each function during every round and assigns a strategy such as Explore, Refine, Reassess or Exploit. It is not an autonomous submission system. Every recommendation is reviewed before use.

## 2. Purpose

The primary purpose is to improve objective values while using a limited query budget efficiently. The workflow seeks to balance exploration of uncertain regions with refinement of areas that have already shown useful performance.

A second purpose is to make the decision process transparent. The workflow records the evidence, assumptions and reasoning behind each recommendation so that later reviewers can understand why a particular point was selected and how the strategy changed over time.

The workflow also serves an educational role by demonstrating adaptive optimisation under uncertainty and showing how historical evidence can be converted into structured decisions without access to the underlying mathematical functions.

## 3. Model Description and Architecture

The workflow follows a sequential cycle:

1. retrieve the cumulative input and output history;
2. compare recent and longer-term performance;
3. assess uncertainty and local stability for each function;
4. classify the function as Explore, Refine, Reassess or Exploit;
5. generate one or more candidate query vectors;
6. check dimensionality, range and six-decimal precision;
7. apply human review before submission;
8. record the returned outputs and update the evidence base.

This architecture allows each function to follow an individual optimisation pathway. A strong region may justify controlled exploitation, while a weak or uninformative region may require broader exploration. The same strategy is not imposed across all eight functions.

<img width="1536" height="1024" alt="model_workflow" src="https://github.com/user-attachments/assets/f9007ac9-ee63-4e3d-91fb-0411e6f4c68e" />


## 4. Model Inputs

The principal inputs are:

- historical query vectors;
- historical objective values;
- the dimensionality of each function;
- the permitted input range from 0 to 1;
- changes between consecutive rounds;
- best-so-far values;
- local stability or inconsistency among neighbouring queries;
- qualitative confidence and uncertainty judgements;
- previous strategy decisions and their outcomes.

The complete optimisation history is reviewed rather than relying only on the latest result. This reduces the risk that a short-term fluctuation determines the next query without reference to the broader pattern.

## 5. Model Outputs

The main output is one six-decimal query vector for each hidden objective function. Supporting outputs include:

- a strategy label for each function;
- a written rationale;
- the expected benefit of the query;
- the principal risk or uncertainty;
- weekly performance comparisons;
- function rankings, interpreted cautiously because scales differ;
- figures and analytical summaries.

These outputs are decision-support artefacts. They do not represent direct knowledge of the hidden functions.

## 6. Model Development and Strategy Evolution

The workflow developed progressively across the first nine rounds. Early submissions relied mainly on broad exploration because little was known about the search landscape. As observations accumulated, several functions began to show stable or improving regions, allowing the strategy to move towards local refinement and exploitation.

By Week 09, the functions had differentiated clearly. Function 5 had shown repeated improvement and became the main exploitation target. Functions 2, 4, 7 and 8 supported local refinement. Functions 3 and 6 required reassessment because recent changes weakened confidence in their current directions. Function 1 remained the main exploration target because repeated queries produced an output effectively equal to zero.

This evolution demonstrates that the workflow adapts according to evidence rather than following a fixed rule. Strategies can change when new outputs challenge earlier interpretations.

## 7. Week 09 Performance

| Function | Week 08 output | Week 09 output | Change | Week 09 strategy |
|---|---:|---:|---:|---|
| F1 | -1.4546199699251391e-58 | -1.4546199699251391e-58 | 0.000000 | Explore |
| F2 | 0.5672775862793291 | 0.47297842839949866 | -0.094299 | Refine |
| F3 | -0.0991107637427902 | -0.1156707106126581 | -0.016560 | Reassess |
| F4 | -12.305008897187289 | -11.788939969158545 | 0.516069 | Refine |
| F5 | 4359.384134322703 | 4394.868042481448 | 35.483908 | Exploit |
| F6 | -1.1197178425911847 | -1.1733030029888645 | -0.053585 | Reassess |
| F7 | 1.3346391663186332 | 1.314307996450604 | -0.020331 | Refine |
| F8 | 9.47621 | 9.4709436 | -0.005266 | Refine |

Function 5 remained the dominant performer and improved again in Week 09. Function 4 also moved in a favourable direction by becoming less negative. Functions 2, 3, 6, 7 and 8 declined by varying amounts, while Function 1 remained unchanged near zero. These mixed results justified differentiated rather than uniform query selection.

## 8. Evaluation Metrics

The workflow is evaluated using observed outputs rather than access to the true functions. The principal measures are:

- best-so-far objective value;
- change from the preceding round;
- direction and stability of longer-term trends;
- consistency among neighbouring queries;
- whether the selected strategy matched the available evidence;
- compliance with dimensionality, range and precision constraints;
- preservation of sufficient exploratory capacity.

Cross-function rankings are used only for descriptive context because the objective functions operate on different numerical scales. Performance is therefore judged primarily within each function across time.

## 9. Strengths

A major strength is adaptability. The workflow can alter its strategy as new evidence appears, allowing promising functions to be refined while uncertain functions continue to be explored.

A second strength is transparency. Each recommendation is accompanied by evidence and a stated rationale rather than being presented as an unexplained output.

The workflow also preserves human oversight. Computational analysis organises the evidence, but the final submission remains subject to review. This reduces the risk of blindly following a misleading local pattern.

Finally, the repository retains raw data, code, summaries and documentation, supporting reproducibility and later audit.

## 10. Intended Uses

The workflow is intended for:

- weekly query recommendation within this BBO challenge;
- analysis of exploration and exploitation strategies;
- transparent explanation of optimisation decisions;
- comparison of strategy evolution across rounds;
- educational study of sequential optimisation under uncertainty;
- reproducible computational analysis of the capstone data.

## 11. Unsuitable Uses

The workflow should not be used to:

- infer the exact analytical form of the hidden functions;
- claim that a global optimum has been proven;
- submit queries autonomously without review;
- transfer recommendations directly to unrelated optimisation tasks;
- support clinical, financial or safety-critical decisions;
- treat qualitative confidence estimates as calibrated probabilities.

Any use beyond the capstone setting would require separate validation and a reassessment of assumptions, constraints and risks.

## 12. Model Assumptions

The workflow assumes that historical observations provide useful guidance for future query selection and that larger objective values are preferable. It also assumes that cautious local movement may be reasonable where repeated improvement has occurred.

These assumptions do not guarantee local smoothness. A hidden function may contain discontinuities, irregular interactions or noise, meaning that nearby points can behave differently. Assumptions are therefore treated as provisional and are reviewed after every new output.

## 13. Known Limitations

The workflow is constrained by a small sequential dataset, unknown objective functions, unknown noise properties and a limited query budget. Higher-dimensional functions are especially difficult to explore because each new point covers only a very small proportion of the search space.

Confidence estimates are partly qualitative, and recommendations depend on human interpretation. Adaptive sampling also means that observations are not independent or uniformly distributed.

The workflow cannot verify whether an apparent improvement path leads to a local or global optimum. Its recommendations represent the strongest decision supported by the available evidence, not a definitive solution.

## 14. Potential Failure Modes

Potential failure modes include:

- premature convergence around a productive but suboptimal region;
- local overfitting to recent observations;
- excessive boundary concentration;
- misleading local trends caused by noise or discontinuity;
- insufficient exploration of distant regions;
- incorrect interpretation of heterogeneous function scales;
- propagation of an early mistaken assumption into later rounds.

These risks are managed through continued exploration, explicit reassessment, comparison with prior rounds and mandatory human review.

## 15. Sources of Bias

Adaptive sampling bias occurs because promising regions receive more queries than weaker areas. Local refinement bias develops when repeated queries cluster near a known productive point. Boundary bias may occur where strong outputs encourage continued movement close to the edge of the permitted domain.

Temporal bias is also present because later decisions benefit from more information than early decisions. These biases are inherent to sequential optimisation and must be recognised when interpreting the dataset and performance.

## 16. Human Oversight and Risk Controls

Human review is mandatory before submission. Candidate queries are checked against the historical evidence, dimensionality requirements, permitted range and intended strategy.

Risk controls include:

- preservation of raw records;
- exact input validation;
- comparison with earlier rounds;
- explicit strategy labels and assumptions;
- retention of exploratory capacity;
- documentation of alternatives and uncertainty;
- reproducible scripts and analytical summaries.

Human oversight does not remove uncertainty, but it provides a critical check against automatic acceptance of weak or contradictory recommendations.

## 17. Transparency and Interpretability

The workflow is designed so that each recommendation can be traced from historical observations to strategy classification and final query selection. The repository preserves the relevant data, code, summaries and written rationale.

Interpretability is supported by using clear strategy categories and by explaining why each function was treated differently. The process therefore provides both a recommendation and an account of how that recommendation was reached.

## 18. Reproducibility

Reproducibility is supported by retaining the original query and output files, cumulative histories, Python analysis scripts, figures and weekly documentation. Another researcher can repeat the analytical calculations and review the evidence available at the time of each decision.

The accompanying [Datasheet](DATASHEET.md) documents the provenance, composition, preprocessing, quality controls and limitations of the data. Additional supporting files include [DATASET.md](DATASET.md), [DECISION_CARD.md](DECISION_CARD.md), [ASSUMPTIONS.md](ASSUMPTIONS.md) and [VALIDATION.md](VALIDATION.md).

## 19. Ethical Considerations

The workflow was developed for educational and research purposes. It contains no personal or sensitive data. Ethical responsibility therefore centres on truthful reporting, appropriate interpretation and clear acknowledgement of uncertainty.

The workflow should not be presented as proving optimality or transferred to high-risk settings without formal validation. Human review should remain in place, and both successful and unsuccessful results should be retained to avoid selective reporting.

## 20. Distribution, Version Control and Maintenance

The workflow is maintained in the `tpnandakumar/Imperial_BBO_Capstone` GitHub repository. Each round is stored in a separate weekly folder with its source data, analysis, figures and documentation.

Git version control preserves changes over time and allows earlier rounds to be revisited. The workflow is maintained by Dr N T Pisharam. Later updates should preserve historical records, document corrections and keep the Datasheet, Model Card and related files consistent.

## 21. Future Development

Future development may include stronger uncertainty estimation, additional performance metrics, improved response-surface visualisation and more formal comparison of alternative candidate queries. As the dataset grows, the workflow may support increasingly quantitative acquisition methods while retaining human review and transparent documentation.

## 22. Version History

| Version | Date | Round | Summary |
|---|---|---:|---|
| 0.9 / Document 1.0 | August 2026 | 9 | Final Module 21 model card submission |

## References

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. (2019). *Model Cards for Model Reporting*. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220-229.

Frazier, P. I. (2018). *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.

Snoek, J., Larochelle, H., and Adams, R. P. (2012). *Practical Bayesian Optimization of Machine Learning Algorithms*. Advances in Neural Information Processing Systems, 25, 2951-2959.

Imperial College London. (2026). *Module 21: Transparency, Interpretability and Responsible AI*. Professional Certificate in Machine Learning and Artificial Intelligence.
