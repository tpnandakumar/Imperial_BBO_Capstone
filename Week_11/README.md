# Week_11

## Bayesian Black Box Optimisation Portfolio

### Week 11 Analysis

## Documentation

- [Datasheet](DATASHEET.md)
- [Model Card](MODEL_CARD.md)
- [Validation Record](VALIDATION.md)
- [Evidence and Provenance](EVIDENCE_PROVENANCE.md)
- [Strategy Progression](STRATEGY_PROGRESSION.md)
- [Reproducibility Checklist](REPRODUCIBILITY_CHECKLIST.md)
- [PCA Strategy Comparison](PCA_STRATEGY_COMPARISON.md)
- [Week 12 Decision Record](WEEK_12_DECISION_RECORD.md)
- [Changelog](CHANGELOG.md)

The Week 11 input and result files remain the authoritative numerical record for this round.

## Contents

1. Introduction
2. Week 11 Results
3. Comparison with Week 10
4. Week 11 Query Strategy
5. Exploration and Exploitation
6. Week 12 Query Selection
7. Functional Progress
8. High Performing Regions
9. Decision Matrix
10. Information Gain and PCA
11. Computational Analysis
12. Repository Files and Reproducibility
13. Conclusion
14. Submission Status
15. References

## 1. Introduction

Week 11 tested the regional strategy developed in Week 10. The previous analysis had used clustering, distance to stronger historical points and local refinement to decide whether each function should be repeated, refined or moved back towards an earlier productive region.

The returned Week 11 values gave a clear outcome test. Every function improved relative to Week 10. Functions 2 and 5 reached new verified best values, Functions 1 and 8 reproduced earlier best values exactly, and Functions 3, 4 and 6 recovered after weaker recent rounds.

Module 23 then introduced principal component analysis as a way of examining structure in the accumulated query history. PCA was applied only after the Week 11 outputs were known. It was compared with direct objective evidence before the Week 12 submission was chosen.

## 2. Week 11 Results

| Function | Week 11 input | Week 11 output | Historical position |
| --- | --- | ---: | --- |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` | Prior best reproduced |
| Function 2 | `0.695000,0.950000` | `0.5848554940277205` | New verified best |
| Function 3 | `0.840000,0.160000,0.840000` | `-0.06542982421105416` | Close to strongest historical region |
| Function 4 | `0.620000,0.420000,0.440000,0.250000` | `-4.868852987697114` | Strong recovery |
| Function 5 | `0.110000,0.998000,0.999900,0.999900` | `4411.0387356061765` | New verified best |
| Function 6 | `0.720000,0.190000,0.700000,0.710000,0.150000` | `-0.7268715077444687` | Clear recovery |
| Function 7 | `0.045000,0.485000,0.255000,0.220000,0.420000,0.745000` | `1.3579108517237013` | Strong positive region retained |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` | Prior best reproduced |

## 3. Comparison with Week 10

| Function | Week 10 output | Week 11 output | Exact change |
| --- | ---: | ---: | ---: |
| Function 1 | `2.8950706668499033e-23` | `0.025559285339829783` | `0.02555928533982978299997104929` |
| Function 2 | `0.5311818841205426` | `0.5848554940277205` | `0.0536736099071779` |
| Function 3 | `-0.08697581687486715` | `-0.06542982421105416` | `0.02154599266381299` |
| Function 4 | `-13.483642655031158` | `-4.868852987697114` | `8.614789667334044` |
| Function 5 | `4394.868042481448` | `4411.0387356061765` | `16.1706931247285` |
| Function 6 | `-1.2283806967341901` | `-0.7268715077444687` | `0.5015091889897214` |
| Function 7 | `1.285160161342515` | `1.3579108517237013` | `0.0727506903811863` |
| Function 8 | `9.4646525` | `9.58024` | `0.1155875` |

The important point is not simply that all eight values improved. The queries were chosen for different reasons. Some repeated confirmed points, some tightened a local region, and others deliberately moved back towards stronger historical locations.

## 4. Week 11 Query Strategy

The Week 11 queries came from the Week 10 clustering analysis. Exact squared Euclidean distance was used to compare the selected Week 11 point with the strongest point observed before Week 11.

