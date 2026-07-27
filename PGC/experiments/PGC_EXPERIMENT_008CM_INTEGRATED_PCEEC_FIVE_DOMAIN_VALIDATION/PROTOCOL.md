# Protocol: 008CM Integrated PCEEC Five-Domain Validation

## 1. Experimental design

Use fresh, predeclared seeds and at least three workload families: clean, missingness and intensified temporal drift. Compare the A-DMIC gated specialist against the reference core and permanent specialist. Preserve temporal train, validation and protected-test separation with zero overlap.

## 2. Domain criteria

### Accuracy, A

Measure mean accuracy, minimum accuracy, log loss and protected-test degradation. Level 5 requires no protected-test leakage, no material regression against the locked balanced baseline and declared minimum performance across every workload.

### Reliability, R

Measure successful completion, deterministic repeatability, failure detection, rollback success, invalid-state release and unresolved solver outcomes. Level 5 requires zero invalid-state release, complete rollback where triggered and no unresolved violation treated as proven.

### Stability, S

Measure cross-seed variance, worst-case degradation, temporal-drift behaviour, missingness response, memory residuals and thread leakage. Level 5 requires bounded degradation, zero worker leakage, zero persistent memory residue and restored A-DMIC homeostasis.

### Efficiency and regeneration, E-R

Measure active models, latency, CPU time, throughput, memory recovery and recovery time. Level 5-R requires complete software-resource recovery and a compute profile that is no worse than the locked threshold. Electrical-energy regeneration must not be claimed unless directly measured.

### Cost efficiency, C

Measure the normalised compute cost index per 1,000 predictions and compare it with the permanent specialist and reference core. Level 5 requires the predeclared cost threshold without sacrificing the minimum Accuracy, Reliability or Stability criteria. Direct monetary cost must not be claimed unless measured.

## 3. Scoring

Each domain receives an integer score from 0 to 5 using locked thresholds in `SCORING_LOCK.json`. No compensatory averaging is allowed. A strong score in one domain cannot conceal failure in another.

## 4. Required outputs

- `per_run_results.csv`
- `domain_scores.csv`
- `statistical_comparisons.csv`
- `results_summary.json`
- `EVIDENCE_MANIFEST.json`
- `FINAL_DECISION.md`

## 5. Formal gate

All deterministic invariants used in scoring must be executable. Suitable constraints must be checked through unit tests, property-based tests or Z3 models. `unknown` is not proof.

## 6. Release gate

The engine may be labelled `A5 R5 S5 E5-R C5` only when every domain independently scores 5 and the evidence manifest confirms that A-DMIC, PCEEC, PFRAMOS and PGC continuity has been preserved.
