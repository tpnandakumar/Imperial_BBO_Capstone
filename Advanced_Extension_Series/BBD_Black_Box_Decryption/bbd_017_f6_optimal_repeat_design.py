from pathlib import Path
import math
import pandas as pd

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

sigma = 0.046738
z95 = 1.959963984540054
z80 = 0.8416212335729143
z90 = 1.2815515655446004

# Historical repeat anchors. These are the only coordinates with direct repeatability evidence.
anchors = [
    {"anchor":"A","coordinate":"0.700000-0.200000-0.700000-0.700000-0.200000","historical_repeats":3,"historical_mean":-0.654612,"historical_sd":0.050585,"historical_range":0.100675},
    {"anchor":"B","coordinate":"0.240000-0.760000-0.240000-0.820000-0.280000","historical_repeats":2,"historical_mean":-1.146510,"historical_sd":0.037890,"historical_range":0.053585},
]
pd.DataFrame(anchors).to_csv(OUT / "BBD_017_F6_REPEAT_ANCHORS.csv", index=False)

# Precision requirements for estimating a fixed-coordinate mean.
precision=[]
for h in [0.05,0.025,0.02,0.01]:
    n=math.ceil((z95*sigma/h)**2)
    precision.append({"target_half_width":h,"confidence_level":0.95,"estimated_sigma":sigma,"required_repeats":n})
pd.DataFrame(precision).to_csv(OUT / "BBD_017_F6_PRECISION_REQUIREMENTS.csv", index=False)

# Two-state/context power requirements.
power=[]
for shift in [0.025,0.05,0.075,0.10]:
    for p,zp in [(0.8,z80),(0.9,z90)]:
        n=math.ceil(2*((z95+zp)*sigma/shift)**2)
        power.append({"target_state_shift":shift,"power":p,"alpha":0.05,"estimated_sigma":sigma,"repeats_per_state":n,"total_two_state_evaluations":2*n})
pd.DataFrame(power).to_csv(OUT / "BBD_017_F6_STATE_SHIFT_POWER.csv", index=False)

# Recommended experiment: two historical anchors, balanced and interleaved.
# 10 observations per anchor gives a practical first-stage repeatability study and allows temporal/block diagnostics.
sequence=[]
for block in range(1,11):
    order = [anchors[0], anchors[1]] if block % 2 else [anchors[1], anchors[0]]
    for pos,a in enumerate(order, start=1):
        sequence.append({
            "evaluation":len(sequence)+1,
            "block":block,
            "position_in_block":pos,
            "anchor":a["anchor"],
            "coordinate":a["coordinate"],
            "purpose":"fixed-coordinate repeatability and drift discrimination"
        })
pd.DataFrame(sequence).to_csv(OUT / "BBD_017_F6_RECOMMENDED_SEQUENCE.csv", index=False)

# Optional stronger state-discrimination designs from BBD 016.
designs = [
    {"design":"Stage_1_repeatability","evaluations":20,"structure":"10 repeats each at anchors A and B, alternating order","primary_question":"Does within-coordinate variability persist under controlled repetition?"},
    {"design":"Stage_2_shift_0.10_90pct","evaluations":10,"structure":"5 repeats per state/context at one fixed anchor","primary_question":"Can a state shift of 0.10 be distinguished with 90% power?"},
    {"design":"Stage_2_shift_0.075_90pct","evaluations":18,"structure":"9 repeats per state/context at one fixed anchor","primary_question":"Can a state shift of 0.075 be distinguished with 90% power?"},
    {"design":"Stage_2_shift_0.05_90pct","evaluations":38,"structure":"19 repeats per state/context at one fixed anchor","primary_question":"Can a state shift of 0.05 be distinguished with 90% power?"},
]
pd.DataFrame(designs).to_csv(OUT / "BBD_017_F6_DESIGN_OPTIONS.csv", index=False)

summary=pd.DataFrame([{
    "function":6,
    "estimated_repeat_sigma":sigma,
    "primary_anchor_A":anchors[0]["coordinate"],
    "control_anchor_B":anchors[1]["coordinate"],
    "recommended_stage1_evaluations":20,
    "recommended_stage1_repeats_per_anchor":10,
    "sequence":"balanced_interleaved_AB_BA_blocks",
    "minimum_shift_target_for_followup":0.075,
    "followup_repeats_per_state_90pct_power":9,
    "exact_function_recovered":False,
    "independent_black_box_evaluation_required":True,
    "interpretation":"prospective_protocol_defined_not_executed"
}])
summary.to_csv(OUT / "BBD_017_F6_OPTIMAL_REPEAT_DESIGN_SUMMARY.csv", index=False)

print("BBD 017 F6 optimal repeat experiment design")
print("\nRecommended Stage 1")
print(pd.DataFrame(designs).iloc[[0]].to_string(index=False))
print("\nSequence")
print(pd.DataFrame(sequence).to_string(index=False))
print("\nSummary")
print(summary.to_string(index=False))
print(f"\nOutputs written to {OUT}")
