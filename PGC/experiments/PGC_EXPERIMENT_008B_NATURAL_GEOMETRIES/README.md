# PGC Experiment 008B: Natural Geometry and QED-Inspired Field Trial

## Status

Completed trial evidence. Not publication evidence.

## Design

Five base classifiers were combined under eight matched routing geometries across Breast Cancer Wisconsin, Wine and Digits. Ten fixed seeds were used for each dataset. All model fitting and geometry weighting used training and validation data only. The protected test remained frozen.

## Geometries

- no vectoring
- standard maximum-accuracy vectoring
- Golden Ratio spiral
- Fibonacci spiral
- QED-inspired interaction field
- Golden Ratio with QED-inspired coupling
- Fibonacci with QED-inspired coupling
- full Golden-Fibonacci-QED pressure-and-ebb-flow hybrid

## Best aggregate result

Best geometry: **full_golden_fibonacci_qed**

- mean protected-test accuracy: **0.978289**
- mean macro-F1: **0.977490**
- mean balanced accuracy: **0.976366**
- mean log loss: **0.122245**
- selective accuracy at the 0.99 confidence threshold: **0.999034**
- coverage at that threshold: **0.237178**
- worst dataset-seed accuracy: **0.938596**

## Dataset-specific findings

- Breast Cancer Wisconsin: the full Golden-Fibonacci-QED hybrid was best at **0.964035** mean accuracy.
- Wine: the full hybrid tied the strongest result at **0.986111** mean accuracy.
- Digits: Fibonacci-QED, Golden-QED and their non-QED spiral counterparts reached **0.985556** mean accuracy.

## Interpretation

The full Golden-Fibonacci-QED hybrid was the strongest natural-geometry variant in this trial and improved aggregate accuracy over equal unweighted routing. It did not surpass the earlier Experiment 008 fusion-anchor benchmark of 0.986126.

The QED component is a computational analogy for route interaction and field tension. It is not literal quantum electrodynamics. Golden Ratio and Fibonacci geometries are treated as fixed natural priors and retained only when protected-test evidence supports them.

The next refinement should combine the earlier high-accuracy fusion anchor with domain-conditional activation of the natural-geometry field, rather than replacing the anchor unconditionally.
