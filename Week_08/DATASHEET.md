# Week 08 Datasheet

## Metadata

- **Course module:** 20
- **Capstone week:** 08
- **Optimisation round:** 8
- **Datasheet version:** 08.1
- **Related dataset description:** [DATASET.md](DATASET.md)
- **Maintainer:** Dr N T Pisharam
- **Repository:** `tpnandakumar/Imperial_BBO_Capstone`

## 1. Motivation

The Week 08 dataset was created to document the eighth round of the Bayesian Black Box Optimisation capstone challenge. It supports the task of selecting one query for each of eight hidden objective functions while progressively improving performance under a limited query budget and incomplete knowledge of the search landscape.

By Week 08, seven earlier optimisation rounds had been completed. The Week 08 data were therefore intended not only to record a further submission, but also to test whether previously identified productive regions continued to improve and whether uncertain functions required broader exploration or local refinement.

## 2. Composition

The dataset contains:

- one Week 08 query for each of eight functions;
- one returned objective value for each function;
- comparisons with Week 07 and earlier rounds;
- derived rankings and change measures;
- strategy classifications for exploration, refinement and exploitation;
- Python scripts supporting analysis and figure generation;
- narrative interpretation in `README.md`.

The exact file-level description is maintained in [DATASET.md](DATASET.md).

The function dimensions range from 2 to 8 variables. Query values are constrained to `[0,1]` and specified to six decimal places. The returned objective values differ substantially in scale, which limits direct comparison across functions without contextual interpretation.

## 3. Collection process

Queries were generated sequentially using evidence accumulated during Weeks 01 to 07. The selection process considered:

- the best-known objective values;
- recent direction and magnitude of change;
- stability across repeated observations;
- uncertainty within the local region;
- the risk of premature convergence;
- the expected information value of a new query;
- the need to preserve exploration for poorly understood functions.

The Week 08 strategy was function-specific:

- **F5:** continued exploitation because it consistently produced the strongest outputs.
- **F2, F7 and F8:** targeted local refinement within productive regions.
- **F3, F4 and F6:** cautious refinement to improve understanding of negative regions.
- **F1:** broader exploration because repeated near-zero outputs provided little evidence of a productive local region.

The returned outputs were supplied by the capstone black box and then entered into the structured result files for analysis.

## 4. Preprocessing and transformations

The raw submitted coordinates and returned outputs were preserved as the primary record. Processing was limited to analytical transformations such as:

- validating dimensionality and numeric precision;
- matching each result to its function and query;
- calculating changes from Week 07 to Week 08;
- ranking functions by observed output;
- assigning exploration, refinement or exploitation categories;
- preparing figure data and narrative summaries.

No transformation was used to alter the underlying objective values. Negative values and very small scientific-notation values were retained rather than normalised away.

## 5. Decision rationale and assumptions

The Week 08 approach depended on several explicit assumptions:

1. Recent local improvement may indicate a productive neighbouring region.
2. Stable high outputs justify cautious exploitation, but do not prove global optimality.
3. Repeated weak or near-zero outputs justify broader exploration.
4. A single decline does not necessarily invalidate a previously productive region.
5. Query budget should be allocated according to evidence and uncertainty rather than equally across functions.
6. Different output scales require function-specific interpretation.

These assumptions should be reviewed whenever later observations contradict the Week 08 interpretation.

## 6. Intended uses

Appropriate uses include:

- documenting the Week 08 submission and response;
- reproducing the Week 08 analysis;
- comparing sequential optimisation rounds;
- explaining the rationale for Week 09 query selection;
- studying exploration and exploitation under black box constraints;
- supporting transparent and interpretable capstone reporting.

## 7. Inappropriate uses

The dataset should not be used to:

- claim that any global optimum has been proven;
- infer the hidden objective equations;
- compare raw outputs across functions without considering scale;
- draw causal conclusions from sequential observations;
- generalise results to unrelated optimisation problems without validation;
- remove unfavourable observations solely to improve the apparent trajectory.

## 8. Distribution and access

The dataset is maintained in the private GitHub repository `tpnandakumar/Imperial_BBO_Capstone`. Access is controlled by the repository owner. Any redistribution must preserve authorship, provenance, file relationships and the limitations described here.

## 9. Maintenance

The repository owner is responsible for:

- preserving the original Week 08 records;
- correcting documented errors through traceable commits;
- keeping `DATASET.md` and `DATASHEET.md` consistent;
- retaining reproducible scripts and figures;
- recording any reinterpretation prompted by later rounds.

The dataset and datasheet should be updated together whenever Week 08 files, assumptions or interpretations change.

## 10. Relationship to the dataset document

This datasheet explains why and how the Week 08 data were created, together with their assumptions, limitations and permitted uses. The reciprocal [DATASET.md](DATASET.md) explains the concrete files, schemas, values, relationships and reproduction procedure.

```text
DATASHEET.md
Context, rationale, assumptions and governance
        ↕
DATASET.md
Files, values, structure and reproduction
```
