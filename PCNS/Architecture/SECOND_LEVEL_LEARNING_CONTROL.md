# Second-Level Learning Control

## Purpose

The first control level regulates computational state and directed execution through A-DMIC and PCC. The second control level regulates learning quality and generalisation.

Its purpose is to prevent:

- underfitting
- overfitting
- premature convergence
- unstable generalisation
- excessive model complexity
- inadequate model capacity

## Evidence inputs

The controller should evaluate:

- training performance
- validation performance
- held-out test performance
- generalisation gap
- uncertainty and calibration
- model complexity
- feature utilisation
- stability across seeds and datasets
- sensitivity to perturbation

## Underfitting response

Possible responses include:

- acquire more relevant information
- improve feature representation
- increase model capacity
- increase training depth
- expand exploration
- reduce excessive regularisation
- allocate additional resources through A-DMIC

## Overfitting response

Possible responses include:

- increase regularisation
- reduce model complexity
- strengthen cross-validation
- stop training earlier
- increase data diversity
- reduce leakage and memorisation
- require independent validation

## Optimal Generalisation Zone

The aim is not to maximise training performance. The aim is to maintain the model within an Optimal Generalisation Zone where accuracy, robustness, stability, efficiency and reproducibility remain balanced.

## Integration with multilevel control

Learning-control feedback may be resolved locally when adjustment is minor. Persistent or conflicting signals escalate to A-DMIC, PCC or the Executive Computational Cortex according to whether the limiting factor is resource state, action strategy or task formulation.
