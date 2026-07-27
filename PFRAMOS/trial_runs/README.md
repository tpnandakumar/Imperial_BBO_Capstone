# PACC Trial Runs

## Purpose

This folder contains exploratory, incomplete, failed, shadow and pilot experiments.

Trial evidence is isolated from publication-grade results until every validation and governance gate has passed.

## Permitted contents

- dry-run dataset discovery
- shadow evaluation
- synthetic validation
- architecture tests
- failed experiments
- incomplete manifests
- unapproved dataset candidates
- ablation pilots
- memory and priority simulations

## Required labels

Every trial record must state one of:

- `exploratory`
- `shadow_only`
- `failed`
- `incomplete`
- `awaiting_permission`
- `candidate_for_promotion`

## Promotion gate

A trial may move into publication-grade training results only after it has:

- an approved dataset manifest
- approved licence and access status
- completed privacy and ethics review where applicable
- contamination review
- fixed model and software versions
- a protected test
- reproducible outputs
- PIMF analysis
- PFRAMOS decision record
- PCECE and memory records
- publication evidence assignment

## Separation rule

Trial metrics must never be presented as final measured publication results unless the experiment is formally promoted and its evidence record passes validation.
