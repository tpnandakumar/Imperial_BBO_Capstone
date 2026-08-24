# Datasheet for Week XX BBO Data

**Document ID:** BBO-WXX-DS  
**Version:** 1.0  
**Status:** Draft / Submitted / Processed / Final  
**Maintainer:** Dr N T Pisharam

## 1. Motivation

Why was this weekly dataset created? What optimisation task and decision does it support?

## 2. Composition

Describe the functions, input dimensions, number of queries, returned objective values, derived summaries and figures included for this week.

For the exact files, schemas, record counts and reproduction instructions, use the companion `DATASET.md` created in the instantiated weekly folder.

## 3. Collection process

Explain:

- how candidate queries were generated;
- which exploration, refinement or exploitation strategy was used;
- what evidence from previous rounds informed the choices;
- the submission and processing dates;
- whether any outputs were pending, corrected or resubmitted.

## 4. Preprocessing and transformations

State any formatting, rounding, normalisation, ranking, delta calculation, aggregation or figure preparation applied to the raw portal data. Clearly distinguish raw observations from derived interpretation.

## 5. Intended uses

Examples:

- weekly performance comparison;
- surrogate modelling;
- exploration versus exploitation analysis;
- uncertainty assessment;
- transparent justification of subsequent queries;
- reproduction of weekly figures and summaries.

## 6. Inappropriate uses

The data must not be treated as:

- a complete representation of any hidden objective function;
- proof that a local optimum is global;
- independent and identically distributed samples;
- directly comparable across functions without accounting for scale;
- suitable for unrelated general-purpose modelling without additional validation.

## 7. Assumptions and limitations

Document hidden-function uncertainty, sparse sampling, adaptive query selection, dimensionality, scale differences, possible noise, pending outputs and any assumptions used in interpretation.

## 8. Distribution and access

State the repository path, visibility, permitted use, citation expectations and whether any files contain restricted or personal information.

## 9. Maintenance and versioning

Identify the maintainer, update triggers and version history. The datasheet and dataset manifest must be revised together whenever weekly data changes.

## 10. Decision transparency

Summarise how the evidence influenced the next query choice using this chain:

```text
Observation -> Interpretation -> Confidence -> Decision -> Query -> Validation
```
