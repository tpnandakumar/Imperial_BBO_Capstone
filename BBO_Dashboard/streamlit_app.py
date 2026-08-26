from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parent
EVIDENCE_FILE = APP_DIR / "data" / "complete_internal_evidence.csv"

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
FUNCTION_NAMES = {function: f"Function {function} · {dimension} dimensions" for function, dimension in DIMENSIONS.items()}
FUNCTION_COLOURS = {
    1: "#8ecae6", 2: "#8dd3c7", 3: "#c9b6e4", 4: "#f6c98d",
    5: "#f3a6b5", 6: "#a9c7e8", 7: "#a8d8b9", 8: "#d7b5dd",
}


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


def navigate(page: str, *, function: int | None = None, week: int | None = None) -> None:
    st.session_state["page"] = page
    if function is not None:
        st.session_state["selected_function"] = function
    if week is not None:
        st.session_state["selected_week"] = week


def section_label(kicker: str, title: str, text: str = "") -> None:
    st.markdown(
        f"<div class='section-label'><span>{kicker}</span><h2>{title}</h2><p>{text}</p></div>",
        unsafe_allow_html=True,
    )


def landing_page(evidence: pd.DataFrame) -> None:
    best = winners(evidence)
    st.markdown(
        """
        <section class="hero">
          <div class="hero-kicker">IMPERIAL COLLEGE LONDON · BLACK BOX OPTIMISATION</div>
          <h1>Thirteen weeks.<br><span>Eight hidden functions.</span></h1>
          <p>An interactive visual companion to the capstone retrospective, connecting every submission, result, experiment and strategic decision.</p>
          <div class="hero-tags"><span>104 submissions</span><span>2 to 8 dimensions</span><span>One evolving strategy</span></div>
        </section>
        """, unsafe_allow_html=True,
    )
    section_label("CHOOSE A READING ROUTE", "Enter the visual book", "Read chronologically, follow one hidden function, or reproduce selected analytical experiments.")
    route_columns = st.columns(3)
    routes = [
        ("Read by Week", "Thirteen chronological chapters showing how the complete strategy developed.", "Week story", {"week": 1}),
        ("Read by Function", "Eight function chapters tracing inputs, outputs, turning points and winners.", "Function story", {"function": 1}),
        ("Explore the Code", "A controlled laboratory for reproducing and varying selected experiments.", "Code laboratory", {}),
    ]
    for column, (title, description, target, arguments) in zip(route_columns, routes):
        with column:
            st.markdown(f"<div class='route-card'><span>VISUAL BOOK</span><h3>{title}</h3><p>{description}</p></div>", unsafe_allow_html=True)
            if st.button(f"Open {title} →", key=f"route_{target}", use_container_width=True):
                navigate(target, **arguments)
                st.rerun()
    section_label("CHRONOLOGICAL STORY", "Journey through the thirteen rounds", "Open any week to see all eight submissions, returned outputs and their place in the optimisation story.")
    week_columns = st.columns(7)
    for week in range(1, 14):
        with week_columns[(week - 1) % 7]:
            if st.button(f"WEEK\n{week:02d}", key=f"home_week_{week}", use_container_width=True):
                navigate("Week story", week=week)
                st.rerun()
    section_label("FUNCTION STORIES", "Follow one function from F1 to F8", "Each page brings together its inputs, outputs, coordinate movement, winning result and full week-by-week evidence.")
    function_columns = st.columns(4)
    for function in range(1, 9):
        row = best[best.function == function].iloc[0]
        with function_columns[(function - 1) % 4]:
            st.markdown(
                f"""<div class="function-card" style="--accent:{FUNCTION_COLOURS[function]}">
                <div class="function-number">F{function}</div><div class="function-meta">{DIMENSIONS[function]} dimensions</div>
                <div class="function-result">{format_number(row.output)}</div><div class="function-caption">Best output · Week {int(row.week)}</div></div>""",
                unsafe_allow_html=True,
            )
            if st.button(f"Open F{function} story →", key=f"home_function_{function}", use_container_width=True):
                navigate("Function story", function=function)
                st.rerun()
    section_label("STRATEGIC EVOLUTION", "How the search learned", "The competition moved from broad discovery to evidence-led refinement and confirmation.")
    st.markdown(
        """<div class="story-ribbon"><div><b>01</b><strong>Explore</strong><span>Map unfamiliar regions</span></div><i>→</i>
        <div><b>02</b><strong>Learn</strong><span>Read patterns and failures</span></div><i>→</i>
        <div><b>03</b><strong>Exploit</strong><span>Refine strong coordinates</span></div><i>→</i>
        <div><b>04</b><strong>Confirm</strong><span>Test and retain winners</span></div></div>""", unsafe_allow_html=True,
    )


