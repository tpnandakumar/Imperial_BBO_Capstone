# PGC Experiment 003

## Title

Coordinated Multimodal Perception and Emotional Balance

## Objective

Test whether the coordinated PGC perception and emotional cognition layer selects more factually appropriate and emotionally proportionate actions than single-signal or unregulated fusion approaches.

## Synthetic scenario families

- genuine threat with congruent emotional cues
- ambiguous alarm with strong emotional cues
- distress without immediate danger
- hidden risk with calm expression
- benign context with misleading emotional intensity
- conflicting modalities requiring clarification

## Modalities

- language
- vision
- audio
- temporal context

Each observation includes factual signal, emotional signal, confidence, reliability and provenance.

## Comparison arms

1. factual perception only
2. emotional signal only
3. unweighted multimodal fusion
4. reliability-weighted fusion
5. coordinated PGC perception and emotion
6. coordinated PGC without PHCS coherence
7. oracle response

## Primary endpoints

- action accuracy
- urgent-threat recall
- missed-threat rate
- false-escalation rate
- emotional proportionality
- factual override accuracy
- coherence pass rate
- abstention rate
- mean decision latency

## Controls

- deterministic scenario generator
- five fixed seeds
- balanced scenario families
- reliability variation
- modality conflict
- no protected result used to tune an arm during the run

## Evidence status

All results are trial evidence and are not publication evidence until replicated with an independent generator and a governed external multimodal dataset.
