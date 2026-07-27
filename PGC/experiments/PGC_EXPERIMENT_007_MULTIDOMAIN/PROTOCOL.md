# PGC Experiment 007: Multi-Domain, Multi-Dataset DDLCT Validation

## Purpose

Test whether one shared DDLCT control architecture generalises across different cognitive domains rather than succeeding only on one synthetic task family.

## DDLCT variants

1. Accuracy then laminarity
2. Laminarity then accuracy
3. Simultaneous DDLCT
4. Untuned domain baseline
5. Accuracy-only honing
6. Laminarity-only control
7. Oracle or empirical upper bound where valid

## Initial domain matrix

| Domain | Minimum task types | Minimum datasets |
|---|---|---:|
| Numerical and tabular | binary and multiclass classification, anomaly or risk estimation | 3 |
| Language | intent, sentiment or affect, contradiction or inference | 3 |
| Vision | object or scene classification, anomaly or relationship recognition | 3 |
| Temporal | sequence prediction, trend reversal, delayed consequence | 2 |
| Memory and recall | immediate recall, delayed recall, interference and provenance recall | 2 |
| Integrated multimodal | at least two modalities contributing to one decision | 2 |

## Shared governance

- train, validation and protected-test separation for every dataset
- no protected-test adaptation
- at least 10 fixed seeds per dataset where computationally feasible
- identical tuning budget across DDLCT sequence variants
- dataset licences and provenance recorded
- all failed and null runs retained
- all outputs labelled trial evidence until independently replicated

## Primary metrics

- protected-test accuracy
- macro-F1
- balanced accuracy
- calibration error
- worst-seed and worst-dataset accuracy
- rescue rate, harm rate and net tuning utility
- inference latency, training time, peak memory and model size
- laminarity index, threshold reversal rate and convergence steps

## Cognition validation pillars

### Data retention

Measure immediate retention, delayed retention, interference resistance, cross-domain retention and catastrophic forgetting.

### Computational processing accuracy

Measure task accuracy, reasoning accuracy, cross-domain integration accuracy, calibration and robustness under noise, missing data and distribution shift.

### Effective recall

Measure retrieval accuracy, contextual relevance, provenance correctness, useful recall rate, misleading recall rate and retrieval latency.

## Selection rule

The preferred architecture must maximise protected-test performance while preserving safety-critical recall and remaining on the best observed accuracy-efficiency-laminarity frontier. It must not be selected from a single dataset or a single favourable seed.

## First execution block

Begin with three CPU-manageable, clearly licensed tabular datasets of different structure, then freeze the shared controller and extend into language, vision, temporal and memory domains.
