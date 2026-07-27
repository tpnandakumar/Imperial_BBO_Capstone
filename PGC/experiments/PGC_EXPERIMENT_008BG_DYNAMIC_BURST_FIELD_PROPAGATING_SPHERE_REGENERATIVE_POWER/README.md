# PGC Experiment 008BG: Dynamic Burst Field, Propagating Sphere and Regenerative Power

## Status

Completed closed-system cross-domain validation. This is not a final confirmatory result.

## Purpose

Integrate and test:

- propagating sphere of influence
- Delta Bridge sensing
- dynamic burst propagation
- wave capture
- selective amplification
- specialist recruitment
- directional vectoring
- dynamic dampening
- regenerative computational reuse

## Closed-system constraint

No new models, features or external information were added during field control. Any gain therefore came only from better internal organisation and reuse of the fixed computational system.

## Design

- 12 heterogeneous datasets
- 3 new seeds: 1009, 1031 and 1063
- 36 dataset-seed units
- three-fold cross-fitting
- 108 development configurations per unit
- development-only optimisation

## Systems compared

- stable 5-stack
- fixed uniform burst
- adaptive-radius sphere
- anisotropic vectorised sphere
- full Delta Bridge regenerative field

## Main result

The fixed uniform burst remained strongest overall.

- mean accuracy: 0.869016
- worst-unit accuracy: 0.413889
- macro-F1: 0.792411
- balanced accuracy: 0.792329
- log loss: 0.355708
- corrected errors: 14
- new errors: 7
- Net Sphere Gain: 7
- mean regenerative power proxy: 0.065076

## Dynamic field result

The full Delta Bridge regenerative field did not outperform the stable 5-stack or fixed burst.

- versus stable 5-stack: mean difference -0.000446
- versus fixed uniform burst: mean difference -0.000878
- versus anisotropic sphere: mean difference -0.000077

None of these comparisons was statistically significant after Holm correction.

The Friedman test was also not significant:

- statistic: 7.746606
- p value: 0.101314

## Interpretation

The experiment shows that a closed system can recover and reuse computational state, but the current regenerative field does not yet convert that reuse into higher predictive accuracy.

The fixed burst benefited from simplicity and consistent moderate reinforcement. The dynamic field introduced additional control complexity, and its capture, amplification, vectoring and dampening rules were not calibrated precisely enough to improve the decision boundary.

The useful finding is that regenerative power is measurable as a computational reuse proxy. The next stage should optimise for a joint objective:

```text
accuracy
+
Net Sphere Gain
+
avoided model evaluations
+
regenerative power proxy
-
control overhead
```

## Evidence boundary

Sphere, pressure, wave, phase and regenerative power are computational control-state proxies. Training and inference times are measured wall-clock values. Electrical energy was not measured.
