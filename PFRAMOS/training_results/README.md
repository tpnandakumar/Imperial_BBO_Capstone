# PFRAMOS Training Results

## Purpose

This folder stores reproducible outputs from every schooling, validation, testing, bias, emergence and promotion cycle.

## Structure

```text
PFRAMOS/training_results/
├── sessions/
├── dataset_manifests/
├── validation_reports/
├── protected_test_reports/
├── bias_reports/
├── emergence_reports/
├── compute_energy_reports/
├── synthesis_reports/
├── promotion_decisions/
├── rollback_reports/
└── deletion_records/
```

Each training session must have a stable session identifier and must link to:

- the append-only training-log entry
- dataset snapshot and source manifests
- exact software environment
- hyperparameters and random seed
- baseline metrics
- validation metrics
- protected-test metrics
- coherence, robustness and calibration results
- bias and emergence findings
- compute, memory and energy measurements
- decision and rationale
- deletion record for temporary Schooling data

## Publication readiness

No result is publishable unless it is traceable to reproducible files in this folder. Claims must use only measured values from project data or clearly labelled external evidence.

## Naming convention

```text
YYYY-MM-DD_session-ID_result-type.ext
```

Example:

```text
2026-07-25_PSVC-001_validation-report.json
```
