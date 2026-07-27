# PGC Experiment 008CA: Laser Target Honing Across A-DMIC Engines

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Integrate Laser Target Honing with floor protection into three established A-DMIC engines and compare each honed engine against its unchanged baseline.

## Engines

- AX-R-BK + A-DMIC
- DTRRR protected stochastic + A-DMIC
- ECSP + A-DMIC

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- 100 aggregate evaluations per system
- A-DMIC-PAHE freedom: ±2.0 percentage points
- no holdout labels used for honing
- vectorised Laser Target Honing with focused specialist pulse, recoil, laser stop and full-route floor fallback

## Results

### AX-R-BK + A-DMIC + LTH

- peak frequency at or above 99.5%: 5%
- near-peak frequency at or above 99.0%: 22%
- median accuracy: 0.982822
- median 95% bootstrap CI: 0.981189 to 0.987135
- modal band: 0.9886
- sample SD: 0.007510
- mean accuracy: 0.983280
- mean 95% CI: 0.981790 to 0.984770
- minimum accuracy: 0.965302
- maximum accuracy: 0.996296
- mean log loss: 0.060733
- mean active models: 3.739
- Net Regenerative Efficiency: 0.838631

Compared with baseline:

- mean accuracy change: +0.000150, not significant
- near-peak frequency: 17% to 22%
- log-loss improvement: -0.015645, Holm-significant
- active models: +0.396
- Net Regenerative Efficiency: -0.011024

### DTRRR protected stochastic + A-DMIC + LTH

- peak frequency at or above 99.5%: 1%
- near-peak frequency at or above 99.0%: 21%
- median accuracy: 0.984430
- median 95% bootstrap CI: 0.982115 to 0.987671
- modal band: 0.9877
- sample SD: 0.007671
- mean accuracy: 0.983378
- mean 95% CI: 0.981856 to 0.984900
- minimum accuracy: 0.965302
- maximum accuracy: 0.997222
- mean log loss: 0.061468
- mean active models: 3.248
- Net Regenerative Efficiency: 0.856462

Compared with baseline:

- mean accuracy change: -0.000044, not significant
- peak frequency: 6% to 1%
- median accuracy increased
- log-loss improvement: -0.015682, Holm-significant
- active models: +0.530
- Net Regenerative Efficiency: -0.017916

### ECSP + A-DMIC + LTH

- peak frequency at or above 99.5%: 3%
- near-peak frequency at or above 99.0%: 21%
- median accuracy: 0.984747
- median 95% bootstrap CI: 0.981579 to 0.986745
- modal band: 0.9753
- sample SD: 0.007817
- mean accuracy: 0.983392
- mean 95% CI: 0.981841 to 0.984943
- minimum accuracy: 0.960380
- maximum accuracy: 0.996296
- mean log loss: 0.058750
- mean active models: 3.519
- Net Regenerative Efficiency: 0.846695

Compared with baseline:

- mean accuracy change: -0.000003, not significant
- near-peak frequency: 18% to 21%
- log-loss improvement: -0.013218, Holm-significant
- active models: +0.457
- Net Regenerative Efficiency: -0.015583

## Interpretation

Laser Target Honing consistently improved calibration in all three engines.

Its strongest peak-frequency benefit appeared in AX-R-BK + A-DMIC, where near-peak frequency increased from 17% to 22% and the 99.5% peak frequency remained at 5%.

DTRRR protected stochastic + A-DMIC retained the highest honed median and maximum accuracy, but LTH reduced its peak frequency and regenerative efficiency.

ECSP + A-DMIC + LTH achieved the lowest log loss and highest honed median, but also the weakest minimum accuracy.

The present LTH implementation should therefore be treated as an optional calibration and peak-access module, not a mandatory layer. It needs a stricter activation gate so that honing is applied only when predicted benefit exceeds its active-model and regenerative cost.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Cardiovascular, atmospheric and laser-honing terms are computational control analogues. Electrical energy was not measured.
