# BBD 022: F8 Direct SOC Rechallenge and Discriminatory Falsification

## Purpose

BBD 021 found that F8 is predicted extremely well by a simple linear model under chronological walk-forward testing. The normalised MAE was approximately `0.016539`, substantially better than the earlier BBD 007 result. BBD 022 therefore reruns the SOC model families under the same chronological protocol and then defines high-value falsification coordinates.

This stage has two separate questions.

1. Does the F8 linear model still win when SOC models are evaluated on the identical walk-forward splits?
2. Where do the strongest surviving models disagree enough for a new evaluator observation to distinguish them?

## Direct same-protocol rechallenge

The thirteen F8 observations are ordered by week. Each model is trained only on observations available before the test week, beginning after five training observations. Eight later observations are therefore predicted prospectively within the historical sequence.

The BBD candidate is the BBD 021 ordinary linear model. The SOC roster is imported from the existing SOC surrogate engine and includes Gaussian-process, tree-ensemble and distance-weighted nearest-neighbour models available for this sample size.

All models are evaluated with the same train/test chronology and the same response-range normalisation. This removes the protocol mismatch that limited interpretation of the earlier BBD 007 comparison.

## Discriminatory falsification search

After the direct rechallenge, the BBD linear model and the three strongest SOC families are fitted to all thirteen historical F8 observations. A scrambled Sobol design samples the eight-dimensional unit cube and is supplemented with all binary corners.

Candidate coordinates are scored using:

- model prediction dispersion;
- maximum prediction spread;
- novelty relative to the thirteen historical F8 coordinates.

The final query list is spatially separated so that it contains distinct experiments rather than near-duplicate points.

## Interpretation

If the BBD linear model wins the direct same-protocol challenge, the earlier BBD 007 loss can be attributed more plausibly to the earlier general-purpose reconstruction protocol rather than to a failure of the linear hypothesis itself.

Even a decisive historical walk-forward win does not establish the exact hidden equation. A linear model can remain locally excellent while diverging from a nonlinear function elsewhere in the unit cube. The discriminatory queries are therefore the required next test.

A genuine black-box output close to the linear prediction at a point where the SOC finalists predict very different values would strengthen the linear generating-function hypothesis. A result favouring a nonlinear SOC model would instead show that the compact equation is a strong local reconstruction.

## Evidence boundary

BBD 022 does not fabricate outputs for the proposed discriminatory coordinates. The generated values are model predictions only. Exact F8 recovery remains false until independent evaluator observations are available at sufficiently discriminatory points.
