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

BBD 005 will compare the strongest reconstructed behaviours with known optimisation benchmark families under coordinate and output transformations. Agreement will be judged by out-of-sample predictive behaviour, not visual similarity alone.
