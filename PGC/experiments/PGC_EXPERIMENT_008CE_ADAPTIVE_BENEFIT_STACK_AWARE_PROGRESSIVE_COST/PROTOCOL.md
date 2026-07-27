# Experiment 008CE Implementation Protocol

## Implemented recommendations

1. A development-only intervention-benefit predictor estimates whether escalation is likely to improve a route.
2. Targeting is stack-aware: FBW-PVF for 3 and 5 models, dual control for 7, and ILS-H for 10 and 11.
3. Stability spin requires measured staged oscillation and is not continuously active.
5. Models are progressively recruited from core models to specialist and then full rescue route.
6. Wall-clock latency and resident-memory change are measured directly.

## Evidence controls

- Holdout labels are not supplied to the controller.
- Electrical energy is not estimated from model count.
- Monetary cost remains unset until a deployment tariff and hardware measurements exist.
- Final superiority requires a frozen independent confirmation study.

## Acceptance tests

- benefit predictor fits only on development predictions
- dense stacks select ILS-H
- sparse stacks select FBW-PVF
- spin activation is never greater than measured oscillation
- active model count remains between the initial stack and full route
- latency and memory fields are populated

## Smoke-test result

All implementation checks passed:

- output probability shape valid
- probabilities normalised
- sparse stack selected FBW-PVF
- spin activation bounded by measured oscillation
- progressive active-model count remained within bounds
- latency recorded
- memory recorded
- electrical energy left unreported rather than estimated
- monetary cost left unreported rather than invented

The smoke test measured approximately 0.78 ms controller latency on the current notebook runtime. This is an implementation check only and is not a deployment benchmark.
