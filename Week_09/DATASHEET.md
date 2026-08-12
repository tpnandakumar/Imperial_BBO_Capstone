# Datasheet for the Bayesian Black Box Optimisation Capstone Dataset

**Author:** Dr N T Pisharam  
**Capstone week:** 09  
**Optimisation round:** 9  
**Document status:** Week 09 datasheet

## 1. Purpose

This datasheet records the dataset available at the end of Week 09. It covers eight hidden objective functions, the submitted query vectors, the returned objective values and the comparisons used to interpret the round.

By the end of Week 09, each function had nine recorded observations. Across all eight functions, the cumulative dataset contained seventy two submitted query vectors and seventy two returned objective values.

The source observations remain authoritative. Rankings, strategy labels and written interpretations are derived from those observations.

## 2. Dataset structure

| Function | Dimensions | Observations by Week 09 |
|---|---:|---:|
| Function 1 | 2 | 9 |
| Function 2 | 2 | 9 |
| Function 3 | 3 | 9 |
| Function 4 | 4 | 9 |
| Function 5 | 4 | 9 |
| Function 6 | 5 | 9 |
| Function 7 | 6 | 9 |
| Function 8 | 8 | 9 |

Every coordinate lies between 0 and 1 and is submitted to six decimal places. The hidden meaning of each coordinate is not disclosed, so features are positional rather than semantically labelled.

## 3. Exact Week 09 inputs

| Function | Input |
|---|---|
| Function 1 | `0.350000,0.700000` |
| Function 2 | `0.725000,0.945000` |
| Function 3 | `0.255000,0.855000,0.295000` |
| Function 4 | `0.310000,0.710000,0.670000,0.230000` |
| Function 5 | `0.120000,0.997000,0.999800,0.999800` |
| Function 6 | `0.240000,0.760000,0.240000,0.820000,0.280000` |
| Function 7 | `0.058000,0.495000,0.248000,0.218000,0.425000,0.742000` |
| Function 8 | `0.050000,0.050000,0.050000,0.050000,0.468000,0.872000,0.572000,0.982000` |

These values are taken directly from `week_09_inputs.csv`.

## 4. Exact Week 09 outputs

| Function | Output |
|---|---:|
| Function 1 | `-1.4546199699251391e-58` |
| Function 2 | `0.47297842839949866` |
| Function 3 | `-0.1156707106126581` |
| Function 4 | `-11.788939969158545` |
| Function 5 | `4394.868042481448` |
| Function 6 | `-1.1733030029888645` |
| Function 7 | `1.314307996450604` |
| Function 8 | `9.4709436` |

These values are taken directly from `week_09_results.csv`.

## 5. Week 08 to Week 09 comparison

| Function | Week 08 output | Week 09 output | Change |
|---|---:|---:|---:|
| Function 1 | `-1.4546199699251391e-58` | `-1.4546199699251391e-58` | `0` |
| Function 2 | `0.5672775862793291` | `0.47297842839949866` | `-0.09429915787983044` |
| Function 3 | `-0.0991107637427902` | `-0.1156707106126581` | `-0.0165599468698679` |
| Function 4 | `-12.305008897187289` | `-11.788939969158545` | `0.516068928028744` |
| Function 5 | `4359.384134322703` | `4394.868042481448` | `35.483908158745` |
| Function 6 | `-1.1197178425911847` | `-1.1733030029888645` | `-0.0535851603976798` |
| Function 7 | `1.3346391663186332` | `1.314307996450604` | `-0.0203311698680292` |
| Function 8 | `9.47621` | `9.4709436` | `-0.0052664` |

Function 5 improved again and Function 4 moved in a favourable direction. Functions 2, 3, 6, 7 and 8 declined, while Function 1 remained unchanged at an effectively zero value.

## 6. How the data were collected

Each round used the same basic collection process. Earlier observations were reviewed, one query vector was selected for each function, the vectors were checked for dimensionality, range and precision, and the queries were submitted through the official platform. Returned values were then stored in the weekly result file.

The dataset is adaptive rather than randomly sampled. Later observations depend on the results of earlier rounds.

## 7. Week 09 sampling choices

Week 09 continued local exploitation for Function 5 because it had shown the strongest sustained improvement. Function 4 also received further refinement after earlier movement suggested a more favourable region.

Function 1 remained an exploration target because its values were effectively zero. Functions 2, 3, 6, 7 and 8 were handled more cautiously because their recent histories contained either declines or only modest local changes.

## 8. Data quality checks

The Week 09 record contains one input vector and one returned value for each function. Dimensionality and range checks are included in the analysis workflow. The source inputs and outputs are retained without scaling, normalisation, imputation or transformation.

Derived summaries are stored separately from the raw weekly record.

## 9. Derived fields

The repository also records weekly changes, rankings, strategy classifications and figure data. These fields are created from the source observations to support interpretation.

They are not values returned by the competition platform and should not be treated as ground truth descriptions of the hidden functions.

## 10. Sampling limitations

Nine observations per function remain sparse, particularly for the higher dimensional objectives. As productive regions receive more attention, the search becomes increasingly concentrated and does not provide uniform coverage of the full space.

The eight functions also operate on different numerical scales. Raw values are therefore most meaningful when compared within the same function over time.

## 11. Intended use

The dataset is suitable for analysing sequential black box optimisation, query history, exploration and exploitation choices, local refinement and reproducibility within this capstone.

It is not suitable for claiming that the hidden functions have been recovered or that a global optimum has been proved.

## 12. Provenance and integrity

The authoritative Week 09 files are:

- `week_09_inputs.csv`
- `week_09_results.csv`

Supporting files include:

- `week_09_analysis_summary.csv`
- `week_09_figure_data_summary.csv`
- `week_09_analysis.py`
- `generate_week_09_figures.py`

The source CSV files remain separate from derived summaries and figures.

## 13. Reproducibility

The stored inputs, outputs and analysis code provide the material needed to reconstruct the Week 09 comparisons and figures from the repository.

## 14. Week 09 summary

Week 09 strengthened the evidence for continued exploitation of Function 5 and showed a further favourable move in Function 4. It also showed that several other local movements were not improving at the same rate. Function 2 remained positive but declined, Functions 3 and 6 deteriorated, Functions 7 and 8 remained positive with small reductions, and Function 1 remained unresolved.

Those mixed results were important because they set up Week 10 as a more selective round rather than a simple continuation of the same search pattern.

## References

Imperial College Business School. Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. *Gaussian Processes for Machine Learning*. MIT Press.

Frazier, P. I. *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.