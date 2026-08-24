# Final Capstone Datasheet

## Purpose

This datasheet describes the assessment-facing evidence set for the completed thirteen-round Imperial Bayesian Black Box Optimisation capstone. It does not replace the weekly source files. The submitted inputs and returned objective values stored in `Week_01` through `Week_13` remain the authoritative numerical record.

## Dataset composition

The capstone contains eight independent hidden objective functions with dimensions 2, 2, 3, 4, 4, 5, 6 and 8. One coordinate vector was submitted for each function in each of thirteen rounds, giving 104 weekly query vectors and 104 returned objective values in the completed experimental sequence.

## Source and provenance

The evidence was accumulated sequentially during the capstone. Each weekly folder records the query submitted for that round, the objective value returned by the authorised evaluator and the analysis used to prepare subsequent decisions. Later analytical methods were not written back into earlier rounds as though they had been available at the time.

The final-round authoritative files are `Week_13/week_13_inputs.csv` and `Week_13/week_13_results.csv`. The final historical comparison is stored in `Week_13/week_13_analysis_summary.csv` and the assessment-facing winner table is `Module_25_Final_BBO_Submission/Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv`.

## Data representation

All coordinate values lie within the permitted interval from 0 to 1. Submitted coordinates retain the required decimal representation. Returned objective values are preserved as supplied rather than rounded for analysis files. Floating-point conversion is used only where needed for plotting.

## Analytical use

The dataset supports:

- within-function optimisation trajectories across thirteen rounds;
- comparison of exploration, refinement, exploitation, recovery and stopping decisions;
- clustering-informed regional analysis;
- PCA of accumulated query trajectories;
- boundary-behaviour analysis;
- repeatability checks;
- final exploration versus exploitation interpretation;
- reproducible generation of summary tables and figures.

The eight functions operate on different output scales, so raw objective magnitudes are not treated as a common cross-function performance score.

## Quality and validation

Week 13 validation confirms eight final input vectors, eight returned objective values, correct function dimensions and coordinates within the permitted domain. Exact Week 12 to Week 13 changes are calculated with decimal arithmetic in the final analysis workflow.

Repeated coordinates provide additional evidence. F1, F4, F7 and F8 reproduced established best values. F6 is an important exception: the identical recorded coordinate `0.700000,0.200000,0.700000,0.700000,0.200000` returned `-0.648848297397347`, `-0.7078316130911375` and `-0.6071562248604215` in Weeks 3, 12 and 13 respectively.

## Limitations

The sample is small and adaptively collected. Later queries were intentionally concentrated around regions that appeared promising, so the data do not represent random coverage of each search space. The hidden mathematical functions are unknown, gradients are unavailable and the strongest observed coordinates are not proofs of global optimality.

PCA and clustering describe structure in the observed search history. They are supporting analytical lenses rather than direct observations of the hidden functions.

## Post-capstone boundary

The Advanced Extension Series and SOC use the completed capstone evidence for additional research after Round 13. Surrogate predictions are not part of this datasheet's verified objective record and are not presented as Imperial evaluator outputs.
