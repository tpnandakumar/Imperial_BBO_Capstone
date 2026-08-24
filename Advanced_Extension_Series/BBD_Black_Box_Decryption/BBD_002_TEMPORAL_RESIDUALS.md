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

## Interpretation rule

A temporal signal is not accepted merely because a correlation coefficient is non-zero. Temporal structure is treated as practically useful only when a correction based entirely on earlier residuals improves later residual prediction over the no-correction baseline.

With only thirteen rounds, p-values and correlations are descriptive rather than definitive. The purpose is model discrimination and hypothesis generation, not a claim of formal proof.

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
