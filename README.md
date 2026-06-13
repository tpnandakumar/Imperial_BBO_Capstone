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