def week_story(evidence: pd.DataFrame) -> None:
    week = int(st.session_state.get("selected_week", 13))
    page_header(f"Week {week:02d}", f"The complete eight-function submission and evaluator response for Round {week}.")
    selected = st.select_slider("Move through the competition", options=list(range(1, 14)), value=week)
    if selected != week:
        navigate("Week story", week=selected)
        st.rerun()
    current = evidence[evidence.week == week].sort_values("function")
    prior = evidence[evidence.week == week - 1].set_index("function") if week > 1 else None
    cards = st.columns(4)
    for _, row in current.iterrows():
        function = int(row.function)
        delta = None if prior is None else float(row.output - prior.loc[function, "output"])
        delta_text = "Opening result" if delta is None else f"{delta:+.3g} from Week {week - 1}"
        with cards[(function - 1) % 4]:
            st.markdown(f"""<div class="week-result" style="--accent:{FUNCTION_COLOURS[function]}"><span>F{function} · {DIMENSIONS[function]}D</span><strong>{format_number(row.output)}</strong><small>{delta_text}</small></div>""", unsafe_allow_html=True)
            if st.button(f"Inspect F{function}", key=f"week_{week}_f{function}", use_container_width=True):
                navigate("Function story", function=function, week=week)
                st.rerun()
    st.subheader("Round evidence")
    table = current[["function", *[f"x{i}" for i in range(1, 9)], "output"]].copy()
    table["function"] = table.function.map(lambda value: f"F{value}")
    st.dataframe(table.dropna(axis=1, how="all"), hide_index=True, use_container_width=True)
    left, right = st.columns(2)
    if week > 1 and left.button(f"← Week {week - 1:02d}", use_container_width=True):
        navigate("Week story", week=week - 1); st.rerun()
    if week < 13 and right.button(f"Week {week + 1:02d} →", use_container_width=True):
        navigate("Week story", week=week + 1); st.rerun()
    if week == 13 and right.button("Continue to Chapter Summary →", use_container_width=True):
        navigate("Chapter Summary"); st.rerun()


