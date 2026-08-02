# Datasheet for the Week 09 BBO Dataset

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- Maintainer: Dr N T Pisharam
- Dataset specification: [DATASET.md](DATASET.md)

## Motivation

This dataset was created to support iterative black box optimisation of eight unknown objective functions. The task is to propose one valid query vector per function, observe the returned scalar value and use the growing evidence base to improve subsequent query selection.

The Week 09 dataset supports three purposes:

1. record the exact submitted queries and returned outputs;
2. make the reasoning behind the next round transparent;
3. preserve a reproducible weekly audit trail of exploration, refinement and exploitation.

## Composition

The dataset contains one Week 09 input vector and one returned output for each of eight hidden functions. Function dimensionality ranges from two to eight variables. Inputs are bounded numeric coordinates and outputs are scalar objective values.

The principal files are described in [DATASET.md](DATASET.md). Derived summaries contain rankings and strategy labels but do not replace the raw records.

## Collection process

Queries were generated using evidence from the preceding eight rounds. Selection was human supervised and combined:

- exploitation of repeatedly productive regions;
- local refinement where performance was stable or improving;
- reassessment where recent outputs declined;
- broader exploration where repeated queries remained uninformative.

For Week 09, Function 5 was treated as the principal exploitation target. Functions 2, 4, 7 and 8 were refined locally. Functions 3 and 6 were reassessed. Function 1 remained the main exploration target because its output was effectively zero.

The exact black box functions were unavailable. Only submitted inputs and returned outputs could be observed.

## Preprocessing

Inputs were checked for:

- correct dimensionality;
- values within `[0,1]`;
- six decimal places for submission;
- one record per function.

Outputs were stored without scaling or imputation. Rankings and strategy labels were added as transparent derived annotations.

## Intended uses

Appropriate uses include:

- analysing Week 09 optimisation performance;
- comparing Week 09 with earlier or later rounds;
- reproducing weekly figures and summaries;
- documenting why Week 10 queries were selected;
- studying exploration and exploitation under limited observations.

## Inappropriate uses

The dataset should not be used to:

- infer the true analytical form of any hidden function;
- claim that a global optimum has been found;
- generalise performance beyond this challenge without qualification;
- treat derived strategy labels as objective ground truth;
- train or validate unrelated models without additional review.

## Known limitations

- The dataset is small and sequential.
- Query points were adaptively selected, so observations are not independent or uniformly sampled.
- Function scales differ substantially.
- The level and source of noise are unknown.
- The hidden functions, gradients and true optima are unavailable.
- Week 09 contains only one new observation per function.

## Assumptions

The analysis assumes that returned outputs correspond correctly to submitted inputs and that larger objective values are preferable. It also assumes that cautious local movement is reasonable in regions with repeated improvement, while broader movement is justified when a region remains uninformative. These assumptions are documented further in [ASSUMPTIONS.md](ASSUMPTIONS.md).

## Distribution and access

The dataset is maintained in the private `tpnandakumar/Imperial_BBO_Capstone` GitHub repository. Access is governed by the repository settings and course requirements. Redistribution outside the permitted educational and research context requires the maintainer's approval.

## Maintenance

The maintainer is Dr N T Pisharam. Corrections should preserve the original raw records, document the reason for change and update the related dataset, model, decision and validation documents in the same development cycle.

## Relationship to the dataset specification

This datasheet explains why and how the data was created. [DATASET.md](DATASET.md) describes the actual files, schemas, record counts and quality checks. The two documents must remain consistent.
