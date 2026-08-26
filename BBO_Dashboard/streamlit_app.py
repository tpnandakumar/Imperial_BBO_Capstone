from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parent
EVIDENCE_FILE = APP_DIR / "data" / "complete_internal_evidence.csv"

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
FUNCTION_NAMES = {function: f"Function {function} · {dimension} dimensions" for function, dimension in DIMENSIONS.items()}


@st.cache_data
def load_assessed_evidence() -> pd.DataFrame:
    evidence = pd.read_csv(EVIDENCE_FILE)
    evidence = evidence[evidence.source.str.startswith("week_")].copy()
    evidence["week"] = evidence.source.str.removeprefix("week_").astype(int)
    evidence = evidence.sort_values(["function", "week"]).reset_index(drop=True)
    assert len(evidence) == 104
    assert evidence.week.min() == 1 and evidence.week.max() == 13
    return evidence


@st.cache_data
def load_complete_internal_evidence() -> pd.DataFrame:
    return pd.read_csv(EVIDENCE_FILE)


def format_number(value: float) -> str:
    value = float(value)
    if value == 0:
        return "0"
    if abs(value) < 0.001 or abs(value) >= 10000:
        return f"{value:.6e}"
    return f"{value:.6f}"


def coordinate_text(row: pd.Series, function: int) -> str:
    return "-".join(f"{row[f'x{index}']:.6f}" for index in range(1, DIMENSIONS[function] + 1))


def winners(evidence: pd.DataFrame) -> pd.DataFrame:
    winning_rows = evidence.loc[evidence.groupby("function").output.idxmax()].copy()
    winning_rows["coordinate"] = [
        coordinate_text(row, int(row.function)) for _, row in winning_rows.iterrows()
    ]
    return winning_rows


def page_header(title: str, introduction: str) -> None:
    st.title(title)
    st.markdown(f"<p class='lead'>{introduction}</p>", unsafe_allow_html=True)


def overview(evidence: pd.DataFrame) -> None:
    page_header(
        "Imperial BBO Challenge",
        "The complete thirteen-round optimisation journey across eight hidden functions.",
    )
    columns = st.columns(4)
    columns[0].metric("Competition rounds", "13")
    columns[1].metric("Hidden functions", "8")
    columns[2].metric("Submitted coordinates", "104")
    columns[3].metric("Input dimensions", "2 to 8")

    st.subheader("The challenge")
    st.write(
        "Each function accepted coordinates between 0 and 1 and returned one hidden score. The equation was unknown. One new coordinate per function was submitted in each round, and the aim was to maximise the returned value."
    )

    st.subheader("Best result achieved for each function")
    best = winners(evidence)
    table = pd.DataFrame({
        "Function": best.function.map(lambda value: f"F{value}"),
        "Dimensions": best.function.map(DIMENSIONS),
        "Winning round": best.week,
        "Winning coordinate": best.coordinate,
        "Best output": best.output.map(format_number),
    })
    st.dataframe(table, hide_index=True, use_container_width=True)

    st.subheader("How the search developed")
    phase_columns = st.columns(4)
    phases = [
        ("Explore", "Early rounds sampled the unknown surfaces and established direction."),
        ("Learn", "Results were compared to identify useful coordinates and relationships."),
        ("Exploit", "Later submissions concentrated around the strongest supported regions."),
        ("Confirm", "The final rounds tested stability and retained the best verified choices."),
    ]
    for column, (title, text) in zip(phase_columns, phases):
        with column:
            st.markdown(f"### {title}")
            st.write(text)


def weekly_progress(evidence: pd.DataFrame) -> None:
    page_header(
        "Weekly Progress",
        "Compare how the returned scores changed from Week 1 to Week 13.",
    )
    selected = st.multiselect(
        "Functions to compare", list(DIMENSIONS), default=list(DIMENSIONS),
        format_func=lambda value: f"F{value}",
    )
    if not selected:
        st.info("Choose at least one function to display the progress chart.")
        return

    frame = evidence[evidence.function.isin(selected)].copy()
    ranges = frame.groupby("function").output.transform("max") - frame.groupby("function").output.transform("min")
    frame["relative_progress"] = (
        frame.output - frame.groupby("function").output.transform("min")
    ) / ranges.replace(0, 1)
    chart = frame.pivot(index="week", columns="function", values="relative_progress")
    chart.columns = [f"F{function}" for function in chart.columns]
    st.line_chart(chart, height=430)
    st.caption(
        "Scores have been scaled within each function so that functions with very different output ranges can be compared. Zero is the lowest observed weekly score and one is the highest."
    )

    best = winners(frame)
    summary = pd.DataFrame({
        "Function": best.function.map(lambda value: f"F{value}"),
        "Best round": best.week,
        "Best output": best.output.map(format_number),
        "Winning coordinate": best.coordinate,
    })
    st.dataframe(summary, hide_index=True, use_container_width=True)


