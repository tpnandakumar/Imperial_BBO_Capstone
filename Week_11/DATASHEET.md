# Week 11 Datasheet

## Purpose

This datasheet documents the verified Week 11 record for the Imperial Bayesian Black Box Optimisation capstone. It describes the submitted query vectors, returned objective values, provenance, analytical use and limitations. The numerical source files remain authoritative.

## Dataset scope

Week 11 contains one submitted query vector and one returned objective value for each of the eight hidden functions. Across Weeks 1 to 11, the cumulative record contains 88 submitted query vectors and 88 returned objective values.

| Function | Dimensions | Week 11 input | Week 11 output |
| --- | ---: | --- | ---: |
| Function 1 | 2 | `0.600000,0.600000` | `0.025559285339829783` |
| Function 2 | 2 | `0.695000,0.950000` | `0.5848554940277205` |
| Function 3 | 3 | `0.840000,0.160000,0.840000` | `-0.06542982421105416` |
| Function 4 | 4 | `0.620000,0.420000,0.440000,0.250000` | `-4.868852987697114` |
| Function 5 | 4 | `0.110000,0.998000,0.999900,0.999900` | `4411.0387356061765` |
| Function 6 | 5 | `0.720000,0.190000,0.700000,0.710000,0.150000` | `-0.7268715077444687` |
| Function 7 | 6 | `0.045000,0.485000,0.255000,0.220000,0.420000,0.745000` | `1.3579108517237013` |
| Function 8 | 8 | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` | `9.58024` |

## Source files

The exact Week 11 query vectors are stored in [week_11_inputs.csv](week_11_inputs.csv). The exact returned values are stored in [week_11_results.csv](week_11_results.csv). Derived summaries are stored separately and do not replace the source record.

## Provenance

The Week 11 queries were selected from the Week 10 analysis. That stage used clustering, distance to stronger historical regions, repeated points and local refinement to decide where each function should be queried next. Week 11 therefore acts as an outcome test of those earlier decisions.

The returned values were then compared with Week 10 and with the stronger historical observations from Weeks 1 to 10. All eight Week 11 values improved relative to Week 10. Functions 2 and 5 reached new verified best values, while Functions 1 and 8 reproduced earlier best values exactly.

## Analytical extensions

After the Week 11 results were available, the full Weeks 1 to 11 input history was examined using centred principal component analysis for Functions 3 to 8. The purpose was to study the geometry of the recorded search trajectories and to test whether lower dimensional structure could improve the Week 12 decision.

PCA was not used to choose the Week 11 queries. It was introduced after the Week 11 results and used only in the transition to Week 12.

## Data quality checks

The Week 11 input vectors conform to the expected dimensions of the eight functions. Every coordinate lies within the permitted interval from 0 to 1. The submitted inputs retain their six decimal place representation. Returned objective values are preserved exactly as supplied in the result file.

## Intended use

This dataset supports:

- within function comparison of optimisation progress;
- validation of the Week 10 strategy;
- analysis of repeated and recovered regions;
- study of the geometry of accumulated query trajectories;
- preparation of the Week 12 strategy comparison;
- reproducible figures and derived summaries.

## Limitations

The dataset is small and adaptively sampled. The observations were not drawn randomly from the full search spaces, so statistical summaries of query variation reflect the search strategy as well as the hidden response surfaces.

PCA of the query coordinates therefore describes how the search moved. It does not prove that the principal directions are the directions of greatest objective improvement. Objective values must be considered separately.

The numerical scales of the eight functions differ substantially. Cross function ranking is therefore descriptive only. Progress is more meaningful when assessed within each function across time.

## Relationship to Week 12

The Week 11 dataset is the evidence base used to prepare the submitted Week 12 query set. The full decision trail is recorded in [PCA_STRATEGY_COMPARISON.md](PCA_STRATEGY_COMPARISON.md) and [WEEK_12_DECISION_RECORD.md](WEEK_12_DECISION_RECORD.md).