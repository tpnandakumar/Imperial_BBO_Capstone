# BBD 005: Benchmark Family Matching

## Purpose

BBD 005 tests whether the observed thirteen-round behaviour resembles transformed versions of standard optimisation benchmark families.

This is not a claim that the Imperial functions are known benchmarks. It is a structured comparison against familiar mathematical geometries.

## Candidate families

The competition includes Sphere, Ellipsoid, Rastrigin, Ackley, Griewank, Schwefel and Rosenbrock.

For each family, BBD 005 applies the constrained common coordinate transformation

```text
z = scale * (x - centre)
```

where the same centre and scale are applied to all coordinates of that function. The transformed benchmark value is then mapped to the observed output through

```text
y_hat = a + b * benchmark(z)
```

The coefficient `b` may be positive or negative, allowing comparison with both maximisation and minimisation orientations.

## Why the transformation is deliberately constrained

With only thirteen observations, a separate shift and scale for every coordinate would create enough free parameters to manufacture apparent matches. BBD 005 therefore searches only a small grid of common centres and scales.

The intention is to identify broad geometric resemblance, not force a benchmark family onto sparse data.

## Validation

Each fixed family, centre and scale combination is evaluated using leave-one-observation-out prediction. The affine output mapping is fitted only on the remaining observations for each held-out prediction.

The winning benchmark family is compared with the BBD 004 symbolic equation using normalised leave-one-out MAE.

## Results

| Function | Best benchmark family | Centre | Scale | Benchmark normalised LOOCV MAE | BBD 004 equation MAE | Better than BBD 004? |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| F1 | Rastrigin | 0.50 | 5.0 | 0.3653 | 0.6972 | Yes |
| F2 | Ackley | 1.00 | 2.0 | 0.4581 | 0.4867 | Yes |
| F3 | Ackley | 0.00 | 20.0 | 0.6248 | 0.6607 | Yes |
| F4 | Rosenbrock | 0.00 | 10.0 | 0.07895 | 0.1182 | Yes |
| F5 | Rosenbrock | 0.00 | 10.0 | 0.01150 | 0.00575 | No |
| F6 | Rosenbrock | 1.00 | 5.0 | 0.2419 | 0.2967 | Yes |
| F7 | Rosenbrock | 0.25 | 0.5 | 0.1101 | 0.02572 | No |
| F8 | Rosenbrock | 0.00 | 10.0 | 0.06835 | 0.01731 | No |

## Interpretation

The benchmark test adds useful evidence, but it does not overturn the strongest symbolic findings.

**F4** is the most interesting new benchmark result. A constrained Rosenbrock transformation improves the normalised held-out error from about `0.118` for the BBD 004 quadratic to about `0.079`. This is consistent with the earlier observation that F4 is dominated by nonlinear curvature and interactions rather than by a stable first-order gradient.

**F5** also resembles a Rosenbrock-type geometry under the constrained transformation, but its BBD 004 quadratic remains substantially more predictive. The benchmark comparison therefore supports curved interacting structure without justifying the stronger claim that F5 is Rosenbrock.

**F7 and F8** are similar. Rosenbrock is the best benchmark family in the restricted competition, yet both symbolic reconstructions are much stronger. F8 remains particularly important because its compact linear equation achieves much lower held-out error than any tested benchmark family.

**F1** is better described by a Rastrigin-like transformed feature than by the BBD 004 cubic, but the error remains relatively high. This is weak resemblance, not decryption.

**F2 and F3** show modest Ackley-like resemblance. Their absolute validation errors remain too large for a family-identification claim.

**F6** gains from a Rosenbrock-like feature, but the repeatability evidence from BBD 002 still requires a variability or hidden-state allowance. A deterministic benchmark match cannot explain its non-identical repeated outputs by itself.

## What BBD 005 establishes

The main result is negative as well as positive: none of the tested standard benchmark families explains the strongest functions better than their best BBD 004 equations. The data therefore do not support simply labelling F5, F7 or F8 as transformed standard benchmark functions.

The strongest benchmark-specific lead is F4, where Rosenbrock-like curvature deserves further consideration inside the BBD 006 ensemble.

## Outputs

Running `bbd_005_benchmark_matching.py` creates:

- `outputs/BBD_005_BENCHMARK_COMPETITION.csv`
- `outputs/BBD_005_BENCHMARK_WINNERS.csv`
- `outputs/BBD_005_BENCHMARK_PREDICTIONS.csv`

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_004_symbolic_recovery.py
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_005_benchmark_matching.py
```

## Decision for BBD 006

BBD 006 will combine the evidence from mechanism identification, residual structure, gradient reconstruction, symbolic equations and benchmark-family matching into a function-specific decryption confidence score. It will reward agreement between independent evidence streams and penalise complexity, poor repeatability and contradictory local behaviour.
