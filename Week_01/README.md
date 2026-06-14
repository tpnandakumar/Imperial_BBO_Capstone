# Week 01

Initial Bayesian Black-Box Optimisation submission.

## Objectives
- Analyse starter datasets
- Identify promising regions of the search space
- Select one query point for each function
- Apply Bayesian optimisation principles
- Balance exploration and exploitation

## Functions
- Function 1 (2D)
- Function 2 (2D)
- Function 3 (3D)
- Function 4 (4D)
- Function 5 (4D)
- Function 6 (5D)
- Function 7 (6D)
- Function 8 (8D)

## # Week 1 BBO Query Selection: Step-by-Step Analysis and Calculation

## Objective

The aim of Week 1 was to decide what number **B** to enter into the BBO portal using the initial data **A** supplied by Imperial.

Imperial supplied two files for each function:

* `initial_inputs.npy`
* `initial_outputs.npy`

These were not labelled as "best". They contained several previous observations. I therefore had to identify the strongest observed region myself.

---

## Step 1: Load the initial data

```python
import numpy as np

initial_inputs = np.load("initial_inputs.npy")
initial_outputs = np.load("initial_outputs.npy")
```
`initial_inputs` contained the previously sampled input points.
`initial_outputs` contained the corresponding output values.
---
## Step 2: Find the best observed output
The best observed output was identified using:
```python
best_index = np.argmax(initial_outputs)
```
Mahematically:
```text
best_index = argmax(y)
```
where `y` is the vector of initial outputs.

This finds the position of the highest output value.
---
## Step 3: Retrieve the matching input point
Once the best index was found, the corresponding input was selected:
```python
best_input = initial_inputs[best_index]
best_output = initial_outputs[best_index]
```
This gave the strongest observed point from the supplied Imperial data.
---

## Step 4: Apply local refinement

The submitted query was not chosen randomly. It was selected close to the best observed input using local refinement.

The general rule was:

```text
Submitted query B = best observed input A + small local adjustment δ
```
or:

```text
B = A + δ
```

The adjustment was chosen heuristically to stay close to the strongest known region while testing whether a nearby point might perform better.
---

## Function-by-Function Calculation
### Function 1
Best observed input:

```text
A = [0.73102363, 0.73299988]
```

Submitted query:

```text
B = [0.740000, 0.740000]
```

Adjustment:

```text
δ = B - A
δ = [0.00897637, 0.00700012]
```
Reason:

The submitted point stayed very close to the strongest observed region, with a small upward local refinement in both dimensions.
---

### Function 2
Best observed input:

```text
A = [0.70263656, 0.92656420]
```
Submitted query:

```text
B = [0.720000, 0.940000]
```
Adjustment:

```text
δ = [0.01736344, 0.01343580]
```
Reason:

The query remained near the best supplied observation while slightly increasing both coordinates to explore the surrounding high-performing region.
---

### Function 3
Best observed input:

```text
A = [0.49258141, 0.61159319, 0.34017639]
```

Submitted query:

```text
B = [0.530000, 0.640000, 0.250000]
```

Adjustment:

```text
δ = [0.03741859, 0.02840681, -0.09017639]
```
Reason:
The first two dimensions were increased slightly while the third was reduced. This explored the local neighbourhood around the least negative initial output.
---
### Function 4
Best observed input:
```text
A = [0.57776561, 0.42877174, 0.42582587, 0.24900741]
```
Submitted query:
```text
B = [0.600000, 0.430000, 0.420000, 0.250000]
```
Adjustment:
```text
δ = [0.02223439, 0.00122826, -0.00582587, 0.00099259]
```
Reason:
The submitted point was effectively a rounded local refinement of the best observed point, staying extremely close to the strongest available region.
---
### Function 5
Best observed input:
```text
A = [0.22418902, 0.84648049, 0.87948418, 0.87851568]
```
Submitted query:

```text
B = [0.210000, 0.870000, 0.900000, 0.900000]
```
Adjustment:
```text
δ = [-0.01418902, 0.02351951, 0.02051582, 0.02148432]
```
Reason:
Function 5 had a very strong initial output. The submitted point remained in the same high-performing region while making small exploratory adjustments.
---
### Function 6
Best observed input:
```text
A = [0.72818610, 0.15469257, 0.73255167, 0.69399651, 0.05640131]
```
Submitted query:
```text
B = [0.750000, 0.180000, 0.700000, 0.720000, 0.040000]
```
Adjustment:
```text
δ = [0.02181390, 0.02530743, -0.03255167, 0.02600349, -0.01640131]
```
Reason:
The query stayed close to the strongest observed point while testing a nearby combination in the five-dimensional space.
---
### Function 7

Best observed input:

```text
A = [0.05789554, 0.49167222, 0.24742222, 0.21811844, 0.42042833, 0.73096984]
```
Submitted query:

```text
B = [0.050000, 0.500000, 0.250000, 0.220000, 0.420000, 0.740000]
```
Adjustment:

```text
δ = [-0.00789554, 0.00832778, 0.00257778, 0.00188156, -0.00042833, 0.00903016]
```

Reason:

