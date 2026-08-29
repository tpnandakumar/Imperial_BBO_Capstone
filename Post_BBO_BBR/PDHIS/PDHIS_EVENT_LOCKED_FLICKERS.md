# PDHIS event-locked flicker characterisation

## Question

Looking backwards from a known event, did the preceding six observations contain a flicker with a characteristic temporal fingerprint?

## Design

The analysis contains 56 event-locked windows across eight functions. The targets are known outcomes: 29 improvements, 6 large function-adjusted changes and 11 new best outputs. Each target week is compared with the six observations immediately before it.

The fingerprint measures peak amplitude, oscillation energy, temporal dispersion, sign-change frequency, peak spacing, directional persistence, late amplification, Delta 2 energy and flicker density. Scaling uses only observations available before the target week.

## Main result

The smallest exploratory within-function permutation p value was 0.034 for peak spacing against new best event. Its Holm-adjusted p value was 0.305. No characteristic should be treated as confirmed unless its adjusted result remains below the defined threshold and it is reproduced prospectively.

## Behavioural shapes

| Pre-event behaviour | Windows | Improvement rate | Large-event rate | New-best rate |
| --- | ---: | ---: | ---: | ---: |
| Intermittent oscillation | 21 | 0.476 | 0.143 | 0.048 |
| Damped oscillation | 12 | 0.583 | 0.083 | 0.167 |
| Irregular flicker | 9 | 0.667 | 0.111 | 0.444 |
| Directed movement | 7 | 0.714 | 0.143 | 0.571 |
| Stable oscillation | 4 | 0.250 | 0.000 | 0.000 |
| Amplifying oscillation | 3 | 0.000 | 0.000 | 0.000 |

## Interpretation

This is an event-locked retrospective analysis. It characterises what was present before outcomes already known to have happened or not happened. It does not allow a later event to enter the flicker calculation. The analysis can identify candidate signatures, but the same locked fingerprint must predict untouched later events before it can be described as an early warning signal.

Weekly sampling and thirteen observations per function limit frequency resolution. Sign-change rate and peak spacing are therefore used instead of a conventional frequency spectrum.

## Reproducibility

Run `python Post_BBO_BBR/PDHIS/generate_pdhis_event_locked_flickers.py` from the repository root.
