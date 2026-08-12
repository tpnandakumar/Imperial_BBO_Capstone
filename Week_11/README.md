# Week_11

## Bayesian Black Box Optimisation Portfolio

### Week 11 Analysis

## Contents

1. Introduction
2. Week 11 Results
3. Comparison of Week 10 and Week 11 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Reflection on Week 12 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Automation Decision
15. References

## 1. Introduction

Week 11 is the outcome stage of the clustering work completed in Week 10. The Week 10 clustering lens, distance cues, recurring regions and boundary tightening were used to choose the eleventh round of queries. This folder therefore tests those decisions rather than presenting clustering as a new Week 11 method.

Every objective improved relative to Week 10. Functions 2 and 5 produced new verified best outputs, while Functions 1 and 8 exactly matched earlier verified best values. The Week 11 results give useful evidence about whether the regions identified in Week 10 were worth revisiting or refining.

This analysis also adds a limited principal component analysis as preparation for the next course topic. PCA was not used to choose the Week 11 queries. It is included only as a head start for Week 12, using the complete Weeks 1 to 11 query history to describe the geometry of the higher dimensional search paths.

## 2. Week 11 Results

| Function | Week 11 input | Week 11 output | Historical position |
| --- | --- | ---: | --- |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` | Matched prior verified best |
| Function 2 | `0.695000,0.950000` | `0.5848554940277205` | New verified best |
| Function 3 | `0.840000,0.160000,0.840000` | `-0.06542982421105416` | Close to the strongest historical region |
| Function 4 | `0.620000,0.420000,0.440000,0.250000` | `-4.868852987697114` | Strong recovery |
| Function 5 | `0.110000,0.998000,0.999900,0.999900` | `4411.0387356061765` | New verified best |
| Function 6 | `0.720000,0.190000,0.700000,0.710000,0.150000` | `-0.7268715077444687` | Clear recovery |
| Function 7 | `0.045000,0.485000,0.255000,0.220000,0.420000,0.745000` | `1.3579108517237013` | Productive positive region retained |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` | Matched prior verified best |

The figure script generates six PNG files directly in `Week_11`. No separate figures folder is created.

## 3. Comparison of Week 10 and Week 11 Performance

| Function | Week 10 output | Week 11 output | Exact change | Direction |
| --- | ---: | ---: | ---: | --- |
| Function 1 | `2.8950706668499033e-23` | `0.025559285339829783` | `0.02555928533982978299997104929` | Improved |
| Function 2 | `0.5311818841205426` | `0.5848554940277205` | `0.0536736099071779` | Improved |
| Function 3 | `-0.08697581687486715` | `-0.06542982421105416` | `0.02154599266381299` | Improved |
| Function 4 | `-13.483642655031158` | `-4.868852987697114` | `8.614789667334044` | Improved |
| Function 5 | `4394.868042481448` | `4411.0387356061765` | `16.1706931247285` | Improved |
| Function 6 | `-1.2283806967341901` | `-0.7268715077444687` | `0.5015091889897214` | Improved |
| Function 7 | `1.285160161342515` | `1.3579108517237013` | `0.0727506903811863` | Improved |
| Function 8 | `9.4646525` | `9.58024` | `0.1155875` | Improved |

The improvement across all eight functions is important because the Week 11 actions were not uniform. Some queries repeated confirmed points, some refined compact neighbourhoods, and others moved back towards stronger historical regions after deterioration.

## 4. Query Selection Strategy

The Week 11 queries were selected in Week 10 through the clustering analysis recorded in `Week_10/README.md` and `Week_10/CLUSTERING_ANALYSIS.md`. Week 11 now provides the outcome test.

The table uses exact squared Euclidean distance between the Week 11 input and the strongest input observed before Week 11. Squared distance keeps the decimal calculation exact without introducing an irrational square root.

