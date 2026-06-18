"""
Week 3 Computational Analysis

This script reproduces the quantitative analysis
reported in Week 3 of the Imperial BBO challenge.

Functions:
- Output change calculations
- Percentage improvements
- Function ranking
- Week 4 strategy allocation

Author: Nandakumar Pisharam
"""

import pandas as pd
import numpy as np

data = {
    "Function": ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    "Week1": [0.000000, 0.454942, -0.101836, -4.359875, 1415.876000, -0.700155, 1.319994, 9.580240],
    "Week2": [0.000000, 0.412137, -0.133256, -23.120154, 2308.149000, -2.070246, 1.069658, 9.524100],
    "Week3": [0.025559, 0.140988, -0.127870, -14.554029, 2840.990000, -0.648848, 0.896603, 9.442960],
}

df = pd.DataFrame(data)

df["Change_W1_to_W3"] = df["Week3"] - df["Week1"]
df["Change_W2_to_W3"] = df["Week3"] - df["Week2"]

df["Percent_Change_W2_to_W3"] = (
    df["Change_W2_to_W3"] / df["Week2"].abs().replace(0, pd.NA)
) * 100

df["Week3_Rank"] = df["Week3"].rank(ascending=False, method="min").astype(int)

def assign_strategy(row):
    if row["Function"] == "F5":
        return "Exploit"
    elif row["Function"] == "F8":
        return "Monitor / cautious exploitation"
    elif row["Function"] in ["F2", "F7"]:
        return "Monitor and refine"
    else:
        return "Explore"

df["Week4_Strategy"] = df.apply(assign_strategy, axis=1)

print("\nWeek 3 Analysis Summary\n")
print(df.to_string(index=False))

df.to_csv("week3_analysis_summary.csv", index=False)

print("\nSaved output file: week3_analysis_summary.csv")
