# Week_01

## Initial Black Box Optimisation Submission

## 1. Starting point

Week 01 began with the observations supplied by Imperial. I did not know the mathematical form of any of the eight functions, so the first task was to identify the strongest observed input for each function and decide how far to move from it.

The highest supplied output was used as a practical reference point, not as proof of an optimum.

## 2. Method

For each function I identified the index of the highest supplied output and retrieved its matching input vector.

```python
best_index = np.argmax(initial_outputs)
best_input = initial_inputs[best_index]
best_output = initial_outputs[best_index]
```

The recorded calculation was:

```text
submitted query = best observed input + local adjustment
```

The adjustment was a manual judgement. The arithmetic reconstructs the movement exactly but does not claim that the chosen adjustment was mathematically optimal.

## 3. Function 1

Best observed input: `[0.73102363, 0.73299988]`

Submitted query: `[0.740000, 0.740000]`

Adjustment: `[0.00897637, 0.00700012]`

I stayed very close to the strongest supplied observation.

## 4. Function 2

Best observed input: `[0.70263656, 0.92656420]`

Submitted query: `[0.720000, 0.940000]`

Adjustment: `[0.01736344, 0.01343580]`

Both coordinates were increased slightly to test the immediate neighbourhood.

## 5. Function 3

Best observed input: `[0.49258141, 0.61159319, 0.34017639]`

Submitted query: `[0.530000, 0.640000, 0.250000]`

Adjustment: `[0.03741859, 0.02840681, -0.09017639]`

The third coordinate was moved more substantially because the supplied region remained weak.

## 6. Function 4

Best observed input: `[0.57776561, 0.42877174, 0.42582587, 0.24900741]`

Submitted query: `[0.600000, 0.430000, 0.420000, 0.250000]`

Adjustment: `[0.02223439, 0.00122826, -0.00582587, 0.00099259]`

This was a close local probe around the strongest supplied point.

## 7. Function 5

Best observed input: `[0.22418902, 0.84648049, 0.87948418, 0.87851568]`

Submitted query: `[0.210000, 0.870000, 0.900000, 0.900000]`

Adjustment: `[-0.01418902, 0.02351951, 0.02051582, 0.02148432]`

The supplied output was already strong, so I kept the query within the same neighbourhood.

## 8. Function 6

Best observed input: `[0.72818610, 0.15469257, 0.73255167, 0.69399651, 0.05640131]`

Submitted query: `[0.750000, 0.180000, 0.700000, 0.720000, 0.040000]`

Adjustment: `[0.02181390, 0.02530743, -0.03255167, 0.02600349, -0.01640131]`

The five coordinates were adjusted locally rather than moving to an unrelated part of the space.

## 9. Function 7

Best observed input: `[0.05789554, 0.49167222, 0.24742222, 0.21811844, 0.42042833, 0.73096984]`

Submitted query: `[0.050000, 0.500000, 0.250000, 0.220000, 0.420000, 0.740000]`

Adjustment: `[-0.00789554, 0.00832778, 0.00257778, 0.00188156, -0.00042833, 0.00903016]`

This was deliberately close to the strongest supplied observation.

## 10. Function 8

Best observed input: `[0.05644741, 0.06595555, 0.02292868, 0.03878647, 0.40393544, 0.80105533, 0.48830701, 0.89308498]`

Submitted query: `[0.060000, 0.070000, 0.030000, 0.040000, 0.410000, 0.820000, 0.500000, 0.910000]`

Adjustment: `[0.00355259, 0.00404445, 0.00707132, 0.00121353, 0.00606456, 0.01894467, 0.01169299, 0.01691502]`

The eight dimensional query remained close to the best supplied point because there was not yet enough evidence to justify a large move.

## 11. Submitted queries

| Function | Query |
| --- | --- |
| F1 | `0.740000-0.740000` |
| F2 | `0.720000-0.940000` |
| F3 | `0.530000-0.640000-0.250000` |
| F4 | `0.600000-0.430000-0.420000-0.250000` |
| F5 | `0.210000-0.870000-0.900000-0.900000` |
| F6 | `0.750000-0.180000-0.700000-0.720000-0.040000` |
| F7 | `0.050000-0.500000-0.250000-0.220000-0.420000-0.740000` |
| F8 | `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000` |

## 12. What the calculation establishes

The reconstruction shows the numerical distance between each strongest supplied point and the submitted query. It does not prove that the selected adjustment was optimal.

## 13. What I learned

Week 01 gave me a baseline for all eight functions and my first returned results from points I had selected myself. Those results became the basis for deciding where Week 02 should stay local and where it should move further away.

## 14. Automation decision

The strongest supplied observations were identified computationally. The local adjustments and final submitted queries were manually selected.

## 15. Reference

Imperial College Business School, Black Box Optimisation Capstone starter data and project materials.