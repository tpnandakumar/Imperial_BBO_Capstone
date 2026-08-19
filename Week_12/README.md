# Week_12

## Bayesian Black Box Optimisation Portfolio

### Week 12 Analysis

## Documentation

- [Pre Result Record](PRE_RESULT_RECORD.md)
- [Module 23 Reflection Preparation](MODULE_23_REFLECTION_PREPARATION.md)
- [Completed Component 23.1 Capstone Reflection](COMPONENT_23_1_CAPSTONE_REFLECTION.md)
- [PCA Evidence Record](PCA_EVIDENCE.md)
- [Validation Record](VALIDATION.md)
- [Verified Week 12 Inputs](week_12_inputs.csv)
- [Verified Week 12 Results](week_12_results.csv)
- [Week 12 Analysis Summary](week_12_analysis_summary.csv)
- [Week 12 Figure Data Summary](week_12_figure_data_summary.csv)

The Week 12 input and result files are the authoritative numerical record for this round. Derived calculations preserve those source values and use exact decimal arithmetic where the calculation permits it.

## Contents

1. Introduction
2. Week 12 Results
3. Comparison with Week 11
4. Week 12 Query Strategy Outcome
5. Exploration and Exploitation
6. PCA and Dimensional Structure
7. Functional Progress
8. High Performing Regions
9. Decision Matrix
10. Information Gain and Variance Structure
11. Computational Analysis
12. Repository Files and Reproducibility
13. Conclusion
14. Submission Status
15. References

## 1. Introduction

Week 12 tested the decisions made after the Week 11 outcome review and the principal component analysis of the accumulated query history. The eight functions were not treated as though they shared one landscape or one useful step size. Each query was assessed against its own historical evidence before the submitted point was fixed.

The returned outputs give a strong result for the round. No function declined relative to Week 11. Functions 2, 3 and 5 reached new verified best values. Functions 1, 4, 7 and 8 matched a previously verified best value exactly. Function 6 improved from Week 11 but remained below its strongest earlier result.

This distinction matters. The Week 12 evidence supports selective use of local refinement, historical recovery and boundary movement. It does not support a claim that one method is best for every function, and it does not establish the global optimum of any hidden objective.

## 2. Week 12 Results

