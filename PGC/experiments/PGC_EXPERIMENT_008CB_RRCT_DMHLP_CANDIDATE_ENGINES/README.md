# PGC Experiment 008CB: RRCT-DMHLP Across Candidate Engines

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Test Radar Ripple Capture and Takeover with FBW-PVF far-range correction, dual-mode handover, ILS-H close-range honing, aligned deadband and floor-protected go-around across the three current A-DMIC candidate engines.

## Engines

- AX-R-BK + A-DMIC
- DTRRR protected stochastic + A-DMIC
- ECSP + A-DMIC

Each engine was evaluated in three modes:

- baseline A-DMIC
- continuous Laser Target Honing
- RRCT-DMHLP selective intervention

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- 100 aggregate evaluations per system
- holdout labels were not used for control or route selection

## Main result

RRCT-DMHLP reduced honing activation to approximately 16% to 17% of samples. It improved calibration relative to baseline and used substantially less intervention than continuous Laser Target Honing.

It did not improve overall accuracy across all candidate engines.

## ECSP

### Baseline

- peak frequency at or above 99.5%: 7%
- near-peak frequency at or above 99.0%: 27%
- median accuracy: 0.984747
- mean accuracy: 0.984641
- minimum accuracy: 0.966862
- maximum accuracy: 0.996296
- mean log loss: 0.072698
- active models: 3.060
- Net Regenerative Efficiency: 0.862313

### RRCT-DMHLP

- peak frequency: 2%
- near-peak frequency: 21%
- median accuracy: 0.984747
- mean accuracy: 0.984024
- minimum accuracy: 0.968713
- maximum accuracy: 0.995370
- mean log loss: 0.060376
- active models: 3.187
- Net Regenerative Efficiency: 0.858528
- activation rate: 15.93%
- FBW rate: 6.89%
- handover rate: 4.03%
- ILS-H rate: 5.01%
- go-around rate: 0.71%

RRCT-DMHLP improved the minimum accuracy and calibration, but reduced peak and near-peak frequency.

## AX-R-BK

### Baseline

- peak frequency: 3%
- near-peak frequency: 22%
- median accuracy: 0.984747
- mean accuracy: 0.983766
- minimum accuracy: 0.967300
- maximum accuracy: 0.996296
- mean log loss: 0.077484
- active models: 3.320
- Net Regenerative Efficiency: 0.850434

### RRCT-DMHLP

- peak frequency: 0%
- near-peak frequency: 20%
- median accuracy: 0.983748
- mean accuracy: 0.983002
- minimum accuracy: 0.965302
- maximum accuracy: 0.994444
- mean log loss: 0.063059
- active models: 3.479
- Net Regenerative Efficiency: 0.847789
- activation rate: 17.46%

The selective controller improved calibration but did not preserve the peak-producing trajectories of AX-R-BK.

## DTRRR protected stochastic

### Baseline

- peak frequency: 2%
- near-peak frequency: 18%
- median accuracy: 0.983821
- mean accuracy: 0.983043
- minimum accuracy: 0.960819
- maximum accuracy: 0.997222
- mean log loss: 0.077481
- active models: 2.714
- Net Regenerative Efficiency: 0.874492

### RRCT-DMHLP

- peak frequency: 2%
- near-peak frequency: 21%
- median accuracy: 0.982505
- mean accuracy: 0.982551
- minimum accuracy: 0.966228
- maximum accuracy: 0.996296
- mean log loss: 0.063519
- active models: 2.880
- Net Regenerative Efficiency: 0.869563
- activation rate: 17.32%

This was the most promising RRCT-DMHLP application. Near-peak frequency increased from 18% to 21%, the minimum accuracy improved materially, and calibration improved, but median and mean accuracy fell.

## Interpretation

The radar-ripple capture concept successfully reduced unnecessary intervention and improved floor behaviour in ECSP and DTRRR protected stochastic.

The present capture criterion is still too focused on confidence, margin and entropy. Those signals identify uncertainty but do not reliably distinguish a naturally correct trajectory from a trajectory that should be redirected.

RRCT-DMHLP should therefore not replace the baseline engines yet. The next version requires a learned development-derived capture classifier that predicts whether intervention is likely to improve the route before system takeover.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Radar, ripple, FBW, ILS and landing terms are computational control analogues. Electrical energy was not measured.
