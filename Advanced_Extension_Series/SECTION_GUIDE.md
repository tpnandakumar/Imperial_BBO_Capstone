# Advanced Extension Series

## Purpose

This series begins after the official thirteen round capstone. It is deliberately separate from Week 01 to Week 13 and does not create an unofficial Week 14.

The aim is to continue the optimisation reasoning until each function has one defensible winning coordinate, with a documented reason to continue, eliminate a candidate, validate a winner or stop.

## SOC: Surrogate Optimisation Competition

The first analytical stage is **SOC, the Surrogate Optimisation Competition**. SOC is our post capstone competition between surrogate models. Several plausible model families compete independently for each of Functions 1 to 8 using the verified thirteen round input output history.

SOC does not change the original capstone record. It selects one surrogate model winner per function by held out predictive performance, then passes those winning evaluators into the Optimisation Extension series.

The competition pathway is:

**Observed evidence -> competing surrogate models -> leave one out validation -> SOC model winner per function -> candidate generation -> Optimisation Extension series**

See [SOC 1: Surrogate Optimisation Competition](SOC_Surrogate_Optimisation_Competition/SECTION_GUIDE.md).

## BBD: Black Box Decryption

**BBD, Black Box Decryption**, is a separate system-identification research track. SOC asks which surrogate predicts well. BBD asks a deeper question: what kind of mathematical generating mechanism is consistent with the complete sequential evidence?

BBD retains temporal ordering, coordinate movement, repeated points and previous outputs. Its first experiment compares static, noisy, time-augmented, movement-aware and state-aware explanations using chronological walk-forward validation.

See [BBD: Black Box Decryption](BBD_Black_Box_Decryption/SECTION_GUIDE.md).

## Optimisation lifecycle

**SOC -> Explore -> Exploit -> Extend -> Eliminate -> Validate -> Winner -> Stop**

A function can move backwards in this sequence when the evidence requires it. A failed exploitation step can reopen exploration. An apparent winner can return to validation if repeatability is uncertain.

## Current position after Week 13

| Function | Status entering extension | Current verified coordinate | Current verified value |
| --- | --- | --- | ---: |
| F1 | Provisionally confirmed winner | `0.600000-0.600000` | `0.025559285339829783` |
| F2 | Active | `0.690000-0.950000` | `0.7335252043269003` |
| F3 | Active | `0.855000-0.145000-0.855000` | `-0.05685061601567621` |
| F4 | Provisionally confirmed winner | `0.600000-0.430000-0.420000-0.250000` | `-4.359874926582439` |
| F5 | Active | `0.090000-0.999999-0.999999-0.999999` | `4440.957216598753` |
| F6 | Active, repeatability unresolved | `0.700000-0.200000-0.700000-0.700000-0.200000` | `-0.6071562248604215` best observed at this coordinate |
| F7 | Provisionally confirmed winner | `0.040000-0.480000-0.260000-0.220000-0.420000-0.740000` | `1.3809299933612855` |
| F8 | Provisionally confirmed winner | `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000` | `9.58024` |

## Active functions

F2, F3, F5 and F6 remain active because the thirteen round evidence does not yet justify a final stopping claim. F1, F4, F7 and F8 remain frozen unless SOC, BBD or later extension evidence gives a specific reason to reopen them.

## Extension numbering

All optimisation work after SOC uses the following sequence:

- Optimisation Extension 1
- Optimisation Extension 2
- Optimisation Extension 3
- subsequent extensions only when justified by new evidence

SOC itself is numbered separately as the surrogate competition stage, beginning with **SOC 1**. BBD uses its own experimental sequence beginning with **BBD 001**.

## Evidence rule

A proposed coordinate is not a verified winner until an objective value has actually been returned by the authorised evaluation process. Modelled, interpolated or extrapolated candidates are labelled as candidates. No output is invented.

SOC predictions and BBD reconstructions are post capstone model evidence. They can guide search, compare candidate regions and test hypotheses about the hidden mechanism, but they are not written into Weeks 01 to 13 as observed results.

## Completion rule

The Advanced Extension Series closes only when every function has one winning coordinate supported by the available evidence and a documented stopping reason. Where further black box evaluation is unavailable, the series records the strongest verified winner and separately records the final surrogate or decryption-based extension winner, its uncertainty and the reason the search stopped.

