# PACC Publication-Grade Training Protocol

## Purpose

Every PACC training activity must generate a complete evidence trail suitable for scientific review and later manuscript preparation.

## Required record for every run

Each run must record:

- experiment identifier
- date and time
- cognitive domain and training lane
- research question and hypothesis
- dataset name, version, source and provenance
- licence, access, privacy and ethics status
- inclusion and exclusion criteria
- preprocessing steps
- mathematical model version
- software version and commit hash
- random seed
- hardware and runtime environment
- memory allocation and reclamation events
- PCECE measurements
- RaR and DMACCE decisions
- dynamic function priority history
- training parameters
- baseline methods
- protected-test definition
- training, validation and protected-test metrics
- uncertainty and calibration
- negative, null and failure results
- PIMF influence analysis
- PFRAMOS conduit decision
- limitations
- publication paper assignment

## Evidence classes

Every reported statement must be classified as:

- `MEASURED`, directly observed in project data
- `DERIVED`, reproducibly calculated from measured data
- `EXTERNAL`, supported by cited literature
- `INFERENCE`, reasoned interpretation supported by evidence
- `HYPOTHESIS`, not yet confirmed

## Dataset evidence gate

A dataset cannot be used for parameter updates until these are complete:

- dataset manifest
- licence approval
- access approval
- provenance verification
- privacy review
- ethics review where applicable
- contamination review
- representativeness review
- train, validation and protected-test split

Discovery and shadow evaluation may proceed before all training gates pass, but must be clearly labelled.

## Experimental sequence

```text
Research question
        ↓
Pre-specified hypothesis
        ↓
Dataset and licence validation
        ↓
Fixed mathematical model version
        ↓
Baseline and ablation design
        ↓
Training run
        ↓
Protected testing
        ↓
PIMF analysis
        ↓
PFRAMOS decision
        ↓
PCECE and memory-efficiency analysis
        ↓
Publication routing
```

## Publication requirements

A result may enter a manuscript as measured evidence only when:

- the run is reproducible
- all metrics resolve to traceable records
- the protected test has not leaked
- negative results are retained
- model and dataset versions are fixed
- figures are generated from stored data
- limitations are recorded
- evidence ownership is assigned to one primary paper

## Writing standard

Publication outputs must use British English, remove em dashes and en dashes, avoid formulaic AI-style phrasing, and distinguish measured findings from interpretation.

## Clinical boundary

Computational cognitive validation does not establish clinical diagnostic validity or human equivalence. Any clinical claim requires separate ethical, regulatory and clinical validation.

## Governing statement

Every training run must be reproducible, auditable and publication-ready from the moment it begins.
