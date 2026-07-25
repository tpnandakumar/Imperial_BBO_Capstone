# PGC System Architecture

## 1. System identity

PGC means Pisharam Genius Configuration in Computational Cognition.

PGC is a configurable cognitive system in which specialised modules are selected, combined, monitored and released according to the active task. No module receives permanent primacy. Temporary terminal authority is assigned to the node with the strongest validated evidence for the current purpose.

## 2. Cognitive flow

Input

→ perception and representation

→ task decomposition

→ capability candidacy

→ PIMF influence diagnosis

→ PFRAMOS route optimisation

→ PHCS coherence evaluation

→ memory read and write decision

→ reasoning or action

→ uncertainty and robustness validation

→ evidence record

→ output or controlled abstention

## 3. Architectural layers

### 3.1 Perception

- language
- code
- vision
- video
- speech
- environmental audio
- tabular data
- time series
- multimodal combinations

### 3.2 Sequence cognition

- Mamba-2 baseline
- Mamba-3 SISO candidate
- Mamba-3 MIMO candidate
- attention-based control models
- temporal tracking
- state-space and recurrent alternatives

### 3.3 Memory

- working memory from the common pool
- reference-aware retained memory
- Titans test-time long-term memory
- MIRAS retention and update variants
- persistent task memory
- protected evidence memory

### 3.4 Reasoning

- state tracking
- induction
- retrieval
- arithmetic
- causal analysis
- planning
- optimisation
- cross-modal integration
- hypothesis generation and falsification

### 3.5 Regulation

- dynamic priority P1 to P15 with sublevels
- PHCS coherence from -1 to +1
- uncertainty and robustness gates
- PIMF persistence and influence states
- memory capacity and expiry control
- PCECE compute and energy control

### 3.6 Learning

- controlled training
- supervised fine-tuning
- test-time learning
- smooth handover
- continual learning
- shadow validation
- protected evaluation

### 3.7 Execution

- local CPU trials
- NVIDIA CUDA
- AMD GPU through supported PyTorch routes
- TorchTitan distributed execution
- AWS Trainium through Neuron

## 4. Governing selection objective

PGC selects a configuration in this order:

1. task fitness
2. evidential validity
3. coherence
4. robustness
5. uncertainty reduction
6. safety and ethical acceptability
7. compute and energy efficiency

A cheaper route cannot replace a materially better validated route merely because it is cheaper. Efficiency optimisation begins after minimum quality and safety requirements are met.

## 5. Memory governance

- all working memory is reclaimable
- the common pool is filled first when more than half of total memory is unused
- active high and medium or low priorities may draw from the common pool when purpose and evidence justify it
- inactive memory returns to the common pool
- persistent memory requires source, purpose, retention and deletion metadata
- surprising information is not automatically retained
- PIMF persistence and PHCS coherence must support promotion to retained memory

## 6. Evidence classes

- discovery evidence
- exploratory trial evidence
- shadow-validation evidence
- candidate-for-promotion evidence
- replicated publication evidence

These classes must never be merged silently.

## 7. PGC version 0.1 boundary

Version 0.1 provides configuration, routing, validation and governance scaffolding. It does not yet implement a full multimodal foundation model or prove hyper-cognitive performance.
