from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
HISTORY = ROOT / "PFRAMOS" / "data" / "recovered_exact_history.csv"
W12_IN = ROOT / "Week_12" / "week_12_inputs.csv"
W12_OUT = ROOT / "Week_12" / "week_12_results.csv"
W13_IN = ROOT / "Week_13" / "week_13_inputs.csv"
W13_OUT = ROOT / "Week_13" / "week_13_results.csv"
OUT = Path(__file__).resolve().parent / "complete_13_round_history.csv"

DIMENSIONS = {
    1: 2,
    2: 2,
    3: 3,
    4: 4,
    5: 4,
    6: 5,
    7: 6,
    8: 8,
}


def parse_function_number(label: str) -> int:
    return int(str(label).strip().split()[-1])


def read_late_week(week: int, input_path: Path, output_path: Path) -> pd.DataFrame:
    inputs = pd.read_csv(input_path)
    outputs = pd.read_csv(output_path)

    if "Function" in inputs.columns:
        inputs = inputs.rename(columns={"Function": "function"})
    if "Input" in inputs.columns:
        rows = []
        for _, row in inputs.iterrows():
            fn = parse_function_number(row["function"])
            values = [float(v) for v in str(row["Input"]).split(",")]
            record = {"Week": week, "Function": fn, "Dimension": DIMENSIONS[fn]}
            for j in range(1, 9):
                record[f"Input_{j}"] = values[j - 1] if j <= len(values) else pd.NA
            rows.append(record)
        inputs = pd.DataFrame(rows)
    else:
        rows = []
        for _, row in inputs.iterrows():
            fn = parse_function_number(row["function"])
            record = {"Week": week, "Function": fn, "Dimension": DIMENSIONS[fn]}
            for j in range(1, 9):
                col = f"x{j}"
                record[f"Input_{j}"] = row[col] if col in row.index and pd.notna(row[col]) else pd.NA
            rows.append(record)
        inputs = pd.DataFrame(rows)

    outputs = outputs.copy()
    outputs["Function"] = outputs["function"].map(parse_function_number)
    outputs = outputs[["Function", "output"]].rename(columns={"output": "Output"})

    merged = inputs.merge(outputs, on="Function", validate="one_to_one")
    merged["Source"] = f"Week_{week:02d} verified submission and returned outputs"
    return merged


def build() -> pd.DataFrame:
    early = pd.read_csv(HISTORY)
    early = early.loc[early["Week"] <= 11].copy()

    week12 = read_late_week(12, W12_IN, W12_OUT)
    week13 = read_late_week(13, W13_IN, W13_OUT)

    columns = [
        "Week", "Function", "Dimension",
        "Input_1", "Input_2", "Input_3", "Input_4",
        "Input_5", "Input_6", "Input_7", "Input_8",
        "Output", "Source",
    ]
    combined = pd.concat([early[columns], week12[columns], week13[columns]], ignore_index=True)
    combined = combined.sort_values(["Function", "Week"]).reset_index(drop=True)

    counts = combined.groupby("Function").size().to_dict()
    expected = {fn: 13 for fn in DIMENSIONS}
    if counts != expected:
        raise ValueError(f"Expected 13 observations per function, found {counts}")

    if not combined["Week"].between(1, 13).all():
        raise ValueError("Unexpected week number in surrogate history")

    for fn, dim in DIMENSIONS.items():
        part = combined.loc[combined["Function"] == fn]
        used = [f"Input_{j}" for j in range(1, dim + 1)]
        if part[used].isna().any().any():
            raise ValueError(f"Missing required coordinate for F{fn}")

    combined.to_csv(OUT, index=False)
    return combined


if __name__ == "__main__":
    df = build()
    print(df.groupby("Function")["Output"].agg(["count", "min", "max"]))
    print(f"Wrote {OUT}")
