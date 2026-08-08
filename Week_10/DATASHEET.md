# Datasheet for the Bayesian Black Box Optimisation Capstone Dataset

**Author:** Dr N T Pisharam  
**Project:** Imperial BBO Optimisation  
**Capstone week:** 10  
**Optimisation round:** 10  
**Document status:** Full detailed datasheet

## 1. Executive Summary

This datasheet documents the Bayesian Black Box Optimisation dataset at the completion of Week 10. The dataset records the sequential optimisation of eight hidden objective functions using only submitted query vectors and the objective values returned by the competition platform. By the end of Week 10, each function had ten recorded observations, giving eighty submitted query vectors and eighty corresponding objective values across the eight optimisation pathways.

Week 10 added an important validation point to the accumulated dataset. Function 5 was deliberately submitted at the exact Week 09 best known input and returned the exact same objective value, `4394.868042481448`. This provided direct evidence of repeatability at that tested location. Functions 2 and 3 improved, Function 1 changed sign but remained effectively near zero, and Functions 4, 6, 7 and 8 declined. The mixed outcome strengthened the case for treating each function independently rather than applying a uniform optimisation rule.

The raw observations remain authoritative. Derived rankings, strategy labels, comparisons, figures and information gain interpretations are analytical products generated from the verified data and are stored separately from the source observations.

## 2. Motivation

The dataset was created to preserve the complete history of a sequential black box optimisation problem in which the underlying mathematical functions are not disclosed. Because gradients, equations and direct access to the response surfaces are unavailable, every later query depends on evidence accumulated from earlier submissions.

A central motivation is traceability. The repository records not only which query was submitted but also what result was returned, how that result compared with earlier observations and how it influenced the next decision. Week 10 is particularly useful because it contains both successful local movements and clear counterexamples to continuation in previously tested directions.

## 3. Dataset Overview

The Week 10 dataset contains observations for eight independent hidden objective functions. Input dimensionality ranges from two to eight variables. Every coordinate is constrained to the interval from zero to one and is submitted to six decimal places.

The dataset is sequential rather than independently sampled. Later observations were selected using evidence available from earlier rounds, so the sampling distribution changes as the search becomes more informed. By the completion of Week 10, ten observations were available for every function.

## 4. Dataset Composition

| Function | Dimensions | Observations by Week 10 |
|---|---:|---:|
| Function 1 | 2 | 10 |
| Function 2 | 2 | 10 |
| Function 3 | 3 | 10 |
| Function 4 | 4 | 10 |
| Function 5 | 4 | 10 |
| Function 6 | 5 | 10 |
| Function 7 | 6 | 10 |
| Function 8 | 8 | 10 |

The dimensional structure remains fixed across all rounds. Week 10 adds one verified observation to each function without altering any earlier record.

## 5. Week 10 Submitted Inputs

| Function | Input |
|---|---|
| Function 1 | `0.450000,0.650000` |
| Function 2 | `0.700000,0.955000` |
| Function 3 | `0.280000,0.875000,0.315000` |
| Function 4 | `0.290000,0.730000,0.690000,0.210000` |
| Function 5 | `0.120000,0.997000,0.999800,0.999800` |
| Function 6 | `0.260000,0.780000,0.260000,0.840000,0.300000` |
| Function 7 | `0.060000,0.500000,0.250000,0.220000,0.430000,0.740000` |
| Function 8 | `0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000` |

These values are reproduced exactly from `week_10_inputs.csv`.

## 6. Week 10 Returned Outputs

| Function | Output |
|---|---:|
| Function 1 | `2.8950706668499033e-23` |
| Function 2 | `0.5311818841205426` |
| Function 3 | `-0.08697581687486715` |
| Function 4 | `-13.483642655031158` |
| Function 5 | `4394.868042481448` |
| Function 6 | `-1.2283806967341901` |
| Function 7 | `1.285160161342515` |
| Function 8 | `9.4646525` |

These values are reproduced exactly from `week_10_results.csv`.

## 7. Week 09 to Week 10 Change

| Function | Week 09 output | Week 10 output | Exact change |
|---|---:|---:|---:|
| Function 1 | `-1.4546199699251391e-58` | `2.8950706668499033e-23` | `2.895070666849903300000000000E-23` |
| Function 2 | `0.47297842839949866` | `0.5311818841205426` | `0.05820345572104394` |
| Function 3 | `-0.1156707106126581` | `-0.08697581687486715` | `0.02869489373779095` |
| Function 4 | `-11.788939969158545` | `-13.483642655031158` | `-1.694702685872613` |
| Function 5 | `4394.868042481448` | `4394.868042481448` | `0` |
| Function 6 | `-1.1733030029888645` | `-1.2283806967341901` | `-0.0550776937453256` |
| Function 7 | `1.314307996450604` | `1.285160161342515` | `-0.029147835108089` |
| Function 8 | `9.4709436` | `9.4646525` | `-0.0062911` |

## 8. Data Collection Methodology

Each round followed the same collection sequence. Historical observations were reviewed, a new query vector was selected for each function, all values were checked against dimensionality and range constraints, and the eight queries were submitted through the official platform. Returned values were then copied into the repository without transformation.

Week 10 retained this procedure. Function 5 was intentionally repeated at the exact Week 09 best known input. The returned value was identical, providing a useful repeat observation within the otherwise adaptive dataset.

## 9. Query Generation Strategy

The Week 10 query set combined different strategies because the eight functions had developed different evidence profiles.

Function 5 was exploited through exact repetition of the established best input. Functions 2, 3, 7 and 8 were refined locally. Functions 4 and 6 were moved within alternative local regions after mixed earlier behaviour. Function 1 received broader exploration because previous outputs had remained effectively zero.

## 10. Optimisation Workflow