| Function | Week 10 clustering informed action | Prior best week | Prior best output | Exact squared distance | Week 11 outcome |
| --- | --- | ---: | ---: | ---: | --- |
| Function 1 | Recover confirmed narrow peak | 3 | `0.025559285339829783` | `0` | Prior best reproduced |
| Function 2 | Local cluster refinement | 6 | `0.5712475315739602` | `0.000025` | New verified best |
| Function 3 | Recovery towards stronger historical region | 4 | `-0.06037987403160633` | `0.0003` | Recovery supported |
| Function 4 | Recovery towards stronger historical region | 1 | `-4.359874926582439` | `0.0009` | Large recovery |
| Function 5 | Boundary cluster refinement | 9 | `4394.868042481448` | `0.00010102` | New verified best |
| Function 6 | Recovery towards stronger historical basin | 3 | `-0.648848297397347` | `0.0031` | Recovery supported |
| Function 7 | Compact positive cluster refinement | 5 | `1.3809299933612855` | `0.000100` | Positive region retained |
| Function 8 | Recover confirmed historical best | 1 | `9.58024` | `0` | Prior best reproduced |

Function 5 gives the clearest boundary result. A small movement beyond the Week 9 and Week 10 plateau produced a new best. Function 2 also strengthened a compact positive region. Functions 3, 4, 6 and 7 show that returning towards stronger historical neighbourhoods was more productive than continuing weaker recent directions.

## 5. Exploration vs Exploitation Analysis

Week 11 was mainly a controlled regional test rather than broad exploration. Functions 1 and 8 tested repeatability. Function 5 refined the strongest boundary region. Function 2 stayed within a tight positive neighbourhood. Functions 3, 4 and 6 used evidence led recovery, while Function 7 remained close to its productive positive region.

The result supports the Week 10 clustering decisions, but it does not justify indefinite local tightening. Function 5 is already close to several boundaries. Function 2 has a new best but the width of the productive region is not known. Repeating Functions 1 and 8 again would preserve known performance but add little information.

## 6. Reflection on Week 12 Query Selection

No Week 12 input set is authorised here. The next decision should use the full history, the Week 11 outcome analysis and the formal PCA module before exact coordinates are locked.

The PCA work in this folder is deliberately preparatory. It can identify concentrated directions in the recorded query paths, especially for the higher dimensional functions, but it cannot determine an optimum or replace the observed outputs. Once the PCA module is completed, this preliminary implementation should be reviewed against the course treatment before candidate Week 12 queries are compared.

## 7. Functional Ranking Evolution

The Week 11 cross function ranking is retained for continuity, although the objectives operate on different scales and should not be compared as if they shared one common response range.

| Rank | Function | Week 11 output | Historical best status |
| ---: | --- | ---: | --- |
| 1 | Function 5 | `4411.0387356061765` | New verified best |
| 2 | Function 8 | `9.58024` | Matched prior verified best |
| 3 | Function 7 | `1.3579108517237013` | Below prior verified best |
| 4 | Function 2 | `0.5848554940277205` | New verified best |
| 5 | Function 1 | `0.025559285339829783` | Matched prior verified best |
| 6 | Function 3 | `-0.06542982421105416` | Below prior verified best |
| 7 | Function 6 | `-0.7268715077444687` | Below prior verified best |
| 8 | Function 4 | `-4.868852987697114` | Below prior verified best |

Within function progress is more informative. On that basis, Week 11 was uniformly favourable.

## 8. High Performing Region Identification

Function 5 remains the clearest high performing region. Its Week 11 point `0.110000,0.998000,0.999900,0.999900` produced `4411.0387356061765`, extending the sequence of stronger outputs as the last three coordinates approached their upper boundaries.

Function 2 produced a new best after a very small movement from its previous strongest point. Functions 1 and 8 reproduced earlier best outputs at exactly the same coordinates, supporting repeatability but not yet defining the surrounding surfaces.

Functions 3, 4 and 6 improved after moving towards stronger historical areas, while Function 7 returned its second strongest recorded value within a compact positive region. These observations are useful for candidate generation, but they are not evidence that any of those locations is a global optimum.

## 9. Decision Matrix and Resource Allocation

