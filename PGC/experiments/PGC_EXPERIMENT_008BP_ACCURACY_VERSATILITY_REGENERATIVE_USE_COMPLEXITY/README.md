# PGC Experiment 008BP: Accuracy, Versatility, Regenerative Use and Complexity

## Status

Completed derived comparative index analysis. This is not an external confirmatory validation.

## Systems compared

- AX-R
- AY-R
- 008BN three-route Hybrid-R
- 008BO AX-R + BK

All four were compared on the common AY fresh-seed evaluation space using breast cancer, wine and digits, ten seeds and ten repeats.

## Main result

AX-R + BK ranked first overall.

- Architecture Value Index: 77.8642
- Accuracy Index: 92.1553
- Versatility Index: 85.8775
- Regenerative Use Index: 72.5344
- Combined Complexity Index: 51.8319
- Versatility Efficiency Quotient: 1.6568
- relationship: Complexity < Versatility

## Ranking

1. AX-R + BK: 77.8642
2. Hybrid-R three-route: 59.4346
3. AX-R: 46.6163
4. AY-R: 16.0805

## Interpretation

AX-R + BK produced the strongest balance of predictive accuracy, cross-dataset breadth, worst-dataset protection, regenerative reuse and operational economy.

The three-route Hybrid-R remained highly versatile, but its additional structural routing and candidate-search complexity reduced its overall architecture value relative to AX-R + BK.

AX-R had the strongest relative regenerative-use score and the lowest operational complexity, but its predictive versatility was lower.

AY-R retained useful milieu behaviour but, in this four-system relative normalisation, its operational and controller complexity exceeded the versatility returned.

## Index definitions

### Accuracy Index

- 35% mean accuracy
- 25% worst-dataset accuracy
- 15% minimum accuracy
- 15% macro-F1
- 10% inverse log loss

### Versatility Index

- 30% best-unit share
- 25% worst-dataset accuracy
- 20% inverse dataset accuracy range
- 15% inverse dataset accuracy standard deviation
- 10% balanced accuracy

### Regenerative Use Index

- 45% Net Regenerative Efficiency
- 20% cache reuse
- 20% avoided-model fraction
- 15% state reuse

### Complexity

Structural Complexity uses route count, available model count, controller depth and candidate budget.

Operational Complexity uses active models, inverse dropout, inverse avoided-model fraction and inverse cache reuse.

Combined Complexity is 35% structural and 65% operational complexity.

## Important boundary

All index values are min-max normalised across these four systems. A score of zero means the lowest value within this comparison, not absence of the underlying capability.

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
