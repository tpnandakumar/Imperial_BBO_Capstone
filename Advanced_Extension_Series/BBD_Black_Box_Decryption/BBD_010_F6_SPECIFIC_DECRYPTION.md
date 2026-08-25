# BBD 010: F6-Specific Decryption

## Why F6 is the first function-specific target

BBD 009 moved F6 to the top of the prospective evidence ranking. F6 was the only function where BBD beat SOC at the function level in the chronological forward-prediction challenge, yet F6 also contains exact repeated coordinates with non-identical outputs.

That combination makes F6 unsuitable for a simple claim of `y = f(x)` without further testing. BBD 010 therefore asks whether F6 is better represented as a static surface or as a static surface plus observable state proxies.

## Competing explanations

BBD 010 compares four models under expanding-window walk-forward validation:

1. coordinate-only Gaussian Process;
2. coordinate-only regularised quadratic response surface;
3. state-aware ridge model;
4. state-aware Gaussian Process.

The state-aware feature set contains the five F6 coordinates plus three quantities available at prediction time:

- scaled week index;
- previous observed F6 output;
- Euclidean movement from the previous F6 coordinate.

These are proxies for possible temporal, path or hidden-context effects. They are not assumed to be the true hidden state.

## Repeated-coordinate test

Exact repeated F6 coordinates are analysed separately. For every repeated coordinate BBD 010 records the weeks, outputs, within-coordinate range and whether the returned values were identical.

Where the same coordinate produces different outputs, a deterministic coordinate-only equation cannot reproduce all observations exactly. The experiment therefore calculates the mean absolute error of the best constant within each repeated-coordinate group. This is used as an empirical lower bound for any deterministic coordinate-only explanation at those repeated points.

## Interpretation rule

If the best state-aware model improves chronological prediction over the best static model, BBD 010 records evidence for `state_or_hidden_context_supported`. If it does not, the static-surface explanation remains preferred despite the repeat variability.

Neither outcome establishes the exact Imperial mechanism. Unobserved evaluator state, stochasticity and other hidden variables remain possible.

## Outputs

Running `bbd_010_f6_specific_decryption.py` creates:

- `outputs/BBD_010_F6_REPEAT_SUMMARY.csv`
- `outputs/BBD_010_F6_REPEAT_DETAIL.csv`
- `outputs/BBD_010_F6_MODEL_COMPETITION.csv`
- `outputs/BBD_010_F6_WALK_FORWARD_PREDICTIONS.csv`
- `outputs/BBD_010_F6_DECRYPTION_SUMMARY.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_010_f6_specific_decryption.py
```

## Evidence boundary

BBD 010 is a post-capstone system-identification experiment. It does not modify the official Week 01 to Week 13 record and does not claim that F6 has been exactly recovered without independent black-box validation.