def function_story(evidence: pd.DataFrame) -> None:
    function = int(st.session_state.get("selected_function", 1))
    frame = evidence[evidence.function == function].sort_values("week").copy()
    best = frame.loc[frame.output.idxmax()]
    final = frame.iloc[-1]
    coordinate_columns = [f"x{i}" for i in range(1, DIMENSIONS[function] + 1)]
    page_header(f"F{function} · Function Story", f"Thirteen rounds of evidence for the {DIMENSIONS[function]}-dimensional hidden function.")
    function_tabs = st.columns(8)
    for candidate in range(1, 9):
        with function_tabs[candidate - 1]:
            if st.button(f"F{candidate}", key=f"story_nav_f{candidate}", type="primary" if candidate == function else "secondary", use_container_width=True):
                navigate("Function story", function=candidate); st.rerun()
    metrics = st.columns(4)
    metrics[0].metric("Dimensions", DIMENSIONS[function])
    metrics[1].metric("Best output", format_number(best.output))
    metrics[2].metric("Winning week", f"Week {int(best.week):02d}")
    metrics[3].metric("Week 13 output", format_number(final.output))
    tabs = st.tabs(["Visual story", "Inputs and outputs", "Coordinate movement", "Week-by-week evidence"])
    with tabs[0]:
        chart = frame[["week", "output"]].copy()
        chart["Cumulative best"] = chart.output.cummax()
        st.subheader("Output development")
        st.line_chart(chart.set_index("week").rename(columns={"output": "Weekly output"}), height=420, color=[FUNCTION_COLOURS[function], "#e6b95c"])
        st.markdown(f"<div class='winner-callout'><span>WINNING COORDINATE</span><strong>{coordinate_text(best, function)}</strong><small>Returned {format_number(best.output)} in Week {int(best.week)}</small></div>", unsafe_allow_html=True)
    with tabs[1]:
        display = frame[["week", *coordinate_columns, "output"]].copy()
        display["Cumulative best"] = frame.output.cummax().to_numpy()
        st.dataframe(display, hide_index=True, use_container_width=True, height=500)
    with tabs[2]:
        st.line_chart(frame.set_index("week")[coordinate_columns], height=430)
        st.caption("Each line shows how one submitted coordinate changed across the thirteen rounds.")
    with tabs[3]:
        for _, row in frame.iterrows():
            selected_week = int(row.week) == int(st.session_state.get("selected_week", -1))
            with st.expander(f"Week {int(row.week):02d} · Output {format_number(row.output)}", expanded=selected_week):
                st.code(coordinate_text(row, function), language=None)
                if st.button(f"Open complete Week {int(row.week):02d}", key=f"f{function}_week_{int(row.week)}"):
                    navigate("Week story", week=int(row.week)); st.rerun()


def summary_chapter(evidence: pd.DataFrame) -> None:
    page_header("Chapter Summary", "The thirteen-week story condensed into outcomes, turning points, trade-offs and learning.")
    best = winners(evidence)
    first = evidence[evidence.week == 1].set_index("function")
    final = evidence[evidence.week == 13].set_index("function")
    st.markdown("<div class='chapter-banner'><span>SHARED FINAL CHAPTER</span><h2>What the complete journey established</h2><p>This chapter joins both reading routes before the project moves beyond the official competition.</p></div>", unsafe_allow_html=True)
    metrics = st.columns(4)
    metrics[0].metric("Competition chapters", "13")
    metrics[1].metric("Function stories", "8")
    metrics[2].metric("Official evaluations", "104")
    metrics[3].metric("Objective", "Maximise")
    st.subheader("Final evidence across all functions")
    rows = []
    for _, row in best.iterrows():
        function = int(row.function)
        rows.append({
            "Function": f"F{function}",
            "Week 1": format_number(first.loc[function, "output"]),
            "Week 13": format_number(final.loc[function, "output"]),
            "Best output": format_number(row.output),
            "Winning week": int(row.week),
            "Winning input": row.coordinate,
        })
    st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)
    columns = st.columns(3)
    with columns[0]:
        st.markdown("### What changed")
        st.write("The search moved from broad sampling towards function-specific refinement, confirmation and selective boundary testing.")
    with columns[1]:
        st.markdown("### What mattered")
        st.write("Dimensionality, repeatability, response scale and the shape of previous results determined the next sensible move.")
    with columns[2]:
        st.markdown("### What was learned")
        st.write("No single optimisation rule was suitable for all eight functions. Feedback had to change both the coordinate and the method.")
    if st.button("Continue to Extend and Evolve →", use_container_width=True):
        navigate("Extend and Evolve"); st.rerun()