This was almost a rounded version of the best observed point. It kept the query within the strongest known region while avoiding exact duplication.
---

### Function 8
Best observed input:

```text
A = [0.05644741, 0.06595555, 0.02292868, 0.03878647, 0.40393544, 0.80105533, 0.48830701, 0.89308498]
```
Submitted query:
```text
B = [0.060000, 0.070000, 0.030000, 0.040000, 0.410000, 0.820000, 0.500000, 0.910000]
```
Adjustment:

```text
δ = [0.00355259, 0.00404445, 0.00707132, 0.00121353, 0.00606456, 0.01894467, 0.01169299, 0.01691502]
```
Reason:

The query was a cautious local refinement of the strongest observed point in the eight-dimensional search space.

---
# Week 1 Query Selection Reconstruction

```python
import numpy as np
import pandas as pd

####
# WEEK 1 QUERY SELECTION METHODOLOGY
#
# Purpose:
# Reconstruct how Week 1 submission points were derived from the initial
# observations supplied by Imperial.
#
# Workflow:
# 1. Load supplied observations.
# 2. Identify strongest observed output.
# 3. Retrieve corresponding input vector.
# 4. Compare strongest observed point with submitted query.
# 5. Calculate local refinement adjustment.
####

#
# FUNCTION 1
# 

f1_best_input = np.array([0.73102363, 0.73299988])
f1_submitted = np.array([0.74000000, 0.74000000])

f1_delta = f1_submitted - f1_best_input

print("\nFUNCTION 1")
print("Best Input:", f1_best_input)
print("Submitted Query:", f1_submitted)
print("Delta:", f1_delta)

# 
# FUNCTION 2
# 

f2_best_input = np.array([0.70263656, 0.92656420])
f2_submitted = np.array([0.72000000, 0.94000000])

f2_delta = f2_submitted - f2_best_input

print("\nFUNCTION 2")
print("Best Input:", f2_best_input)
print("Submitted Query:", f2_submitted)
print("Delta:", f2_delta)

# 
# FUNCTION 3
# 

f3_best_input = np.array([
    0.49258141,
    0.61159319,
    0.34017639
])

f3_submitted = np.array([
    0.53000000,
    0.64000000,
    0.25000000
])

f3_delta = f3_submitted - f3_best_input

print("\nFUNCTION 3")
print("Best Input:", f3_best_input)
print("Submitted Query:", f3_submitted)
print("Delta:", f3_delta)

# 
# FUNCTION 4
# 

f4_best_input = np.array([
    0.57776561,
    0.42877174,
    0.42582587,
    0.24900741
])

f4_submitted = np.array([
    0.60000000,
    0.43000000,
    0.42000000,
    0.25000000
])

f4_delta = f4_submitted - f4_best_input

print("\nFUNCTION 4")
print("Best Input:", f4_best_input)
print("Submitted Query:", f4_submitted)
print("Delta:", f4_delta)

# 
# FUNCTION 5
# 

f5_best_input = np.array([
    0.22418902,
    0.84648049,
    0.87948418,
    0.87851568
])

f5_submitted = np.array([
    0.21000000,
    0.87000000,
    0.90000000,
    0.90000000
])

f5_delta = f5_submitted - f5_best_input

print("\nFUNCTION 5")
print("Best Input:", f5_best_input)
print("Submitted Query:", f5_submitted)
print("Delta:", f5_delta)

# 
# FUNCTION 6
# 

f6_best_input = np.array([
    0.72818610,
    0.15469257,
    0.73255167,
    0.69399651,
    0.05640131
])

f6_submitted = np.array([
    0.75000000,
    0.18000000,
    0.70000000,
    0.72000000,
    0.04000000
])

f6_delta = f6_submitted - f6_best_input

print("\nFUNCTION 6")
print("Best Input:", f6_best_input)
print("Submitted Query:", f6_submitted)
print("Delta:", f6_delta)

# 
# FUNCTION 7
# 

f7_best_input = np.array([
    0.05789554,
    0.49167222,
    0.24742222,
    0.21811844,
    0.42042833,
    0.73096984
])

f7_submitted = np.array([
    0.05000000,
    0.50000000,
    0.25000000,
    0.22000000,
    0.42000000,
    0.74000000
])

f7_delta = f7_submitted - f7_best_input

print("\nFUNCTION 7")
print("Best Input:", f7_best_input)
print("Submitted Query:", f7_submitted)
print("Delta:", f7_delta)

#
# FUNCTION 8
# 

f8_best_input = np.array([
    0.05644741,
    0.06595555,
    0.02292868,
    0.03878647,
    0.40393544,
    0.80105533,
    0.48830701,
    0.89308498
])

f8_submitted = np.array([
    0.06000000,
    0.07000000,
    0.03000000,
    0.04000000,
    0.41000000,
    0.82000000,
    0.50000000,
    0.91000000
])

f8_delta = f8_submitted - f8_best_input
print("\nFUNCTION 8")
print("Best Input:", f8_best_input)
print("Submitted Query:", f8_submitted)
print("Delta:", f8_delta)
##
# SUMMARY TABLE
#
summary = pd.DataFrame({
    "Function": ["F1","F2","F3","F4","F5","F6","F7","F8"],
    "Dimensions": [2,2,3,4,4,5,6,8]
})

print("\nSUMMARY")
print(summary)
##
# INTERPRETATION
##
print("""
Week 1 methodology:
1. Analyse supplied observations.
2. Identify strongest observed point.
3. Use strongest point as centre of promising region.
4. Apply local refinement.
5. Submit refined query.
General formula:
Submitted Query = Best Observed Input + Local Refinement Delta
""")
```

