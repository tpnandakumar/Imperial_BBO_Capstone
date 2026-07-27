# PGC Experiment 008CM: Basal Ganglia, Cerebellar and Descending-Tract Modulation and Integration

## Status

Executed reproducible development simulation and integrated as an opt-in experimental PGC regulator.

## Scientific basis

The experiment translates functional principles rather than claiming biological equivalence:

- basal ganglia direct, indirect and hyperdirect pathways provide facilitation, suppression and rapid braking;
- cerebellar circuitry provides prediction, damping, timing and error correction;
- reticulospinal, vestibulospinal, rubrospinal and tectospinal analogues provide global stability, reference-frame preservation, fine correction and target orientation.

The basal ganglia source describes complementary direct and indirect pathway activity, rapid hyperdirect inhibition, and reciprocal basal ganglia-cerebellar connectivity. The cerebellar source describes excitatory and inhibitory microcircuits, movement timing, velocity, motor learning, dysmetria, and connections with reticulospinal, vestibulospinal, rubrospinal and tectospinal pathways.

## Experimental design

- 10 fixed fresh seeds
- 6 perturbation scenarios
- 5 controller arms
- 120 closed-loop steps per run
- 300 total runs

### Scenarios

1. overfitting pressure
2. underfitting pressure
3. abrupt distribution shift
4. noisy validation
5. excessive update gain
6. rotational perturbation

### Arms

1. baseline
2. basal ganglia only
3. cerebellar only
4. basal ganglia plus cerebellum
5. full basal ganglia, cerebellar and descending-tract integration

## Results

The full integrated arm ranked first on the predefined composite score.

- mean accuracy proxy: 0.984596
- mean target error: 0.052640
- mean final error: 0.015531
- mean stability: 0.900970
- mean recovery step: 20.583
- composite score: 0.855075

The full arm achieved the best mean accuracy, target error, final error, stability and recovery time. It required the greatest active-module count and compute-cost index. It did not eliminate every loss-of-track event or minimise every isolated metric.

## Integration decision

The full regulator is integrated as an experimental opt-in module. It does not silently replace the established PGC path. Promotion requires validation on real datasets, ablation testing, resource profiling and protected hold-out evidence.

## Artefacts

- `run_experiment.py`
- `system_summary.csv`
- `results_summary.json`
- `EVIDENCE_MANIFEST.json`
- `bg_cerebellar_descending_regulator.py`

The deterministic runner regenerates the complete 300-row `per_run_results.csv`.

## Evidence boundary

This is a synthetic closed-loop target-tracking experiment. It tests the encoded computational controllers. It does not establish biological equivalence, clinical validity, external-dataset generalisation, direct electrical-energy regeneration or direct monetary cost.
