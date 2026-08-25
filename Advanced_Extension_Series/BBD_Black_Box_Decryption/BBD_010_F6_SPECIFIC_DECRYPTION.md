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

## Result

The coordinate-only Gaussian Process was the strongest model in eight walk-forward tests.

| Rank | Model | Feature mode | Normalised walk-forward MAE |
| --- | --- | --- | ---: |
| 1 | Static Gaussian Process | Coordinates only | **0.0441** |
| 2 | Static quadratic ridge | Coordinates only | **0.0547** |
| 3 | State-aware Gaussian Process | Coordinates plus state proxies | 0.1697 |
| 4 | State-aware ridge | Coordinates plus state proxies | 0.2717 |

The best state-aware model was therefore worse than the best static model by about `0.1257` normalised MAE. On the available thirteen observations, the tested week, previous-output and movement proxies do **not** improve prospective prediction.

The BBD 010 mechanism decision is therefore:

`static_surface_preferred`

This is stronger evidence for a predominantly coordinate-driven F6 response than the earlier residual analysis alone suggested.

## Repeated-coordinate test

F6 contains **two exact repeated-coordinate groups**, and both have non-identical outputs. The maximum within-coordinate output range is approximately `0.100675`.

A deterministic coordinate-only function cannot reproduce two different outputs at the exact same coordinate. Across the repeated groups, the empirical mean absolute error floor for the best within-coordinate constant prediction is approximately `0.030852`.

This creates an important distinction. The broad response is best predicted by a static coordinate-only surface, but the repeated evaluations show an additional unresolved variability component.

A parsimonious current representation is therefore:

`observed F6 response = static coordinate-dependent surface + unresolved variability`

The available evidence does not establish whether that variability is evaluator noise, an unmeasured hidden state, numerical context or another mechanism.

## Interpretation

BBD 010 does **not** support adding simple temporal or path features merely because repeated coordinates differed. In fact, those additions substantially worsened forward prediction.

The next F6 decryption stage should therefore focus on decomposing the residual variability around a strong static surface rather than replacing the static surface with a time-dependent function.

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

BBD 010 is a post-capstone system-identification experiment. It does not modify the official Week 01 to Week 13 record. F6 remains explicitly marked as not exactly recovered because the repeated-coordinate inconsistency and lack of an independent discriminatory black-box evaluation prevent an exact-function claim.
