"""
Week 05 Analysis Tool
Imperial BBO Capstone

Purpose:
Analyse Week 05 optimisation results, compare function performance,
rank outputs, classify optimisation strategy and export a summary CSV.
"""

import pandas as pd


WEEK_05_RESULTS = {
    "F1": 0.012779642669914939,
    "F2": 0.28016822307722516,
    "F3": -0.11392206377710448,
    "F4": -27.44051496086922,
    "F5": 3682.2110623386798,
    "F6": -1.073875453695542,
    "F7": 1.3809299933612855,
    "F8": 9.5113,
}


STRATEGY_CLASSIFICATION = {
    "F1": "Explore",
    "F2": "Refine",
    "F3": "Explore",
    "F4": "Explore",
    "F5": "Exploit",
    "F6": "Explore",
    "F7": "Refine",
    "F8": "Monitor",
}


def build_week_05_summary():
    rows = []

    for function, output in WEEK_05_RESULTS.items():
        rows.append(
            {
                "Function": function,
                "Week_05_Output": output,
                "Strategy": STRATEGY_CLASSIFICATION[function],
                "Positive_Output": output > 0,
            }
        )

    df = pd.DataFrame(rows)

    df["Rank"] = df["Week_05_Output"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    df = df.sort_values("Rank")

    return df


def print_summary(df):
    best = df.iloc[0]
    worst = df.iloc[-1]

    print("\nWeek 05 BBO Analysis Summary")
    print("=" * 40)
    print(f"Best function: {best['Function']} | Output: {best['Week_05_Output']}")
    print(f"Worst function: {worst['Function']} | Output: {worst['Week_05_Output']}")
    print("\nFunction Ranking")
    print(df[["Rank", "Function", "Week_05_Output", "Strategy"]].to_string(index=False))


def main():
    df = build_week_05_summary()

    output_file = "week_05_analysis_summary.csv"
    df.to_csv(output_file, index=False)

    print_summary(df)
    print(f"\nSummary exported to: {output_file}")


if __name__ == "__main__":
    main()
