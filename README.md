# Imperial BBO Capstone
---
## Author

Dr Nandakumar Theekkootu Pisharam

Consultant Neurologist
Imperial College Business School

Black-Box Optimisation Capstone Portfolio for the Imperial College Business School Artificial Intelligence and Machine Learning Programme.

---
## Module 21 and Week 09 Documentation

Module 21 corresponds to Week 09 of the BBO capstone. The required assignment documents are linked below:

- [Datasheet for the Bayesian Black Box Optimisation Capstone Dataset](Week_09/DATASHEET.md)
- [Model Card for the Bayesian Black Box Optimisation Workflow](Week_09/MODEL_CARD.md)
- [Week 09 analysis and supporting evidence](Week_09/README.md)

---
## Project Overview

This repository documents my work on the Imperial College Business School Black-Box Optimisation (BBO) Capstone Challenge. The project focuses on optimising eight unknown objective functions with varying dimensionality while operating under strict query constraints. Unlike traditional optimisation problems, the mathematical structure of the objective functions remains hidden, requiring optimisation decisions to be made using only information gathered from previous observations.

The challenge mirrors many real-world machine learning problems where systems are expensive to evaluate, poorly understood, or analytically intractable. Rather than relying on explicit equations or gradients, optimisation must be performed through iterative experimentation, evidence-based reasoning and progressive refinement of query selection strategies.

Throughout the capstone, optimisation decisions evolve from exploratory sampling towards increasingly data-driven approaches incorporating concepts from Bayesian optimisation, regression modelling, uncertainty estimation and Support Vector Machines (SVMs).

This repository serves as both a project archive and a technical portfolio documenting the development of optimisation strategies across multiple iterations of the challenge.

---
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

---

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

---
## Inputs and Outputs

### Input Format

Each function accepts a vector of values constrained between 0 and 1. Inputs are submitted to six decimal places.

Example:

```text
0.600000-0.600000
```
---
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
---
These outputs provide the only information available about function behaviour and guide future optimisation decisions.

---
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

---
## Optimisation Timeline

### Week 1 - Baseline Exploration

The first optimisation round focused on broad exploration to establish baseline behaviour across all functions.

### Week 2 - Exploration-Exploitation Balancing

Results revealed substantial variation between functions. Strong-performing regions became candidates for exploitation, while weaker-performing functions required additional exploration.

### Week 3 - Evidence based Query Selection

Query selection became increasingly evidence based. Previous observations informed future sampling decisions, reflecting a transition from heuristic exploration towards model-guided optimisation.
---

## Technical Approach

### Bayesian Optimisation Concepts

The challenge naturally aligns with Bayesian optimisation principles, where observations collected during previous iterations guide future query selection. Rather than relying on exhaustive search, Bayesian optimisation uses prior information and observed results to identify promising regions of the search space.

### Exploration and Exploitation

Exploration involves sampling uncertain or previously untested regions of the search space. Exploitation focuses on refining regions that have already demonstrated strong performance. Effective optimisation requires a balance between these competing objectives.

### Support Vector Machines (SVMs)

Support Vector Machines could potentially classify regions of the search space into high-performing and lower-performing zones. Soft-margin SVMs allow for uncertainty and noisy observations, while kernel SVMs can model non-linear decision boundaries. These techniques may become increasingly useful as the dataset grows.

---

## Current Results

The optimisation process has revealed substantial variation between functions. Some functions demonstrated stable positive performance, while others continued to exhibit weak or negative responses despite exploration of alternative regions.

### Performance Snapshot (Week 2)

| Function | Output | Observation |
|-----------|-----------|-------------|
| Function 1 | ~0 | Near-zero response |
| Function 2 | 0.412 | Stable positive response |
| Function 3 | -0.133 | Weak-performing region |
| Function 4 | -23.120 | Significant deterioration |
| Function 5 | 2308.149 | Strongest performer |
| Function 6 | -2.070 | Continued decline |
| Function 7 | 1.070 | Moderate positive response |
| Function 8 | 9.524 | Stable high-performing region |

---

## Visualisation Gallery

Figure 1 - Function Performance Dashboard

[Insert Performance Snapshot Infographic]

Figure 2 - Function Dimensionality Dashboard

[Insert Function Dimensions Infographic]

Figure 3 - Exploration vs Exploitation Framework

[Insert Exploration-Exploitation Infographic]

Figure 4 - Bayesian Optimisation Workflow

[Insert Bayesian Optimisation Workflow]

Figure 5 - Repository Architecture

[Insert Repository Structure Infographic]

---

## Lessons Learned

### Learning Under Uncertainty

The challenge demonstrated the importance of making optimisation decisions with incomplete information. Because the objective functions remained hidden throughout the competition, every query represented a balance between risk and potential reward.

### Local versus Global Optima

Strong-performing regions do not necessarily represent global optima. Continued exploration remains essential throughout the optimisation process to avoid premature convergence.

### Evidence-Based Decision Making

One of the most valuable lessons was the transition from intuition-driven exploration to evidence-based optimisation. Query selection became progressively informed by historical observations and emerging patterns.

---

## Future Work

Future developments may include:

- Gaussian Process Optimisation
- Expected Improvement acquisition functions
- Probability of Improvement methods
- Thompson Sampling
- Support Vector Machine classification
- Response Surface Modelling
- Kernel-based optimisation approaches
- Advanced visual analytics and dashboards

As additional observations become available, optimisation decisions can become increasingly model-driven, allowing more sophisticated use of Bayesian optimisation and machine learning techniques.

---

## Repository Structure

```bash
Imperial_BBO_Capstone/
|
|-- README.md
|-- data/
|-- figures/
|-- results/
|-- reports/
|-- references/
|
|-- Week_01/
|-- Week_02/
|-- Week_03/
|
|-- notebooks/
|-- optimisation_logs/
|-- visualisations/
|
`-- docs/
```
## References

Imperial College Business School. Artificial Intelligence and Machine Learning Programme.

Scikit-learn Developers. Machine Learning Documentation.

Rasmussen CE, Williams CKI. Gaussian Processes for Machine Learning.

Sutton RS, Barto AG. Reinforcement Learning: An Introduction.