| Function | Week 12 input | Week 12 output | Historical position |
| --- | --- | ---: | --- |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` | Matched prior verified best |
| Function 2 | `0.690000,0.950000` | `0.7335252043269003` | New verified best |
| Function 3 | `0.850000,0.150000,0.850000` | `-0.05985127532683556` | New verified best |
| Function 4 | `0.600000,0.430000,0.420000,0.250000` | `-4.359874926582439` | Matched prior verified best |
| Function 5 | `0.100000,0.999000,1.000000,1.000000` | `4427.343995806448` | New verified best |
| Function 6 | `0.700000,0.200000,0.700000,0.700000,0.200000` | `-0.7078316130911375` | Improved, but below prior verified best |
| Function 7 | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` | `1.3809299933612855` | Matched prior verified best |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` | Matched prior verified best |

The source files contain eight functions with the expected dimensions of 2, 2, 3, 4, 4, 5, 6 and 8. Every coordinate remains within the permitted interval from 0 to 1.

## 3. Comparison with Week 11

| Function | Week 11 output | Week 12 output | Exact change | Direction |
| --- | ---: | ---: | ---: | --- |
| Function 1 | `0.025559285339829783` | `0.025559285339829783` | `0` | Unchanged |
| Function 2 | `0.5848554940277205` | `0.7335252043269003` | `0.1486697102991798` | Improved |
| Function 3 | `-0.06542982421105416` | `-0.05985127532683556` | `0.00557854888421860` | Improved |
| Function 4 | `-4.868852987697114` | `-4.359874926582439` | `0.508978061114675` | Improved |
| Function 5 | `4411.0387356061765` | `4427.343995806448` | `16.3052602002715` | Improved |
| Function 6 | `-0.7268715077444687` | `-0.7078316130911375` | `0.0190398946533312` | Improved |
| Function 7 | `1.3579108517237013` | `1.3809299933612855` | `0.0230191416375842` | Improved |
| Function 8 | `9.58024` | `9.58024` | `0` | Unchanged |

The numerical changes should be interpreted within each function because the objective scales differ substantially. The useful portfolio level observation is that every Week 12 value was either higher than or equal to its Week 11 counterpart.

## 4. Week 12 Query Strategy Outcome

The submitted Week 12 coordinates can be classified directly from the verified history without reconstructing an unrecorded rationale.

| Function | Observed Week 12 action | Exact squared movement from Week 11 | Outcome |
| --- | --- | ---: | --- |
| Function 1 | Repeated the Week 11 coordinate | `0` | Prior best matched again |
| Function 2 | Small local move from Week 11 | `0.000025000000` | New verified best |
| Function 3 | Returned to the Week 4 coordinate | `0.000300000000` | New verified best |
| Function 4 | Returned to the Week 1 coordinate | `0.000900000000` | Prior best matched exactly |
| Function 5 | Continued a small boundary movement | `0.000101020000` | New verified best |
| Function 6 | Returned to the Week 3 coordinate | `0.003100000000` | Improved, but did not reproduce the earlier best |
| Function 7 | Returned to the Week 5 coordinate | `0.000100000000` | Prior best matched exactly |
| Function 8 | Repeated the Week 11 coordinate | `0` | Prior best matched again |

The contrast between Functions 4, 7 and 6 is informative. Reusing earlier coordinates reproduced the historical best exactly for Functions 4 and 7, whereas Function 6 returned a different value at its Week 3 coordinate. That observation should be retained when repeatability is considered in the final round.

## 5. Exploration and Exploitation

Week 12 was predominantly conservative. Functions 1 and 8 repeated established points. Functions 3, 4, 6 and 7 moved back to historically strong coordinates. Function 2 made a small local adjustment, while Function 5 made another small move towards the boundary.

This allocation reduced broad exploration while still allowing two kinds of information to be collected. First, the repeated historical coordinates tested whether earlier performance could be recovered. Second, the local moves for Functions 2 and 5 tested whether the productive direction remained useful.

The results support that balance for this round. Function 2 improved to `0.7335252043269003`, and Function 5 improved to `4427.343995806448`. At the same time, repeated points for Functions 1, 4, 7 and 8 retained their strongest verified values. Function 6 remains the main exception because its repeated historical coordinate did not recover the earlier output of `-0.648848297397347`.

## 6. PCA and Dimensional Structure

PCA was applied to Functions 3 to 8 because they have more than two input dimensions. The calculation centres the recorded query coordinates and applies singular value decomposition without additional scaling. The resulting components describe the geometry of the submitted query path only. They do not reveal the hidden objective function.

| Function | PC1 ratio, Weeks 1 to 11 | PC1 ratio, Weeks 1 to 12 | PC1 and PC2 cumulative, Weeks 1 to 12 | Components needed for at least 90 percent |
| --- | ---: | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9838996406737395` | `0.9969604487927284` | `1` |
| Function 4 | `0.929457542635097` | `0.9292557920986704` | `0.9989404400066912` | `1` |
| Function 5 | `0.9676115302998125` | `0.9636237264281431` | `0.9955573981146854` | `1` |
| Function 6 | `0.864773785020967` | `0.8646651132320834` | `0.9862926907251949` | `2` |
| Function 7 | `0.8602299516486513` | `0.852719368317185` | `0.9664631898138984` | `2` |
| Function 8 | `0.9021092653998608` | `0.9187898217824582` | `0.9728920432464374` | `1` |

The most concentrated recorded trajectories remain Functions 3, 4, 5 and 8, where one component accounts for at least 90 percent of the observed coordinate variance. Functions 6 and 7 require two components to reach the same threshold. This difference is useful for describing how the search has moved, but it is not a reason by itself to choose a Week 13 coordinate.

## 7. Functional Progress

Function 1 has now reproduced `0.025559285339829783` at the same coordinate in Weeks 3, 11 and 12. Function 2 reached a new best after changing only its first coordinate from `0.695000` to `0.690000` while retaining `0.950000` in the second coordinate.

Function 3 returned to `0.850000,0.150000,0.850000`, the coordinate used in Week 4, and improved slightly beyond the earlier Week 4 value of `-0.06037987403160633`. Function 4 returned to its Week 1 coordinate and reproduced `-4.359874926582439` exactly.

Function 5 extended the established boundary pattern to `0.100000,0.999000,1.000000,1.000000` and reached `4427.343995806448`. Function 6 returned to its Week 3 coordinate but reached `-0.7078316130911375`, below the earlier Week 3 value of `-0.648848297397347`.

Function 7 returned to its Week 5 coordinate and reproduced `1.3809299933612855` exactly. Function 8 again returned `9.58024` at the same coordinate used in Weeks 1, 11 and 12.

## 8. High Performing Regions

The strongest verified Function 5 point is now `0.100000,0.999000,1.000000,1.000000`, with output `4427.343995806448`. The result extends the sequence of high values observed while the second, third and fourth coordinates moved towards their upper bounds and the first coordinate moved lower.

Function 2 has a new strongest observed point at `0.690000,0.950000`, with output `0.7335252043269003`. Function 3 has a new strongest observed output of `-0.05985127532683556` at `0.850000,0.150000,0.850000`.

