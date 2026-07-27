# Project-Owned Schooling Sources

## Initial sources

PFRAMOS begins with two project-owned corpora:

1. Current Imperial BBO corpus
2. Honeycomb Publications corpus

They are trained in separate lanes before any cross-lane synthesis.

## Current Imperial BBO corpus

Primary uses:

- sequential optimisation
- trajectory learning
- delta and influence analysis
- robustness testing
- P-C4 compute allocation
- emergent-route discovery

Safeguards:

- preserve chronological order
- exclude future outputs
- exclude unsubmitted candidate coordinates
- prevent leakage from protected weeks
- retain exact six-decimal inputs and returned outputs
- compare only against evidence available at each historical decision point

## Honeycomb Publications corpus

Primary uses:

- British English style and consistency
- manuscript organisation
- publishing metadata
- title, subtitle and market-positioning analysis
- narrative continuity and structural reasoning
- bias, representation and sensitivity evaluation
- emergent language and publishing workflows

Safeguards:

- unpublished manuscripts require explicit inclusion
- personal correspondence is excluded
- contracts and financial records are excluded
- third-party copyrighted material requires training permission
- medical and personal information is excluded
- public website copy must be separated from private manuscript material

## Lane separation

```text
Imperial BBO source
        ↓
Optimisation lane
Efficiency lane
Emergence lane
Reasoning lane

Honeycomb Publications source
        ↓
Language and reasoning lane
Bias and representation lane
Emergence lane
```

Shared synthesis is permitted only after each source-specific candidate passes its own protected test.

## Current status

The Imperial BBO source is active because the canonical Weeks 1 to 11 evidence is already present in the PFRAMOS repository.

Honeycomb Publications is authorised but remains pending a verified repository connector and an explicit content inclusion manifest. This prevents private or unpublished material from being ingested accidentally.

## Governing rule

Project ownership authorises consideration, not indiscriminate ingestion. Every record must still pass provenance, privacy, duplication, quality and protected-test controls.