def round_dashboard(evidence: pd.DataFrame, complete: pd.DataFrame) -> None:
    page_header(
        "BBO Optimisation Dashboard",
        "Inspect each function at any competition round using the genuine submitted inputs and evaluator outputs.",
    )
    control_one, control_two = st.columns(2)
    with control_one:
        function = st.selectbox(
            "Function", list(DIMENSIONS), format_func=lambda value: FUNCTION_NAMES[value],
            key="round_function",
        )
    with control_two:
        week = st.select_slider("Round", options=list(range(1, 14)), value=13)

    weekly = evidence[evidence.function == function].sort_values("week").copy()
    visible = weekly[weekly.week <= week]
    current = visible.iloc[-1]
    best = visible.loc[visible.output.idxmax()]
    dimension = DIMENSIONS[function]
    coordinate_columns = [f"x{index}" for index in range(1, dimension + 1)]
    starter_count = len(complete[(complete.function == function) & (complete.source == "starter")])

    metrics = st.columns(5)
    metrics[0].metric("Objective", "Maximise")
    metrics[1].metric("Samples available", starter_count + week)
    metrics[2].metric("Dimensions", dimension)
    metrics[3].metric("Best raw output", format_number(best.output))
    metrics[4].metric("Competition progress", f"{week / 13:.1%}")

    with st.expander("All functions at this round"):
        rows = []
        for candidate_function in range(1, 9):
            candidate = evidence[
                (evidence.function == candidate_function) & (evidence.week <= week)
            ]
            candidate_best = candidate.loc[candidate.output.idxmax()]
            rows.append({
                "Function": f"F{candidate_function}", "Round": week,
                "Dimensions": DIMENSIONS[candidate_function],
                "Current output": candidate.iloc[-1].output,
                "Best output so far": candidate_best.output,
                "Best round": int(candidate_best.week),
            })
        st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)

    tabs = st.tabs(["Overview", "History", "Submission", "Strategy", "PCA", "Diagnostics"])
    with tabs[0]:
        st.subheader(f"Function {function}, Round {week}")
        st.markdown("### Best observed input")
        st.dataframe(
            pd.DataFrame([[best[column] for column in coordinate_columns]], columns=coordinate_columns),
            hide_index=True, use_container_width=True,
        )
        columns = st.columns(3)
        columns[0].metric("Best output", format_number(best.output))
        columns[1].metric("Found in round", int(best.week))
        columns[2].metric("Rounds retained", int(week - best.week + 1))
        st.write("This is the strongest genuine evaluator result available at the selected round.")
    with tabs[1]:
        history = visible[["week", "output"]].copy()
        history["Best observed output"] = history.output.cummax()
        history = history.rename(columns={"output": "Round output"}).set_index("week")
        st.line_chart(history, height=390)
        history_table = visible[["week", *coordinate_columns, "output"]].copy()
        history_table["Best so far"] = visible.output.cummax().to_numpy()
        st.dataframe(history_table, hide_index=True, use_container_width=True)
    with tabs[2]:
        st.subheader("Submitted coordinate")
        st.dataframe(
            pd.DataFrame([[current[column] for column in coordinate_columns]], columns=coordinate_columns),
            hide_index=True, use_container_width=True,
        )
        columns = st.columns(3)
        columns[0].metric("Evaluator output", format_number(current.output))
        columns[1].metric("Difference from best", format_number(current.output - best.output))
        if len(visible) > 1:
            previous = visible.iloc[-2]
            movement = np.linalg.norm(
                current[coordinate_columns].to_numpy(float)
                - previous[coordinate_columns].to_numpy(float)
            )
            columns[2].metric("Movement from prior round", f"{movement:.6f}")
        else:
            columns[2].metric("Movement from prior round", "First round")
    with tabs[3]:
        st.subheader("Observed search behaviour")
        strategy_rows = []
        previous_row = None
        for _, row in visible.iterrows():
            if previous_row is None:
                movement = np.nan
                decision = "Opening query"
            else:
                movement = float(np.linalg.norm(
                    row[coordinate_columns].to_numpy(float)
                    - previous_row[coordinate_columns].to_numpy(float)
                ))
                if movement == 0:
                    decision = "Confirmation"
                elif movement <= 0.05 * np.sqrt(dimension):
                    decision = "Local exploitation"
                else:
                    decision = "Broader exploration"
            strategy_rows.append({
                "Round": int(row.week), "Movement": movement,
                "Observed role": decision, "Output": row.output,
            })
            previous_row = row
        st.dataframe(pd.DataFrame(strategy_rows), hide_index=True, use_container_width=True)
        st.caption(
            "The role is inferred from coordinate movement. It describes the observed search pattern and is not an evaluator label."
        )
    with tabs[4]:
        st.subheader("Coordinate structure available at this round")
        allowed_sources = ["starter", *[f"week_{value:02d}" for value in range(1, week + 1)]]
        cumulative = complete[
            (complete.function == function) & complete.source.isin(allowed_sources)
        ][coordinate_columns].dropna().to_numpy(float)
        centred = cumulative - cumulative.mean(axis=0, keepdims=True)
        if len(cumulative) >= 2 and np.any(centred):
            _, singular_values, components = np.linalg.svd(centred, full_matrices=False)
            variance = singular_values ** 2
            ratio = variance / variance.sum()
            pca_table = pd.DataFrame({
                "Component": [f"PC{index}" for index in range(1, len(ratio) + 1)],
                "Explained variance": ratio,
                "Cumulative variance": np.cumsum(ratio),
            })
            st.bar_chart(pca_table.set_index("Component")[["Explained variance"]])
            st.dataframe(pca_table, hide_index=True, use_container_width=True)
            with st.expander("Component loadings"):
                st.dataframe(
                    pd.DataFrame(
                        components, columns=coordinate_columns,
                        index=[f"PC{index}" for index in range(1, len(components) + 1)],
                    ),
                    use_container_width=True,
                )
        else:
            st.info("There are not enough distinct observations for a stable component calculation.")
    with tabs[5]:
        unique_count = visible[coordinate_columns].drop_duplicates().shape[0]
        diagnostic_rows = pd.DataFrame([
            ("Weekly observations visible", len(visible)),
            ("Unique submitted coordinates", unique_count),
            ("Repeated submissions", len(visible) - unique_count),
            ("Observed output span", format_number(visible.output.max() - visible.output.min())),
            ("Best round", int(best.week)),
            ("Best retained at selected round", "Yes" if current.output == best.output else "No"),
        ], columns=["Diagnostic", "Result"])
        st.dataframe(diagnostic_rows, hide_index=True, use_container_width=True)
        repeated = visible[visible.duplicated(coordinate_columns, keep=False)]
        if not repeated.empty:
            st.markdown("### Repeated-coordinate checks")
            st.dataframe(
                repeated[["week", *coordinate_columns, "output"]],
                hide_index=True, use_container_width=True,
            )


