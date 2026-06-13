# Imperial BBO Capstone

Black-Box Optimisation Capstone Portfolio for the Imperial College Business School Artificial Intelligence and Machine Learning Programme.

## Project Overview

This repository documents my work on the Imperial College Business School Black-Box Optimisation (BBO) Capstone Challenge. The project focuses on optimising eight unknown objective functions with varying dimensionality while operating under strict query constraints. Unlike traditional optimisation problems, the mathematical structure of the objective functions remains hidden, requiring optimisation decisions to be made using only information gathered from previous observations.

The challenge mirrors many real-world machine learning problems where systems are expensive to evaluate, poorly understood, or analytically intractable. Rather than relying on explicit equations or gradients, optimisation must be performed through iterative experimentation, evidence-based reasoning and progressive refinement of query selection strategies.

Throughout the capstone, optimisation decisions evolve from exploratory sampling towards increasingly data-driven approaches incorporating concepts from Bayesian optimisation, regression modelling, uncertainty estimation and Support Vector Machines (SVMs).

This repository serves as both a project archive and a technical portfolio documenting the development of optimisation strategies across multiple iterations of the challenge.

## Real-World Relevance

Black-box optimisation is widely used across machine learning, engineering, robotics, finance, pharmaceutical development and healthcare. Many practical optimisation problems involve systems whose underlying mathematical relationships are unknown, computationally expensive to evaluate, or inaccessible to direct analytical methods.

Applications include:

- Hyperparameter optimisation of machine learning models
- Reinforcement learning policy optimisation
- Drug discovery and molecular design
- Engineering design optimisation
- Resource allocation and scheduling
- Clinical decision-support systems

As a consultant neurologist with an interest in healthcare artificial intelligence, the concepts explored within this project have direct relevance to future work involving referral triage systems, diagnostic support tools and optimisation of healthcare resources under uncertainty.


## Problem Statement

The challenge consists of eight independent black-box functions ranging from two to eight dimensions. The mathematical form of each function is hidden from participants.

Each optimisation round requires the submission of one query point per function. Following evaluation, the optimisation platform returns an objective value representing the quality of the selected query location.

The objective is to maximise performance while operating under conditions of uncertainty, limited observations and restricted query budgets.

Key challenges include:

- Unknown response surfaces
- Limited sampling opportunities
- High-dimensional search spaces
- Potential local optima
- Absence of gradient information
- Uncertainty regarding feature interactions

Success depends on progressively improving query selection using evidence gathered from previous optimisation rounds.

## Inputs and Outputs

### Input Format

Each function accepts a vector of values constrained between 0 and 1. Inputs are submitted to six decimal places.

Example:

```text
0.600000-0.600000
```

### Function Dimensionality

The challenge contains eight functions ranging from two to eight dimensions.

| Function | Dimensions |
|-----------|-----------|
| Function 1 | 2 |
| Function 2 | 2 |
| Function 3 | 3 |
| Function 4 | 4 |
| Function 5 | 4 |
| Function 6 | 5 |
| Function 7 | 6 |
| Function 8 | 8 |

Increasing dimensionality expands the search space and increases optimisation complexity.

### Output Format

Each submitted query returns a numerical objective value.

Example:

```text
2308.148
```

These outputs provide the only information available about function behaviour and guide future optimisation decisions.


## Challenge Objectives

### Primary Goal

The primary objective is to maximise the output returned by each black-box function.

### Constraints

Key constraints include:

- Unknown response surfaces
- Limited observations
- One query per function per round
- No gradient information
- Potential local optima
- High-dimensional search spaces

### Success Criteria

Success depends on progressively improving query quality while maintaining an effective balance between exploration and exploitation.


## Optimisation Timeline

### Week 1 – Baseline Exploration

The first optimisation round focused on broad exploration to establish baseline behaviour across all functions.

### Week 2 – Exploration-Exploitation Balancing 

Results revealed substantial variation between functions. Strong-performing regions became candidates for exploitation, while weaker-performing functions required additional exploration.

### Week 3 – Evidence based Query Selection

Query selection became increasingly evidence based. Previous observations informed future sampling decisions, reflecting a transition from heuristic exploration towards model-guided optimisation.
