"""PDHIS analysis of the official thirteen-round BBO evidence.

The script calculates output deltas from order 1 to order 10 for all eight
functions, examines their chronological relationship with the next observed
change, and creates publication-ready evidence figures.  Starter observations
are excluded because they are not part of the weekly sequence.
"""

from __future__ import annotations

from pathlib import Path
import warnings

import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
OUT = Path(__file__).resolve().parent
FIG = OUT / "infographics"
FIG.mkdir(parents=True, exist_ok=True)

NAVY = "#14213d"
TEAL = "#4f9d96"
GOLD = "#d4a72c"
CORAL = "#d65a6f"
PURPLE = "#7c67ad"
PALE = "#f5f7fb"


def save(fig: plt.Figure, number: int, slug: str, caption: str) -> None:
    fig.text(0.5, 0.018, f"PDHIS-{number:02d}. {caption}", ha="center", va="bottom",
             fontsize=9.5, color="#334155", wrap=True)
    path = FIG / f"PDHIS-{number:02d}_{slug}.jpg"
    fig.savefig(path, dpi=210, bbox_inches="tight", facecolor="white", pil_kwargs={"quality": 91})
    plt.close(fig)


def normalise(values: pd.Series) -> pd.Series:
    lo, hi = values.min(), values.max()
    if np.isclose(hi, lo):
        return pd.Series(np.zeros(len(values)), index=values.index)
    return (values - lo) / (hi - lo)


