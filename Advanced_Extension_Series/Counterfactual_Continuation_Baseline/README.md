# Counterfactual Continuation Baseline

## Purpose

This folder preserves the first post-capstone continuation analysis that was developed immediately after the thirteen authorised BBO rounds closed. It is not part of the assessed Week 13 record and it does not create a Round 14 result.

The baseline asked a counterfactual question: if another evaluation opportunity existed, which functions would still justify optimisation and which should stop? That question led directly to the more systematic Advanced Extension Series and SOC, the Surrogate Optimisation Competition.

## Relationship to SOC

This baseline uses direct local reasoning from the verified thirteen-round history. SOC extends that idea by making several surrogate model families compete using held-out predictive performance before candidate optimisation begins.

The baseline therefore has a clear research role:

**Week 13 verified evidence -> counterfactual continuation baseline -> SOC -> Optimisation Extension Series**

## Files

- `SMART_ADVANCED_ANALYSIS_AND_EXTENSION.md`: initial function-specific continuation analysis
- `SMART_ADVANCED_STOPPING_POLICY.md`: Explore, Exploit, Extend and Stop policy
- `smart_advanced_extension.py`: reproducible F2 local interpolation and candidate construction
- `smart_advanced_extension_candidates.csv`: candidate table with explicit non-observed-output status

## Evidence boundary

No value in this folder is presented as an authorised BBO output beyond Round 13. Candidate coordinates remain research proposals unless they receive an external verified evaluation. The official assessed optimisation history remains in `Week_01` through `Week_13`.