# BBD 004: Symbolic Equation Recovery

## Purpose

BBD 004 tests whether the thirteen-round observations can be represented by compact explicit polynomial equations rather than only by flexible surrogate models.

This is an equation-recovery experiment, not a claim that the Imperial hidden functions have been exactly identified.

## Candidate equation families

For each function, the experiment compares regularised polynomial equations using the original coordinates:

- degree 1, linear terms;
- degree 2, linear, squared and interaction terms;
- degree 3 for F1 to F3 only, where the polynomial library remains small enough to justify testing with thirteen observations.

Higher-dimensional cubic libraries are deliberately excluded because the number of possible terms would be far larger than the available evidence.

## Model selection

Each candidate equation is tested by leave-one-observation-out validation. Ridge regularisation is searched over a fixed range of strengths.

The selection score combines:

```text
normalised validation MAE + mild complexity penalty
```

The complexity term acts as a minimum-description-length safeguard. A larger polynomial library must produce a meaningful validation improvement before it can displace a simpler equation.

## BBD 004 results

| Function | Selected family | Normalised LOOCV MAE | Training R2-like | Interpretation |
| --- | --- | ---: | ---: | --- |
| F1 | cubic | 0.697160 | 0.781024 | weak predictive recovery despite extra complexity |
| F2 | quadratic | 0.486712 | 0.841823 | moderate but not yet convincing equation recovery |
| F3 | linear | 0.660674 | 0.010017 | no useful compact polynomial recovery |
| F4 | quadratic | 0.118235 | 0.999917 | strong nonlinear reconstruction, suggesting curvature and interactions rather than a stable first-order gradient |
| F5 | quadratic | 0.005749 | 1.000000 | exceptionally strong reconstruction on the observed history, but the near-zero regularisation and 14-term library require independent challenge testing |
| F6 | quadratic | 0.296721 | 0.992002 | good in-sample reconstruction but weaker held-out performance, consistent with repeatability uncertainty |
| F7 | quadratic | 0.025723 | 0.999941 | very strong predictive reconstruction, although the 27-term equation is not yet parsimonious |
| F8 | linear | 0.017307 | 0.999988 | strongest interpretable result: a simple eight-term linear equation predicts the observed history extremely well |

## Most important findings

### F8: strongest compact decryption candidate

F8 selected a linear equation rather than a quadratic surface:

```text
y_hat = 10.97788502
        + 0.116539399*x1
        + 0.1910685871*x2
        + 0.05156106242*x3
        + 0.8145764472*x4
        + 0.3239666929*x5
        - 1.411856604*x6
        - 0.7715635142*x7
        - 0.04556514659*x8
```

Its normalised leave-one-out MAE was approximately `0.0173`, while its training R2-like value was approximately `0.999988`. The coefficient signs also agree closely with the stable gradient directions identified in BBD 003, especially the strong negative influence of x6 and x7.

This makes F8 the clearest current example of an explicit, compact mathematical reconstruction. It remains a recovered predictive equation, not a proven identity for the hidden Imperial function.

### F5: strongest numerical equation recovery

F5 selected a quadratic response with normalised leave-one-out MAE of approximately `0.00575`. This is the lowest predictive error in BBD 004 and agrees with the exceptionally coherent gradient evidence from BBD 003.

The fitted quadratic contains 14 non-trivial terms and uses almost no ridge shrinkage. The result is therefore highly promising but must be challenged for interpolation risk and parameter instability before being treated as a genuine structural decryption.

### F7: strong but more complex

F7 selected a quadratic equation with normalised leave-one-out MAE of approximately `0.0257`. This strongly supports the directional structure found in BBD 003, but the fitted library contains 27 non-trivial terms. BBD 005 and later sparsification should determine whether a much simpler equivalent form exists.

### F4: nonlinear structure revealed

F4 was weak under the first-order gradient model in BBD 003 yet achieved normalised leave-one-out MAE of approximately `0.118` with a quadratic equation. This combination is important. It suggests that F4 may be dominated by curvature and interactions, so a single global gradient was the wrong structural description rather than evidence that no structure existed.

## Why the equations remain provisional

With only thirteen adaptive observations, many mathematical expressions can interpolate or nearly interpolate the same points. A low training error is therefore not sufficient evidence of decryption.

BBD 004 gives greatest weight to:

- leave-one-out prediction error;
- agreement with the directional evidence from BBD 003;
- equation complexity;
- consistency with repeated-coordinate evidence from BBD 002.

F6 requires particular caution because repeated coordinates have produced non-identical outputs.

## Outputs

Running `bbd_004_symbolic_recovery.py` creates:

- `outputs/BBD_004_EQUATION_COMPETITION.csv`
- `outputs/BBD_004_RECOVERED_EQUATIONS.csv`
- `outputs/BBD_004_EQUATION_TERMS.csv`

The reported compact equations are reconstructions from the observed history. They are not presented as the original Imperial equations.

## Reproduction

From the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_004_symbolic_recovery.py
```

## Decision for BBD 005

BBD 005 will compare the strongest reconstructed behaviours with known optimisation benchmark families under coordinate and output transformations. The primary structural targets are F5, F7 and F8, with F4 now added as a nonlinear candidate. Agreement will be judged by held-out predictive behaviour and parameter stability, not visual similarity alone.
