"""Test whether Delta 6 to Delta 10 provide pointers to later low-order change.

Every predictor is calculated from observations available at the prediction
week. The target is the sign of Delta 1, Delta 2 or Delta 3 one week later.
High-order oscillation means that the latest high-order Delta changes sign
relative to its preceding value.
"""

from __future__ import annotations

from math import comb
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Post_BBO_BBR" / "PDHIS"
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"


def load_weekly() -> pd.DataFrame:
    frame = pd.read_csv(DATA)
    frame = frame[frame.source.str.fullmatch(r"week_\d{2}", na=False)].copy()
    frame["week"] = frame.source.str.extract(r"(\d+)").astype(int)
    frame = frame.sort_values(["function", "week"])
    if not (frame.groupby("function").size() == 13).all():
        raise ValueError("Expected thirteen weekly outputs for each function.")
    return frame[["function", "week", "output"]]


def delta_series(values: np.ndarray, order: int) -> np.ndarray:
    return np.diff(values.astype(float), n=order)


def build_cases(weekly: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for function, group in weekly.groupby("function"):
        values = group.sort_values("week").output.to_numpy(float)
        deltas = {order: delta_series(values, order) for order in range(1, 11)}
        for high_order in range(6, 11):
            high = deltas[high_order]
            # high[index] ends at zero-based week index high_order + index.
            for high_index in range(1, len(high)):
                end_index = high_order + high_index
                if end_index + 1 >= len(values):
                    continue
                current = high[high_index]
                previous = high[high_index - 1]
                for target_order in range(1, 4):
                    target = deltas[target_order]
                    target_index = end_index + 1 - target_order
                    rows.append({
                        "function": function,
                        "prediction_week": end_index + 1,
                        "high_order": high_order,
                        "target_order": target_order,
                        "high_delta": current,
                        "high_positive": int(current > 0),
                        "high_oscillation": int(current * previous < 0),
                        "next_target_delta": target[target_index],
                        "next_target_positive": int(target[target_index] > 0),
                    })
    return pd.DataFrame(rows)


def fisher_two_sided(a: int, b: int, c: int, d: int) -> float:
    row_one, row_two = a + b, c + d
    col_one, total = a + c, a + b + c + d
    low = max(0, col_one - row_two)
    high = min(row_one, col_one)

    def probability(x: int) -> float:
        return comb(row_one, x) * comb(row_two, col_one - x) / comb(total, col_one)

    observed = probability(a)
    return min(1.0, sum(probability(x) for x in range(low, high + 1) if probability(x) <= observed + 1e-12))


def summarise(cases: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (high_order, target_order), group in cases.groupby(["high_order", "target_order"]):
        exposed = group[group.high_oscillation == 1]
        unexposed = group[group.high_oscillation == 0]
        a = int(exposed.next_target_positive.sum())
        b = int(len(exposed) - a)
        c = int(unexposed.next_target_positive.sum())
        d = int(len(unexposed) - c)
        odds_ratio = ((a + 0.5) * (d + 0.5)) / ((b + 0.5) * (c + 0.5))
        rows.append({
            "high_order": high_order,
            "target_order": target_order,
            "forward_cases": len(group),
            "oscillation_cases": len(exposed),
            "positive_after_oscillation": a,
            "positive_rate_after_oscillation": exposed.next_target_positive.mean() if len(exposed) else np.nan,
            "positive_without_oscillation": c,
            "positive_rate_without_oscillation": unexposed.next_target_positive.mean() if len(unexposed) else np.nan,
            "corrected_odds_ratio": odds_ratio,
            "fisher_p": fisher_two_sided(a, b, c, d),
        })
    return pd.DataFrame(rows)


def write_findings(summary: pd.DataFrame) -> None:
    d9 = summary[(summary.high_order == 9) & (summary.target_order == 3)].iloc[0]
    best = summary.loc[summary.fisher_p.idxmin()]
    lines = [
        "# Higher-order Delta pointers to later behaviour",
        "",
        "## Research question",
        "",
        "Can an oscillation in Delta 6 to Delta 10 provide an early pointer to a positive Delta 1, Delta 2 or Delta 3 value one week later? The later low-order value is the target behaviour.",
        "",
        "## Timing rule",
        "",
        "Each higher-order Delta and its oscillation status are calculated only from values available by the prediction week. The target is taken from the following week. This prevents later information from entering the predictor.",
        "",
        "## Delta 9 to later Delta 3",
        "",
        f"There are {int(d9.forward_cases)} usable forward cases. Delta 9 oscillated in {int(d9.oscillation_cases)} of them. A positive Delta 3 followed in {int(d9.positive_after_oscillation)} oscillation cases, a rate of {d9.positive_rate_after_oscillation:.3f}, compared with {d9.positive_rate_without_oscillation:.3f} when Delta 9 did not oscillate. The corrected odds ratio is {d9.corrected_odds_ratio:.3f} and the two-sided exact p value is {d9.fisher_p:.3f}.",
        "",
        "This is a pointer test, not proof of prediction. Delta 9 has only two eligible prediction times per function in a thirteen-week sequence, and observations within each function are related.",
        "",
        "## Strongest observed pairing",
        "",
        f"The smallest unadjusted exact p value occurred for Delta {int(best.high_order)} oscillation and later Delta {int(best.target_order)} positivity: p = {best.fisher_p:.3f} across {int(best.forward_cases)} cases. Fifteen pairings were examined, so this result is descriptive and should not be treated as confirmed evidence.",
        "",
        "## Interpretation",
        "",
        "Delta 6 to Delta 10 can be studied as possible early pointers because they describe repeated changes in lower-order movement. They cannot be assumed to cause later behaviour. A useful signal would need to recur in longer sequences, remain present on untouched functions and outperform simple sign, persistence and chance baselines.",
        "",
        "## Reproducibility",
        "",
        "Run `python Post_BBO_BBR/PDHIS/generate_pdhis_high_order_pointers.py` from the repository root.",
        "",
    ]
    (OUT / "PDHIS_HIGH_ORDER_POINTERS.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cases = build_cases(load_weekly())
    summary = summarise(cases)
    cases.to_csv(OUT / "PDHIS_HIGH_ORDER_POINTER_CASES.csv", index=False)
    summary.to_csv(OUT / "PDHIS_HIGH_ORDER_POINTER_SUMMARY.csv", index=False)
    write_findings(summary)
    d9 = summary[(summary.high_order == 9) & (summary.target_order == 3)].iloc[0]
    print(d9.to_string())


if __name__ == "__main__":
    main()
