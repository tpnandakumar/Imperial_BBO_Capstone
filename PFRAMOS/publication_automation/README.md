# Automatic PFRAMOS Publication Pipeline

## Purpose

The publication automation layer routes validated training results into the correct paper track without mixing the ownership of scientific claims.

## Automatic sequence

```text
New training result
        ↓
Evidence completeness check
        ↓
Primary paper assignment
        ↓
Secondary relevance tagging
        ↓
Duplicate-claim and scope check
        ↓
Paper evidence register
        ↓
Candidate manuscript update
        ↓
Internal review gate
        ↓
Submission-readiness assessment
```

## Automatic actions

The system may automatically:

- detect new training-result records
- classify the training lane and data form
- assign one primary paper owner
- tag relevant secondary papers
- block incomplete or non-reproducible evidence
- identify mixed-scope manuscripts
- generate an evidence-routing report
- maintain a paper-specific evidence register
- identify sections that now have supporting evidence
- flag missing baselines, tests, references or disclosures

## Actions requiring human approval

The system must not automatically:

- invent results or narrative
- declare a scientific claim proven
- move a paper to submission-ready without internal review
- name authors or affiliations without approval
- release private BBO candidates or unpublished manuscripts
- submit to a journal
- accept licence or copyright terms

## Paper ownership rule

Every result has one primary paper owner. Other papers may cite or discuss the result as secondary evidence, but they must not independently present it as a new primary finding.

## Status flow

```text
no_evidence
    ↓
candidate
    ↓
under_internal_review
    ↓
submission_ready
    ↓
submitted
    ↓
revision_or_decision
```

`submission_ready` remains a human-controlled state.
