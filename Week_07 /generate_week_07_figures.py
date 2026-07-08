import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create figures folder
figures_dir = Path("figures")
figures_dir.mkdir(exist_ok=True)

weeks = range(1, 8)
all_data = []

for week in weeks:
    week_folder = Path(f"../Week_{week:02d}")
    result_file = week_folder / f"week_{week:02d}_results.csv"

    df = pd.read_csv(result_file)

    # Adjust column names if needed
    df.columns = [c.strip().lower() for c in df.columns]

    output_col = [c for c in df.columns if "output" in c][0]
    function_col = [c for c in df.columns if "function" in c][0]

    df["week"] = week
    df["output"] = df[output_col]
    df["function"] = df[function_col]

    all_data.append(df[["week", "function", "output"]])

data = pd.concat(all_data, ignore_index=True)

plt.figure(figsize=(12, 7))

for function in sorted(data["function"].unique()):
    subset = data[data["function"] == function]
    plt.plot(
        subset["week"],
        subset["output"],
        marker="o",
        linewidth=2,
        label=function
    )

plt.title("Figure 1A. Function Output Evolution, Weeks 1 to 7", fontsize=16)
plt.xlabel("Week")
plt.ylabel("Output value")
plt.xticks(list(weeks))
plt.grid(True, linestyle=":", linewidth=0.7)
plt.legend(title="Function", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.savefig(figures_dir / "figure_1A_function_output_evolution_weeks_1_to_7.png", dpi=300)
plt.close()

print("Figure 1A created successfully.")