The workflow followed a repeated sequence of historical review, function specific assessment, candidate selection, dimensionality and range checking, official submission, exact result capture and comparison with the preceding round.

This structure preserves a clear distinction between observed data and later interpretation.

## 11. Data Preprocessing

No scaling, normalisation, imputation or transformation was applied to the raw inputs or returned outputs. Input vectors were preserved to six decimal places exactly as submitted. Returned values were stored at the precision provided by the platform.

Preprocessing was limited to structural validation, parsing for analysis and generation of derived summaries.

## 12. Data Validation and Quality Assurance

Quality assurance checks confirmed that every Week 10 function had exactly one query vector and one returned result. Input dimensionality was checked against the fixed specification for each function, and all coordinates were confirmed to remain within the permitted interval.

The Week 10 scripts use exact decimal comparison for changes between Weeks 09 and 10. Raw CSV files remain separate from figures and narrative interpretation.

## 13. Feature Description

Each input feature is a continuous numerical coordinate within the corresponding function's search space. Feature names are positional because the underlying semantic meaning of each coordinate is not disclosed by the competition.

The target for each observation is a single continuous objective value. Higher returned values are treated as better within each function because the challenge objective is maximisation.

## 14. Data Labelling and Derived Variables

Derived fields include function rank, week to week change, strategy classification, status and information gain interpretations. These variables are generated from the verified observations and are intended to support analysis.

They are not competition outputs and should not be interpreted as ground truth labels for the hidden functions.

## 15. Week 10 Strategy Classification

| Function | Week 10 output | Strategy after Week 10 |
|---|---:|---|
| Function 1 | `2.8950706668499033e-23` | Explore |
| Function 2 | `0.5311818841205426` | Refine |
| Function 3 | `-0.08697581687486715` | Refine |
| Function 4 | `-13.483642655031158` | Reassess |
| Function 5 | `4394.868042481448` | Exploit |
| Function 6 | `-1.2283806967341901` | Reassess |
| Function 7 | `1.285160161342515` | Refine |
| Function 8 | `9.4646525` | Refine |

## 16. Exploratory Data Characteristics

The dataset contains a mixture of broad exploratory observations and increasingly concentrated local observations. Productive regions receive more attention over time, while unresolved functions retain broader search behaviour.

Function 5 is the clearest example of concentration around a high performing boundary region. Function 1 provides the opposite pattern, with repeated attempts still producing values effectively near zero.

## 17. Repeatability Evidence

Week 10 provides a direct repeat observation for Function 5. The Week 09 input `0.120000,0.997000,0.999800,0.999800` was submitted again in Week 10 and returned `4394.868042481448` on both occasions.

This supports repeatability at that tested point. It does not establish the mathematical form of Function 5, prove global optimality or demonstrate stability throughout the surrounding search region.

## 18. Missing Data

The verified Week 10 files contain a complete input and output record for all eight functions. No Week 10 observation is missing from the stored weekly dataset.

The hidden mathematical definitions of the objective functions remain unavailable by design and are therefore not treated as missing records.

## 19. Data Provenance

The primary data originate from query vectors submitted through the official BBO platform and objective values returned by that platform. The repository stores those values in `week_10_inputs.csv` and `week_10_results.csv`.

Analytical summaries and figures are derived from those source files and from verified Week 09 comparison data.

## 20. Data Integrity

Source observations are not overwritten during analysis. Derived outputs are written to separate summary files. The authoritative Week 10 files are `week_10_inputs.csv` and `week_10_results.csv`.

## 21. Bias and Sampling Considerations

The dataset is intentionally adaptively sampled. Query points are selected using earlier results, so observations are not independent or uniformly distributed across the search spaces. Productive areas can become overrepresented as exploitation increases.

This is appropriate for optimisation but limits claims about the global geometry of the hidden functions.

## 22. Limitations

The true functions and global optima are unknown. Ten observations per function remain sparse, particularly for the higher dimensional objectives. Apparent trends may represent local behaviour rather than global structure.

Cross function numerical rankings should also be interpreted cautiously because the eight objectives operate on different scales.

## 23. Intended Uses

The dataset is intended for analysis of sequential black box optimisation, exploration and exploitation behaviour, reproducibility, strategy development and educational study of decision making under uncertainty.

## 24. Unsuitable Uses

The dataset should not be used to claim recovery of the hidden objective functions, proof of a global optimum or general superiority of one optimisation algorithm over another.

It should not be transferred directly into safety critical decision making without independent validation and substantially stronger evidence.

## 25. Ethical and Responsible Use

The capstone dataset contains optimisation values rather than personal or clinical records. The principal responsible use issues concern transparency, reproducibility and appropriate limits on claims.

Derived interpretations should remain clearly distinguishable from platform returned observations. Later methodological developments should not be presented retrospectively as though they had been used in earlier rounds unless the contemporaneous record supports that statement.

## 26. Reproducibility

Week 10 analysis can be reproduced from the repository root with:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The analysis script uses the Week 09 result file for exact comparison. The figure script writes generated files directly into `Week_10` and does not require a separate figures folder.

## 27. Week 10 Summary

Week 10 expanded the cumulative dataset to eighty submitted query vectors and eighty returned objective values. Functions 2 and 3 improved, Function 5 repeated its best known result exactly, Function 1 remained effectively near zero, and Functions 4, 6, 7 and 8 declined.

The value of the round lies not only in the successful movements but also in the information supplied by unsuccessful ones. The Week 10 observations narrowed the evidence available for subsequent decisions and provided the basis for a more differentiated Week 11 strategy.

## References

Imperial College Business School. Artificial Intelligence and Machine Learning Programme, Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. Gaussian Processes for Machine Learning. MIT Press.

Frazier, P. I. A Tutorial on Bayesian Optimization. arXiv:1807.02811.