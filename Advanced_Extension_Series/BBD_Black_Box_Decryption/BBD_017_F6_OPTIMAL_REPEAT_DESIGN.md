# BBD 017: F6 Optimal Repeat Experiment Design

## Purpose

BBD 016 quantified the observed F6 repeatability scale at approximately `sigma = 0.046738`. BBD 017 converts that uncertainty estimate into a prospective experimental protocol.

This stage does not invent new black-box outputs. It specifies which coordinates should be repeated, how often they should be repeated, and how the sequence should be arranged if independent evaluator access becomes available.

## Experimental question

Can the non-identical F6 outputs at identical coordinates be separated into ordinary repeat variation, temporal drift, or a reproducible hidden-state shift?

## Fixed-coordinate anchors

The design deliberately starts with the two coordinates for which the thirteen-round history already contains direct repeatability evidence.

**Anchor A**

`0.700000-0.200000-0.700000-0.700000-0.200000`

Historical repeats: 3. Historical range: approximately `0.100675`.

**Anchor B**

`0.240000-0.760000-0.240000-0.820000-0.280000`

Historical repeats: 2. Historical range: approximately `0.053585`.

Using historical repeat anchors avoids confusing coordinate extrapolation with repeatability.

## Recommended Stage 1

Run **20 independent F6 evaluations**, comprising **10 repeats at Anchor A and 10 repeats at Anchor B**.

Use balanced interleaved blocks:

`A, B | B, A | A, B | B, A ...`

for ten two-evaluation blocks.

This structure is preferable to completing all A evaluations followed by all B evaluations because coordinate identity is then less confounded with evaluation order. The block structure also permits descriptive tests for drift and block effects.

## Analysis plan

For each anchor estimate:

- mean and standard deviation;
- 95% confidence interval for the mean;
- within-anchor variance;
- early-versus-late mean difference;
- residual association with evaluation order;
- block effect;
- variance ratio between anchors.

Pool variance only if the anchor-specific variances are reasonably compatible. If variability differs materially between A and B, retain a heteroscedastic representation.

## Hidden-state follow-up

A controlled state/context experiment should only be attempted if a reproducible candidate state can be defined independently of the F6 output.

Using the BBD 016 variance estimate, approximate 90% power requires:

- shift `0.10`: 5 repeats per state;
- shift `0.075`: 9 repeats per state;
- shift `0.05`: 19 repeats per state;
- shift `0.025`: 74 repeats per state.

A practical first hidden-state target is therefore a shift of at least `0.075`.

## Decision logic

If repeated outputs collapse to a very narrow distribution, revisit whether historical variation came from changing evaluator conditions.

If stable non-zero variance persists at both anchors without order or block structure, a stochastic or unrecorded-context component becomes more plausible.

If output changes systematically with order or block despite fixed coordinates, test temporal drift explicitly.

If a pre-specified external state reproducibly shifts the fixed-coordinate mean beyond repeat variance, hidden-state dependence gains direct support.

## Evidence boundary

BBD 017 is an **experimental design**, not an executed validation. No synthetic value produced by this protocol is to be labelled as an Imperial observation. Exact F6 recovery remains false until independent black-box evaluations are available.
