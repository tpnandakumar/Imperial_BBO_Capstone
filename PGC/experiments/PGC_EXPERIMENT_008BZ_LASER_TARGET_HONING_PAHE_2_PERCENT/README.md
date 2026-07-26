# PGC Experiment 008BZ: Laser Target Honing under PAHE ±2.0%

## Status

Completed fresh matched comparative development experiment. This is not final confirmatory evidence.

## Design

- datasets: breast cancer, wine and digits
- 10 independent cycle seeds
- 10 repeats per cycle
- 100 aggregate evaluations per system
- PAHE freedom: ±2.0 percentage points, equal to ±0.02 on the 0 to 1 scale
- no holdout labels used for route selection

## Systems

- PBAC dynamic honing under ±2.5% as reference
- PBAC dynamic honing under ±2.0%
- PBAC laser target honing under ±2.0%
- PBAC laser target honing under ±2.0% with floor protection

## Laser target honing

The controller honed:

- route order
- local model membership
- alternate-route pulse strength
- specialist-equivalent blend timing
- recoil timing
- local stopping point
- full 11-model floor fallback

## Main result

No system produced an aggregate run at or above 99.5%.

Near-peak frequency at or above 99.0% was:

- dynamic honing ±2.5%: 19%
- dynamic honing ±2.0%: 12%
- laser target honing ±2.0%: 12%
- laser target honing ±2.0% with floor protection: 30%

## Best peak-access system

PBAC laser target honing ±2.0% with floor protection:

- near-peak frequency: 30%
- median accuracy: 0.981433
- median 95% bootstrap CI: 0.979045 to 0.984284
- modal bands: 0.9829, 0.9906, 0.9914 and 0.9915
- modal frequency: 10 of 100
- sample SD: 0.006525
- mean accuracy: 0.982656
- mean 95% CI: 0.981361 to 0.983951
- minimum accuracy: 0.973051
- maximum accuracy: 0.991520
- mean active models: 9.560
- mean Net Regenerative Efficiency: 0.623615

## Other findings

Dynamic honing under ±2.0% had the lowest SD, 0.005717, and the highest Net Regenerative Efficiency, 0.648537, among the ±2.0% systems.

Unprotected laser honing did not improve peak frequency and increased active-model use.

## Statistical evidence

The overall Friedman comparison was not significant:

- statistic: 4.946537
- p value: 0.175754

No pairwise superiority was statistically confirmed after Holm correction.

## Interpretation

Tightening the atmosphere from ±2.5% to ±2.0% reduced ordinary near-peak access. Adding floor protection then increased near-peak frequency to 30%, showing that laser honing is more effective when a conservative full-route fallback is available.

The true 99.5% peak basin was still not entered. The remaining bottleneck is likely trajectory timing and route-state recognition rather than freedom amplitude alone.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Cardiovascular and atmospheric terms are computational control analogues. Electrical energy was not measured.