def function_explorer(evidence: pd.DataFrame) -> None:
    page_header(
        "Function Explorer",
        "Follow one function through every submitted coordinate and evaluator response.",
    )
    function = st.selectbox(
        "Choose a function", list(DIMENSIONS),
        format_func=lambda value: FUNCTION_NAMES[value],
    )
    frame = evidence[evidence.function == function].sort_values("week").copy()
    best = frame.loc[frame.output.idxmax()]
    first = frame.iloc[0]
    final = frame.iloc[-1]

    columns = st.columns(4)
    columns[0].metric("Dimensions", DIMENSIONS[function])
    columns[1].metric("Best round", int(best.week))
    columns[2].metric("Best output", format_number(best.output))
    columns[3].metric("Final output", format_number(final.output))

    st.subheader("Output by round")
    st.line_chart(frame.set_index("week")[["output"]].rename(columns={"output": f"F{function} output"}), height=350)

    st.subheader("Coordinate movement")
    coordinate_columns = [f"x{index}" for index in range(1, DIMENSIONS[function] + 1)]
    coordinate_chart = frame.set_index("week")[coordinate_columns]
    st.line_chart(coordinate_chart, height=350)

    st.subheader("What changed")
    comparison = pd.DataFrame([
        {"Point": "Week 1", "Coordinate": coordinate_text(first, function), "Output": format_number(first.output)},
        {"Point": "Best round", "Coordinate": coordinate_text(best, function), "Output": format_number(best.output)},
        {"Point": "Week 13", "Coordinate": coordinate_text(final, function), "Output": format_number(final.output)},
    ])
    st.dataframe(comparison, hide_index=True, use_container_width=True)

    st.subheader("Complete thirteen-round record")
    table = frame[["week", *coordinate_columns, "output"]].copy()
    table["week"] = table.week.astype(int)
    st.dataframe(table, hide_index=True, use_container_width=True)
    st.download_button(
        "Download this function's record", table.to_csv(index=False).encode("utf-8"),
        file_name=f"Imperial_BBO_F{function}_weeks_01_to_13.csv", mime="text/csv",
    )


