# PFRAMOS Competition Scout

## Purpose

The Competition Scout identifies official machine-learning competitions that can serve as controlled external schools and examination halls for PFRAMOS.

Competition participation is never assumed to grant unrestricted reuse of data. Every competition is governed by its own rules, licence and permitted-use conditions.

## Candidate classes

- `open_learning`: data may enter the Schooling pipeline if all other checks pass
- `competition_only`: data may be used only inside an isolated competition sandbox
- `restricted`: no training or download beyond what the rules explicitly permit
- `unclear`: quarantine until the rules are resolved

## Protected test rule

Hidden or protected test data must never be added to a training dataset. Leaderboard scores are external evaluation evidence, not labels for reverse engineering.

## Evaluation value

Competition results may contribute evidence on:

- generalisation
- public versus private leaderboard gap
- calibration
- robustness
- runtime
- peak memory
- compute and energy proxies
- submission efficiency
- overfitting to leaderboard feedback

## Submission control

The scout may discover and classify competitions automatically. It must not submit entries automatically unless:

1. the competition rules permit automated submission
2. credentials are stored as protected secrets
3. the exact candidate model and dataset snapshot are frozen
4. submission limits are enforced
5. a human has explicitly approved participation

## Isolation

```text
Competition discovery
        ↓
Rules and licence review
        ↓
Use classification
        ↓
Open learning ─────────→ Schooling quarantine
Competition only ─────→ Isolated sandbox
Restricted or unclear → Quarantine
        ↓
External validation
        ↓
Permanent result manifest
```

## Governing principle

Use competitions to test capability under independent rules, not to contaminate protected benchmarks or bypass data-use restrictions.
