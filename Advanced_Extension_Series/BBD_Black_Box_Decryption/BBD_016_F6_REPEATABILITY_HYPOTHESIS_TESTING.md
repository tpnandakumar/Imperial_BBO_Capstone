# BBD 016: F6 Repeatability Hypothesis Testing

## Purpose

BBD 015 showed that the repeated-coordinate anomaly in F6 is real in the recorded history but is not explained by the sequence or same-round context variables we reconstructed. BBD 016 therefore formalises the competing explanations and asks what additional repeat evidence would be required to separate them.

## Competing hypotheses

### H0: exact coordinate-only determinism

Under this hypothesis, an identical coordinate must return an identical output:

\[
y=f(\mathbf{x}).
\]

Because F6 contains identical coordinates with different recorded outputs, exact coordinate-only determinism is falsified for the observed record unless the evaluator itself introduces measurement or numerical variation.

### H1: static surface plus independent repeat variation

\[
y=f(\mathbf{x})+\varepsilon, \qquad \varepsilon\sim N(0,\sigma^2).
\]

The within-coordinate repeat variance is estimated by pooling the two repeated F6 coordinate groups. This model is treated as a repeatability description, not proof that the evaluator is genuinely stochastic.

### H2: static surface plus hidden state

\[
y=f(\mathbf{x})+h(z)+\varepsilon,
\]

where \(z\) is an unrecorded evaluator state or context. BBD 015 did not identify such a state from the variables available in the thirteen-round history. H2 therefore remains possible but unproven.

## Tests performed

BBD 016 calculates:

- the pooled within-coordinate repeat standard deviation;
- all pairwise differences between identical-coordinate evaluations;
- each difference expressed in units of the repeat-difference standard deviation expected under an iid Gaussian variation model;
- two-sided tail probabilities under that descriptive iid model;
- the number of repeats required to estimate a coordinate mean to selected 95% confidence half-widths;
- the number of evaluations required per state or context to detect specified hidden-state shifts with 80% and 90% power.

## Interpretation boundary

The current repeat sample is extremely small. There are only two repeated-coordinate groups, five repeated observations and four repeat pairs. Therefore the pooled variance estimate is uncertain and the power calculations are planning calculations, not validated properties of the Imperial evaluator.

Compatibility with an iid variation model does not prove stochasticity. It means only that the observed repeat discrepancies are not unexpectedly large relative to the pooled repeat variance estimated from the same limited data.

## Outputs

Running `bbd_016_f6_repeatability_hypothesis_testing.py` creates:

- `outputs/BBD_016_F6_REPEAT_GROUP_SUMMARY.csv`
- `outputs/BBD_016_F6_PAIRWISE_REPEAT_TESTS.csv`
- `outputs/BBD_016_F6_REPEAT_PRECISION_DESIGN.csv`
- `outputs/BBD_016_F6_STATE_SHIFT_POWER_DESIGN.csv`
- `outputs/BBD_016_F6_REPEATABILITY_HYPOTHESIS_SUMMARY.csv`

## Decision rule

BBD 016 does not declare F6 stochastic simply because repeated outputs differ. The strongest defensible statement remains:

\[
Y_{F6}=f(\mathbf{x})+\varepsilon_{\text{unresolved}},
\]

with exact coordinate-only determinism falsified for the recorded observations and the source of the remaining variation still unidentified.

An independent repeat experiment at deliberately fixed coordinates is required to distinguish stable repeat noise from a deterministic hidden-state mechanism.
