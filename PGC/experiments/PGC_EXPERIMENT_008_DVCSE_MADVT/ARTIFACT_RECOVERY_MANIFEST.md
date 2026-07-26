# Experiment 008 Artefact Recovery Manifest

## Authoritative location

- Repository: `tpnandakumar/Imperial_BBO_Capstone`
- Branch: `agent/pframos-v0.1`
- Experiment: `PGC_EXPERIMENT_008_DVCSE_MADVT`

## Verified files present

- `PROTOCOL.md`
- `README.md`

## Verified historical execution artefacts

The original execution produced the following in-session objects:

- per-run results dataframe
- aggregate dataframe
- JSON-serialisable result summary
- pretty JSON text, reported length 4,543 characters
- CSV text, reported length 56,904 characters

## Files expected but not recovered

- `results_summary.json`
- `per_run_results.csv`

The exact payloads are not contained in the repository, screenshots or accessible file sources. They must not be recreated from aggregate values or inferred from later experiments.

## Verified findings preserved in README

- Best reported full-coverage arm: Fusion Anchor without dynamic vectoring
- Mean protected-test accuracy: 0.986126
- Dynamic vectoring was neutral for Fusion Anchor
- Dynamic vectoring slightly improved Rankine cruise
- Dynamic vectoring slightly harmed fixed hybrid
- No arm achieved 0.9999 mean protected-test accuracy across all datasets
- Selective performance must be reported with coverage

## Recovery procedure

1. Locate the original execution session, notebook state, exported attachment or cached artefact.
2. Recover the exact `json_text` and `csv_text` strings.
3. Confirm their reported lengths before committing.
4. Validate JSON parsing and CSV row/column consistency.
5. Commit the exact files without transformation.
6. Record checksums and provenance in this manifest.

## Experiment status

**Historically executed, partially preserved, not independently reproduced.**

Further experiments may proceed, but Experiment 008 must remain labelled screenshot-supported historical trial evidence until its exact artefacts are recovered or the experiment is reproduced from source.
