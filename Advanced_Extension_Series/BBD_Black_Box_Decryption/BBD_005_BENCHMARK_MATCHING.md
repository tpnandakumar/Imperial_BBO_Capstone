# BBD 005: Benchmark Family Matching

## Purpose

BBD 005 tests whether the observed thirteen-round behaviour resembles transformed versions of standard optimisation benchmark families.

This is not an attempt to claim that the Imperial functions are known benchmarks. It is a structured comparison against familiar mathematical geometries.

## Candidate families

The current competition includes:

- Sphere
- Ellipsoid
- Rastrigin
- Ackley
- Griewank
- Schwefel
- Rosenbrock

For each family, BBD 005 applies a constrained common coordinate transformation

```text
z = scale * (x - centre)
```

where the same centre and scale are applied to all coordinates of that function. The transformed benchmark value is then mapped to the observed output through an affine relationship

```text
y_hat = a + b * benchmark(z)
```

The coefficient `b` may be positive or negative, allowing comparison with both maximisation and minimisation orientations.

## Why the transformation is deliberately constrained

With only thirteen observations, allowing a separate shift and scale for every coordinate would create enough free parameters to manufacture apparent matches. BBD 005 therefore searches only a small grid of common centres and scales.

The intention is to identify broad geometric resemblance, not force a benchmark family onto sparse data.

## Validation

Each fixed family, centre and scale combination is evaluated using leave-one-observation-out prediction. The affine output mapping is fitted only on the remaining observations for each held-out prediction.

The winning benchmark family is then compared with the BBD 004 symbolic equation using normalised leave-one-out MAE.

A benchmark resemblance is considered especially interesting when:

- its held-out error is low;
- it improves on the BBD 004 symbolic reconstruction;
- the geometry agrees with BBD 003 gradient evidence;
- repeated-coordinate behaviour does not contradict a deterministic interpretation.

## Outputs

Running `bbd_005_benchmark_matching.py` creates:

- `outputs/BBD_005_BENCHMARK_COMPETITION.csv`
- `outputs/BBD_005_BENCHMARK_WINNERS.csv`
- `outputs/BBD_005_BENCHMARK_PREDICTIONS.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_005_benchmark_matching.py
```

For direct comparison with BBD 004, run BBD 004 first so its recovered-equation summary is present in the output directory.

## Decision for BBD 006

BBD 006 will combine the evidence from mechanism identification, residual structure, gradient reconstruction, symbolic equations and benchmark-family matching into a function-specific decryption confidence score.
