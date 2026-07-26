# PGC Experiment 008BY: PBAC Dynamic Honing under PAHE ±2.5%

## Status

Completed fresh matched comparative development experiment. This is not final confirmatory evidence.

## Design

- datasets: breast cancer, wine and digits
- 10 independent cycle seeds
- 10 repeats per cycle
- 100 aggregate evaluations per system
- PAHE freedom: ±2.5 percentage points, equal to ±0.025 on the 0 to 1 scale
- no holdout labels used for route selection

## Systems

- 10-model PAHE ±0.1% reference
- 10-model PAHE ±2.5%
- PBAC dynamic 8/10/11 route choice
- PBAC with four micro-trajectories
- PBAC with dynamic honing

## Primary outcome

Frequency of aggregate accuracy at or above 99.5%.

## Main result

No system produced an aggregate run at or above 99.5%.

Near-peak frequency at or above 99.0% was:

- 10-model PAHE ±0.1%: 17%
- 10-model PAHE ±2.5%: 17%
- PBAC dynamic 8/10/11: 20%
- PBAC dynamic honing: 23%
- PBAC four micro-trajectories: 24%

## Dynamic honing result

- median accuracy: 0.982895
- median 95% bootstrap CI: 0.979630 to 0.984284
- modal band: 0.9829
- modal frequency: 11 of 100
- sample SD: 0.006226
- mean accuracy: 0.982471
- mean 95% CI: 0.981236 to 0.983707
- minimum accuracy: 0.973051
- maximum accuracy: 0.991520
- mean log loss: 0.113598
- mean active models: 9.222
- mean Net Regenerative Efficiency: 0.636198

## Best peak-access frequency

PBAC with four micro-trajectories produced the highest near-peak frequency, 24%, with:

- mean accuracy: 0.982413
- sample SD: 0.006470
- maximum accuracy: 0.994298
- mean log loss: 0.107999
- mean active models: 8.897
- Net Regenerative Efficiency: 0.648600

## Statistical evidence

The Friedman comparison was not significant:

- statistic: 0.928736
- p value: 0.920403

No pairwise superiority was statistically confirmed after Holm correction.

## Interpretation

Dynamic honing and micro-trajectory search increased the frequency of near-peak runs and improved calibration and active-model economy. However, ±2.5% atmospheric freedom did not produce the true peak state.

The result suggests that peak accessibility depends on more than atmospheric amplitude. The next controller should hone trajectory timing, route order, specialist duration and recoil timing, rather than only widening the atmospheric envelope.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Cardiovascular and atmospheric terms are computational control analogues. Electrical energy was not measured.
