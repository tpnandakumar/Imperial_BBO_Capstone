# PGC Experiment 008F: Multi-Core Braided Ripple-Capture Conduit

## Status

Completed trial evidence. Not publication evidence.

## Design

This experiment compared a protected fusion anchor with several multi-core conduit configurations across Breast Cancer Wisconsin, Wine and Digits. Ten fixed seeds were used with a 60% training split, 20% validation split and 20% protected test split. Protected-test labels were excluded from all tuning.

Five model cores remained semi-independent and were combined through matched configurations:

1. Fusion anchor
2. Parallel multi-core conduit
3. Braided conduit with Zones of Maximum Influence
4. Braided conduit with ripple capture
5. Full braided conduit with Zones of Maximum Influence, ripple capture and dynamic conduit closure with reopening pressure

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fusion anchor | 0.976087 | 0.975107 | 0.973977 | 0.131571 | 0 | 0 | 0 | 0.929825 |
| Parallel multi-core | 0.976087 | 0.975107 | 0.973977 | 0.131571 | 0 | 0 | 0 | 0.929825 |
| **Braided with Zones of Maximum Influence** | **0.976472** | **0.975511** | **0.974303** | 0.131295 | 2 | 0 | **+2** | 0.929825 |
| Braided with ripple capture | 0.975546 | 0.974655 | 0.973510 | 0.130252 | 2 | 1 | +1 | 0.929825 |
| Full braided dynamic system | 0.975838 | 0.974985 | 0.973909 | **0.127809** | 4 | 2 | +2 | 0.929825 |

## Dataset-specific findings

- Breast Cancer Wisconsin: the full dynamic braid improved mean accuracy from 0.959649 to 0.961404.
- Digits: braided ZMI, braided ripple and the full dynamic braid improved mean accuracy from 0.982500 to 0.982778.
- Wine: ripple and dynamic closure reduced mean accuracy from 0.986111 to 0.983333, while braided ZMI preserved the anchor result.

## Interpretation

The strongest accuracy result came from braiding the cores and allocating local influence through Zones of Maximum Influence. This produced two rescues and no harms.

Ripple capture and dynamic closure improved log loss and generated more rescues, but they overreached on the Wine dataset. This indicates that ripple propagation and reopening pressure require stronger domain-conditional control.

The next refinement should preserve the braided ZMI core and allow ripple capture only when a domain-specific rescue model predicts a positive net benefit. Dynamic closure should remain a stress-test and uncertainty mechanism rather than automatically altering the final route.