| Function | Week 11 action | Prior best week | Exact squared distance | Outcome |
| --- | --- | ---: | ---: | --- |
| Function 1 | Recover confirmed peak | 3 | `0` | Prior best reproduced |
| Function 2 | Local refinement | 6 | `0.000025` | New best |
| Function 3 | Recover stronger region | 4 | `0.0003` | Recovery supported |
| Function 4 | Recover stronger region | 1 | `0.0009` | Large recovery |
| Function 5 | Boundary refinement | 9 | `0.00010102` | New best |
| Function 6 | Recover stronger basin | 3 | `0.0031` | Recovery supported |
| Function 7 | Refine compact positive region | 5 | `0.000100` | Productive region retained |
| Function 8 | Recover confirmed best | 1 | `0` | Prior best reproduced |

Function 5 gave the clearest boundary result. The small move beyond the Week 9 and Week 10 plateau produced another improvement. Function 2 also benefited from a small local adjustment. For Functions 3, 4 and 6, moving back towards stronger historical areas was more productive than continuing the weaker recent direction.

## 5. Exploration and Exploitation

Week 11 was mainly a controlled regional test rather than broad exploration. Functions 1 and 8 tested repeatability. Function 5 exploited the strongest known boundary region. Function 2 refined a compact positive neighbourhood. Functions 3, 4 and 6 used recovery towards earlier stronger points, while Function 7 remained close to its productive region.

The results supported those choices, but they did not justify indefinite local tightening. Repeated best points give confidence about reproducibility, not about the shape of the surrounding surface. Likewise, a new local best does not prove that the region contains a global optimum.

## 6. Week 12 Query Selection

The Week 12 decision used three sources of evidence: the full Weeks 1 to 11 objective history, the Week 11 outcome analysis, and PCA of the accumulated query trajectories.

PCA was used as a comparison method rather than as an automatic replacement for the existing strategy. For Functions 3, 4, 5 and 8, more than 90 percent of the recorded query variance lay in the first principal component. Functions 6 and 7 required two components to reach the same threshold.

That concentration described how the search had moved. It did not prove that the principal directions were the directions of greatest objective improvement. The PCA results were therefore compared with actual performance before each Week 12 query was selected.

| Function | Strongest evidence | Week 12 treatment |
| --- | --- | --- |
| Function 1 | Exact repeated best | Retain confirmed point |
| Function 2 | New Week 11 best and favourable local direction | Small local refinement |
| Function 3 | Stronger historical point | Return to historical best |
| Function 4 | Large recovery towards stronger historical point | Return to historical best |
| Function 5 | PCA concentration and objective trend agree | Controlled boundary refinement |
| Function 6 | Two component structure and stronger historical point | Return to historical best |
| Function 7 | Two component structure and stronger historical point | Return to historical best |
| Function 8 | Exact repeated best | Retain confirmed point |

The exact reasoning is recorded in [PCA_STRATEGY_COMPARISON.md](PCA_STRATEGY_COMPARISON.md) and [WEEK_12_DECISION_RECORD.md](WEEK_12_DECISION_RECORD.md).

## 7. Functional Progress

Cross function ranking is retained only for continuity because the eight objectives operate on different numerical scales. Within function progress is more meaningful.

| Function | Week 11 status |
| --- | --- |
| Function 1 | Prior best reproduced |
| Function 2 | New verified best |
| Function 3 | Recovery close to prior best |
| Function 4 | Large recovery |
| Function 5 | New verified best |
| Function 6 | Clear recovery |
| Function 7 | Strong positive result |
| Function 8 | Prior best reproduced |

Week 11 was therefore favourable across all eight functions, but the type of progress differed substantially.

## 8. High Performing Regions

Function 5 remains the clearest high performing region. Its Week 11 point `0.110000,0.998000,0.999900,0.999900` returned `4411.0387356061765`, extending the improvement seen as the last three coordinates moved towards their upper boundaries.

Function 2 also reached a new best after a very small local movement. Functions 1 and 8 reproduced earlier best outputs at exactly the same coordinates, providing direct repeatability evidence. Functions 3, 4 and 6 improved after moving back towards stronger historical areas, while Function 7 remained within a compact positive region.

