# Weekly Dataset and Datasheet Standard

**Document ID:** BBO-DOC-STD-001  
**Version:** 1.0  
**Maintainer:** Dr N T Pisharam

## Purpose

Every optimisation week must contain both a `DATASET.md` and a `DATASHEET.md`.

The two documents serve different but complementary purposes:

- `DATASET.md` explains **what the weekly dataset contains**, where each file is located, how the files relate to one another, and how the data should be read.
- `DATASHEET.md` explains **why the data was created**, how it was collected, what assumptions and limitations apply, how it may be used, and who maintains it.

Each document must explicitly refer to the other so that the technical contents and the contextual explanation remain connected.

## Mandatory weekly structure

```text
Week_XX/
├── README.md
├── DATASET.md
├── DATASHEET.md
├── week_XX_inputs.csv
├── week_XX_results.csv
├── week_XX_analysis_summary.csv          # where available
├── week_XX_figure_data_summary.csv       # where available
├── week_XX_analysis.py
├── generate_week_XX_figures.py
└── figures/
```

## DATASET.md requirements

`DATASET.md` must include:

1. Week identifier and optimisation round.
2. Exact list of files forming the dataset.
3. Number of functions, records and dimensions.
4. Column definitions for each CSV file.
5. Input formatting rules and value ranges.
6. Output interpretation and scale warnings.
7. Missing values, gaps or known inconsistencies.
8. Relationship between raw data, derived summaries and figures.
9. Reproduction instructions.
10. A direct cross-reference to `DATASHEET.md`.

Required statement:

> For motivation, provenance, collection strategy, assumptions, limitations, intended uses and maintenance, see `DATASHEET.md`.

## DATASHEET.md requirements

`DATASHEET.md` must include:

1. Motivation.
2. Composition.
3. Collection process.
4. Preprocessing and transformations.
5. Intended uses.
6. Inappropriate uses.
7. Assumptions and limitations.
8. Distribution and access.
9. Maintenance and versioning.
10. A direct cross-reference to `DATASET.md`.

Required statement:

> For the exact files, schemas, record counts and reproduction instructions, see `DATASET.md`.

## Update rule

Both documents must be updated in the same commit whenever weekly inputs, outputs, summaries or figures are added or corrected.

A weekly folder is not considered complete until:

- `DATASET.md` matches the files actually present;
- `DATASHEET.md` accurately describes how and why the data was produced;
- both documents cross-reference one another;
- the weekly `README.md` links to both documents.

## Quality standard

All documentation must use British English, avoid unsupported claims, distinguish observed results from interpretation, and preserve a clear audit trail through Git history.
