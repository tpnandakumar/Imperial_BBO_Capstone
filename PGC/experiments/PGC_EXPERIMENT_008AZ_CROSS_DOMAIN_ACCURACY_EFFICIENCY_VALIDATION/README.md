# PGC Experiment 008AZ: Cross-Domain Accuracy and Efficiency Validation

## Status

Completed Phase 1 cross-domain exploratory validation. This is not a final confirmatory result.

## Purpose

Test whether the event-triggered cardiovascular microcirculation and pulsatile conduit generalise beyond the original three datasets, while measuring actual wall-clock training time, inference time, candidate evaluations and model activation.

## Data coverage

Twelve heterogeneous datasets were used:

- breast cancer
- wine
- digits
- iris
- moons
- circles
- 95:5 imbalanced binary classification
- 99:1 imbalanced binary classification
- high-dimensional sparse-like multiclass data
- 15% label-noise multiclass data
- mixed redundant multiclass data
- sequential waveform classification

Three new split seeds were used: 401, 419 and 443, giving 36 dataset-seed units.

## Systems compared

- best single model selected from development out-of-fold performance
- static 5-model stack
- static 10-model stack
- pulsatile 10-model stack
- event-triggered specialist microcirculation

## Validation protocol

- 20% stratified holdout
- three-fold development cross-fitting
- development-only system selection and micro-tuning
- identical splits for all systems
- one holdout evaluation after each development configuration was fixed

## Main results

| System | Mean accuracy | Worst unit | Macro-F1 | Balanced accuracy | Log loss | Models activated per sample |
|---|---:|---:|---:|---:|---:|---:|
| Best single | **0.870799** | **0.386111** | **0.798027** | **0.796879** | 0.379253 | 1.000 |
| Static 5-stack | 0.868059 | 0.383333 | 0.791528 | 0.791657 | **0.346426** | 5.000 |
| Event-triggered microcirculation | 0.868047 | 0.383333 | 0.791486 | 0.791696 | 0.348603 | 7.425 |
| Static 10-stack | 0.866979 | 0.386111 | 0.791606 | 0.791318 | 0.376850 | 10.000 |
| Pulsatile 10-stack | 0.866979 | 0.386111 | 0.791604 | 0.791318 | 0.376666 | 10.000 |

## Statistical evidence

The Friedman test across all five systems was not significant:

- statistic: 3.989637
- p value: 0.407410

Pairwise development-independent comparisons also showed no significant advantage after Holm correction:

- event-triggered microcirculation versus static 5-stack: mean difference -0.000012, Holm p = 1.000000
- event-triggered microcirculation versus static 10-stack: mean difference 0.001068, Holm p = 0.900512
- pulsatile 10-stack versus static 10-stack: mean difference approximately 0, Holm p = 1.000000

## Efficiency findings

The event-triggered system activated 7.425 models per sample on average, compared with 10 for the full static stack. This represents a 25.8% reduction in model activation.

Its measured inference-time ratio was 0.547 relative to the static 10-stack, corresponding to approximately 45.3% lower inference time in this experiment.

The static 5-stack remained more efficient, using five models per sample and approximately 21.8% of the static 10-stack inference time, while also achieving the best mean log loss.

## Interpretation

The cross-domain result does not support a universal accuracy advantage for pulsatile or event-triggered regulation under this first broad protocol.

The most important positive finding is efficiency: event-triggered microcirculation preserved performance close to the static 5-stack and static 10-stack while reducing average model activation and inference time.

The strongest cross-domain accuracy came from development-selected single models. This indicates that dataset-specific model selection currently adds more value than applying one universal cardiovascular regulation policy across all data types.

The next stage should therefore use data-family-specific autonomic policies rather than one global threshold set. Imbalanced, nonlinear, sequential and high-dimensional data should each receive separately tuned specialist routing.

## Measurement boundary

Training and inference times are measured wall-clock times. Candidate counts and models activated are measured computational quantities. Electrical energy and monetary cost were not measured.
