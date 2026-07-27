# PGC Experiment 008AY: Fresh-Seed Micro-Tuned Optimised Milieu

## Status

Completed fresh-seed comparative replication. This is not a single untouched confirmatory test.

## Purpose

Isolate the protocols that exceeded 0.99 in Experiment 008AX, rerun them on ten entirely new split seeds, and test whether dynamic micro-tuning can create a more consistently optimised internal milieu.

## New seeds

181, 197, 211, 227, 241, 257, 271, 283, 307 and 331.

## Stack depths

- 5-model stack
- 10-model stack

## Arms

- isolated stable interior
- pulsatile pressure-gradient micro-tuning
- dynamic optimised milieu

## Micro-tuned variables

- model-flow scales
- ridge alpha
- heart-rate proxy
- pulse-pressure proxy
- systolic phase position
- viscosity
- compressibility
- lubrication
- venous recovery

## Search design

- ten new split seeds
- ten independent repeats per seed
- 100 repeat-level evaluations per stack
- 200 repeat-level evaluations in total
- 9,000 development candidates
- development-only screening
- cross-fitted ridge refinement
- protected evaluation after each winner was fixed

## Fresh-seed results

| Stack | Mean protected accuracy | 95% CI | Minimum | Maximum | Runs at or above 0.99 | Mean log loss |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 0.981564 | 0.980290 to 0.982838 | 0.969786 | 0.991667 | 10 | 0.805830 |
| 10 | **0.984678** | **0.983391 to 0.985966** | **0.975341** | **0.995370** | **20** | **0.799014** |

Across both stacks, 30 of 200 repeat-level evaluations reached or exceeded 0.99.

## Best fresh-seed run

- seed: 211
- stack size: 10
- selected arm: isolated stable interior
- phase: diastole
- protected accuracy: **0.995370**
- protected worst-dataset accuracy: 0.986111
- macro-F1: 0.995368
- balanced accuracy: 0.995370
- log loss: 0.793226
- ridge alpha: 1.136104
- viscosity: 0.610911
- compressibility: 0.143529
- lubrication: 0.563618
- recovery: 0.554986

## Arm behaviour

The isolated stable interior was selected in 94 of 100 repeats for both stack sizes. This shows that the dominant above-0.99 signature is a low-deformation, stable internal milieu rather than continuous strong pulsation.

For the 10-stack, the less frequently selected dynamic arms were highly successful when development evidence supported them:

- pulsatile pressure-gradient micro-tuning was selected 5 times and reached at least 0.99 in 4 of those 5 selections
- dynamic optimised milieu was selected once and achieved 0.995370

This indicates that micro-tuning should be event-triggered rather than continuously active.

## Interpretation

The fresh-seed experiment confirms that above-0.99 outcomes are reproducible on new splits, but not yet stable as an average operating level.

The 10-stack improved mean protected accuracy from 0.983954 in 008AX to 0.984678 in 008AY and improved mean log loss from 0.801245 to 0.799014.

The most credible operating rule is therefore:

```text
maintain a stable low-deformation interior
+
activate pulsatile or dynamic micro-tuning only when development evidence shows a local advantage
+
return rapidly to baseline through venous recovery
```

## Evidence boundary

The earlier above-0.99 outcomes were used only to define broad candidate regions. They were not used to select winners on the new seeds.

Each seed-specific protected split was reused across ten predeclared repeats. The experiment is therefore a fresh-seed comparative replication, not a single untouched final confirmation.