def zscore(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    sd = np.nanstd(values)
    return (values - np.nanmean(values)) / sd if sd > 0 else np.zeros_like(values)


def benjamini_hochberg(values: pd.Series) -> np.ndarray:
    """Return Benjamini-Hochberg false-discovery adjusted q values."""
    p = values.to_numpy(float)
    order = np.argsort(p)
    ranked = p[order]
    adjusted = ranked * len(p) / np.arange(1, len(p) + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    result = np.empty_like(adjusted)
    result[order] = np.minimum(adjusted, 1.0)
    return result


def load_weekly() -> pd.DataFrame:
    df = pd.read_csv(DATA)
    df = df[df["source"].str.fullmatch(r"week_\d{2}", na=False)].copy()
    df["week"] = df["source"].str.extract(r"(\d+)").astype(int)
    df = df.sort_values(["function", "week"])
    counts = df.groupby("function").size()
    if not (counts == 13).all() or len(counts) != 8:
        raise ValueError(f"Expected 13 rounds for eight functions, found {counts.to_dict()}")
    df["output_normalised"] = df.groupby("function")["output"].transform(normalise)
    coords = [f"x{i}" for i in range(1, 9)]
    df["coordinate_movement"] = df.groupby("function", group_keys=False)[coords].apply(
        lambda g: np.sqrt(g.diff().pow(2).sum(axis=1, min_count=1))
    ).reset_index(level=0, drop=True)
    return df


def calculate_deltas(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    wide = df.pivot(index="week", columns="function", values="output_normalised")
    records = []
    for function in wide.columns:
        current = wide[function].to_numpy(float)
        for order in range(1, 11):
            current = np.diff(current)
            for end_week, value in zip(range(order + 1, 14), current):
                records.append({"function": int(function), "order": order,
                                "end_week": end_week, "delta": value})
    deltas = pd.DataFrame(records)

    tests = []
    rng = np.random.default_rng(42)
    for order in range(1, 11):
        block = deltas[deltas.order == order].copy()
        future = []
        for row in block.itertuples():
            if row.end_week >= 13:
                continue
            y = wide.loc[:, row.function]
            future.append({"function": row.function, "order": order,
                           "end_week": row.end_week, "delta": row.delta,
                           "next_change": y.loc[row.end_week + 1] - y.loc[row.end_week],
                           "next_output": y.loc[row.end_week + 1]})
        t = pd.DataFrame(future)
        x = np.concatenate([zscore(g.delta.to_numpy()) for _, g in t.groupby("function")])
        dy = np.concatenate([zscore(g.next_change.to_numpy()) for _, g in t.groupby("function")])
        ny = np.concatenate([zscore(g.next_output.to_numpy()) for _, g in t.groupby("function")])
        rho_change = spearmanr(x, dy).statistic if len(np.unique(x)) > 1 else np.nan
        rho_output = spearmanr(x, ny).statistic if len(np.unique(x)) > 1 else np.nan
        active = (np.abs(x) > 1e-12) & (np.abs(dy) > 1e-12)
        hit = np.mean(np.sign(x[active]) == np.sign(dy[active])) if active.any() else np.nan

        null = []
        for _ in range(2000):
            shuffled = t.copy()
            shuffled["next_change"] = shuffled.groupby("function")["next_change"].transform(
                lambda s: rng.permutation(s.to_numpy())
            )
            sy = np.concatenate([zscore(g.next_change.to_numpy()) for _, g in shuffled.groupby("function")])
            null.append(spearmanr(x, sy).statistic if len(np.unique(sy)) > 1 else 0.0)
        null = np.nan_to_num(np.asarray(null))
        p = (1 + np.sum(np.abs(null) >= abs(rho_change))) / (1 + len(null))
        tests.append({"order": order, "forward_cases": len(t),
                      "spearman_next_change": rho_change,
                      "spearman_next_output": rho_output,
                      "direction_hit_rate": hit,
                      "permutation_p": p,
                      "null_rho_low": np.quantile(null, 0.025),
                      "null_rho_high": np.quantile(null, 0.975)})
    metrics = pd.DataFrame(tests)
    metrics["fdr_q"] = benjamini_hochberg(metrics["permutation_p"])
    return deltas, metrics


def function_tests(df: pd.DataFrame, deltas: pd.DataFrame) -> pd.DataFrame:
    wide = df.pivot(index="week", columns="function", values="output_normalised")
    rows = []
    for function in range(1, 9):
        y = wide[function]
        for order in range(1, 11):
            b = deltas[(deltas.function == function) & (deltas.order == order) &
                       (deltas.end_week < 13)].copy()
            b["next_change"] = [y.loc[w + 1] - y.loc[w] for w in b.end_week]
            rho = spearmanr(b.delta, b.next_change).statistic if b.delta.nunique() > 1 else np.nan
            active = (b.delta.abs() > 1e-12) & (b.next_change.abs() > 1e-12)
            hit = np.mean(np.sign(b.loc[active, "delta"]) == np.sign(b.loc[active, "next_change"])) if active.any() else np.nan
            rows.append({"function": function, "order": order, "n": len(b),
                         "spearman_next_change": rho, "direction_hit_rate": hit})
    return pd.DataFrame(rows)


def figure_hierarchy(metrics: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 5.8))
    ax.axis("off")
    ax.set_title("Pisharam Delta Hierarchy and Influence States", fontsize=22, weight="bold", color=NAVY, pad=20)
    labels = ["Observed output\nY", "Δ1\nchange", "Δ2\nacceleration", "Δ3\nchange in acceleration",
              "Δ4\npersistence", "Δ5 to Δ10\nhigher-order structure"]
    xs = np.linspace(0.07, 0.93, len(labels))
    colors = ["#dfeff0", "#d9f0ea", "#e7e0f4", "#f5dfeb", "#fae7cc", "#e5e9f2"]
    for i, (x, label, colour) in enumerate(zip(xs, labels, colors)):
        ax.text(x, 0.62, label, ha="center", va="center", fontsize=12, weight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.75", fc=colour, ec="white", lw=2))
        if i < len(labels) - 1:
            ax.annotate("", (xs[i + 1] - 0.07, 0.62), (x + 0.07, 0.62),
                        arrowprops=dict(arrowstyle="->", color=TEAL, lw=2))
    ax.text(0.5, 0.30, "Interpretive states: Emerging  |  MaxInflu  |  Plateau  |  Reversal  |  Boundary  |  Oscillation  |  Recovery  |  Equilibrium",
            ha="center", fontsize=12, color="#475569",
            bbox=dict(boxstyle="round,pad=0.8", fc=PALE, ec="#cbd5e1"))
    ax.text(0.5, 0.12, "Every higher order removes one weekly observation. Predictive evidence therefore contracts rapidly.",
            ha="center", fontsize=11, color=CORAL, weight="bold")
    save(fig, 1, "delta_hierarchy", "PDHIS separates measured Delta orders from interpretive influence states; higher orders are retained only with adequate evidence.")


def heatmap(df: pd.DataFrame, number: int, value: str, title: str, slug: str, caption: str,
            centre: float | None = None) -> None:
    mat = df.pivot(index="function", columns="week", values=value)
    fig, ax = plt.subplots(figsize=(12, 6.5))
    sns.heatmap(mat, cmap="vlag" if centre is not None else "viridis", center=centre,
                linewidths=.7, linecolor="white", ax=ax, cbar_kws={"label": value.replace("_", " ")})
    ax.set_title(title, fontsize=20, weight="bold", color=NAVY, pad=14)
    ax.set_xlabel("Official BBO week"); ax.set_ylabel("Hidden function")
    save(fig, number, slug, caption)


def delta_heatmap(deltas: pd.DataFrame, order: int, number: int) -> None:
    b = deltas[deltas.order == order]
    mat = b.pivot(index="function", columns="end_week", values="delta")
    vmax = np.nanquantile(np.abs(mat.to_numpy()), .95)
    vmax = vmax if vmax > 0 else 1
    fig, ax = plt.subplots(figsize=(12, 6.5))
    sns.heatmap(mat, cmap="vlag", norm=TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax),
                linewidths=.7, linecolor="white", ax=ax, cbar_kws={"label": f"Δ{order} of normalised output"})
    ax.set_title(f"Delta {order} across all eight functions", fontsize=20, weight="bold", color=NAVY, pad=14)
    ax.set_xlabel("Ending week of finite difference"); ax.set_ylabel("Hidden function")
    save(fig, number, f"delta_{order}_heatmap", f"Delta {order} is calculated from the official weekly output sequence after within-function range normalisation; red and blue show opposing directions.")


def figure_predictability(metrics: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
    axes[0].plot(metrics.order, metrics.spearman_next_change, marker="o", lw=2.5, color=TEAL, label="Next change")
    axes[0].plot(metrics.order, metrics.spearman_next_output, marker="s", lw=2, color=PURPLE, label="Next output")
    axes[0].axhline(0, color="#94a3b8", lw=1)
    axes[0].fill_between(metrics.order, metrics.null_rho_low, metrics.null_rho_high, color=GOLD, alpha=.2, label="95% shuffled range")
    axes[0].set_ylabel("Pooled Spearman correlation"); axes[0].legend(ncol=3, frameon=False)
    axes[0].set_title("Does a Delta level predict what happens next?", fontsize=20, weight="bold", color=NAVY, pad=14)
    axes[1].bar(metrics.order, metrics.forward_cases, color="#9bc7c2")
    for x, y in zip(metrics.order, metrics.forward_cases): axes[1].text(x, y + 1, str(int(y)), ha="center", fontsize=9)
    axes[1].set_xlabel("Delta order"); axes[1].set_ylabel("Forward cases")
    axes[1].set_xticks(range(1, 11))
    save(fig, 6, "predictability_by_order", "Chronological association is shown together with the number of usable forward cases and the shuffled-data reference interval.")


def figure_reliability(metrics: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 6.2))
    colours = [TEAL if q < .05 else "#cbd5e1" for q in metrics.fdr_q]
    ax.bar(metrics.order, -np.log10(metrics.fdr_q), color=colours)
    ax.axhline(-np.log10(.05), color=CORAL, ls="--", label="FDR q = 0.05")
    ax.set_xticks(range(1, 11)); ax.set_xlabel("Delta order"); ax.set_ylabel("Adjusted evidence, -log10(q)")
    ax.set_title("Randomisation and multiple-testing check", fontsize=20, weight="bold", color=NAVY, pad=14)
    ax.legend(frameon=False)
    save(fig, 7, "permutation_validation", "Within-function shuffling breaks chronology. Benjamini-Hochberg correction covers all ten Delta orders; no order reaches q below 0.05.")


def figure_function_matrix(ft: pd.DataFrame) -> None:
    mat = ft[ft.order <= 4].pivot(index="function", columns="order", values="spearman_next_change")
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(mat, cmap="vlag", center=0, vmin=-1, vmax=1, annot=True, fmt=".2f",
                linewidths=.8, linecolor="white", ax=ax, cbar_kws={"label": "Spearman correlation"})
    ax.set_title("Function-specific Delta relationship with the next change", fontsize=19, weight="bold", color=NAVY, pad=14)
    ax.set_xlabel("Delta order"); ax.set_ylabel("Hidden function")
    save(fig, 8, "function_predictive_matrix", "Correlations are calculated separately for each function. Small samples and repeated outputs require cautious interpretation.")


def figure_movement(df: pd.DataFrame) -> None:
    d = df.copy()
    d["absolute_output_change"] = d.groupby("function")["output_normalised"].diff().abs()
    fig, ax = plt.subplots(figsize=(11, 7))
    sns.scatterplot(data=d, x="coordinate_movement", y="absolute_output_change", hue="function",
                    palette="tab10", s=85, alpha=.82, ax=ax)
    ax.set_xlabel("Euclidean movement in submitted coordinates"); ax.set_ylabel("Absolute change in normalised output")
    ax.set_title("Input movement and output response are not equivalent", fontsize=20, weight="bold", color=NAVY, pad=14)
    ax.legend(title="Function", ncol=4, frameon=False)
    save(fig, 9, "movement_vs_output_delta", "Each point is one weekly transition. Large coordinate movement did not guarantee a large response, supporting separate input and output Delta analyses.")


def figure_evidence_decay(metrics: pd.DataFrame) -> None:
    fig, ax1 = plt.subplots(figsize=(12, 6.5))
    ax1.plot(metrics.order, metrics.forward_cases, marker="o", lw=3, color=TEAL)
    ax1.fill_between(metrics.order, 0, metrics.forward_cases, color=TEAL, alpha=.12)
    ax1.set_xlabel("Delta order"); ax1.set_ylabel("Available forward cases", color=TEAL)
    ax1.set_xticks(range(1, 11)); ax1.tick_params(axis="y", labelcolor=TEAL)
    ax2 = ax1.twinx()
    ax2.plot(metrics.order, metrics.direction_hit_rate * 100, marker="s", lw=2, color=PURPLE)
    ax2.axhline(50, color="#94a3b8", ls="--")
    ax2.set_ylabel("Direction hit rate (%)", color=PURPLE); ax2.tick_params(axis="y", labelcolor=PURPLE)
    ax1.set_title("The higher-order evidence boundary", fontsize=20, weight="bold", color=NAVY, pad=14)
    save(fig, 10, "higher_order_evidence_boundary", "Delta 1 to Delta 10 are computable, but the forward evidence contracts with every order; apparent late-order accuracy must not be mistaken for reliability.")


def figure_all_order_magnitude(deltas: pd.DataFrame) -> None:
    summary = deltas.groupby(["function", "order"])["delta"].apply(
        lambda s: np.median(np.abs(s))
    ).reset_index(name="median_absolute_delta")
    mat = summary.pivot(index="function", columns="order", values="median_absolute_delta")
    mat = np.log10(mat + 1e-6)
    fig, ax = plt.subplots(figsize=(12, 6.8))
    sns.heatmap(mat, cmap="mako", linewidths=.7, linecolor="white", ax=ax,
                cbar_kws={"label": "log10 median absolute Delta"})
    ax.set_title("Delta 1 to Delta 10 magnitude across eight functions", fontsize=20,
                 weight="bold", color=NAVY, pad=14)
    ax.set_xlabel("Delta order"); ax.set_ylabel("Hidden function")
    save(fig, 19, "all_order_magnitude",
         "Cell colour summarises the median absolute finite difference. Higher orders measure progressively nested change. Larger magnitude reflects variation already present and does not establish predictability.")


def figure_all_order_relationships(ft: pd.DataFrame) -> None:
    mat = ft.pivot(index="function", columns="order", values="spearman_next_change")
    labels = mat.copy().astype(object)
    nmat = ft.pivot(index="function", columns="order", values="n")
    for function in mat.index:
        for order in mat.columns:
            value = mat.loc[function, order]
            labels.loc[function, order] = "" if pd.isna(value) else f"{value:.2f}\nn={int(nmat.loc[function, order])}"
    fig, ax = plt.subplots(figsize=(13, 7.2))
    sns.heatmap(mat, cmap="vlag", center=0, vmin=-1, vmax=1, annot=labels, fmt="",
                linewidths=.7, linecolor="white", ax=ax,
                cbar_kws={"label": "Spearman correlation with next change"})
    ax.set_title("All-order relationship map and evidence count", fontsize=20,
                 weight="bold", color=NAVY, pad=14)
    ax.set_xlabel("Delta order"); ax.set_ylabel("Hidden function")
    save(fig, 20, "all_order_relationship_map",
         "Each cell embeds correlation and sample size. Late-order extremes are unstable because only a few chronological comparisons remain.")


def function_figures(df: pd.DataFrame, deltas: pd.DataFrame, ft: pd.DataFrame) -> None:
    for function in range(1, 9):
        sub = df[df.function == function]
        fig, axes = plt.subplots(2, 1, figsize=(11, 7.8), sharex=False, gridspec_kw={"height_ratios": [1, 1.35]})
        axes[0].plot(sub.week, sub.output_normalised, color=NAVY, marker="o", lw=2.5)
        axes[0].set_xticks(range(1, 14)); axes[0].set_ylabel("Normalised output")
        axes[0].set_title(f"F{function}: output and Delta structure", fontsize=19, weight="bold", color=NAVY, pad=12)
        palette = [TEAL, PURPLE, CORAL, GOLD]
        for order, colour in zip(range(1, 5), palette):
            b = deltas[(deltas.function == function) & (deltas.order == order)]
            axes[1].plot(b.end_week, b.delta, marker="o", lw=1.8, label=f"Δ{order}", color=colour)
        axes[1].axhline(0, color="#94a3b8", lw=1); axes[1].set_xticks(range(2, 14))
        axes[1].set_xlabel("Ending week"); axes[1].set_ylabel("Finite difference"); axes[1].legend(ncol=4, frameon=False)
        first = ft[(ft.function == function) & (ft.order == 1)].iloc[0]
        fig.text(.99, .965, f"Δ1 next-change ρ={first.spearman_next_change:.2f}  |  n={int(first.n)}",
                 ha="right", va="top", fontsize=10, color="#475569")
        save(fig, 10 + function, f"f{function}_delta_profile",
             f"F{function} retains the official thirteen-week sequence. Delta 1 to Delta 4 show response dynamics; the embedded statistic tests only the next weekly change.")


def write_tables(df: pd.DataFrame, deltas: pd.DataFrame, metrics: pd.DataFrame, ft: pd.DataFrame) -> None:
    deltas.to_csv(OUT / "PDHIS_DELTA_1_TO_10.csv", index=False)
    metrics.to_csv(OUT / "PDHIS_PREDICTABILITY_BY_ORDER.csv", index=False)
    ft.to_csv(OUT / "PDHIS_FUNCTION_RELATIONSHIPS.csv", index=False)
    weekly = df[["function", "week", "output", "output_normalised", "coordinate_movement"]]
    weekly.to_csv(OUT / "PDHIS_WEEKLY_EVIDENCE.csv", index=False)


def main() -> None:
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    sns.set_theme(style="whitegrid", font_scale=1.05)
    df = load_weekly()
    deltas, metrics = calculate_deltas(df)
    ft = function_tests(df, deltas)
    write_tables(df, deltas, metrics, ft)
    figure_hierarchy(metrics)
    heatmap(df, 2, "output_normalised", "Thirteen-week output landscape", "normalised_output_heatmap",
            "Outputs are normalised within each function solely for cross-function visual comparison; official raw values remain in the evidence table.")
    delta_heatmap(deltas, 1, 3)
    delta_heatmap(deltas, 2, 4)
    delta_heatmap(deltas, 3, 5)
    figure_predictability(metrics)
    figure_reliability(metrics)
    figure_function_matrix(ft)
    figure_movement(df)
    figure_evidence_decay(metrics)
    function_figures(df, deltas, ft)
    figure_all_order_magnitude(deltas)
    figure_all_order_relationships(ft)
    print(metrics.to_string(index=False))


if __name__ == "__main__":
    main()