## Important Note

This script documents the observed Week 1 decision process.

What it proves mathematically is:

```text
Best observed point
+
Local refinement adjustment
=
Submitted query
```
What it does NOT prove is the exact mental rule used to choose each refinement delta. The evidence suggests that the deltas were selected heuristically to remain close to the strongest observed region while introducing limited exploration.
****

## Overall Week 1 Method

The Week 1 method was:

```text
1. Load the initial observations supplied by Imperial.
2. Identify the highest output using argmax().
3. Retrieve the input vector corresponding to that best output.
4. Use that input vector as the centre of a promising region.
5. Apply a small local adjustment.
6. Submit the adjusted point to the BBO portal.
```
---

## Why this method was used

At Week 1, the true mathematical functions were hidden. Therefore, the safest strategy was not random guessing. The best available evidence came from the supplied initial observations.

The submitted query points were therefore chosen by exploiting the strongest known regions while applying small exploratory perturbations. This allowed testing of nearby points without moving too far away from promising areas.
---

## Conclusion

The Week 1 inputs were derived from the initial data supplied by Imperial. The best observed point was identified mathematically using `argmax(initial_outputs)`. The submitted query was then calculated as a local refinement:

```text
B = A + δ
```

where `A` was the best observed input and `δ` was a small manually selected adjustment designed to explore the local neighbourhood.


## Submitted Queries

| Function | Query                                                                   |
| -------- | ----------------------------------------------------------------------- |
| 1        | 0.740000-0.740000                                                       |
| 2        | 0.720000-0.940000                                                       |
| 3        | 0.530000-0.640000-0.250000                                              |
| 4        | 0.600000-0.430000-0.420000-0.250000                                     |
| 5        | 0.210000-0.870000-0.900000-0.900000                                     |
| 6        | 0.750000-0.180000-0.700000-0.720000-0.040000                            |
| 7        | 0.050000-0.500000-0.250000-0.220000-0.420000-0.740000                   |
| 8        | 0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000 |


## Results

## Results

### Function Outputs

| Function |      Output |
| -------- | ----------: |
| 1        |    0.000000 |
| 2        |    0.454942 |
| 3        |   -0.101836 |
| 4        |   -4.359875 |
| 5        | 1415.876394 |
| 6        |   -0.700155 |
| 7        |    1.319994 |
| 8        |    9.580240 |

### Performance and Strategy Summary

Function 5 produced the strongest response by a substantial margin, suggesting the presence of a highly rewarding region within the search space. Functions 7 and 8 also demonstrated positive performance and emerged as potential candidates for future exploitation. In contrast, Functions 3, 4 and 6 generated negative outputs, indicating weaker-performing regions that would require additional exploration in subsequent rounds.

### Key Observations

* Function 5 was the dominant performer.
* Functions 7 and 8 showed stable positive responses.
* Function 4 exhibited the poorest performance.
* Significant variation existed between functions.
* Initial exploration successfully identified promising search regions.
* Results established the baseline for Week 2 optimisation decisions.

## Strategy Summary

The initial submission used local refinement around the strongest observed regions while maintaining awareness of uncertainty, local maxima and increasing dimensionality. Functions with smoother behaviour were approached using exploitation, whereas higher-dimensional functions required more cautious exploration.

## Reflection

Week 1 focused on broad exploratory sampling across all eight functions. At this stage, no information regarding the underlying response surfaces was available, meaning all optimisation decisions were necessarily heuristic. Query points were selected to provide broad coverage of the search space while attempting to identify potentially promising regions for future investigation.

The results revealed substantial variation in function behaviour. Function 5 produced an exceptionally strong positive response (1415.876), indicating the presence of a highly rewarding region within the search space. Functions 7 and 8 also returned positive objective values, suggesting potential opportunities for further exploitation. In contrast, Functions 3, 4 and 6 produced negative outputs, indicating that the selected regions were unlikely to be optimal and would require additional exploration during subsequent rounds.

A key lesson from Week 1 was the importance of uncertainty management. Without prior observations, optimisation decisions relied heavily on intuition and broad coverage rather than evidence-based reasoning. The objective was therefore not necessarily to maximise performance immediately, but to gather information that could guide future optimisation decisions.

The results established a baseline understanding of each function and provided the foundation for Week 2. Functions demonstrating strong performance became candidates for exploitation, while weaker-performing functions required further exploratory investigation. This marked the transition from purely exploratory sampling towards a more structured exploration–exploitation strategy.


## Contents

This folder will contain:
data/
queries/
reflection/
figures/
notebooks/
results/
analysis/
