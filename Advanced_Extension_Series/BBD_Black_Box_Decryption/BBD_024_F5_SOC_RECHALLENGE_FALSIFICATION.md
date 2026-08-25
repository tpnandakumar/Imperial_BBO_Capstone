# BBD 024: F5 Direct SOC Rechallenge and Discriminatory Falsification

## Purpose

BBD 023 found that a dedicated Matérn 2.5 Gaussian Process predicted the historical F5 trajectory more accurately than the earlier general BBD and SOC comparisons. BBD 024 tests that result under a direct same-protocol contest and then converts the remaining model disagreement into prospective falsification coordinates.

## Direct rechallenge

The BBD 023 winning Matérn 2.5 model is compared against the full SOC model library using the same chronological walk-forward protocol. Each model trains only on observations available before the test week. Testing begins after five historical observations and produces eight forward predictions.

This removes a major source of ambiguity from the earlier BBD 007 comparison because the dedicated F5 model and SOC alternatives now face the same train-test sequence.

## Falsification roster

The prospective identification stage retains:

- the BBD 023 Matérn 2.5 Gaussian Process;
- the BBD 023 quadratic ridge approximation;
- the strongest SOC alternatives under the direct rechallenge.

The models are fitted to all available historical F5 observations only after the chronological competition has been completed.

## Query search

A Sobol design samples the four-dimensional unit hypercube, with additional corners and boundary-near candidates. For each candidate coordinate the experiment measures:

- prediction standard deviation across the finalist models;
- full prediction spread;
- distance from the nearest historical F5 coordinate;
- a combined discrimination score that rewards both disagreement and novelty.

The highest scoring spatially diverse points form a sequential falsification queue. They are proposed experiments, not returned Imperial outputs.

## Interpretation rule

A future black-box result close to the Matérn prediction would strengthen the smooth local-surface interpretation. A result closer to the quadratic or another SOC alternative would weaken it. The most informative observation is therefore not necessarily the coordinate expected to maximise F5, but the coordinate at which plausible mechanisms make sharply different predictions.

## Evidence boundary

BBD 024 can establish which candidate model currently predicts the observed chronology best and can define efficient falsification experiments. It cannot establish the exact original F5 generating equation without independent black-box responses at discriminatory coordinates.

`exact_function_recovered = False`
