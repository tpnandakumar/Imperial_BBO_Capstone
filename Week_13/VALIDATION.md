# Week 13 Validation Record

## Source checks

The final round record contains eight submitted coordinate vectors and eight returned objective values. Function dimensions are 2, 2, 3, 4, 4, 5, 6 and 8. All submitted coordinates are within the permitted interval from 0 to 1.

## Numerical integrity

Week 13 outputs are stored exactly as supplied:

- Function 1: `0.025559285339829783`
- Function 2: `0.6413430885133908`
- Function 3: `-0.05685061601567621`
- Function 4: `-4.359874926582439`
- Function 5: `4440.957216598753`
- Function 6: `-0.6071562248604215`
- Function 7: `1.3809299933612855`
- Function 8: `9.58024`

Exact Week 12 to Week 13 differences are calculated with decimal arithmetic in the analysis workflow.

## Fixed input checks

Several final inputs repeat earlier coordinates. Functions 1, 4, 7 and 8 reproduced their established best values exactly.

Function 6 requires separate treatment. The coordinate `0.700000,0.200000,0.700000,0.700000,0.200000` appears in Weeks 3, 12 and 13 but returned three different values: `-0.648848297397347`, `-0.7078316130911375` and `-0.6071562248604215`.

The verified observation is response variability at an identical recorded coordinate. The available data do not establish whether the cause is stochasticity, hidden context, evaluation noise or another platform property.

## Validation boundary

The final results identify the strongest observed values in the thirteen submitted rounds. They do not prove that any of those points is a global optimum of the hidden function.
