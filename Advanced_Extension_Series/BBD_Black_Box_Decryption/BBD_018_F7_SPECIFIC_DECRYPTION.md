# BBD 018: F7-Specific Decryption

## Purpose

BBD 018 begins function-specific decryption of F7 after F6 reached the current evidence ceiling available from the thirteen-round history.

F7 is a strong candidate because earlier stages found very high gradient coherence and strong retrospective symbolic structure, while BBD 007 showed that SOC still predicted F7 slightly better prospectively. This stage therefore asks whether F7 is best described by a compact linear surface, a quadratic interaction surface, or a flexible Gaussian Process when all models are judged by chronological walk-forward prediction.

## Competing models

The experiment compares:

- Matérn 2.5 Gaussian Process;
- linear ridge models;
- quadratic ridge models with several regularisation strengths;
- sparse quadratic Lasso models.

All comparisons preserve chronological ordering. Each prediction is made from earlier rounds only.

## Structural evidence carried forward

BBD 003 reported a global-to-recent gradient cosine of approximately `0.975357` for F7, indicating unusually stable directional structure across the sampled trajectory.

BBD 004 produced a strong quadratic retrospective reconstruction, although its 27 retained terms reduced confidence that the recovered expression represented the exact hidden equation.

BBD 007 then provided the necessary caution: SOC achieved normalised prospective MAE of about `0.195676`, compared with about `0.291394` for the then-current BBD mechanism.

BBD 018 therefore does not treat the earlier quadratic equation as established truth. It re-tests simpler and more regularised coordinate-only mechanisms prospectively.

## Repeatability

The script also checks exact repeated coordinates. Any non-identical outputs would prevent exact coordinate-only determinism from being claimed.

## Interpretation rule

A model can be called a strong F7 structural candidate only if it combines:

1. low chronological walk-forward error;
2. stable coordinate-effect signs;
3. no unresolved repeated-coordinate contradiction;
4. substantially simpler structure than the earlier 27-term quadratic where possible.

Even then, exact function recovery remains false without independent discriminatory evaluations away from the historical trajectory.
