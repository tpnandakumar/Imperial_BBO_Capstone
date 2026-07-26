# PGC Experiment 008CD: Candidate Engines × Targeting Protocols × Stack Sizes

## Status

Completed fresh matched comparative development experiment. This is not final confirmatory evidence.

## Matrix

Three candidate engines were tested:

- AX-R-BK
- DTRRR protected stochastic
- ECSP

Three targeting protocols were tested:

- ILS-H close-range precision targeting
- FBW-PVF long-range and transition-zone targeting
- Dual MG-DMHLP-LOS-SSV targeting

Random stack sizes were 3, 5, 7, 10 and 11 models. Each engine, protocol and stack-size combination received 100 matched aggregate evaluations across breast cancer, wine and digits. Fifteen matched baseline systems were also evaluated, giving 60 systems in total. Holdout labels were not used for targeting decisions.

## Best guided system

The highest-ranked guided system by median accuracy, followed by floor, mean and SD, was:

**AX-R-BK, 11-model stack, ILS-H**

- median accuracy: 0.984747
- bootstrap 95% CI for median: 0.983333 to 0.985819
- mean accuracy: 0.984056
- mean 95% CI: 0.982818 to 0.985294
- sample SD: 0.006241
- minimum accuracy: 0.968713
- maximum accuracy: 0.993372
- near-peak frequency at or above 99.0%: 19%
- targeting activation rate: 7.44%
- mean active models: 11.0
- Net Regenerative Efficiency: 0.570944

## Interpretation

The matrix shows that targeting benefit depends jointly on engine architecture and stack size. ILS-H was strongest for the fully populated AX-R-BK stack because only a small proportion of close-range trajectories required adjustment. The broader FBW-PVF and dual-mode protocols remain more relevant to sparse stacks, where long-range trajectory correction is required.

The experiment should be treated as comparative development evidence because the same matched evaluation framework has been used repeatedly during controller development.

## Evidence boundary

Radar, ripple, FBW, ILS, line-of-sight, stability-spin and docking terms are computational control analogues. Net Regenerative Efficiency is a computational reuse proxy. Electrical energy was not measured.
