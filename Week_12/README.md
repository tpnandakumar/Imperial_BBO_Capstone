# Week 12

## Bayesian Black Box Optimisation Portfolio

### Verified Round 12 Outcome

## Documentation

- [Pre Result Record](PRE_RESULT_RECORD.md)
- [Module 23 Reflection Preparation](MODULE_23_REFLECTION_PREPARATION.md)
- [Completed Component 23.1 Capstone Reflection](COMPONENT_23_1_CAPSTONE_REFLECTION.md)
- [Verified Week 12 Results](week_12_results.csv)
- [Week 12 Analysis Summary](week_12_analysis_summary.csv)

The submitted inputs and returned outputs are the authoritative numerical record for this round.

## 1. Introduction

Week 12 tested the strategy selected after the Week 11 analysis and Module 23 PCA review. The submission did not use one method across all eight functions. Instead, direct historical performance, repeatability, local refinement and principal component structure were compared before each query was chosen.

The returned results provide a strong test of that approach. No function deteriorated relative to Week 11. Functions 2, 3 and 5 reached new verified best values. Functions 4 and 7 recovered their historical best values exactly. Functions 1 and 8 repeated their verified best values, while Function 6 improved but remained below its earlier best.

## 2. Week 12 Results

| Function | Week 12 input | Week 12 output | Outcome |
| --- | --- | ---: | --- |
| Function 1 | `0.600000,0.600000` | `0.025559285339829783` | Exact repeat of verified best |
| Function 2 | `0.690000,0.950000` | `0.7335252043269003` | New verified best |
| Function 3 | `0.850000,0.150000,0.850000` | `-0.05985127532683556` | New verified best |
| Function 4 | `0.600000,0.430000,0.420000,0.250000` | `-4.359874926582439` | Historical best recovered |
| Function 5 | `0.100000,0.999000,1.000000,1.000000` | `4427.343995806448` | New verified best |
| Function 6 | `0.700000,0.200000,0.700000,0.700000,0.200000` | `-0.7078316130911375` | Improved from Week 11 |
| Function 7 | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` | `1.3809299933612855` | Historical best recovered |
| Function 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` | Exact repeat of verified best |

## 3. Week 11 to Week 12 Change

| Function | Week 11 output | Week 12 output | Exact change |
| --- | ---: | ---: | ---: |
| Function 1 | `0.025559285339829783` | `0.025559285339829783` | `0` |
| Function 2 | `0.5848554940277205` | `0.7335252043269003` | `0.1486697102991798` |
| Function 3 | `-0.06542982421105416` | `-0.05985127532683556` | `0.00557854888421860` |
| Function 4 | `-4.868852987697114` | `-4.359874926582439` | `0.508978061114675` |
| Function 5 | `4411.0387356061765` | `4427.343995806448` | `16.3052602002715` |
| Function 6 | `-0.7268715077444687` | `-0.7078316130911375` | `0.0190398946533312` |
| Function 7 | `1.3579108517237013` | `1.3809299933612855` | `0.0230191416375842` |
| Function 8 | `9.58024` | `9.58024` | `0` |

The largest moderate scale improvement was Function 2. Its small local movement from `0.695000,0.950000` to `0.690000,0.950000` raised the objective from `0.5848554940277205` to `0.7335252043269003`. This gives strong support to the local directional evidence identified after Week 11.

## 4. Testing the Week 12 Strategy

Week 12 is useful because the different query choices can now be judged against their returned values rather than discussed only as planned strategies.

Function 2 tested a small local refinement and produced a substantial new best. Function 5 tested a further boundary refinement in the direction supported by both its objective history and the concentrated PCA trajectory. It improved again to `4427.343995806448`.

Functions 3, 4, 6 and 7 returned to stronger historical regions. Function 3 slightly exceeded its previous best. Functions 4 and 7 reproduced their earlier best values exactly. Function 6 improved from Week 11, although its Week 3 result of `-0.648848297397347` remains stronger than the Week 12 value.

Functions 1 and 8 repeated already confirmed best points and returned the same values again. These results strengthen the evidence for repeatability at those exact coordinates, although they add little information about the surrounding surface.

## 5. What the PCA Comparison Added

The PCA analysis was useful because it showed how concentrated the higher dimensional query histories had become. It was not treated as proof that a principal direction was also the direction of greatest objective improvement.

Function 5 provided the clearest case where structural concentration and objective performance agreed. The boundary move supported by that comparison produced another new best. For Functions 3, 4, 6 and 7, direct historical performance remained more useful than extrapolating along a principal component. Their Week 12 results support that decision.

This makes the Week 12 outcome more informative than a simple test of PCA. It tested whether PCA should influence the strategy only when its structural evidence agreed with observed performance.

## 6. Exploration and Simplification

By Week 12, several functions no longer benefited from broad exploration. Functions 1 and 8 had repeatable best points. Functions 4 and 7 had identifiable historical optima within the observed sample, and returning to those points recovered the same values. Function 5 had a clear boundary trajectory, while Function 2 still showed useful local improvement.

Function 6 remains less settled. Returning to its earlier best coordinates improved the Week 11 result but did not reproduce the earlier objective value. This is an important exception because it shows that not every historical recovery behaves like Functions 1, 4, 7 or 8.

The final round should therefore preserve function specific reasoning. Some functions now favour exploitation or confirmation, while others still justify a carefully chosen final test.

## 7. Evidence for the Final Round

The final Round 13 decision should be made only after the next course strategy has been reviewed alongside the Week 12 evidence. The present results already provide several useful constraints.

Function 2 has strong evidence for a productive local direction. Function 5 has continued to improve along a controlled boundary trajectory. Function 3 has just established a new best in its recovered historical region. Functions 1 and 8 are highly repeatable at their best observed points. Functions 4 and 7 have recovered their historical best values. Function 6 remains the clearest case where another analytical comparison may still add value.

These observations provide the starting point for the final exploration versus exploitation decision rather than fixing the Round 13 coordinates in advance.

## 8. Repository Status

The Week 12 folder now contains the verified submitted inputs, returned outputs, pre result reasoning, Module 23 reflection preparation and the exact Week 11 to Week 12 comparison.

The next development stage will add the full reproducible analysis, figure data, validation, datasheet and model card once the Week 12 strategy review and final round preparation are completed.

## 9. Conclusion

Week 12 provides strong evidence that comparing methods before selecting each query was useful. Every function either improved or retained a verified best level relative to Week 11. Three functions reached new best values, two recovered historical best values, and two repeated confirmed best values exactly.

The most useful lesson is not that one technique won across the portfolio. Different functions responded to different forms of evidence. That distinction will be central to the final Round 13 strategy.