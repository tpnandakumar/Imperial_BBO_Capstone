# PFRAMOS Technology Sweep, Nodal Recruitment and Integration Module

## Purpose

This module continuously scans high-quality AI, machine learning, large language model and deep learning research sources, identifies potentially useful techniques, and recruits promising methods as quarantined experimental nodes.

It does not automatically integrate any discovered technique into production PFRAMOS logic.

## Source hierarchy

Priority is given to:

1. peer-reviewed journals and conference proceedings
2. official preprint repositories
3. official research laboratory publications
4. recognised standards and benchmark organisations
5. reputable university repositories

Initial machine-readable sources include arXiv categories relevant to AI, ML, LLMs, NLP, computer vision and statistical learning. Additional adapters can be added for OpenReview, JMLR, TMLR, Nature Machine Intelligence and other primary sources.

## Recruitment lifecycle

```text
Discovered
    ↓
Screened
    ↓
Quarantined Candidate
    ↓
Experimental Node
    ↓
Retrospective Validation
    ↓
Controlled Prospective Validation
    ↓
Approved Recruitment
    ↓
Integrated Node
```

A paper can also be rejected, deferred, deprecated, retired or archived.

## Recruitment gates

Each candidate is scored for:

- relevance to PFRAMOS
- novelty
- technical maturity
- reproducibility
- evidence quality
- transferability
- computational cost
- energy implications
- safety and failure modes
- duplication with existing nodes

No candidate can move beyond quarantine without a traceable source, explicit rationale, implementation plan and validation protocol.

## Integration policy

The module may:

- propose a new node
- propose an extension to an existing node
- propose a benchmark or validation test
- propose a computational optimisation
- propose a coherence or robustness improvement

The module may not:

- alter production candidate generation automatically
- change a submitted BBO record
- activate an experimental node in live optimisation
- suppress contradictory research
- convert popularity into evidence quality

## Outputs

- `outputs/public/tech_sweep/latest_discoveries.json`
- `outputs/public/tech_sweep/recruitment_summary.json`
- `outputs/private/tech_sweep/recruitment_candidates.json`
- append-only learning log entries

## Schedule

The GitHub workflow runs weekly on Wednesday and can also be triggered manually.