| Function | Main Week 11 evidence | Main uncertainty before Week 12 | Priority |
| --- | --- | --- | --- |
| Function 1 | Prior best reproduced | Shape around the narrow positive point | Medium |
| Function 2 | New best | Width and direction of the productive neighbourhood | High |
| Function 3 | Recovery close to prior best | Whether further recovery remains worthwhile | Medium |
| Function 4 | Large recovery | Whether the earlier strong region can be approached more closely | High |
| Function 5 | New boundary best | Further gain versus over concentration risk | High |
| Function 6 | Clear recovery | Whether the stronger historical basin can be regained | Medium |
| Function 7 | Strong positive result | Whether refinement is reaching diminishing returns | Medium |
| Function 8 | Prior best reproduced | Information value of leaving a repeatable best point | Medium |

These priorities guide preparation only. They are not Week 12 submissions.

## 10. Information Gain Analysis

Week 11 added both performance and structural information. Functions 1 and 8 confirmed repeatability. Function 5 showed that its boundary region could still improve after a plateau. Function 2 strengthened evidence for a compact positive neighbourhood. Functions 3, 4 and 6 showed that recovery towards earlier strong regions could reverse recent declines.

### Exploratory PCA head start

PCA is applied only to Functions 3 to 8. Functions 1 and 2 remain in direct two dimensional geometry. The calculation uses centred input coordinates without additional scaling. All BBO coordinates share the same nominal `[0,1]` range, so this first pass retains the actual movement magnitude recorded in the search history.

| Function | PC1 explained variance ratio | PC1 plus PC2 cumulative ratio | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

The recorded query paths are therefore concentrated in one or two principal directions. This is not evidence that the hidden objective surfaces have the same dimensionality. The points were deliberately generated by a structured search, so concentration is expected. The useful question for next week is whether the principal directions help explain how the coordinates have been moving together and whether that should influence the candidate review.

## 11. Computational Analysis and Coding Implementation

`week_11_analysis.py` validates the Week 11 inputs and outputs, checks them against the verified history, calculates exact Week 10 to Week 11 changes, identifies the strongest pre Week 11 observations, and calculates exact squared distances to those inputs. It then performs centred PCA for Functions 3 to 8 using NumPy singular value decomposition.

`generate_week_11_figures.py` exports `week_11_figure_data_summary.csv` and creates six figures in the Week 11 folder. The first four figures examine the outcome history and proximity to prior best regions. The final two summarise the exploratory PCA variance concentration.

Source inputs and outputs remain exact strings or `Decimal` values. Floating point conversion is limited to plotting and PCA, where it is required by the numerical routines.

## 12. Repository Files and Reproducibility

The flat Week 11 structure contains:

- `README.md`
- `week_11_inputs.csv`
- `week_11_results.csv`
- `week_11_analysis_summary.csv`
- `week_11_figure_data_summary.csv`
- `week_11_analysis.py`
- `generate_week_11_figures.py`

Run:

```bash
python Week_11/week_11_analysis.py
python Week_11/generate_week_11_figures.py
```

The analysis script should be run first because the figure script reads its summary file.

## 13. Conclusion

Week 11 provides a strong outcome test of the clustering work completed in Week 10. All eight functions improved relative to Week 10. Functions 2 and 5 reached new verified best outputs, while Functions 1 and 8 reproduced earlier best values exactly.

The PCA work adds a useful head start for the next module without changing the chronology. It describes the search trajectories already observed and will be reviewed again before Week 12 candidate queries are locked.

## 14. Automation Decision

No automatic Week 12 submission is authorised. The scripts may validate data, calculate distances, perform exploratory PCA and prepare figures, but they must not promote a Week 12 input set as final.

Final Week 12 coordinates require manual review after the PCA module, full function by function comparison, bounds checking, dimensional validation and confirmation of six decimal submission formatting.

## 15. References

1. `Week_10/README.md`, Stage 2 Component 22.1: Clustering Lens and Week 11 Strategy Refinement.
2. `Week_10/CLUSTERING_ANALYSIS.md`, clustering evidence used before the eleventh query round.
3. `Week_11/week_11_inputs.csv`, verified Week 11 inputs.
4. `Week_11/week_11_results.csv`, verified Week 11 outputs.
5. Verified Weeks 1 to 11 input and output histories supplied with the Week 11 submission record.
6. Course sequence supplied for this stage: clustering techniques followed by principal component analysis.
