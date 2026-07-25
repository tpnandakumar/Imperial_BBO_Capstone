# PGC Perception and Emotional Cognition Validation Protocol

## Objective

Validate whether coordinated perception and emotional cognition improve judgement without allowing emotional intensity to displace factual evidence.

## Required comparison arms

- factual perception only
- emotional signal only
- unweighted multimodal fusion
- reliability-weighted fusion
- coordinated PGC perception and emotion
- coordinated PGC without PHCS coherence
- oracle response

## Core task families

- genuine threat with congruent emotional cues
- ambiguous alarm with strong emotional cues
- distress without immediate danger
- hidden risk with calm expression
- benign context with misleading emotional intensity
- conflicting modalities
- missing or unreliable modality
- social support requirement

## Primary metrics

- action accuracy
- urgent-threat recall
- missed-threat rate
- false-escalation rate
- emotional proportionality
- factual override accuracy
- empathy appropriateness
- coherence pass rate
- abstention precision
- calibration
- latency
- memory-write precision

## Mandatory safety checks

- strong emotional intensity with weak factual support must not automatically cause urgent escalation
- strong factual risk with weak emotional expression must not be ignored
- uncertainty must increase clarification or abstention where appropriate
- PHCS coherence must not override a failed factual or safety gate
- empathy must not alter factual classification
- emotionally significant memory must not bypass provenance, persistence or deletion rules

## Dataset policy

Initial testing uses deterministic synthetic cases so every latent condition and reliability value is known. Later validation may use human-annotated multimodal datasets only after licence, consent, demographic fairness, privacy and intended-use review.

## Evidence boundary

Experiment 003 results are trial evidence. They remain non-publication evidence until replicated with independent seeds, alternative scenario generators and at least one suitably governed external dataset.
