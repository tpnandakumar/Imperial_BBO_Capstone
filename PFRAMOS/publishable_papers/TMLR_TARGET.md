# Primary Journal Target: Transactions on Machine Learning Research

## Target paper

**Provisional title**

PFRAMOS: A Fit-Regulated, Agreement-Guided Multinodal Framework for Auditable Sequential Optimisation

## Why TMLR

TMLR is the primary target because its scope includes:

- new algorithms with sound empirical validation
- experimental studies of the design and behaviour of learning systems
- applications that reveal strengths and weaknesses of methods
- new performance-assessment methods
- analytical frameworks for practical learning methods

The central acceptance test is whether the claims are supported by accurate, convincing and clear evidence, and whether some members of the TMLR audience would be interested in the findings. A new state-of-the-art result is not required.

## Current submission requirements

- double-blind anonymised manuscript
- active OpenReview profiles for all authors
- mandatory TMLR LaTeX template and style file
- original work with no prohibited dual submission
- funding, competing-interest and conflict disclosures
- ethical and societal impact consideration
- anonymised supplementary material
- reproducibility material encouraged
- accepted and submitted material licensed under CC BY 4.0
- authors remain responsible for all content, including material prepared with LLM assistance

## Primary contribution

The first paper will evaluate whether PFRAMOS improves auditable sequential optimisation through:

- fit regulation
- agreement-guided multinodal decision-making
- coherence-based active-path selection
- Dynamic Temporary Terminal Active Nodes
- robustness and uncertainty gating
- P-C4 cost-conscious computation
- emergent-route and laminar-conduit analysis

## Evidence boundary

The paper must not claim that PFRAMOS is superior until reproducible comparisons demonstrate superiority on protected evaluations.

The initial BBO history provides a case study, not sufficient evidence of broad generalisation by itself. Independent datasets and baseline methods are required.

## Required baseline families

- established BBO strategy used in the project
- random or quasi-random search
- Gaussian-process Bayesian optimisation where applicable
- HEBO where technically and legally reproducible
- one or more modern alternative optimisers appropriate to the data form
- ablated PFRAMOS variants

## Required study stages

1. Freeze a named PFRAMOS experimental version.
2. Pre-specify the primary hypothesis and outcome.
3. Build independent benchmark datasets and protected test splits.
4. Reproduce baseline methods.
5. Run ablation studies.
6. Measure quality, robustness, calibration, compute and energy proxies.
7. Test bias, contamination and temporal leakage.
8. Conduct prospective or shadow validation.
9. Generate a complete reproducibility package.
10. Prepare the anonymised TMLR manuscript and supplement.

## Publication rule

The manuscript moves to `submission_ready` only when every quantitative claim resolves to a training-result record, dataset manifest, code version and immutable training-log hash.
