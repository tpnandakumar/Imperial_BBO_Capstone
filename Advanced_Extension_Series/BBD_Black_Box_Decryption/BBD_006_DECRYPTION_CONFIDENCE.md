# BBD 006: Decryption Ensemble and Confidence Ranking

## Purpose

BBD 006 combines the evidence from BBD 001 to BBD 005 into a single function-specific confidence score. The aim is not to declare that a hidden function has been exactly recovered, but to distinguish strong structural evidence from weak or contradictory evidence.

## Evidence combined

The confidence score uses six separate evidence dimensions:

1. **Predictive equation performance** from BBD 004 leave-one-out validation.
2. **Equation compactness**, because a short expression is stronger evidence of structural recovery than a large near-interpolating polynomial.
3. **Gradient coherence** from BBD 003, combining transition prediction with agreement between global and recent gradient directions.
4. **Repeatability** from BBD 002, with a penalty when identical submitted coordinates return non-identical outputs.
5. **Mechanism simplicity** from BBD 001 and BBD 002, favouring a stable coordinate-only explanation over unresolved temporal or hidden-state dependence.
6. **Benchmark geometry support** from BBD 005. This is deliberately given low weight because the hidden function does not need to belong to a standard benchmark family.

## Weighting

The current ensemble is:

```text
30% equation predictive evidence
15% equation compactness
25% gradient coherence
15% repeatability
10% mechanism simplicity
 5% benchmark geometry
```

The weighting is intentionally conservative. A function cannot receive high confidence merely because one flexible equation fits the thirteen observations extremely well.

## Confidence bands

```text
80 to 100   high
65 to <80   moderate_high
50 to <65   moderate
35 to <50   low_moderate
0  to <35   low
```

These bands describe confidence in the current reconstruction, not probability that the equation is the exact Imperial source function.

## Current best description

For each function, BBD 006 also records the strongest current structural description. If a constrained benchmark-family match has lower leave-one-out error than the symbolic equation, the benchmark-like geometry is reported. Otherwise, the selected BBD 004 symbolic equation remains the current best description.

## Output

Running `bbd_006_decryption_confidence.py` creates:

- `outputs/BBD_006_DECRYPTION_CONFIDENCE.csv`

The table includes the overall confidence rank and all component scores, so the final ranking remains auditable rather than being a single unexplained number.

## Reproduction

BBD 006 requires the output tables from BBD 001 to BBD 005. From the repository root, run the full BBD workflow or execute the stages in sequence before running:

```bash
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_006_decryption_confidence.py
```

## Interpretation boundary

The thirteen observations were adaptively selected rather than sampled from a designed identification experiment. Several coordinates moved together, the dimensionality varies across F1 to F8, and repeated-point behaviour is not uniform. The confidence score therefore measures how well the available evidence supports a reconstruction. It does not prove identity with the unknown Imperial objective.

## Decision for BBD 007

BBD 007 will test whether the reconstructed functions have practical predictive value by placing BBD-derived predictions against the SOC surrogate competition. The useful question is no longer only whether an equation fits the historical data, but whether it can make defensible predictions that compete with flexible surrogate models.