def extend_evolve_chapter() -> None:
    page_header("Extend and Evolve", "The bridge from the assessed Imperial challenge to the independent post-BBO programme.")
    st.warning("Everything beyond this point is post-capstone research and is not part of the official thirteen-round submission.")
    st.markdown(
        """<div class="evolve-loop">
        <div><b>Explore and Exploit</b><span>Optimise using current evidence</span></div><i>→</i>
        <div><b>Extend</b><span>Widen the question</span></div><i>→</i>
        <div><b>Evolve</b><span>Improve the method</span></div><i>→</i>
        <div><b>Experiment</b><span>Run a reproducible test</span></div><i>→</i>
        <div><b>Evaluate</b><span>Judge the evidence</span></div><i>↺</i>
        </div>""", unsafe_allow_html=True,
    )
    st.subheader("Post-BBO Advanced Next Stage")
    columns = st.columns(3)
    stages = [
        ("Maximisation", "Continue numbered optimisation runs until one defensible winning coordinate remains for each active function."),
        ("Resolution", "Reconstruct behaviour, test competing equations and separate supported findings from provisional hypotheses."),
        ("Evolution", "Use every evaluated experiment to redesign the next search and strengthen its validation."),
    ]
    for column, (title, text) in zip(columns, stages):
        with column:
            st.markdown(f"### {title}")
            st.write(text)
    st.info("The post-BBO repository section will be linked here once its public Advanced Next Stage index is created.")


