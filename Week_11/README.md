# Week_11

## Bayesian Black Box Optimisation Portfolio

### Week 11 Analysis

## Documentation

- [PCA Strategy Comparison](PCA_STRATEGY_COMPARISON.md)
- [Week 12 Decision Record](WEEK_12_DECISION_RECORD.md)

The Week 11 inputs and returned outputs remain the authoritative numerical record for this round.

## Contents

1. Introduction
2. Week 11 Results
3. Comparison of Week 10 and Week 11 Performance
4. Query Selection Strategy
5. Exploration vs Exploitation Analysis
6. Week 12 Query Selection
7. Functional Ranking Evolution
8. High Performing Region Identification
9. Decision Matrix and Resource Allocation
10. Information Gain Analysis
11. Computational Analysis and Coding Implementation
12. Repository Files and Reproducibility
13. Conclusion
14. Submission Decision
15. References

## 1. Introduction

Week 11 tested the clustering work completed in Week 10. Distance cues, recurring regions and boundary tightening had been used to choose the eleventh round of queries, so the returned values provided a direct test of those decisions.

Every objective improved relative to Week 10. Functions 2 and 5 produced new verified best outputs, while Functions 1 and 8 exactly matched earlier verified best values. Functions 3, 4 and 6 recovered after weaker recent rounds, and Function 7 returned to a strong positive region.

Module 23 then introduced principal component analysis as a way of examining structure in the accumulated query history. PCA was not used to choose the Week 11 queries. It was applied after the Week 11 results were known and compared with the full objective history before the Week 12 submission was selected.

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

The result supports the Week 10 clustering decisions, but it does not justify indefinite local tightening. Function 5 is already close to several boundaries. Function 2 has a new best but the width of the productive region is not known. Functions 1 and 8 provide repeatability evidence at their known best points.

## 6. Week 12 Query Selection

The Week 12 decision used three layers of evidence: the complete Weeks 1 to 11 objective history, the Week 11 outcome analysis, and the PCA structure introduced in Module 23. PCA was treated as a comparison method rather than a replacement for the existing strategy.

For Functions 3, 4, 5 and 8, more than 90 percent of the recorded query variance lay in the first principal component. Functions 6 and 7 required two components to reach the same threshold. That concentration showed that the historical query paths had become structurally narrow, but it did not establish that the principal directions were the directions of greatest objective improvement.

The principal component results were therefore compared with direct performance evidence. This led to different choices across the eight functions:

| Function | Strongest evidence used | Week 12 decision |
| --- | --- | --- |
| Function 1 | Exact repeat of the prior best | Retain confirmed best point |
| Function 2 | New Week 11 best and favourable local direction | Small local refinement |
| Function 3 | Stronger verified historical point | Return to historical best |
| Function 4 | Large recovery towards stronger historical region | Return to historical best |
| Function 5 | PCA concentration and objective trend agree | Further controlled boundary refinement |
| Function 6 | Two component structure and stronger historical point | Return to historical best |
| Function 7 | Two component structure and stronger historical point | Return to historical best |
| Function 8 | Exact repeat of the prior best | Retain confirmed best point |

The submitted Week 12 queries were:

```text
Function 1
0.600000-0.600000

Function 2
0.690000-0.950000

Function 3
0.850000-0.150000-0.850000

Function 4
0.600000-0.430000-0.420000-0.250000

Function 5
0.100000-0.999000-1.000000-1.000000

Function 6
0.700000-0.200000-0.700000-0.700000-0.200000

Function 7
0.040000-0.480000-0.260000-0.220000-0.420000-0.740000

Function 8
0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000
```

The full function by function reasoning is recorded in [PCA_STRATEGY_COMPARISON.md](PCA_STRATEGY_COMPARISON.md) and [WEEK_12_DECISION_RECORD.md](WEEK_12_DECISION_RECORD.md).

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

Functions 3, 4 and 6 improved after moving towards stronger historical areas, while Function 7 returned its second strongest recorded value within a compact positive region. These observations informed the Week 12 candidate review without being treated as proof of a global optimum.

## 9. Decision Matrix and Resource Allocation

