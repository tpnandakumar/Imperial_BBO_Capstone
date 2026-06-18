# Week_04

# Contents

Introduction
Week 4 Results
Comparison of Week 3 and Week 4 Performance
Query Selection Strategy
Exploration vs Exploitation Analysis
Reflection on Week 5 Query Selection
Functional Ranking Evolution
High-Performing Region Identification
Decision Matrix and Resource Allocation
Information Gain Analysis
Computational Analysis and Coding Implementation
Conclusion


## Introduction

The Week 4 optimisation round built on the accumulated evidence from Weeks 1–3. By this stage, the search process had moved beyond broad exploratory sampling and had become increasingly evidence driven. Previous outputs had identified clear differences between functions, including strong exploitation candidates, stable positive performers, declining functions requiring monitoring, and uncertain low-output regions requiring further exploration.

The main objective of Week 4 was to use this evidence to select query points that balanced exploitation, monitoring and targeted exploration. Strong-performing functions were prioritised for local refinement, while unstable or poorly understood functions were assigned exploratory movements to improve understanding of the search landscape. This reflected the broader principle of Bayesian optimisation, where query selection should maximise both expected improvement and information gain.

## Week 4 Results
