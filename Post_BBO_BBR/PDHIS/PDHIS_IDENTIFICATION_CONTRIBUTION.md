# PDHIS identification contribution

## Positive development

Pisharam Delta Hierarchy and Influence State (PDHIS) provides a formal method for extracting mathematical behaviour from an observed sequence when the generating equation is unknown. It identifies the Signature of Change through recursive Delta orders and measurable temporal characteristics.

The contribution is not limited to forecasting. PDHIS separates four questions that are often confused:

1. What mathematical behaviour is present in the completed sequence?
2. Which characteristics distinguish direction, acceleration, reversal, persistence, oscillation, recovery and stabilisation?
3. Which retrospective characteristics are associated with known events?
4. Which characteristics remain sufficiently stable to test as prospective indicators?

## What PDHIS identified in BBO

Across F1 to F8, PDHIS identified function-specific retrospective behaviour. The hierarchy distinguished stable retention, localised movement, progressive improvement, overshoot, deterioration, recovery, repeated-coordinate stability and unresolved variability.

The formal state combines:

- first-order to tenth-order Delta
- sign reversal and oscillation frequency
- oscillation energy
- temporal dispersion
- directional persistence
- cross-order coherence
- event-locked flicker characteristics

This creates a reproducible mathematical description rather than relying on visual impression alone.

## Mathematical identification table

| Component | Mathematical definition | What it identifies |
| --- | --- | --- |
| First-order Delta | \(\Delta^1y_t=y_t-y_{t-1}\) | Direct observed change |
| Higher-order Delta | \(\Delta^ky_t=\Delta^{k-1}y_t-\Delta^{k-1}y_{t-1}\) | Acceleration, curvature and recursively nested change |
| Oscillation | \(O^k_t=\mathbf{1}(d^k_td^k_{t-1}<0)\) | Sign reversal at one Delta order |
| Oscillation energy | \(E^k_t=w^{-1}\sum_r(d^k_r)^2\) | Strength accumulated within a temporal window |
| Temporal dispersion | \(D^k_t=\sqrt{\sum_r(r-\mu)^2(d^k_r)^2/\sum_r(d^k_r)^2}\) | Whether energy is concentrated or spread through time |
| Persistence | \(R^k_t=\text{longest same-sign run}/w\) | Continuation of directional behaviour |
| Cross-order coherence | \(C_t=(K-1)^{-1}\sum_k\mathbf{1}[\operatorname{sign}(d^k_t)=\operatorname{sign}(d^{k+1}_t)]\) | Agreement across neighbouring Delta orders |
| Signature of Change | \(S_t=[d^1_t,\ldots,d^K_t,\nu_t,E_t,D_t,R_t,C_t]\) | Reproducible mathematical state of observed behaviour |
| Prospective event | \(P(Y_{t+h}=1\mid S_t)=\operatorname{logistic}(\beta_0+\beta^\top S_t)\) | Candidate probability of a genuinely later target |

## Complementary surrogate identification

The representative F5 and F7 surrogate equations address input-output structure. F5 is represented by a Matérn 2.5 Gaussian-process equation and F7 by a full quadratic equation with 27 numerical terms. PDHIS addresses the temporal behaviour of change. Together they identify two complementary aspects of an unknown function:

\[
\text{input-output structure}\quad\text{and}\quad\text{behaviour of change through time}
\]

Neither is presented as the original hidden equation.

## Representative equation results

| Surrogate | Complete observations | Representative equation | Weekly walk-forward MAE | Normalised MAE |
| --- | ---: | --- | ---: | ---: |
| F5 | 33 | Matérn 2.5 Gaussian process | 49.919 | 0.01124 |
| F7 | 43 | Full quadratic, 27 terms plus intercept | 0.06667 | 0.04837 |

The F5 equation, using standardised coordinates \(z\), is:

\[
\widehat F_5(x)=\bar y+s_y\sum_{i=1}^{33}\alpha_iK_{5/2}(z,z_i)
\]

The F7 equation is:

\[
\widehat F_7(x)=\beta_0+\sum_{j=1}^{6}\beta_jz_j+\sum_{j=1}^{6}\gamma_jz_j^2+\sum_{j<k}\gamma_{jk}z_jz_k
\]

Complete reproducibility tables:

- [F5 input scaling](../representative_surrogates/F5_INPUT_SCALING.csv)
- [F5 Matérn kernel weights](../representative_surrogates/F5_MATERN52_WEIGHTS.csv)
- [F5 hyperparameter validation](../representative_surrogates/F5_HYPERPARAMETER_VALIDATION.csv)
- [F7 input scaling](../representative_surrogates/F7_INPUT_SCALING.csv)
- [F7 quadratic coefficients](../representative_surrogates/F7_QUADRATIC_COEFFICIENTS.csv)
- [F7 hyperparameter validation](../representative_surrogates/F7_HYPERPARAMETER_VALIDATION.csv)
- [Weekly walk-forward predictions](../representative_surrogates/WEEKLY_WALK_FORWARD_PREDICTIONS.csv)
- [Combined validation graph](../representative_surrogates/F5_F7_REPRESENTATIVE_SURROGATES.jpg)

## Identification and validation table

| Analysis | Identification | Evidence boundary | Development value |
| --- | --- | --- | --- |
| Delta 1 to Delta 10 | Function-specific direction, reversal, oscillation, recovery and stabilisation | Higher orders retain fewer observations | Defines the retrospective hierarchy |
| Advanced Delta signature | Held-out-function balanced accuracy 0.624 | Expanding-week balanced accuracy 0.563 with weaker calibration | Identifies a candidate multilevel state |
| Delta 9 to later Delta 3 | Delta 9 oscillation occurred in 15 of 16 eligible cases | Exact p value 0.438, so oscillation was not selective | Identifies the need for a more specific propagation measure |
| Event-locked flicker | Peak spacing 4.00 before new bests versus 2.02 otherwise | Adjusted p value 0.305 | Identifies a temporal characteristic for further study |
| Matched event atlas | Same-function controls and threshold sensitivity | Smallest adjusted paired value 0.845 | Identifies the present stability boundary |
| Held-out fingerprint | Complete nine-feature transfer test | Balanced accuracy 0.433 versus baseline 0.500 | Defines the next prospective research requirement |

## Identification of the evidence boundary

The validation programme also produced useful identification results. Delta 9 oscillation occurred too frequently to distinguish later positive Delta 3 behaviour in the short record. The initial peak-spacing candidate changed under closer matching and alternative event thresholds. The complete fingerprint did not improve on the simple held-out-function baseline.

These findings identify the current boundary of the data and prevent a retrospective signature from being mistaken for a forecasting rule. They also specify the next research design: longer independent sequences, repeated anchor inputs, input-adjusted residual Delta and a locked prospective target.

## Contribution statement

> PDHIS extracts a structured and reproducible Signature of Change from sparse black-box sequences. It identifies retrospective mathematical behaviour, candidate event-linked characteristics and the point at which available evidence becomes insufficient for prospective inference. This is a positive methodological contribution even though advance prediction remains a later validation objective.