Functions 1, 4, 7 and 8 have repeatable best coordinates within the recorded history. Function 6 has a historically strong coordinate, but the Week 12 return to that point did not reproduce its earlier value. The distinction between a repeatable coordinate and a merely strong historical observation should therefore remain explicit.

## 9. Decision Matrix

The Week 12 evidence narrows the questions that remain before the final round, but it does not fix any Week 13 coordinate.

| Function | Week 12 evidence | Remaining question before Week 13 |
| --- | --- | --- |
| Function 1 | Best value repeated again | Whether another repeat adds enough information to justify the query |
| Function 2 | New best after a small local move | Whether the local direction still has defensible room for refinement |
| Function 3 | New best at a historical coordinate | Whether confirmation or a nearby test is more informative |
| Function 4 | Historical best reproduced exactly | Whether to preserve the point or use the final query for local information |
| Function 5 | New best at the boundary | Whether any further movement is possible or useful without unsupported extrapolation |
| Function 6 | Improved, but historical best was not reproduced | Whether the variation reflects local sensitivity or another source of uncertainty |
| Function 7 | Historical best reproduced exactly | Whether confirmation is preferable to a small local probe |
| Function 8 | Best value repeated again | Whether another repeat has sufficient information value |

This matrix is deliberately evidence based. It records what the Week 12 results leave unresolved without inventing the final submission.

## 10. Information Gain and Variance Structure

Week 12 provided both performance evidence and repeatability evidence. Functions 2, 3 and 5 supplied new best values. Functions 1, 4, 7 and 8 showed that selected best coordinates could reproduce earlier values exactly. Function 6 showed the opposite pattern and therefore contributes useful uncertainty information even though it did not recover its historical best.

The PCA update adds a second layer. The Week 12 observation increased the PC1 explained variance ratio for Functions 3 and 8 and reduced it slightly for Functions 4, 5, 6 and 7. These changes are descriptive of the recorded search path. They should be considered alongside objective performance rather than treated as an optimisation rule.

The combination of objective change, exact query movement, previous best status and PCA structure is therefore more informative than any one measure on its own.

## 11. Computational Analysis

`week_12_analysis.py` validates the authoritative Week 12 source files, checks function coverage, dimensions, coordinate bounds and exact stored strings, then compares Week 12 with the complete verified history held in the Week 11 analysis record.

Exact objective changes and squared query movements use `Decimal`. Floating point conversion is limited to PCA because singular value decomposition requires numerical arrays. The PCA calculation is centred, is not additionally scaled and is restricted to Functions 3 to 8.

The script writes `week_12_analysis_summary.csv` and `week_12_figure_data_summary.csv`. `generate_week_12_figures.py` reads those derived records and can create five analytical figures directly in the Week 12 folder. No separate figures directory is created.

## 12. Repository Files and Reproducibility

The core Week 12 files are:

- `README.md`
- `week_12_inputs.csv`
- `week_12_results.csv`
- `week_12_analysis_summary.csv`
- `week_12_figure_data_summary.csv`
- `week_12_analysis.py`
- `generate_week_12_figures.py`

The input and result CSV files were already present and verified, so their source values are not rewritten. The derived summaries can be reproduced by running `python week_12_analysis.py`, followed by `python generate_week_12_figures.py` if the figures are required.

Supporting Week 12 documents remain in the same flat folder. No additional figure subdirectory is required.

## 13. Conclusion

Week 12 strengthened the portfolio without a decline in any function relative to Week 11. Three functions reached new verified best values, four matched a prior verified best, and Function 6 improved while remaining below its earlier best.

The round also sharpened the interpretation of repeated coordinates. Exact recovery was seen for several functions, but not for Function 6. PCA helped describe how concentrated the accumulated query paths had become, while the objective results remained the primary evidence for performance.

The next decision should therefore begin from the full twelve round history rather than from the latest point alone.

## 14. Submission Status

Week 12 is complete. The submitted inputs and returned outputs are both available and verified. The Week 12 analytical record can therefore be treated as final for this round.

No Week 13 input set is authorised by this folder. The final submission should only be fixed after the next course strategy has been reviewed, candidate points have been compared against the complete history and the exact dimensions, bounds and six decimal submission format have been checked.

## 15. References

1. `Week_12/week_12_inputs.csv`, verified Week 12 submitted inputs.
2. `Week_12/week_12_results.csv`, verified Week 12 returned outputs.
3. `Week_11/week_11_analysis.py`, verified Weeks 1 to 11 input and output history used for longitudinal comparison.
4. `Week_12/PCA_EVIDENCE.md`, supporting record for the PCA comparison.
5. `Week_12/VALIDATION.md`, source validation and interpretation limits.