| Function | Main Week 11 evidence | Week 12 treatment |
| --- | --- | --- |
| Function 1 | Prior best reproduced | Confirmed best retained |
| Function 2 | New best | Small local refinement |
| Function 3 | Recovery close to prior best | Historical best selected |
| Function 4 | Large recovery | Historical best selected |
| Function 5 | New boundary best | Boundary refinement continued |
| Function 6 | Clear recovery | Historical best selected |
| Function 7 | Strong positive result | Historical best selected |
| Function 8 | Prior best reproduced | Confirmed best retained |

The Week 12 allocation therefore combines confirmation, local refinement, historical recovery and one PCA consistent boundary move rather than applying a single rule across all functions.

## 10. Information Gain Analysis

Week 11 added both performance and structural information. Functions 1 and 8 confirmed repeatability. Function 5 showed that its boundary region could still improve after a plateau. Function 2 strengthened evidence for a compact positive neighbourhood. Functions 3, 4 and 6 showed that recovery towards earlier strong regions could reverse recent declines.

### PCA comparison

PCA was applied to Functions 3 to 8. Functions 1 and 2 remained in direct two dimensional geometry. The calculation used centred input coordinates without additional scaling because all BBO coordinates share the same nominal `[0,1]` range.

| Function | PC1 explained variance ratio | PC1 plus PC2 cumulative ratio | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

The result shows that the submitted query paths were concentrated in one or two principal directions. The objective history was then used to decide whether those directions should influence the next submission. Function 5 showed the strongest agreement between structural concentration and objective improvement. For the remaining higher dimensional functions, verified historical performance provided the stronger immediate target.

## 11. Computational Analysis and Coding Implementation

`week_11_analysis.py` validates the Week 11 inputs and outputs, checks them against the verified history, calculates exact Week 10 to Week 11 changes, identifies the strongest pre Week 11 observations, and calculates exact squared distances to those inputs. It then performs centred PCA for Functions 3 to 8 using NumPy singular value decomposition.

`generate_week_11_figures.py` exports `week_11_figure_data_summary.csv` and creates six figures in the Week 11 folder. The first four figures examine the outcome history and proximity to prior best regions. The final two summarise the PCA variance concentration.

Source inputs and outputs remain exact strings or `Decimal` values. Floating point conversion is limited to plotting and PCA, where it is required by the numerical routines.

## 12. Repository Files and Reproducibility

The flat Week 11 structure contains:

- `README.md`
- `PCA_STRATEGY_COMPARISON.md`
- `WEEK_12_DECISION_RECORD.md`
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

Week 11 provided a strong outcome test of the clustering work completed in Week 10. All eight functions improved relative to Week 10. Functions 2 and 5 reached new verified best outputs, while Functions 1 and 8 reproduced earlier best values exactly.

Module 23 then provided a useful structural test through PCA. The principal component results were compared with the objective history rather than used as an automatic optimisation rule. This comparison led to a mixed Week 12 strategy in which direct historical evidence remained dominant for most functions, while Function 5 supported a further PCA consistent boundary refinement and Function 2 supported a small local move from its new best.

## 14. Submission Decision

The Week 12 input set has now been submitted. The Week 11 repository therefore records the complete decision trail from Week 11 inputs and outputs through PCA comparison to the final Week 12 coordinates.

Week 12 returned outputs are not yet part of this record. They will be added when they are received and verified, at which point the next weekly analysis can test whether the selected strategies were supported by the new evidence.

## 15. References

1. `Week_10/README.md`, clustering analysis and Week 11 strategy refinement.
2. `Week_10/CLUSTERING_ANALYSIS.md`, clustering evidence used before the eleventh query round.
3. `Week_11/week_11_inputs.csv`, verified Week 11 inputs.
4. `Week_11/week_11_results.csv`, verified Week 11 outputs.
5. `Week_11/PCA_STRATEGY_COMPARISON.md`, PCA comparison used before the Week 12 submission.
6. `Week_11/WEEK_12_DECISION_RECORD.md`, final Week 12 decision record.
7. Verified Weeks 1 to 11 input and output histories used in the Week 11 analysis.
8. Module 23 course material introducing principal component analysis for the next optimisation stage.