def retrospective(evidence: pd.DataFrame) -> None:
    page_header(
        "Capstone Retrospective",
        "Evidence for the required reflection on progress, decisions, trade-offs, outcomes and practical learning.",
    )
    st.info(
        "The discussion response must remain your own reflection and stay below 2,000 words. This page organises the supporting evidence."
    )

    st.subheader("1. Initial codebase")
    st.write(
        "Explain how the starting codebase was chosen, whether it came from a public library, previous work or was built from scratch, and why it was selected. Add the public link so peers can inspect it."
    )
    st.markdown(
        "**Evidence to mention:** the starting workflow had to accept functions with 2 to 8 dimensions, retain six-decimal coordinates and keep each function within the interval from 0 to 1."
    )
    st.warning(
        "The numerical records do not identify the origin of the starting code. Confirm this from the repository history before completing this paragraph."
    )

    st.subheader("2. Weekly modification and feedback")
    st.write(
        "Explain what changed in the code each week, why each adjustment was made, how it affected the results and which changes had the greatest impact. Select a transition below for numerical evidence."
    )
    transition = st.slider("Compare consecutive rounds", 2, 13, 13)
    previous = evidence[evidence.week == transition - 1].set_index("function")
    current = evidence[evidence.week == transition].set_index("function")
    rows = []
    for function in range(1, 9):
        columns = [f"x{index}" for index in range(1, DIMENSIONS[function] + 1)]
        movement = ((current.loc[function, columns] - previous.loc[function, columns]) ** 2).sum() ** 0.5
        output_change = current.loc[function, "output"] - previous.loc[function, "output"]
        rows.append({
            "Function": f"F{function}", "Coordinate movement": movement,
            "Output change": output_change,
            "Outcome": "Improved" if output_change > 0 else ("Unchanged" if output_change == 0 else "Reduced"),
        })
    st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)

    st.subheader("3. Final results")
    st.write(
        "Describe how the score changed in the final weeks. Then explain what you would do differently with more time or a fresh start."
    )
    first = evidence[evidence.week == 1].set_index("function")
    final = evidence[evidence.week == 13].set_index("function")
    best = winners(evidence).set_index("function")
    result_rows = []
    for function in range(1, 9):
        result_rows.append({
            "Function": f"F{function}",
            "Week 1 output": format_number(first.loc[function, "output"]),
            "Week 13 output": format_number(final.loc[function, "output"]),
            "Best output": format_number(best.loc[function, "output"]),
            "Best round": int(best.loc[function, "week"]),
            "Final round retained best": bool(final.loc[function, "output"] == best.loc[function, "output"]),
        })
    st.dataframe(pd.DataFrame(result_rows), hide_index=True, use_container_width=True)
    st.caption(
        "F3, F5 and F6 reached their strongest weekly result in Week 13. Some other functions had already peaked, so their final-round role was confirmation rather than further movement."
    )
    with st.expander("Fresh-start considerations"):
        st.markdown(
            """
            - Establish one consistent experiment log from the first round.
            - Reserve explicit rounds for repeated-coordinate checks.
            - Scale movement according to dimensionality instead of using one step size for every function.
            - Separate exploratory candidates from local refinement candidates before selecting each submission.
            - Record the expected value, uncertainty and reason for every proposed coordinate before evaluation.
            """
        )

    st.subheader("4. Trade-offs and decisions")
    st.write(
        "Identify the most significant trade-offs and explain how exploration and exploitation, or short-term gains and longer-term learning, were balanced."
    )
    trade_columns = st.columns(3)
    with trade_columns[0]:
        st.markdown("### Exploration")
        st.write("Larger coordinate movements gathered information but risked losing a strong known region.")
    with trade_columns[1]:
        st.markdown("### Exploitation")
        st.write("Smaller local changes refined promising regions but could miss a separate, better peak.")
    with trade_columns[2]:
        st.markdown("### Confirmation")
        st.write("Repeating a coordinate tested stability but used a round without exploring a new point.")

    repeated_rows = []
    for function in range(1, 9):
        frame = evidence[evidence.function == function]
        columns = [f"x{index}" for index in range(1, DIMENSIONS[function] + 1)]
        repeated_rows.append({
            "Function": f"F{function}",
            "Rounds": 13,
            "Unique coordinates": int(frame[columns].drop_duplicates().shape[0]),
            "Confirmation rounds": int(13 - frame[columns].drop_duplicates().shape[0]),
        })
    st.dataframe(pd.DataFrame(repeated_rows), hide_index=True, use_container_width=True)

    st.subheader("5. Learning and application")
    st.markdown("**Most important lesson and future application**")
    st.write(
        "The strongest lesson is that the same strategy should not be imposed on every function. Dimensionality, response scale, repeatability and the amount of evidence all changed what counted as a sensible next move."
    )
    st.write(
        "In practical work, the same principle means balancing discovery against safe use of what is already known. Feedback should alter the next decision, while validation prevents an attractive but unsupported result from being treated as certain."
    )
    st.markdown("**What was surprising**")
    st.write(
        "Use your own experience here. The evidence offers several possible examples: some early winners survived to the end, F5 continued improving at the boundary, and repeated coordinates were valuable for distinguishing stability from apparent progress."
    )

    with st.expander("Final-round strategy prompts from the course"):
        st.markdown(
            """
            - How did the exploration and exploitation balance change as evidence increased?
            - Which approaches were effective, and which were difficult?
            - How did evaluator feedback alter the next coordinate?
            - What can iterative improvement contribute when the evaluator is unknown?
            - How could feedback-led strategies improve planning, efficiency or convergence?
            """
        )

    with st.expander("Submission and peer-review checklist"):
        st.markdown(
            """
            - Submit the response directly to the discussion board.
            - Keep the response below 2,000 words.
            - Compare strategies and trade-offs when responding to peers.
            - Offer constructive suggestions that could strengthen a peer's approach.
            - Connect peer reflections to challenges in your own work or practice.
            - Check that shared repositories have clear README files.
            - Check for appropriate licensing.
            - Check that code is documented and includes examples where useful.
            """
        )


