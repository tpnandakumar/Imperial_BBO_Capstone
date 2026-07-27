# Journal-Specific Formatting Guide

## Principle

Each paper must be written first as a scientifically complete master manuscript, then rendered into the exact format required by the target journal.

The master manuscript must not be manually distorted to fit one journal. Journal-specific formatting belongs in a separate rendering profile.

## Required workflow

```text
Master scientific manuscript
        ↓
Publication cleaner
        ↓
Journal profile selection
        ↓
Template and section mapping
        ↓
Anonymity and disclosure checks
        ↓
Reference, figure and table checks
        ↓
Journal-specific PDF
        ↓
Human submission approval
```

## TMLR profile

For Transactions on Machine Learning Research:

- use the official TMLR LaTeX style file and template
- do not alter fonts, spacing or layout
- submit an anonymised PDF
- maintain double-blind anonymity in the manuscript and supplement
- use OpenReview for submission
- include appendices after the references where needed
- keep supplementary material within the journal limit and in PDF or ZIP form
- anonymise code, data and repository links used during review
- include broader-impact discussion where material risks exist
- verify originality and prevent reuse of archival text, figures or results
- ensure all authors have complete active OpenReview profiles
- retain author responsibility for all content, including any LLM-assisted drafting

## Journal rendering folders

```text
PFRAMOS/publishable_papers/journal_formats/
├── tmlr/
│   ├── source/
│   ├── figures/
│   ├── tables/
│   ├── references/
│   ├── supplement/
│   ├── anonymised_review/
│   └── accepted_version/
└── future_journals/
```

## Master-to-journal section mapping

| Master section | TMLR rendering |
|---|---|
| Title and authors | Anonymous title at review stage |
| Structured abstract | Journal abstract |
| Introduction | Introduction |
| Literature review | Related Work or integrated background |
| Methodology | Method or Approach |
| Data and provenance | Data, Experimental Setup or Appendix |
| Results | Experiments and Results |
| Discussion | Discussion |
| Limitations | Limitations |
| Ethics and impact | Broader Impact Statement where required |
| References | TMLR bibliography |
| Extended methods | Appendix or anonymised supplement |

## Formatting safeguards

Every journal-rendered manuscript must pass:

- em-dash and en-dash removal
- explicit AI-marker audit
- British English review unless the journal explicitly requires another convention
- anonymity scan
- reference completeness and DOI verification
- figure resolution and caption audit
- table value traceability
- page, file type and supplement-size checks
- template integrity check
- journal-policy freshness check

## Freshness requirement

Journal policies can change. The official journal instructions must be checked again immediately before submission. The verification date must be recorded in the manuscript manifest.

## Legal and submission boundary

Automation may prepare, validate and package the files. It must not accept copyright or licence terms, confirm authorship, disclose conflicts, or submit the paper without explicit human approval.
