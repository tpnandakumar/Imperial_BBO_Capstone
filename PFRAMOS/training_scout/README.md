# PFRAMOS Training Scout

## Purpose

The Training Scout searches GitHub for datasets that may support PFRAMOS schooling, validation, testing and node development.

It does not trust, download or train on a repository merely because it contains data files. Every candidate must pass provenance, licence, integrity, relevance, duplication, privacy, poisoning and temporal checks before entering the Schooling cycle.

## Operating sequence

```text
GitHub discovery
      ↓
Repository and file metadata screening
      ↓
Candidate scoring
      ↓
Manifest creation
      ↓
Download into Schooling/incoming
      ↓
Quarantine and integrity checks
      ↓
Approved Schooling dataset
      ↓
Training, validation and protected testing
      ↓
Dataset removal after audit retention
```

## Search targets

The scout may look for:

- CSV, JSON, JSONL, Parquet and compressed dataset archives
- optimisation traces
- benchmark datasets
- numerical reasoning datasets
- uncertainty and calibration datasets
- robust machine-learning evaluation data
- efficient-computing measurements
- model-routing and mixture-of-experts traces
- reproducible experiment outputs

## Exclusions

The scout must reject or quarantine:

- repositories without an identifiable licence
- unclear redistribution or training rights
- personal, clinical or confidential data without formal approval
- executable archives or opaque binaries
- data with missing provenance
- benchmark test sets likely to contaminate protected evaluation
- repositories with unexplained generated labels
- duplicated datasets presented as independent evidence
- data whose integrity hash changes unexpectedly

## Candidate score

A candidate is scored across:

- source authority
- licence clarity
- dataset relevance
- schema accessibility
- documentation quality
- maintenance recency
- reproducibility
- independence
- estimated download cost
- expected training value
- privacy and safety risk

Discovery score alone never authorises training.

## Download policy

Approved files are downloaded only into an ephemeral Schooling workspace. Git stores the dataset manifest, source commit SHA, file hashes, licence record, schema summary, validation results and deletion record. Large raw datasets should not be committed to the repository.

## Scheduling

Recommended operating pattern:

- daily lightweight scout for new or changed repositories
- Thursday extended discovery sweep
- Sunday candidate validation and dataset freeze
- weekly schooling only after the validated snapshot is approved

## Governing rule

Discover broadly, download selectively, quarantine first, train only on validated evidence and preserve enough metadata to reproduce every schooling session.
