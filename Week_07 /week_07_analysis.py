"""
Week 07 Analysis Tool
Imperial BBO Capstone

This script analyses Week 07 BBO results, ranks all functions,
assigns strategy classifications and exports a reproducible
analysis summary.
"""

import pandas as pd


WEEK_07_RESULTS = {
    "F1": -1.4546199699251391e-58,
    "F2": 0.2399291698606551,
    "F3": -0.09116928906376276,
    "F4": -10.745961383135121,
    "F5": 4278.816638076986,
    "F6": -1.119713499832813,
    "F7": 1.1543358123792982,
    "F8": 9.49476,
}


STRATEGY = {
    "F1": "Explore",
    "F2": "Reassess",
    "F3": "Refine",
    "F4": "Refine",
    "F5": "Exploit",
    "F6": "Refine",
    "F7": "Monitor",
    "F8": "Monitor",
}


INTERPRETATION = {
    "F1": "Near zero and requires continued exploration",
    "F2": "Positive but declined from Week 06",
    "F3": "Improved and moving closer to zero",
    "F4": "Improved despite remaining negative",
    "F5": "Highest performing function",
    "F6": "Improved while remaining negative",
    "F7": "Stable positive performance",
    "F8": "Stable high performance",
}


def build_summary() -> pd.DataFrame:
    rows = []

    for function, output in WEEK_07_RESULTS.items():
        rows.append(
            {
                "Function": function,
                "Week_07_Output": output,
                "Rank": None,
                "Strategy": STRATEGY[function],
                "Interpretation": INTERPRETATION[function],
            }
        )

    df = pd.DataFrame(rows)

    df["Rank"] = df["Week_07_Output"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    df = df[
        [
            "Function",
            "Week_07_Output",
            "Rank",
            "Strategy",
            "Interpretation",
        ]
    ]

    df = df.sort_values("Rank")

    return df


def print_report(df: pd.DataFrame) -> None:
    best = df.iloc[0]
    worst = df.iloc[-1]

    print("\nWeek 07 BBO Analysis Report")
    print("=" * 40)
    print(f"Best Function: {best['Function']}")
    print(f"Best Output: {best['Week_07_Output']}")
    print(f"Worst Function: {worst['Function']}")
    print(f"Worst Output: {worst['Week_07_Output']}")

    print("\nStrategy Allocation")
    print("Exploit: F5")
    print("Refine: F3, F4, F6")
    print("Monitor: F7, F8")
    print("Reassess: F2")
    print("Explore: F1")

    print("\nRanking Summary")
    print(
        df[
            [
                "Rank",
                "Function",
                "Week_07_Output",
                "Strategy",
                "Interpretation",
            ]
        ].to_string(index=False)
    )


def main() -> None:
    summary = build_summary()

    output_file = "week_07_analysis_summary.csv"
    summary.to_csv(output_file, index=False)

    print_report(summary)
    print(f"\nAnalysis summary exported to: {output_file}")


if __name__ == "__main__":
    main()
