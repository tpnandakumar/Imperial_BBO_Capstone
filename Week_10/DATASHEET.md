# Datasheet for the Bayesian Black Box Optimisation Capstone Dataset

**Author:** Dr N T Pisharam  
**Capstone week:** 10  
**Optimisation round:** 10  
**Document status:** Week 10 datasheet

## 1. Purpose

This datasheet records the dataset available at the end of Week 10. It covers eight hidden objective functions, the submitted query vectors, the returned objective values and the derived comparisons used to interpret the round.

By the end of Week 10, each function had ten recorded observations. Across the eight functions, the cumulative record therefore contained eighty submitted query vectors and eighty returned objective values.

The source observations remain authoritative. Rankings, strategy labels, figures and written interpretations are derived from those observations.

## 2. Dataset structure

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

Every input coordinate lies between 0 and 1 and is submitted to six decimal places. The hidden meaning of each coordinate is not disclosed, so features are positional rather than semantically labelled.

## 3. Exact Week 10 inputs

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

These values are taken directly from `week_10_inputs.csv`.

## 4. Exact Week 10 outputs

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

These values are taken directly from `week_10_results.csv`.

## 5. Week 09 to Week 10 comparison

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

Functions 2 and 3 improved. Function 5 repeated its Week 09 value exactly. Functions 4, 6, 7 and 8 declined. Function 1 changed sign but remained effectively near zero.

## 6. How the data were collected

Each round followed the same basic sequence. Earlier observations were reviewed, one new query vector was selected for each function, the vectors were checked for dimensionality, range and precision, and the queries were submitted through the official platform. The returned values were then stored in the weekly result file.

The dataset is therefore adaptive. Later points are not independent random samples because earlier results influence where the next query is placed.

## 7. Week 10 sampling choices

Week 10 used different treatments for different functions.

Function 5 repeated the exact Week 09 input to test whether the strongest known result could be reproduced. Functions 2, 3, 7 and 8 received local refinement. Functions 4 and 6 were moved to alternative local positions. Function 1 received broader exploration because its earlier outputs had remained effectively near zero.

## 8. Repeatability evidence

Function 5 used the same input in Weeks 09 and 10:

`0.120000,0.997000,0.999800,0.999800`

Both rounds returned:

`4394.868042481448`

This provides repeatability evidence for that exact tested point. It does not establish stability across the surrounding region and does not prove global optimality.

## 9. Data quality checks

The Week 10 record contains one input vector and one returned value for each of the eight functions. Dimensionality and range checks are included in the analysis script. Week 09 to Week 10 changes are calculated using exact decimal arithmetic.

No scaling, normalisation, imputation or transformation is applied to the source inputs or returned outputs. Derived summaries are written separately.

## 10. Derived fields

The repository also contains rankings, weekly changes, strategy classifications and figure data. These are analytical fields created from the stored observations.

They are not outputs returned by the competition platform and should be read as interpretations rather than ground truth about the hidden functions.

## 11. Sampling limitations

The dataset is small and adaptively sampled. Ten observations per function provide sparse coverage, especially for functions with five, six or eight dimensions. Productive regions receive more attention over time, so the dataset does not provide uniform coverage of the search space.

The eight functions also operate on different numerical scales. Raw values should therefore be compared mainly within each function across time rather than between functions.

## 12. Intended use

The dataset is suitable for analysing sequential black box optimisation, exploration and exploitation decisions, query history, repeatability and reproducibility within this capstone.

It is not suitable for claiming that the hidden mathematical functions have been recovered or that a global optimum has been proved.

## 13. Provenance and integrity

The authoritative Week 10 files are:

- `week_10_inputs.csv`
- `week_10_results.csv`

Supporting files include:

- `week_10_analysis_summary.csv`
- `week_10_figure_data_summary.csv`
- `week_10_analysis.py`
- `generate_week_10_figures.py`

The source CSV files are not overwritten during analysis.

## 14. Reproducibility

From the repository root:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

## 15. Week 10 summary

Week 10 added a useful mixture of positive, negative and repeat observations. Functions 2 and 3 improved. Function 5 reproduced its strongest known value exactly. Function 4 deteriorated substantially and Function 6 also declined, giving clear reasons to reassess those directions. Functions 7 and 8 remained positive but moved slightly lower. Function 1 remained unresolved.

The value of the round lies in both the objective values and the information gained about which search directions deserved to continue.

## References

Imperial College Business School. Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. *Gaussian Processes for Machine Learning*. MIT Press.

Frazier, P. I. *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.