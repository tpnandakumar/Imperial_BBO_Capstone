# BBD: Black Box Decryption

## What BBD means

BBD stands for Black Box Decryption. It began after the official thirteen-round capstone had finished.

During the capstone, we knew which numbers had been submitted and which scores had been returned, but we did not know the hidden equations. BBD uses that completed history to ask a simple question:

> What kind of mathematical rule could have produced these results?

BBD does not change the original results. It does not claim that a predicted value came from the Imperial evaluator. It also does not claim that an exact equation has been found unless the evidence can prove it.

## A simple example

Imagine trying to understand a locked machine. You can choose the settings on its dials and observe the number shown on its screen. After several trials, you may learn that one dial matters greatly, two dials move together or the same setting sometimes produces a different answer.

You may then build several possible explanations and check which one predicts earlier unseen results most accurately. That is what BBD does with the eight hidden functions.

## How the checks are made

BBD follows four basic steps:

1. Build several possible explanations from the earlier results.
2. Ask each explanation to predict the next historical result without seeing it first.
3. Compare the prediction with the result that was actually returned.
4. Keep, revise or reject the explanation according to the evidence.

The order of the thirteen rounds is preserved. This matters because a fair test must use only the information that was available at that point in time.

## What has been learned so far

| Function | Current finding | What remains uncertain |
| --- | --- | --- |
| F4 | The surface is repeatable and strongly nonlinear. A smooth Matérn model currently predicts it best | The exact equation and its behaviour far from the tested path |
| F5 | The surface is smooth, repeatable and strongly directed towards a boundary | Whether the local pattern describes the whole function |
| F6 | The same coordinate can return different results | Whether this is random variation, hidden state or another unobserved cause |
| F7 | A simple quadratic description works well in the tested region | Whether it remains valid in untested parts of the search space |
| F8 | A low-complexity description performs well | Whether the apparent simplicity is global or limited to the sampled path |
| F1, F2 and F3 | Their historical behaviour has been examined in the shared studies | Dedicated function-specific decryption is still required |

## Have the hidden functions been decrypted?

BBD has successfully narrowed the likely behaviour of several functions. It has found useful and reproducible explanations for parts of the observed search space.

It has not recovered the exact hidden equations. It has also not proved the global optimum of any function. The correct conclusion is therefore:

- useful function-specific decryption has been achieved;
- several weak explanations have been rejected;
- the strongest remaining explanations have been identified;
- exact mathematical recovery remains unproved.

## Research stages

### BBD 001 to BBD 009: building the method

The first nine studies compared static, time-related, movement-related and state-related explanations. They examined repeated coordinates, changes between rounds, simple equations, known benchmark shapes and forward prediction.

The main lesson was that fitting the full history well is not enough. A credible explanation must also predict later historical results using only earlier observations.

- [BBD 002: residual structure and repeatability](BBD_002_TEMPORAL_RESIDUALS.md)
- [BBD 003: directional reconstruction](BBD_003_GRADIENT_RECONSTRUCTION.md)
- [BBD 004: equation recovery](BBD_004_SYMBOLIC_RECOVERY.md)
- [BBD 005: benchmark-family matching](BBD_005_BENCHMARK_MATCHING.md)
- [BBD 006: confidence ranking](BBD_006_DECRYPTION_CONFIDENCE.md)
- [BBD 007: BBD versus SOC prediction challenge](BBD_007_BBD_VS_SOC_CHALLENGE.md)
- [BBD 008: tests designed to separate competing explanations](BBD_008_DISCRIMINATORY_QUERY_DESIGN.md)
- [BBD 009: confidence updated using forward evidence](BBD_009_PROSPECTIVE_CONFIDENCE.md)

### BBD 010 to BBD 017: Function 6

These studies examined why Function 6 returned different outputs at repeated coordinates. A strong coordinate-based surface was found, but the remaining variation could not be explained reliably by the tested time, movement or compressed context measures.

- [BBD 010: F6-specific decryption](BBD_010_F6_SPECIFIC_DECRYPTION.md)
- [BBD 011: F6 residual decomposition](BBD_011_F6_RESIDUAL_DECOMPOSITION.md)
- [BBD 012: F6 stochastic or deterministic test](BBD_012_F6_STOCHASTIC_DETERMINISTIC.md)
- [BBD 013: F6 latent-context test](BBD_013_F6_LATENT_VARIABLE_RECONSTRUCTION.md)

### BBD 018 to BBD 020: Function 7

Function 7 was best described by a lightly regularised quadratic model within the historical region. Later tests simplified the explanation and identified coordinates that could separate competing global interpretations.

- [BBD 018: F7-specific decryption](BBD_018_F7_SPECIFIC_DECRYPTION.md)
- [BBD 019: F7 quadratic simplification](BBD_019_F7_QUADRATIC_SIMPLIFICATION.md)
- [BBD 020: F7 falsification design](BBD_020_F7_DISCRIMINATORY_FALSIFICATION.md)

### BBD 021 and BBD 022: Function 8

Function 8 showed comparatively simple structure over the observed path. The follow-up study compared that explanation with the strongest competing surrogate and designed tests for the remaining disagreement.

- [BBD 021: F8-specific decryption](BBD_021_F8_SPECIFIC_DECRYPTION.md)
- [BBD 022: F8 SOC rechallenge](BBD_022_F8_SOC_RECHALLENGE_FALSIFICATION.md)

### BBD 023 and BBD 024: Function 5

Function 5 was highly predictable along the historical path. A Matérn model performed best, while a quadratic equation remained a useful local approximation. The later challenge showed that these explanations disagree sharply in untested regions.

- [BBD 023: F5-specific decryption](BBD_023_F5_SPECIFIC_DECRYPTION.md)
- [BBD 024: F5 SOC rechallenge and falsification](BBD_024_F5_SOC_RECHALLENGE_FALSIFICATION.md)

### BBD 025: Function 4

BBD 025 tested the earlier suggestion that Function 4 might resemble a Rosenbrock function. The test selected the Rosenbrock settings inside each historical training window, which prevented later results from influencing earlier predictions.

The Matérn model ranked first with a normalised forward error of `0.021834`. The Rosenbrock explanation ranked fifth at `0.032816`. The Rosenbrock shape remains a useful clue, but it is not the strongest current explanation.

The best F4 coordinate was tested in Weeks 1, 12 and 13. It returned exactly the same result each time. This supports a stable coordinate-based surface over the observed region.

- [BBD 025: F4-specific decryption](BBD_025_F4_SPECIFIC_DECRYPTION.md)

## Why new evaluator results would help

Several explanations can fit the same short historical path. The most useful new test is not another point close to the known best. It is a point where the remaining explanations predict clearly different results.

A genuine evaluator result at such a point could reject one explanation and support another. Without new authorised evaluations, BBD can rank the explanations and design the best tests, but it cannot prove the exact global equation.

## Reproducing the work

Install the required packages from the repository root:

```bash
python -m pip install -r Advanced_Extension_Series/BBD_Black_Box_Decryption/requirements-bbd.txt
```

Each numbered script can then be run directly. For example:

```bash
python Advanced_Extension_Series/BBD_Black_Box_Decryption/bbd_025_f4_specific_decryption.py
```

The scripts write their result tables to the `outputs` folder. The GitHub workflow also runs the complete BBD sequence and collects the output tables.

## Evidence boundary

All BBD work is post-capstone research. Weeks 01 to 13 remain the official assessed record. BBD predictions, proposed coordinates and reconstructed equations are not presented as Imperial evaluator results.
