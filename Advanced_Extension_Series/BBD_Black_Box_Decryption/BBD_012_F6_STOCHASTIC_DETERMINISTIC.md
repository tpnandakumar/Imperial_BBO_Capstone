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

## Results

The heteroscedastic model was the strongest of the three tested residual mechanisms:

| Residual model | AICc |
|---|---:|
| Heteroscedastic, variance linked to GP uncertainty | **-20.8270** |
| Independent Gaussian | -11.0242 |
| AR(1) Gaussian | -8.9018 |

The AICc gap from the best model to the second-best model was approximately **9.80**, which meets the experiment's threshold for a tentative preference. The estimated heteroscedastic coefficient was negative, meaning the fitted residual variance decreased as the standardised GP uncertainty increased over this very small residual sample. That direction is counter-intuitive and therefore should not be over-interpreted as a physical mechanism.

The direct Spearman association between absolute residual size and GP predictive standard deviation was only `-0.357` with `p = 0.385`. The lag-one residual correlation was approximately `-0.082`. These diagnostics do not support a strong simple autoregressive explanation and do not independently confirm the heteroscedastic mechanism.

## Determinism test

F6 contains two repeated-coordinate groups with non-identical outputs. Therefore an exact deterministic rule of the form `y = f(x)` is falsified for the recorded observations unless there is unobserved state, evaluator variation or stochasticity.

This does not prove that the underlying objective itself is stochastic. It shows that the observable five-coordinate vector alone is insufficient to reproduce every recorded F6 output exactly.

## Current interpretation

The strongest current representation is:

`observed F6 = static coordinate-dependent surface + unresolved non-constant residual process`

The residual process is **tentatively heteroscedastic among the three models tested**, but the sample contains only eight walk-forward residuals. The earlier BBD 011 short-memory improvement remains useful predictive evidence, while BBD 012 shows that a simple AR(1) likelihood model is not the strongest global residual description.

Exact function recovery remains false.

## Outputs

Running `bbd_012_f6_stochastic_deterministic.py` creates:

- `outputs/BBD_012_F6_RESIDUAL_SEQUENCE.csv`
- `outputs/BBD_012_F6_STOCHASTIC_MODEL_COMPARISON.csv`
- `outputs/BBD_012_F6_REPEAT_DETERMINISM.csv`
- `outputs/BBD_012_F6_STOCHASTIC_DETERMINISTIC_SUMMARY.csv`

## Evidence boundary

BBD 012 remains a post-capstone system-identification experiment. The sample is too small to infer the exact stochastic law of F6. The result narrows the surviving explanations but still requires an independent black-box evaluation before any exact decryption claim can be made.
