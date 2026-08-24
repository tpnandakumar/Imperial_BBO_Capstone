# Optimisation Extension 1

## Aim

Optimisation Extension 1 converts the Week 13 findings into a formal candidate-elimination programme. It does not claim new black-box outputs. Its purpose is to decide what should be tested next, what is already sufficiently supported, and what evidence would trigger stopping.

## F1: provisionally confirmed winner

**Verified winner:** `0.600000-0.600000`

The same value `0.025559285339829783` was reproduced repeatedly at this coordinate. Routine exploration is stopped. F1 reopens only if a new method identifies a materially different candidate with a defensible expected advantage.

**Stop location:** `0.600000-0.600000`.

## F2: active local optimisation

**Current verified winner:** `0.690000-0.950000`, value `0.7335252043269003`.

The neighbouring tested points at first coordinates `0.695000` and `0.685000`, with the second coordinate held at `0.950000`, were both weaker. A quadratic interpolation through the three verified observations gives a candidate first coordinate near `0.689414`.

**Extension 1 candidate:** `0.689414-0.950000`.

This is an interpolation candidate, not a verified result. If evaluated, it should compete directly against the verified `0.690000-0.950000` winner. If it fails to exceed the Week 12 value, the verified Week 12 point remains the winner and the local bracket is considered resolved unless a new orthogonal direction is justified.

**Provisional stop location:** the strongest verified coordinate inside the `0.685000` to `0.695000` local bracket, currently `0.690000-0.950000`.

## F3: active directional extension

**Current verified winner:** `0.855000-0.145000-0.855000`, value `-0.05685061601567621`.

The final two refinements improved the objective. The next candidate continues the same pattern by a deliberately small step.

**Extension 1 candidate:** `0.860000-0.140000-0.860000`.

If improvement continues, a subsequent extension may move another small step. If performance declines, the search should bracket the reversal between the last improving point and the first weaker point, then refine inside that bracket.

**Stop location:** the strongest verified coordinate after the first confirmed reversal bracket has been resolved.

## F4: provisionally confirmed winner

**Verified winner:** `0.600000-0.430000-0.420000-0.250000`, value `-4.359874926582439`.

The historical best was recovered and reproduced. Routine optimisation is stopped.

**Stop location:** `0.600000-0.430000-0.420000-0.250000`.

## F5: active boundary extension

**Current verified winner:** `0.090000-0.999999-0.999999-0.999999`, value `4440.957216598753`.

The final rounds continued to improve while the last three coordinates approached the upper boundary. The unresolved degree of freedom is primarily the first coordinate.

**Extension 1 candidate:** `0.080000-1.000000-1.000000-1.000000`.

If this improves, further reductions of the first coordinate can be tested with shrinking step size. If it fails, the winner remains the strongest verified point before the failure and a smaller interpolation between the successful and unsuccessful first-coordinate values becomes the next candidate.

**Stop location:** the strongest verified point at or immediately before the first resolved non-improving boundary step.

## F6: active uncertainty resolution

**Current best observed coordinate:** `0.700000-0.200000-0.700000-0.700000-0.200000`.

This identical coordinate returned `-0.648848297397347`, `-0.7078316130911375` and `-0.6071562248604215` on different evaluations. A single returned maximum is therefore not sufficient to characterise the coordinate.

**Extension 1 action:** repeat the same coordinate before directional movement.

If further evaluations remain variable, F6 should move to replicated comparison of the current coordinate against nearby candidates. A winner should be based on a repeatable summary of performance rather than the single highest draw.

**Stop location:** the coordinate with the strongest replicated evidence once response variability has been characterised sufficiently to distinguish location effect from evaluation variability.

## F7: provisionally confirmed winner

**Verified winner:** `0.040000-0.480000-0.260000-0.220000-0.420000-0.740000`, value `1.3809299933612855`.

The historical best was recovered and retained. Routine optimisation is stopped.

**Stop location:** the verified winner above.

## F8: provisionally confirmed winner

**Verified winner:** `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000`, value `9.58024`.

The same strongest value was reproduced repeatedly. Routine optimisation is stopped.

**Stop location:** the verified winner above.

## Decision after Optimisation Extension 1

The analytical programme is complete for this extension, but the empirical programme cannot progress beyond candidate generation without new objective evaluations. F2, F3 and F5 each have a defined next candidate. F6 has a defined replication test. F1, F4, F7 and F8 have documented stopping locations.

The next numbered extension should be created only after the Extension 1 candidates receive genuine outputs. Those outputs determine which candidates are eliminated, which functions continue and where the next search interval lies.
