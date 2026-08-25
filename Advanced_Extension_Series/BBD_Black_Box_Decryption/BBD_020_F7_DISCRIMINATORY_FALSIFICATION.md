# BBD 020: F7 Discriminatory Falsification Design

## Purpose

BBD 019 showed that F7 is best reconstructed locally by the full 27-term quadratic model, with normalised chronological walk-forward MAE of approximately `0.03487`. BBD 020 now asks the more demanding question: where do the surviving F7 explanations disagree most strongly?

The aim is falsification, not another retrospective fit.

## Competing explanations

The experiment compares five distinct F7 mechanisms fitted to the full thirteen-round history:

- the BBD 019 27-term quadratic ridge candidate;
- a simple linear ridge surface;
- a Matérn 2.5 Gaussian Process;
- the strongest available SOC model fitted to F7;
- the Rosenbrock-like benchmark candidate identified in BBD 005.

## Query search

A scrambled Sobol design explores the six-dimensional unit cube and is supplemented by all corners. Candidate points are scored by:

1. prediction standard deviation across the competing models;
2. maximum prediction spread;
3. novelty relative to the historical F7 coordinates.

Queries are then separated spatially so that the final list contains genuinely different falsification experiments rather than several near-duplicates.

## Interpretation

A high-scoring point is one where the current models make substantially different predictions. A genuine black-box output at such a point would have much greater evidential value for function identification than another small move near the historical optimisation path.

If the observed output agrees closely with the quadratic while rejecting the other models, confidence in the BBD 019 mechanism should increase.

If the quadratic fails while another model succeeds, the 27-term expression should be treated as a local interpolation of the sampled trajectory rather than a candidate generating function.

## Evidence boundary

BBD 020 produces prospective coordinates and model predictions only. It does not create or infer Imperial outputs for those coordinates. Exact F7 recovery remains false until independent evaluator observations are available.
