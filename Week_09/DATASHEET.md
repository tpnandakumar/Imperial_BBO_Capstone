# Datasheet for the Bayesian Black Box Optimisation Capstone Dataset

**Author:** Dr N T Pisharam  
**Course module:** 21  
**Capstone week:** 09  
**Optimisation round:** 9  
**Document version:** 1.0  
**Status:** Final Module 21 submission  
**Repository:** `tpnandakumar/Imperial_BBO_Capstone`

## 1. Executive Summary

This datasheet documents the Bayesian Black Box Optimisation dataset developed during the Imperial College London Machine Learning and Artificial Intelligence capstone project. It records the optimisation process up to Round 9, including submitted query vectors, returned objective values and the analytical evidence used to guide later rounds. The dataset is sequential rather than static because each new submission builds on the results collected previously.

The dataset covers eight hidden objective functions with dimensionalities ranging from two to eight variables. By the end of Round 9, each function had nine recorded query vectors and nine corresponding outputs. This produced a cumulative total of 72 query vectors and 72 objective values. The repository also contains analytical summaries, Python scripts and figures generated from these source records.

Transparency and reproducibility were central to the project. Raw inputs and outputs were preserved, while rankings, strategy labels and visualisations were created separately. This allows each optimisation decision to be traced back to the evidence available at the time.

## 2. Motivation

The capstone challenge requires participants to improve eight unknown objective functions using only the information returned after each submission. The mathematical form of each function, its gradients, noise properties and true optimum are hidden. Query selection must therefore rely on observed results and the interpretation of emerging patterns.

The dataset was created to preserve the complete optimisation history rather than only the final queries. This makes it possible to review how the strategy developed from broad exploration during the early rounds towards more focused refinement and exploitation as evidence accumulated. It also preserves unsuccessful directions, which are important because they explain why later decisions changed.

The dataset has an educational purpose as well. It demonstrates how sequential optimisation develops under uncertainty, how exploration and exploitation are balanced, and how limited observations affect confidence in the conclusions.

## 3. Dataset Provenance

The data were generated directly through the official Imperial Bayesian Black Box Optimisation capstone process. Query vectors were submitted to the course platform, and the returned objective values were recorded exactly as received before being added to the cumulative history. The retained Week 09 input file, output file and official processed-submission record provide the authoritative source evidence for this round.

All rankings, strategy labels, comparisons and figures were derived from these original records. Derived material supports interpretation but does not replace the raw data.

## 4. Dataset Composition

| Function | Dimensions | Query vectors by Round 9 | Returned outputs by Round 9 |
|---|---:|---:|---:|
| Function 1 | 2 | 9 | 9 |
| Function 2 | 2 | 9 | 9 |
| Function 3 | 3 | 9 | 9 |
| Function 4 | 4 | 9 | 9 |
| Function 5 | 4 | 9 | 9 |
| Function 6 | 5 | 9 | 9 |
| Function 7 | 6 | 9 | 9 |
| Function 8 | 8 | 9 | 9 |

Each input coordinate is a continuous value between 0 and 1. Submission values are recorded to six decimal places. Each query produces one scalar objective value. The output scales differ substantially across functions, so cross-function rankings must be interpreted cautiously.

The Week 09 folder contains the raw weekly records, cumulative histories, analytical summaries, code, figures and documentation needed to review the round and reproduce the analysis.

<img width="1536" height="1024" alt="dataset_composition" src="https://github.com/user-attachments/assets/d236414e-32c1-4ca8-bb2b-30a4739573d3" />


## 5. Collection Process

Data were collected sequentially across nine optimisation rounds. At the start of each round, the full history of earlier inputs and outputs was reviewed. One new query vector was then selected for each function and submitted through the official platform. Returned values were recorded without modification and added to the cumulative dataset.

Query selection was human supervised and used four broad strategies:

1. **Explore** when a region remained uninformative or poorly sampled.
2. **Refine** when a local region showed useful or stable behaviour.
3. **Reassess** when recent results weakened or conflicted with earlier evidence.
4. **Exploit** when repeated observations supported continued local improvement.

For Week 09, Function 5 was the principal exploitation target. Functions 2, 4, 7 and 8 were refined locally. Functions 3 and 6 were reassessed, while Function 1 remained the main exploration target because its output was effectively zero.

## 6. Preprocessing, Cleaning and Labelling

The raw query vectors and objective values were preserved without scaling, normalisation, imputation or transformation. Preprocessing focused on data integrity rather than numerical alteration.

Each query was checked for the correct number of dimensions, compliance with the permitted range from 0 to 1, six-decimal submission precision and one complete input-output pair per function. Returned outputs were matched to the corresponding submitted vectors before analysis.