def evidence_table(evidence: pd.DataFrame) -> None:
    page_header(
        "Assessment Evidence",
        "Filter and download the genuine Week 1 to Week 13 input and output record.",
    )
    left, right = st.columns(2)
    with left:
        selected_functions = st.multiselect(
            "Functions", list(DIMENSIONS), default=list(DIMENSIONS),
            format_func=lambda value: f"F{value}",
        )
    with right:
        week_range = st.slider("Week range", 1, 13, (1, 13))
    filtered = evidence[
        evidence.function.isin(selected_functions)
        & evidence.week.between(week_range[0], week_range[1])
    ].copy()
    filtered["function"] = filtered.function.map(lambda value: f"F{value}")
    visible_columns = ["function", "week", *[f"x{i}" for i in range(1, 9)], "output"]
    filtered = filtered[visible_columns].dropna(axis=1, how="all")
    st.dataframe(filtered, hide_index=True, use_container_width=True, height=520)
    st.download_button(
        "Download filtered assessment evidence", filtered.to_csv(index=False).encode("utf-8"),
        file_name="Imperial_BBO_assessment_evidence.csv", mime="text/csv",
    )


def apply_style() -> None:
    st.markdown(
        """
        <style>
        :root { --navy: #17365d; --gold: #d0a247; }
        .stApp { background: linear-gradient(180deg, #f9fbfd 0%, #edf3f8 100%); }
        [data-testid="stSidebar"] { background: #172b49; }
        [data-testid="stSidebar"] * { color: #f7f4ea; }
        h1, h2, h3 { color: var(--navy); letter-spacing: -0.02em; }
        .lead { color: #53667d; font-size: 1.12rem; max-width: 780px; margin-top: -0.55rem; }
        [data-testid="stMetric"] { background: white; border: 1px solid #dbe4ee; border-radius: 14px; padding: 1rem; }
        [data-testid="stMetricValue"] { color: var(--navy); }
        .stButton > button, .stDownloadButton > button { border-radius: 10px; border-color: var(--gold); }
        </style>
        """, unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Imperial BBO Challenge", page_icon="◈", layout="wide",
        initial_sidebar_state="expanded",
    )
    apply_style()
    evidence = load_assessed_evidence()
    complete = load_complete_internal_evidence()
    with st.sidebar:
        st.markdown("## Imperial BBO Challenge")
        st.caption("Thirteen-round capstone dashboard")
        page = st.radio(
            "Navigate", [
                "Overview", "Round dashboard", "Weekly progress", "Function explorer",
                "Capstone retrospective", "Assessment evidence",
            ],
            label_visibility="collapsed",
        )
        st.divider()
        st.caption("Official Week 1 to Week 13 evidence only")
    if page == "Overview":
        overview(evidence)
    elif page == "Round dashboard":
        round_dashboard(evidence, complete)
    elif page == "Weekly progress":
        weekly_progress(evidence)
    elif page == "Function explorer":
        function_explorer(evidence)
    elif page == "Capstone retrospective":
        retrospective(evidence)
    else:
        evidence_table(evidence)


if __name__ == "__main__":
    main()
