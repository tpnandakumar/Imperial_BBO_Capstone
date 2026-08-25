# BBD 015: F6 Repeat-Pair Forensic Reconstruction

## Purpose

BBD 014 showed that richer deterministic coordinate-only models did not improve on the Matérn 2.5 Gaussian Process. BBD 015 therefore returns to the strongest anomaly in F6: identical coordinates with different recorded outputs.

The aim is to reconstruct the sequence context surrounding every repeated F6 evaluation and test whether any recorded variable changes systematically with the change in output.

## Question

> When F6 was evaluated at exactly the same coordinate more than once, what else in the recorded sequence was different?

This is a forensic identification exercise, not a new optimisation round.

## Repeated-coordinate record

Two F6 coordinates were repeated, producing five repeated occurrences and four pairwise comparisons.

The first coordinate,

`0.700000-0.200000-0.700000-0.700000-0.200000`,

was observed in Weeks 3, 12 and 13 with outputs `-0.648848`, `-0.707832` and `-0.607156` respectively. The Week 12 to Week 13 comparison is especially informative because the coordinate was unchanged in consecutive rounds but the output increased by approximately `0.100675`.

The second coordinate,

`0.240000-0.760000-0.240000-0.820000-0.280000`,

was observed in consecutive Weeks 8 and 9. Again, there was no coordinate movement, yet the output changed from approximately `-1.119718` to `-1.173303`, a difference of about `-0.053585`.

These consecutive-repeat observations make a simple coordinate-only exact deterministic explanation especially difficult to sustain for the recorded data.

## Context reconstructed

For every repeated F6 occurrence, the experiment records:

- week position;
- previous F6 output;
- previous F6 output change;
- movement from the previous F6 coordinate;
- similarity to the immediately preceding coordinate;
- next F6 output and next movement, used only as retrospective forensic context;
- same-round outputs of the other seven functions, standardised across the thirteen rounds.

The same-round cross-function values are treated as descriptive evaluator-context signals only. They are not assumed to be causally available before an F6 evaluation.

## Repeat-pair findings

No recorded sequence variable established a convincing explanation for the repeated-output anomaly.

The largest individual descriptive associations were the same-round standardised F3 and F5 outputs, each with Spearman correlation of approximately `-0.80` between context change and absolute F6 output change. With only four repeat pairs, the corresponding `p` value was `0.20`, so these values are leads rather than evidence of a mechanism.

The pre-evaluation sequence fingerprint had Spearman correlation approximately `-0.40` with absolute F6 output change. The cross-function same-round fingerprint was also approximately `-0.40`. Combining both fingerprints increased the magnitude to approximately `-0.80`, but again with only four pairs this is not confirmatory and the negative direction does not support a simple model in which greater contextual difference causes greater F6 output difference.

The experiment therefore records `sequence_context_candidate = False` and interprets the result as `no_repeat_pair_context_explanation_established`.

## What BBD 015 rules out

The repeated-pair evidence now makes several simple explanations less plausible:

- the output change is not caused merely by changing the F6 coordinate, because two important changes occurred with zero coordinate movement;
- simple elapsed time does not explain the pattern consistently;
- the recorded pre-evaluation sequence fingerprint does not track the magnitude of the repeat anomaly;
- same-round behaviour of the other functions does not provide a convincing evaluator-wide state explanation in the available sample.

This does not prove stochasticity. An unrecorded evaluator state, numerical randomness, hidden conditioning variable or another mechanism outside the retained history remains possible.

## Outputs

Running `bbd_015_f6_repeat_pair_forensics.py` creates:

- `outputs/BBD_015_F6_REPEAT_OCCURRENCES.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_DIFFERENCES.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_ASSOCIATIONS.csv`
- `outputs/BBD_015_F6_REPEAT_FINGERPRINT_DISTANCES.csv`
- `outputs/BBD_015_F6_FINGERPRINT_ASSOCIATIONS.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_FORENSIC_SUMMARY.csv`

## Evidence boundary

There are only four repeat-pair comparisons. Large descriptive correlations are therefore unstable and are not treated as proof. Exact function recovery remains false. The strongest next evidence would come from controlled repeated independent evaluations at fixed F6 coordinates, preferably repeated several times under deliberately matched and deliberately changed surrounding conditions.
