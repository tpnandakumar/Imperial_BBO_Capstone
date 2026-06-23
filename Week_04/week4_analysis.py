import pandas as pd

week4_outputs = {
    "F1": 0.00000014754580129542488,
    "F2": 0.5228458934672892,
    "F3": -0.06037987403160633,
    "F4": -22.55187651826871,
    "F5": 3238.333368768757,
    "F6": -0.8733671274789931,
    "F7": 1.1968303712356705,
    "F8": 9.539439999999999,
}

df = pd.DataFrame(
    week4_outputs.items(),
    columns=["function", "output"]
)

df["week"] = 4
df = df.sort_values("output", ascending=False).reset_index(drop=True)
df["rank"] = df.index + 1

def classify(row):
    f = row["function"]
    if f == "F5":
        return "Dominant exploitation target"
    if f == "F8":
        return "Stable high-performing region"
    if f in ["F2", "F7"]:
        return "Refinement candidate"
    if f == "F1":
        return "Near-zero exploratory candidate"
    if f in ["F3", "F4", "F6"]:
        return "Low-performing exploratory candidate"
    return "Unclassified"

df["classification"] = df.apply(classify, axis=1)

df = df[["week", "function", "output", "rank", "classification"]]

print(df)

df.to_csv("week4_analysis_summary.csv", index=False)
