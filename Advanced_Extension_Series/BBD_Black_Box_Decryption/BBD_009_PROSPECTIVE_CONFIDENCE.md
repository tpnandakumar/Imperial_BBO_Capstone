# BBD 009: Prospective-Evidence Confidence Recalibration

## Purpose

BBD 009 recalibrates the earlier structural-confidence ranking after the prospective challenge in BBD 007 and the unresolved model disagreement identified by BBD 008.

BBD 006 measured how strongly the thirteen-round history supported a compact structural reconstruction. BBD 007 showed that this was not sufficient evidence of generalisation. BBD 009 therefore gives forward prediction substantially more weight and prevents an excellent retrospective fit from being labelled strong when SOC predicts later observations more accurately.

## Evidence components

For each function the recalibrated index combines four bounded components:

- **25% retrospective structural evidence:** the BBD 006 score divided by 100;
- **40% prospective competitiveness:** `min(1, SOC forward MAE / BBD forward MAE)`;
- **20% forward test win rate:** the proportion of BBD 007 held-out rounds individually won by BBD;
- **15% mechanism resolution:** `1 / (1 + BBD 008 top normalised prediction spread)`.

The raw evidence-strength index is therefore:

`100 × (0.25R + 0.40P + 0.20W + 0.15M)`

where `R` is retrospective structural evidence, `P` is prospective competitiveness, `W` is forward test win rate and `M` is mechanism resolution.

## Prospective veto

Forward evidence has explicit veto power. If SOC wins the function-level BBD 007 challenge, the recalibrated score is capped at 65. If BBD wins, the cap is 85. The upper cap remains below a claim of confirmation because the project still lacks a genuinely new independent black-box evaluation at a BBD 008 discriminatory point.

These thresholds are methodological safeguards rather than estimated probabilities.

## Interpretation

The score is an **evidence-strength index**, not the probability that the exact Imperial equation has been recovered. A high value means the current structural explanation is supported by retrospective fit, forward performance and relatively low unresolved disagreement. It does not establish identity with the original evaluator.

Every function remains marked `exact_function_recovered = False` until independent discriminatory evidence is available.

## Output

Running `bbd_009_prospective_confidence.py` creates:

- `outputs/BBD_009_PROSPECTIVE_CONFIDENCE.csv`

The table preserves the BBD 006 score, BBD 007 forward errors and wins, BBD 008 disagreement, the recalibrated score, its evidence band and the change from the retrospective ranking.

## Reproduction

From the repository root:

```bash
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_001_system_identification.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_002_temporal_residuals.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_003_gradient_reconstruction.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_004_symbolic_recovery.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_005_benchmark_matching.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_006_decryption_confidence.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_007_bbd_vs_soc_challenge.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_008_discriminatory_query_design.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_009_prospective_confidence.py
```
