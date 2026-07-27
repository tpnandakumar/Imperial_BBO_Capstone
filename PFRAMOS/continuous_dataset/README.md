# PFRAMOS Continuous Evidence Dataset

## Purpose

PFRAMOS requires a continuously growing, versioned and traceable dataset for training, validation and controlled node recruitment.

The dataset must not be a single mutable file. It is an append-only evidence system that preserves provenance, source quality, temporal order, transformation history and model-use restrictions.

## Data layers

```text
Raw evidence
    ↓
Provenance and integrity checks
    ↓
Deduplication and normalisation
    ↓
Quality and relevance scoring
    ↓
Quarantine
    ↓
Validated evidence store
    ↓
Time-aware train, validation and test views
    ↓
Controlled retraining
    ↓
Post-training audit and rollback
```

## Core stores

```text
PFRAMOS/continuous_dataset/
├── raw/
├── quarantine/
├── validated/
├── rejected/
├── manifests/
├── snapshots/
├── splits/
├── drift_reports/
└── training_runs/
```

Large source files should normally remain in controlled external storage or GitHub Actions artefacts. Git stores manifests, schemas, hashes, summaries and compact validated records.

## Record requirements

Every record must include:

- stable record identifier
- source identifier and source type
- acquisition timestamp
- event or publication timestamp
- immutable content hash
- licence and usage status
- evidence lineage
- transformation history
- quality score
- relevance score
- independence score
- conflict indicators
- privacy and safety status
- nodal roles supported
- training eligibility
- validation state

## Temporal discipline

Training and evaluation must follow time order. Future evidence cannot enter an earlier training fold.

For any prediction time `T`:

- training data must precede `T`
- validation data must precede or equal the decision freeze date
- test data must remain unseen until final evaluation
- live submissions must not be used as training labels before their outputs are returned

## Continuous ingestion

Thursday and Sunday technology sweeps create raw research records. BBO weekly inputs and returned outputs create optimisation observations. Experimental nodes create reproducible derived measurements.

All new records enter quarantine first. They become training-eligible only after integrity, duplication, quality, provenance and temporal checks pass.

## Retraining gates

Retraining may be proposed when one or more conditions are met:

- sufficient new validated evidence volume
- statistically meaningful distribution drift
- sustained performance degradation
- new validated nodal capability
- material reduction in compute or energy cost
- explicit scheduled review

Retraining is blocked when:

- provenance is incomplete
- train-test leakage is detected
- source conflicts remain unresolved
- the new dataset reduces independent evidence diversity
- quality gain is not demonstrated

## Continuous learning is not uncontrolled learning

PFRAMOS may continuously collect evidence, but it does not continuously alter production models without validation.

The governing sequence is:

```text
Continuous collection
      ↓
Controlled validation
      ↓
Versioned training candidate
      ↓
Retrospective testing
      ↓
Prospective shadow testing
      ↓
Human approval
      ↓
Production promotion
```

## Governing rule

PFRAMOS continuously expands its evidence base while keeping every production model reproducible, temporally valid and reversible.
