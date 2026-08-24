# BBD 002: Temporal Residual Structure and Repeatability

## Purpose

BBD 001 showed that time or state-aware models improved chronological prediction for F1 and F2, while static models remained stronger for F3 to F8. BBD 002 asks whether those apparent temporal gains survive a more direct residual test.

The experiment first fits a static Gaussian Process using only the coordinates available before each test week. It then studies the resulting out-of-sample residuals in temporal order.

The central question is:

> After coordinate effects have been modelled, is there still predictable information left in time, previous residuals or repeated evaluations?

## Tests

For each function, BBD 002 records:

- walk-forward residuals from a coordinate-only Gaussian Process;
- Spearman correlation between residual and week;
- Spearman correlation between absolute prediction error and week;
- lag-one residual correlation;
- a chronological competition between no residual correction, linear time-drift correction and previous-residual correction;
- exact repeated-coordinate diagnostics, including output range and whether repeated outputs are identical.

## BBD 002 results

The experiment completed successfully in GitHub Actions with nine walk-forward residual observations per function.

| Function | Residual correction winner | Repeatability finding | Current interpretation |
| --- | --- | --- | --- |
| F1 | No correction | two repeated groups, identical outputs | residuals correlate with week, but explicit temporal corrections made forecasting worse |
| F2 | No correction | one repeated group with non-identical outputs, range `0.112336` | the BBD 001 state-aware advantage is not explained by simple time drift or residual persistence |
| F3 | No correction | one non-identical repeat group, small range `0.000529` | static coordinate model remains preferred; absolute error fell strongly over later weeks |
| F4 | No correction | repeated output identical | strong static interpretation remains supported |
| F5 | No correction | repeated output identical | no residual correction improved prediction; this strengthens the case for direct structural equation recovery |
| F6 | Previous residual | two non-identical repeat groups, maximum range `0.100675` | strongest evidence of response variability and some short-memory residual structure |
| F7 | No correction | repeated output identical | static interpretation remains stronger; prediction error reduced sharply in later rounds |
| F8 | Previous residual | repeated output identical | a small residual-memory improvement exists, but there is no repeated-output variability at the tested repeat point |

### F1

F1 showed a strong monotonic association between static-model residual and week, with Spearman rho `0.816667`. However, neither a linear time-drift correction nor a previous-residual correction improved chronological residual prediction. The no-correction baseline remained best. BBD therefore does not currently support treating F1 as a genuinely time-varying evaluator.

### F2

F2 showed almost no residual-week association, Spearman rho `0.033333`, and neither temporal correction improved prediction. This is important because BBD 001 had selected a state-aware model. BBD 002 suggests that the useful additional information in BBD 001 was more likely associated with state or path features than with simple elapsed time.

The repeated-coordinate diagnostic also identified one F2 repeat group with non-identical outputs and a range of approximately `0.112336`. This rules out a perfectly deterministic coordinate-only description at that repeated point unless the stored observations contain another unmodelled factor.

### F3, F4, F5 and F7

No residual correction improved these functions. Their strongest current explanation remains a static coordinate-dependent surface, with any temporal pattern interpreted cautiously.

F3, F4 and F7 showed strong reductions in absolute static-model error as the rounds progressed. This can arise because later searches became concentrated in better understood local regions. It should not be mistaken for evidence that the objective itself changed with time.

F5 remains particularly important. Its no-correction residual baseline was markedly better than either temporal correction, and its repeated coordinate reproduced the same output. Together with the BBD 001 quadratic winner, this strengthens the case for BBD 003 and BBD 004 to search for an explicit local mathematical structure rather than a temporal mechanism.

### F6

F6 is the clearest exception. Previous-residual correction reduced residual MAE from approximately `0.055875` to `0.040740`. It also contained two repeated-coordinate groups with non-identical outputs, with a maximum repeated-output range of approximately `0.100675`.

This does not identify the cause. It does show that a purely deterministic `y=f(x)` model is incomplete for the observed F6 record and that short-memory information has some predictive value in this small sample.

### F8

F8 also benefited from previous-residual correction, reducing residual MAE from approximately `0.005609` to `0.004357`. Its repeated output was nevertheless identical. The improvement is therefore treated as a weak residual-memory signal rather than evidence that F8 is intrinsically time varying.

## Interpretation rule

A temporal signal is not accepted merely because a correlation coefficient is non-zero. Temporal structure is treated as practically useful only when a correction based entirely on earlier residuals improves later residual prediction over the no-correction baseline.

With only thirteen rounds, p-values and correlations are descriptive rather than definitive. The purpose is model discrimination and hypothesis generation, not a claim of formal proof.

## BBD 002 conclusion

BBD 002 narrows the decryption problem considerably.

- Simple temporal drift is not supported as the dominant explanation for F1 or F2.
- F3, F4, F5 and F7 remain best treated as predominantly static surfaces at this stage.
- F6 requires an uncertainty or hidden-state term because exact coordinates can return materially different values.
- F8 shows a small short-memory residual effect, but its repeatability evidence remains deterministic at the tested repeated point.

The next experiment should therefore move from temporal diagnosis to geometry: **BBD 003 will estimate directional derivatives, coordinate sensitivities and local gradient structure from the ordered sequence of input movements and output changes.**

## Why repeatability matters

Repeated coordinates act as natural controls. If the same coordinate returns the same value at different weeks, that supports a stable deterministic interpretation at that tested point. If the same coordinate returns different values, the observation is compatible with noise, hidden state, temporal drift or another unobserved evaluator factor.

BBD 002 does not assign a cause without evidence. It only establishes whether non-identical repeated outputs occurred and whether temporal residual models improve prediction.

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_002_temporal_residuals.py
```

Outputs are written to `Advanced_Extension_Series/BBD_Black_Box_Decryption/outputs/`.

## Evidence boundary

All BBD 002 outputs are post-capstone analytical results. They do not alter or replace the verified Week 01 to Week 13 observations.