Derived annotations included function rankings, changes between rounds, best-so-far summaries and strategy labels such as Explore, Refine, Reassess and Exploit. These labels describe the decision taken during a particular round. They are not ground-truth properties of the hidden functions.

## 7. Data Quality

At the end of Round 9, the cumulative record contained nine complete query-output pairs for each of the eight functions. No missing weekly outputs were identified in the supplied Round 1 to Round 9 records. Dimensionality, numerical range, precision and input-output correspondence were checked before analytical summaries were produced.

Quality assurance also included comparison of Week 09 with Week 08, verification of exact changes in objective values and regeneration of figures from the stored source data. Validation confirms the accuracy and consistency of the records, but it cannot verify the unknown mathematical landscape itself.

## 8. Intended Uses

The dataset is suitable for:

- analysing sequential black box optimisation;
- comparing performance between rounds;
- studying exploration, refinement, reassessment and exploitation;
- reproducing weekly summaries and figures;
- documenting why later query points were selected;
- teaching transparent optimisation under limited observations.

## 9. Unsuitable Uses

The dataset should not be used to infer the analytical form of the hidden functions, prove that a global optimum has been reached or claim uniform coverage of the search space. It should not be treated as an independently sampled dataset because later observations depend on earlier results.

It is also unsuitable for direct use in clinical, financial, safety-critical or unrelated operational settings. Transfer to another optimisation problem would require separate validation because the observations and strategy were developed for this specific challenge.

## 10. Limitations and Sources of Bias

The principal limitation is the small number of observations relative to the size of the search spaces. Only one new query per function is obtained during each round, and higher-dimensional functions are particularly difficult to explore thoroughly.

Adaptive sampling creates uneven coverage because promising regions receive more attention than weaker regions. Local refinement may lead to overconcentration around a productive point, while boundary refinement may reduce exploration of central regions. Temporal bias is also present because later decisions benefit from more evidence than early decisions.

The functions may contain discontinuities, irregular local structure or noise. Nearby query points therefore do not necessarily produce similar results. These uncertainties limit the strength of any claim about local or global optimality.

## 11. Assumptions

The analysis assumes that each returned output corresponds correctly to its submitted query and that larger objective values are preferable. It also assumes that historical observations provide useful guidance for later decisions and that cautious local movement may be reasonable where repeated improvement has been observed.

These assumptions are practical rather than proven. They are reviewed as new evidence becomes available and may be revised when later outputs conflict with earlier interpretations.

## 12. Ethical Considerations

The dataset contains no personal, clinical or identifiable information. It consists entirely of numerical optimisation inputs and outputs generated through the capstone challenge.

Responsible use requires clear acknowledgement of uncertainty, adaptive sampling bias and the inability to prove global optimality. Derived labels should support human interpretation rather than be treated as objective truth. The repository preserves both successful and unsuccessful observations so that the research record remains balanced and auditable.

## 13. Distribution and Accessibility

The dataset is maintained in the `tpnandakumar/Imperial_BBO_Capstone` GitHub repository. Each optimisation round is stored in a separate weekly folder with its data, scripts, figures and documentation. Access and redistribution are governed by repository settings, course requirements and any applicable licence conditions.

The accompanying [Model Card](MODEL_CARD.md) explains how this dataset was used within the optimisation workflow. The file-level structure and schemas are described in [DATASET.md](DATASET.md).

## 14. Version Control and Maintenance

Git version control preserves the historical development of the dataset. Each weekly update records newly submitted queries, returned values, revised summaries and related documentation. Earlier rounds are retained rather than overwritten.

The dataset is maintained by Dr N T Pisharam. Corrections should preserve the original source records wherever possible, explain the reason for the change and update all affected analytical and documentation files in the same development cycle.

## 15. Future Development

The dataset will continue to expand as later optimisation rounds are completed. Future work may add longer-term performance measures, uncertainty summaries, stronger validation procedures and improved visualisations. These additions should remain separate from the authoritative raw inputs and outputs.

## 16. Version History

| Version | Date | Round | Summary |
|---|---|---:|---|
| 1.0 | August 2026 | 9 | Final Module 21 datasheet submission |

## References

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., and Crawford, K. (2021). *Datasheets for Datasets*. Communications of the ACM, 64(12), 86-92.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. (2019). *Model Cards for Model Reporting*. Proceedings of the Conference on Fairness, Accountability, and Transparency, 220-229.

Frazier, P. I. (2018). *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.

Imperial College London. (2026). *Module 21: Transparency, Interpretability and Responsible AI*. Professional Certificate in Machine Learning and Artificial Intelligence.
