
"""
Week 06 Analysis Tool
Imperial BBO Capstone

This script reads Week 06 results, ranks all functions, assigns
strategy classifications and exports a reproducible analysis summary.
"""

import pandas as pd


WEEK_06_RESULTS = {
    "F1": 0.012779642669914939,
    "F2": 0.28016822307722516,
    "F3": -0.11392206377710448,
    "F4": -27.44051496086922,
    "F5": 3682.2110623386798,
    "F6": -1.073875453695542,
    "F7": 1.3809299933612855,
    "F8": 9.5113,
}


STRATEGY = {
    "F1": "Explore",
    "F2": "Refine",
    "F3": "Explore",
    "F4": "Explore",
    "F5": "Exploit",
    "F6": "Explore",
    "F7": "Refine",
    "F8": "Monitor",
}


CONFIDENCE = {
    "F1": "Low",
    "F2": "Moderate",
    "F3": "Low",
    "F4": "Very Low",
    "F5": "High",
    "F6": "Low",
    "F7": "Moderate",
    "F8": "High",
}


INFORMATION_GAIN = {
    "F1": "Low",
    "F2": "Moderate",
    "F3": "Moderate",
    "F4": "High",
    "F5": "High",
    "F6": "Moderate",
    "F7": "Moderate",
    "F8": "Moderate",
}


CURRENT_ASSESSMENT = {
    "F1": "Near Zero",
    "F2": "Positive",
    "F3": "Negative",
    "F4": "Worst Performer",
    "F5": "Best Performer",
    "F6": "Negative",
    "F7": "Improving",
    "F8": "Stable High Performance",
}


INTERPRETATION = {
    "F1": "Little improvement observed. Continue exploratory sampling.",
    "F2": "Moderate positive performance with potential for further optimisation.",
    "F3": "Negative output indicates that improved search regions have not yet been identified.",
    "F4": "Lowest objective value. Broader exploration recommended.",
    "F5": "Consistent improvement across successive optimisation rounds. Continue local exploitation.",
    "F6": "Continued exploration required to reduce uncertainty.",
    "F7": "Steady improvement supports continued local refinement.",
    "F8": "Stable objective values suggest a reliable search region requiring only minor refinement.",
}


def build_summary() -> pd.DataFrame:
    rows = []

    for function, output in WEEK_06_RESULTS.items():
        rows.append(
            {
                "Function": function,
                "Week_06_Output": output,
                "Strategy": STRATEGY[function],
                "Confidence": CONFIDENCE[function],
                "Information_Gain": INFORMATION_GAIN[function],
                "Current_Assessment": CURRENT_ASSESSMENT[function],
                "Interpretation": INTERPRETATION[function],
            }
        )

    df = pd.DataFrame(rows)

    df["Rank"] = df["Week_06_Output"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    df = df[
        [
            "Function",
            "Week_06_Output",
            "Rank",
            "Strategy",
            "Confidence",
            "Information_Gain",
            "Current_Assessment",
            "Interpretation",
        ]
    ]

    df = df.sort_values("Rank")

    return df


def print_report(df: pd.DataFrame) -> None:
    best = df.iloc[0]
    worst = df.iloc[-1]

    print("\nWeek 06 BBO Analysis Report")
    print("=" * 40)
    print(f"Best Function: {best['Function']}")
    print(f"Best Output: {best['Week_06_Output']}")
    print(f"Worst Function: {worst['Function']}")
    print(f"Worst Output: {worst['Week_06_Output']}")

    print("\nStrategy Allocation")
    print("Exploit: F5")
    print("Refine: F2, F7")
    print("Monitor: F8")
    print("Explore: F1, F3, F4, F6")

    print("\nRanking Summary")
    print(
        df[
            [
                "Rank",
                "Function",
                "Week_06_Output",
                "Strategy",
                "Confidence",
                "Information_Gain",
            ]
        ].to_string(index=False)
    )


def main() -> None:
    summary = build_summary()

    output_file = "week_06_analysis_summary.csv"
    summary.to_csv(output_file, index=False)

    print_report(summary)
    print(f"\nAnalysis summary exported to: {output_file}")


if __name__ == "__main__":
    main()
