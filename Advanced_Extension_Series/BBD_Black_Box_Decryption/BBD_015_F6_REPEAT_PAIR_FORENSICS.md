# BBD 015: F6 Repeat-Pair Forensic Reconstruction

## Purpose

BBD 014 showed that richer deterministic coordinate-only models did not improve on the Matérn 2.5 Gaussian Process. BBD 015 therefore returns to the strongest anomaly in F6: identical coordinates with different recorded outputs.

The aim is to reconstruct the sequence context surrounding every repeated F6 evaluation and test whether any recorded variable changes systematically with the change in output.

## Question

> When F6 was evaluated at exactly the same coordinate more than once, what else in the recorded sequence was different?

This is a forensic identification exercise, not a new optimisation round.

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

## Repeat-pair analysis

Each pair of identical F6 coordinates is compared by:

- signed and absolute output change;
- change in each individual context variable;
- a pre-evaluation sequence fingerprint distance;
- a cross-function same-round fingerprint distance;
- a combined descriptive fingerprint distance.

Spearman association is used because there are only four repeat pairs and no linear distributional assumption is defensible.

## Evidence rule

With only four pairwise comparisons, even a large correlation is treated as a lead rather than confirmation. BBD 015 does not fit a high-dimensional predictive model to four pairs.

## Outputs

Running `bbd_015_f6_repeat_pair_forensics.py` creates:

- `outputs/BBD_015_F6_REPEAT_OCCURRENCES.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_DIFFERENCES.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_ASSOCIATIONS.csv`
- `outputs/BBD_015_F6_REPEAT_FINGERPRINT_DISTANCES.csv`
- `outputs/BBD_015_F6_FINGERPRINT_ASSOCIATIONS.csv`
- `outputs/BBD_015_F6_REPEAT_PAIR_FORENSIC_SUMMARY.csv`

## Evidence boundary

The experiment can identify recorded sequence variables that co-vary with the repeated-output anomaly. It cannot prove that such a variable is part of the original evaluator. Exact function recovery remains false unless an independent black-box evaluation can discriminate the surviving explanations.
