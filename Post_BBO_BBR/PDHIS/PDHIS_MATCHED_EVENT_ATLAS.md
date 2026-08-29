# PDHIS matched event atlas and stability analysis

## Purpose

This extension exploits the existing event-locked evidence by pairing each event with the nearest non-event window from the same function. It then tests threshold sensitivity and transfer to a function excluded from fitting.

## Matched comparison

The smallest paired sign-flip p value was 0.094 for temporal dispersion against large event across 6 pairs. Its Holm-adjusted p value was 0.845. Matching controls function identity and favours a nearby comparison week, but it does not create additional independent events.

## Threshold sensitivity

The large-event definition was varied from 1.00 to 2.00 times the function-adjusted historical scale. The direction of the peak-spacing difference was not stable across the tested thresholds. Event counts and complete feature results are retained in `PDHIS_EVENT_THRESHOLD_SENSITIVITY.csv`.

## Transfer to an unseen function

The complete nine-feature fingerprint was fitted on seven functions and tested on the eighth. Balanced accuracy was 0.433, ROC AUC was 0.396 and Brier score was 0.244. The prevalence baseline balanced accuracy was 0.500 with Brier score 0.181.

## Interpretation

These checks ask whether the candidate fingerprint survives closer controls, alternative event thresholds and a held-out function. They do not turn retrospective discovery into prospective confirmation. A characteristic should be locked only if its direction is stable, its adjusted evidence is credible and its transfer performance improves on the simple baseline.

## Reproducibility

Run `python Post_BBO_BBR/PDHIS/generate_pdhis_matched_event_atlas.py` from the repository root.
