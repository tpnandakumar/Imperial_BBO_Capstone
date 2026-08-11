# Extended Research and Validation

## Purpose

The core of this repository documents the Imperial Bayesian Black Box Optimisation capstone. The assessed work is represented by the weekly query submissions, returned results, analytical code, experiment records, reproducibility material, model documentation and supporting notebooks.

During the capstone, additional questions arose about how optimisation decisions could be tested more rigorously, how computational behaviour could be validated, and how candidate selection could be examined beyond a single returned objective value. These questions led to two extended research streams, PGC and PFRAMOS.

The extended work records research and validation that developed from the capstone and is presented separately from the core BBO submission.

## PGC

PGC developed as a validation and experimental stream concerned with computational behaviour, reproducibility and formal checking. The material currently includes executable experiments, validation protocols, system architecture documentation and monitored formal proof workflows.

One example is the 008CL-B formal proof workflow, which was configured to run through GitHub Actions and to preserve verified result artefacts. This work reflects an attempt to move from informal confidence in computational output towards explicit verification and reproducible evidence.

PGC therefore contributes to the capstone primarily as an example of how questions about reliability and validation emerging during optimisation can lead to more formal experimental methods.

## PFRAMOS

PFRAMOS developed as a broader experimental framework for examining optimisation behaviour and computational strategy. Its current material includes historical data auditing, walk forward analysis, candidate experiments, technical sweeps, training studies and supporting audit components.

Within the context of this capstone, its relevance lies in the attempt to examine optimisation decisions across time rather than judging a query only by its immediate returned value. Historical trajectories, candidate comparison and repeated validation provide a wider perspective on robustness and strategy selection.

PFRAMOS subsequently developed beyond the immediate requirements of the capstone. Material concerned with broader architecture, training, publication planning and later research directions forms part of the extended research arising from the project rather than the assessed BBO requirements.

## Relationship to the assessed capstone

The distinction used throughout this repository is:

```text
Imperial BBO Capstone
|
|-- Core assessed work
|   |-- Weekly BBO submissions and returned results
|   |-- Analysis and reproducibility code
|   |-- Experiment records
|   |-- Notebooks and visualisations
|   |-- Datasheet and model documentation
|   `-- Final capstone analysis
|
`-- Extended research arising from the capstone
    |-- PGC: validation, experimental checking and formal verification
    `-- PFRAMOS: historical analysis, candidate evaluation and broader strategy research
```

The extended research does not alter the submitted BBO results and is not presented as evidence that the underlying black box functions were known. The competition outputs remain the authoritative observations for the optimisation challenge.

## Evidence and limitations

The presence of an experiment, workflow or research proposal does not by itself establish that a method is superior to Bayesian optimisation or to another optimisation strategy. The corresponding experiment and recorded results define the evidence available for each claim.

Later PGC and PFRAMOS developments are identified separately from the methods recorded in the weekly BBO rounds. This distinction preserves the chronology of the capstone and separates observed results from subsequent methodological development.

## Why the extended work is retained

The additional research is retained to make the development process transparent. The capstone began as a constrained black box optimisation problem, but repeated experimentation raised broader questions about reliability, robustness, validation and strategy selection. PGC and PFRAMOS document how those questions were explored beyond the minimum submission requirements.

For assessment, the weekly BBO folders and capstone experiment records remain the primary evidence. PGC and PFRAMOS provide supplementary evidence of the research and engineering questions that emerged from that work.