def code_laboratory(evidence: pd.DataFrame, complete: pd.DataFrame) -> None:
    page_header("Explore the Code", "Reproduce an official analysis, change controlled settings and compare the result without altering the capstone record.")
    st.markdown("<div class='lab-notice'><strong>Safe experiment boundary</strong><span>Official evidence is read-only. Results created here are interactive demonstrations and are never presented as submitted competition outcomes.</span></div>", unsafe_allow_html=True)
    experiment = st.selectbox("Choose an experiment", ["PCA coordinate analysis", "Movement classification", "Output progression"])
    function = st.selectbox("Function", list(DIMENSIONS), format_func=lambda value: FUNCTION_NAMES[value], key="lab_function")
    week = st.select_slider("Evidence available through", options=list(range(1, 14)), value=13, key="lab_week")
    coordinate_columns = [f"x{i}" for i in range(1, DIMENSIONS[function] + 1)]
    official = evidence[(evidence.function == function) & (evidence.week <= week)].sort_values("week")
    official_tab, variation_tab, source_tab = st.tabs(["Official reproduction", "Interactive variation", "Open the code"])
    with official_tab:
        st.success("OFFICIAL REPRODUCTION · Uses saved evidence and the dashboard's documented calculation.")
        if experiment == "PCA coordinate analysis":
            allowed = ["starter", *[f"week_{value:02d}" for value in range(1, week + 1)]]
            values = complete[(complete.function == function) & complete.source.isin(allowed)][coordinate_columns].dropna().to_numpy(float)
            centred = values - values.mean(axis=0, keepdims=True)
            _, singular_values, components = np.linalg.svd(centred, full_matrices=False)
            variance = singular_values ** 2
            ratio = variance / variance.sum()
            pca = pd.DataFrame({"Component": [f"PC{i}" for i in range(1, len(ratio) + 1)], "Explained variance": ratio, "Cumulative variance": np.cumsum(ratio)})
            st.bar_chart(pca.set_index("Component")[["Explained variance"]], color=FUNCTION_COLOURS[function])
            st.dataframe(pca, hide_index=True, use_container_width=True)
            with st.expander("Component loadings"):
                st.dataframe(pd.DataFrame(components, columns=coordinate_columns, index=pca.Component), use_container_width=True)
        elif experiment == "Movement classification":
            threshold = 0.05 * np.sqrt(DIMENSIONS[function])
            values = official[coordinate_columns].to_numpy(float)
            movement = np.r_[np.nan, np.linalg.norm(np.diff(values, axis=0), axis=1)]
            roles = ["Opening query" if np.isnan(value) else "Confirmation" if value == 0 else "Local exploitation" if value <= threshold else "Broader exploration" for value in movement]
            st.metric("Documented movement threshold", f"{threshold:.6f}")
            st.dataframe(pd.DataFrame({"Week": official.week, "Movement": movement, "Observed role": roles, "Output": official.output}), hide_index=True, use_container_width=True)
        else:
            progression = official[["week", "output"]].copy()
            progression["Cumulative best"] = progression.output.cummax()
            st.line_chart(progression.set_index("week"), height=420, color=[FUNCTION_COLOURS[function], "#e6b95c"])
    with variation_tab:
        st.info("INTERACTIVE VARIATION · The settings below were not necessarily used in the official submission.")
        if experiment == "PCA coordinate analysis":
            include_starter = st.toggle("Include starter observations", value=True)
            scale_coordinates = st.toggle("Standardise coordinates", value=False)
            sources = [*(["starter"] if include_starter else []), *[f"week_{value:02d}" for value in range(1, week + 1)]]
            values = complete[(complete.function == function) & complete.source.isin(sources)][coordinate_columns].dropna().to_numpy(float)
            if scale_coordinates:
                standard_deviation = values.std(axis=0, ddof=0)
                values = (values - values.mean(axis=0)) / np.where(standard_deviation == 0, 1, standard_deviation)
            centred = values - values.mean(axis=0, keepdims=True)
            _, singular_values, _ = np.linalg.svd(centred, full_matrices=False)
            ratio = singular_values ** 2 / np.sum(singular_values ** 2)
            st.bar_chart(pd.DataFrame({"Explained variance": ratio}, index=[f"PC{i}" for i in range(1, len(ratio) + 1)]), color="#b9a7d4")
        elif experiment == "Movement classification":
            threshold = st.slider("Local-movement threshold", 0.001, 0.500, float(min(0.05 * np.sqrt(DIMENSIONS[function]), 0.5)), 0.001)
            values = official[coordinate_columns].to_numpy(float)
            movement = np.r_[np.nan, np.linalg.norm(np.diff(values, axis=0), axis=1)]
            roles = ["Opening query" if np.isnan(value) else "Confirmation" if value == 0 else "Local exploitation" if value <= threshold else "Broader exploration" for value in movement]
            st.dataframe(pd.DataFrame({"Week": official.week, "Movement": movement, "Interactive role": roles}), hide_index=True, use_container_width=True)
        else:
            normalise = st.toggle("Normalise output to the observed range", value=True)
            progression = official[["week", "output"]].copy()
            if normalise:
                span = progression.output.max() - progression.output.min()
                progression["output"] = (progression.output - progression.output.min()) / (span if span else 1)
            progression["Cumulative best"] = progression.output.cummax()
            st.line_chart(progression.set_index("week"), height=420, color=["#9bcfc5", "#dfb7c0"])
    with source_tab:
        st.write("The live demonstrations are implemented in the dashboard source. The repository file can be inspected, downloaded or run locally.")
        st.link_button("Open streamlit_app.py on GitHub", "https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/BBO_Dashboard/streamlit_app.py")
        st.code("streamlit run BBO_Dashboard/streamlit_app.py", language="bash")


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
        :root { --navy: #203a59; --gold: #e6b95c; --mint: #dff4ee; --blue: #e4f1f8; --lavender: #eee8f7; --peach: #fff0df; }
        .stApp { background: radial-gradient(circle at 88% 0%, #e8f6f4 0, transparent 30%), linear-gradient(180deg, #fffdfa 0%, #f3f7fa 100%); }
        .main .block-container { max-width: 1380px; padding-top: 2rem; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #e7f1f7 0%, #edf5f1 55%, #f4eef8 100%); border-right: 1px solid #d4e1e8; }
        [data-testid="stSidebar"] * { color: #29445f; }
        h1, h2, h3 { color: var(--navy); letter-spacing: -0.035em; }
        .lead { color: #53667d; font-size: 1.12rem; max-width: 780px; margin-top: -0.55rem; }
        [data-testid="stMetric"] { background: rgba(255,255,255,.9); border: 1px solid #dbe5eb; border-radius: 18px; padding: 1rem; box-shadow: 0 10px 30px rgba(32,58,89,.06); }
        [data-testid="stMetricValue"] { color: var(--navy); }
        .stButton > button, .stDownloadButton > button { border-radius: 12px; border-color: #c9d9e2; font-weight: 650; min-height: 2.75rem; background: rgba(255,255,255,.78); }
        .stButton > button:hover { border-color: #80b8b0; color: var(--navy); box-shadow: 0 5px 18px rgba(32,58,89,.10); }
        .hero { background: linear-gradient(125deg, #dff1f7 0%, #e5f4ef 48%, #eee7f6 100%); border:1px solid #d4e4ea; border-radius:28px; padding:4rem 4.25rem; margin-bottom:3rem; box-shadow:0 24px 60px rgba(32,58,89,.10); position:relative; overflow:hidden; }
        .hero:after { content:""; position:absolute; width:350px; height:350px; right:-90px; top:-150px; border:1px solid rgba(53,107,126,.14); border-radius:50%; box-shadow:0 0 0 60px rgba(255,255,255,.25),0 0 0 120px rgba(255,255,255,.18); }
        .hero-kicker { color:#4f8982; font-weight:800; font-size:.76rem; letter-spacing:.16em; margin-bottom:1.3rem; }
        .hero h1 { color:#203a59; font-size:clamp(2.8rem,5vw,5.2rem); line-height:.98; margin:0 0 1.5rem; max-width:900px; }
        .hero h1 span { color:#8672a5; }
        .hero p { font-size:1.18rem; color:#536a7e; max-width:760px; line-height:1.65; }
        .hero-tags { display:flex; gap:.7rem; flex-wrap:wrap; margin-top:2rem; }
        .hero-tags span { border:1px solid rgba(66,111,126,.20); background:rgba(255,255,255,.45); border-radius:999px; padding:.5rem .85rem; color:#3d6074; font-size:.86rem; }
        .section-label { margin:3.4rem 0 1.25rem; }
        .section-label span { color:#5b918b; font-size:.74rem; font-weight:800; letter-spacing:.15em; }
        .section-label h2 { margin:.25rem 0 .3rem; font-size:2rem; }
        .section-label p { color:#627489; max-width:850px; margin:0; }
        .function-card { background:rgba(255,255,255,.9); border-radius:20px; padding:1.25rem 1.3rem; margin-top:.8rem; border-top:6px solid var(--accent); box-shadow:0 12px 32px rgba(32,58,89,.08); min-height:155px; }
        .route-card { background:rgba(255,255,255,.82); border:1px solid #dbe6eb; border-radius:20px; padding:1.35rem; min-height:178px; box-shadow:0 12px 30px rgba(32,58,89,.06); }
        .route-card span { color:#5b918b; font-size:.68rem; font-weight:850; letter-spacing:.14em; }
        .route-card h3 { margin:.45rem 0; }
        .route-card p { color:#65788a; font-size:.9rem; line-height:1.55; }
        .function-number { font-size:1.8rem; font-weight:850; color:var(--navy); }
        .function-meta,.function-caption { color:#738397; font-size:.79rem; }
        .function-result { font-size:1.24rem; font-weight:750; color:#294963; margin-top:1.15rem; overflow-wrap:anywhere; }
        .week-result { background:rgba(255,255,255,.92); border-left:6px solid var(--accent); border-radius:16px; padding:1rem 1.1rem; margin:.55rem 0 .25rem; box-shadow:0 8px 24px rgba(32,58,89,.07); }
        .week-result span,.week-result small { display:block; color:#718196; }
        .week-result strong { display:block; color:var(--navy); font-size:1.28rem; margin:.35rem 0; overflow-wrap:anywhere; }
        .story-ribbon { display:flex; align-items:center; justify-content:space-between; gap:1rem; background:linear-gradient(100deg,#e2f3ee,#e7f0f8,#f0e9f7,#fff0df); padding:1.6rem; border:1px solid #d8e3e7; border-radius:20px; color:#29445f; }
        .story-ribbon div { display:grid; gap:.15rem; }
        .story-ribbon b { color:#5a938b; font-size:.72rem; }
        .story-ribbon strong { font-size:1.08rem; }
        .story-ribbon span { color:#687c8e; font-size:.78rem; }
        .story-ribbon i { color:#a88952; font-style:normal; font-size:1.4rem; }
        .winner-callout { background:linear-gradient(120deg,#fff3df,#fff); border:1px solid #eed8aa; border-radius:18px; padding:1.25rem 1.4rem; margin:1.25rem 0; }
        .winner-callout span,.winner-callout small { display:block; color:#78663e; }
        .winner-callout span { font-size:.7rem; font-weight:800; letter-spacing:.13em; }
        .winner-callout strong { display:block; color:#203a59; font-size:1.05rem; margin:.4rem 0; overflow-wrap:anywhere; }
        .chapter-banner { background:linear-gradient(110deg,#e5f3f0,#e8f1f8,#f1eaf7); border:1px solid #d6e3e8; border-radius:22px; padding:1.65rem 1.8rem; margin:1rem 0 1.5rem; }
        .chapter-banner span { color:#5b918b; font-size:.68rem; font-weight:850; letter-spacing:.14em; }
        .chapter-banner h2 { margin:.4rem 0; }
        .chapter-banner p { margin:0; color:#65788a; }
        .lab-notice { display:grid; gap:.35rem; background:#fff4e5; border:1px solid #ecd8b4; border-radius:16px; padding:1rem 1.2rem; margin:1rem 0 1.5rem; }
        .lab-notice strong { color:#6f5931; }
        .lab-notice span { color:#786b55; }
        .evolve-loop { display:flex; gap:.6rem; align-items:stretch; margin:1.5rem 0 2rem; }
        .evolve-loop div { flex:1; display:grid; align-content:center; gap:.35rem; background:linear-gradient(145deg,#edf7f4,#f2eef8); border:1px solid #d9e4e7; border-radius:16px; padding:1rem; }
        .evolve-loop b { color:#29445f; }
        .evolve-loop span { color:#687c8e; font-size:.78rem; }
        .evolve-loop i { align-self:center; color:#a88952; font-style:normal; font-size:1.25rem; }
        [data-testid="stDataFrame"] { border-radius:16px; overflow:hidden; box-shadow:0 8px 25px rgba(32,58,89,.05); }
        @media(max-width:800px) { .hero{padding:2.2rem 1.5rem}.story-ribbon,.evolve-loop{display:grid}.story-ribbon i,.evolve-loop i{transform:rotate(90deg)} }
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
    if "page" not in st.session_state:
        st.session_state["page"] = "Visual home"
    with st.sidebar:
        st.markdown("## ◈ Imperial BBO")
        st.caption("Interactive capstone evidence")
        pages = [
            "Visual home", "Week story", "Function story", "Code laboratory",
            "Chapter Summary", "Extend and Evolve", "Round dashboard",
            "Weekly progress", "Capstone retrospective", "Assessment evidence",
        ]
        page = st.radio(
            "Navigate", pages,
            key="page",
            label_visibility="collapsed",
        )
        st.divider()
        st.caption("Official Week 1 to Week 13 evidence only")
    if page == "Visual home":
        landing_page(evidence)
    elif page == "Week story":
        week_story(evidence)
    elif page == "Function story":
        function_story(evidence)
    elif page == "Code laboratory":
        code_laboratory(evidence, complete)
    elif page == "Chapter Summary":
        summary_chapter(evidence)
    elif page == "Extend and Evolve":
        extend_evolve_chapter()
    elif page == "Round dashboard":
        round_dashboard(evidence, complete)
    elif page == "Weekly progress":
        weekly_progress(evidence)
    elif page == "Capstone retrospective":
        retrospective(evidence)
    else:
        evidence_table(evidence)


if __name__ == "__main__":
    main()
