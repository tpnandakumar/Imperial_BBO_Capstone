# PGC Experiment 003 Results

## Evidence status

**Trial evidence only. Not publication evidence. Not approved for promotion.**

Execution completed successfully across five fixed seeds, with 100 cases in each of six scenario families per seed. This produced 600 cases per seed and 3,000 evaluated cases in total.

The GitHub workflow completed the unit tests, Experiments 001 to 003, result validation and artefact upload successfully.

## Main finding

The initial coordinated PGC perception and emotional cognition configuration was too conservative in genuine-threat scenarios. It avoided false escalation but missed urgent threats at an unacceptable rate.

This is a safety-relevant negative result and must remain in the evidence record.

## Aggregate comparison

| Arm | Action accuracy | Urgent-threat recall | Missed-threat rate | False-escalation rate | Emotional proportionality | Factual override accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Factual only | 0.497000 | 1.000000 | 0.000000 | 0.000000 | 0.873250 | 0.660667 |
| Emotional only | 0.215000 | 0.992000 | 0.008000 | 0.355000 | 0.638783 | 0.002667 |
| Unweighted fusion | 0.990667 | 1.000000 | 0.000000 | 0.000000 | 0.997433 | 0.990667 |
| Reliability-weighted fusion | 0.862667 | 1.000000 | 0.000000 | 0.000000 | 0.968117 | 0.778000 |
| PGC perception and emotion | 0.563000 | 0.014000 | 0.986000 | 0.000000 | 0.811850 | 0.454667 |
| PGC without coherence | 0.563000 | 0.014000 | 0.986000 | 0.000000 | 0.811850 | 0.454667 |
| Oracle | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 |

## Interpretation

The result does not show that emotional cognition is harmful. It shows that the first PGC regulation thresholds compressed high factual risk too strongly before the urgent-response decision.

The current factual-support calculation combines the fused factual estimate with aggregate evidence strength. This protects against weak observations, but in the present configuration it also lowered strongly supported threat cases below the urgent-response threshold.

The identical performance of PGC with and without PHCS coherence shows that the present coherence branch did not materially affect action selection in this dataset. This component requires a more discriminating ablation.

## Promotion decision

`promotion_candidate = false`

The integrated layer remains experimental and must not replace the simpler fusion controls.

## Required correction sequence

1. Separate observation reliability from threat magnitude so reliability does not suppress a consistently high factual estimate twice.
2. Add a protected high-risk override when several reliable modalities independently support serious risk.
3. Recalibrate urgent-response thresholds on training and validation cases only.
4. Preserve a protected test split for the corrected configuration.
5. Add explicit false-negative cost for urgent threats.
6. Strengthen the PHCS ablation so coherence can change routing only after factual and safety gates pass.
7. Run a new experiment under a new identifier rather than overwriting this result.

## Scientific boundary

This experiment validates the execution pathway and exposes a regulatory failure. It does not validate emotional intelligence, human-like emotion or autonomous judgement.
