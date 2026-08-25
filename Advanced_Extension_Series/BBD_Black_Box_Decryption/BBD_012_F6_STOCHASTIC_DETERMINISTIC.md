# BBD 012: F6 Stochastic-versus-Deterministic Decomposition

## Purpose

BBD 010 and BBD 011 established two facts about F6. First, a coordinate-only Gaussian Process gives the strongest forward prediction among the tested static and state-aware mechanisms. Second, identical F6 coordinates can return different outputs, so exact coordinate-only determinism cannot explain every recorded observation.

BBD 012 asks what kind of residual process remains after the static surface has been removed.

## Competing residual explanations

The experiment compares three small-sample stochastic models fitted to the chronological static-GP residual sequence:

1. independent Gaussian residuals with constant mean and variance;
2. first-order autoregressive Gaussian residuals, where the current residual may depend on the previous residual;
3. heteroscedastic Gaussian residuals whose variance changes with the Gaussian Process predictive uncertainty.

The comparison uses AICc rather than training fit alone because the residual sequence is very short and extra parameters must be penalised heavily.

## Determinism test

Repeated coordinates are analysed separately. If an identical coordinate has different observed outputs, an exact deterministic rule of the form `y = f(x)` is falsified for the recorded data unless there is unobserved state, stochasticity or evaluator variation.

This does not prove that the underlying objective itself is stochastic. It proves only that the observable coordinate vector is insufficient to reproduce every recorded output exactly.

## Conservative interpretation rule

Because there are only eight walk-forward residuals, BBD 012 does not label a stochastic family as established unless it clearly separates from the next-best tested model. A difference of at least four AICc units is used as a tentative, not definitive, preference threshold.

## Outputs

Running `bbd_012_f6_stochastic_deterministic.py` creates:

- `outputs/BBD_012_F6_RESIDUAL_SEQUENCE.csv`
- `outputs/BBD_012_F6_STOCHASTIC_MODEL_COMPARISON.csv`
- `outputs/BBD_012_F6_REPEAT_DETERMINISM.csv`
- `outputs/BBD_012_F6_STOCHASTIC_DETERMINISTIC_SUMMARY.csv`

## Evidence boundary

BBD 012 remains a post-capstone system-identification experiment. The sample is too small to infer the exact stochastic law of F6. The purpose is to eliminate unsupported explanations and state the strongest remaining mechanism with an explicit uncertainty boundary.
