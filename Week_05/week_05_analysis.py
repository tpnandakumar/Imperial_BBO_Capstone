"""
Week 05 Analysis Tool
Imperial BBO Capstone
"""

import pandas as pd

results = {
    "F1": 0.012779642669914939,
    "F2": 0.28016822307722516,
    "F3": -0.11392206377710448,
    "F4": -27.44051496086922,
    "F5": 3682.2110623386798,
    "F6": -1.073875453695542,
    "F7": 1.3809299933612855,
    "F8": 9.5113,
}

strategy = {
    "F1": "Explore",
    "F2": "Refine",
    "F3": "Explore",
    "F4": "Explore",
    "F5": "Exploit",
    "F6": "Explore",
    "F7": "Refine",
    "F8": "Monitor",
}

df = pd.DataFrame(
    [
        {
            "Function": function,
            "Week_05_Output": output,
            "Positive_Output": output > 0,
            "Strategy": strategy[function],
        }
        for function, output in results.items()
    ]
)

df["Rank"] = df["Week_05_Output"].rank(ascending=False, method="min").astype(int)
df["Absolute_Output"] = df["Week_05_Output"].abs()
df = df.sort_values("Rank")

summary = df[
    ["Function", "Week_05_Output", "Rank", "Strategy", "Positive_Output", "Absolute_Output"]
]

ranking = df[["Rank", "Function", "Week_05_Output", "Strategy"]]

statistics = pd.DataFrame(
    {
        "Metric": [
            "Best Function",
            "Best Output",
            "Worst Function",
            "Worst Output",
            "Positive Outputs",
            "Negative Outputs",
            "Mean Output",
            "Median Output",
        ],
        "Value": [
            df.iloc[0]["Function"],
            df.iloc[0]["Week_05_Output"],
            df.iloc[-1]["Function"],
            df.iloc[-1]["Week_05_Output"],
            int(df["Positive_Output"].sum()),
            int((~df["Positive_Output"]).sum()),
            df["Week_05_Output"].mean(),
            df["Week_05_Output"].median(),
        ],
    }
)

decision_matrix = pd.DataFrame(
    [
        ["F5", "Very high", "High", "Exploit", "Best performer with sustained improvement"],
        ["F8", "High", "High", "Monitor", "Stable high output"],
        ["F7", "Moderate high", "Moderate", "Refine", "Stable positive output"],
        ["F2", "Moderate", "Moderate", "Refine", "Positive but variable"],
        ["F1", "Low", "Low", "Explore", "Near zero output"],
        ["F3", "Low", "Low", "Explore", "Negative output"],
        ["F6", "Low", "Low", "Explore", "Negative output"],
        ["F4", "Very low", "Very low", "Explore", "Lowest output"],
    ],
    columns=["Function", "Performance_Level", "Confidence", "Strategy", "Rationale"],
)

summary.to_csv("week_05_analysis_summary.csv", index=False)
ranking.to_csv("week_05_ranking.csv", index=False)
statistics.to_csv("week_05_statistics.csv", index=False)
decision_matrix.to_csv("week_05_decision_matrix.csv", index=False)

with open("week_05_console_report.txt", "w", encoding="utf-8") as f:
    f.write("Week 05 BBO Analysis Report\n")
    f.write("===========================\n\n")
    f.write(f"Best function: {df.iloc[0]['Function']}\n")
    f.write(f"Best output: {df.iloc[0]['Week_05_Output']}\n")
    f.write(f"Worst function: {df.iloc[-1]['Function']}\n")
    f.write(f"Worst output: {df.iloc[-1]['Week_05_Output']}\n\n")
    f.write("Ranking:\n")
    f.write(ranking.to_string(index=False))
    f.write("\n\nStrategy Summary:\n")
    f.write("Exploit: F5\n")
    f.write("Refine: F2, F7\n")
    f.write("Monitor: F8\n")
    f.write("Explore: F1, F3, F4, F6\n")

print("Week 05 analysis complete.")
print("Files created:")
print("week_05_analysis_summary.csv")
print("week_05_ranking.csv")
print("week_05_statistics.csv")
print("week_05_decision_matrix.csv")
print("week_05_console_report.txt")