## 9. Decision Matrix

| Function | Main Week 11 evidence | Week 12 action |
| --- | --- | --- |
| Function 1 | Repeatability | Retain best |
| Function 2 | New local best | Refine |
| Function 3 | Historical recovery | Return to best |
| Function 4 | Historical recovery | Return to best |
| Function 5 | New boundary best | Refine boundary |
| Function 6 | Historical recovery | Return to best |
| Function 7 | Productive region | Return to best |
| Function 8 | Repeatability | Retain best |

The Week 12 submission therefore combines confirmation, refinement and historical recovery rather than applying one rule to every function.

## 10. Information Gain and PCA

Week 11 added more than higher objective values. Functions 1 and 8 tested repeatability. Function 5 showed that its boundary region could still improve after a plateau. Function 2 strengthened the evidence for a compact local region. Functions 3, 4 and 6 showed that a deliberate return towards earlier strong areas could reverse weaker recent results.

The PCA analysis added a different type of information by showing how concentrated the query trajectories had become.

| Function | PC1 explained variance | PC1 plus PC2 | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

Function 5 was the clearest case where the PCA structure and objective evidence pointed in the same direction. For the other higher dimensional functions, direct historical performance provided the stronger immediate target.

## 11. Computational Analysis

`week_11_analysis.py` validates the Week 11 inputs and outputs, compares them with Week 10, identifies the strongest earlier observations, calculates exact squared distances and performs centred PCA for Functions 3 to 8 using NumPy singular value decomposition.

`generate_week_11_figures.py` exports the figure data summary and creates six Week 11 figures. Source inputs and outputs remain exact strings or `Decimal` values. Floating point conversion is limited to plotting and PCA calculations.

## 12. Repository Files and Reproducibility

The Week 11 folder now contains the numerical record, executable analysis and a fuller assessment trail:

- `README.md`
- `DATASHEET.md`
- `MODEL_CARD.md`
- `VALIDATION.md`
- `EVIDENCE_PROVENANCE.md`
- `STRATEGY_PROGRESSION.md`
- `REPRODUCIBILITY_CHECKLIST.md`
- `PCA_STRATEGY_COMPARISON.md`
- `WEEK_12_DECISION_RECORD.md`
- `CHANGELOG.md`
- `week_11_inputs.csv`
- `week_11_results.csv`
- `week_11_analysis_summary.csv`
- `week_11_figure_data_summary.csv`
- `week_11_analysis.py`
- `generate_week_11_figures.py`

Run from the repository root:

```bash
python Week_11/week_11_analysis.py
python Week_11/generate_week_11_figures.py
```

The supporting documentation explains provenance, validation and limitations without changing the underlying competition record.

## 13. Conclusion

Week 11 was a strong outcome test of the Week 10 regional strategy. Every function improved relative to Week 10, two functions reached new verified best values, and two reproduced earlier best values exactly.

The next development was analytical rather than simply numerical. PCA was tested against the accumulated history, but the principal component structure was retained only where it added useful evidence. The Week 12 submission therefore came from method comparison rather than automatic use of the newest technique.

## 14. Submission Status

The Week 12 input set and verified outputs are preserved in `../Week_12/week_12_inputs.csv` and `../Week_12/week_12_results.csv`. The Week 12 results provide the outcome test for the strategy documented here and inform the final Round 13 decision.

The completed Component 23.1 reflection is recorded in `../Week_12/COMPONENT_23_1_CAPSTONE_REFLECTION.md`.

## 15. References

1. `Week_10/README.md`, Week 10 regional analysis and Week 11 strategy.
2. `Week_10/CLUSTERING_ANALYSIS.md`, clustering evidence used before the Week 11 submission.
3. `week_11_inputs.csv`, verified Week 11 inputs.
4. `week_11_results.csv`, verified Week 11 outputs.
5. `PCA_STRATEGY_COMPARISON.md`, PCA comparison used before the Week 12 submission.
6. `WEEK_12_DECISION_RECORD.md`, final Week 12 decision record.
7. `../Week_12/week_12_inputs.csv`, submitted Week 12 inputs.
8. Module 23 course material introducing principal component analysis.