# PGC Experiment 008AN: Energy and Cost Efficiency

## Status

Completed derived efficiency analysis from Experiment 008AM.

## Purpose

Quantify how much compute can be reduced while retaining the strongest 008AM result.

## Measurement boundary

Measured directly:

- wall-clock runtime
- candidate counts
- model architecture
- accuracy and calibration metrics

Not measured directly:

- electrical energy in kWh
- hardware power draw
- monetary cost

Therefore, energy and cost efficiency are represented by reproducible compute proxies:

- number of candidate evaluations
- proportional runtime share
- fraction of the original search budget retained

## Main result

The strongest arm remained **high viscosity with high lubrication**.

- protected-test accuracy: 0.988596
- log loss: 0.808669
- exact development optimum first reached at configuration 48
- full arm budget: 100 configurations
- candidate evaluations retained: 48%
- candidate evaluations saved: **52%**
- proportional runtime share: approximately 1.851 seconds of the measured 23.142-second total experiment runtime

## Interpretation

The high-viscosity, high-lubrication regime did not merely preserve the peak accuracy. It reached its exact development optimum before half of its allocated arm budget was consumed.

This means the regime is a candidate for early stopping based on:

1. stable bootstrap uncertainty
2. no improvement over a defined patience window
3. preserved worst-case development accuracy
4. stable log loss

The 52% saving is a compute proxy. It should not be described as a measured 52% reduction in electrical energy unless power draw is instrumented in a future run.

## Recommended operational rule

For confirmation runs, stop the search arm when:

- the best development score has not improved for 12 consecutive candidates
- bootstrap standard deviation remains within 5% of its best value
- worst-case accuracy does not decline
- at least 40 candidates have been evaluated

This should preserve the laminar optimum while reducing search time, energy demand and cost.
