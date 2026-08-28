from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from hpo_engine import tune_clustering, tune_surrogate


APP_DIR = Path(__file__).resolve().parent
EVIDENCE_FILE = APP_DIR / "data" / "complete_internal_evidence.csv"
METHOD_REGISTER_FILE = APP_DIR / "METHOD_EXPERIMENT_REGISTER.csv"
CAPSTONE_STORY_FILE = APP_DIR / "CAPSTONE_WEEK_STORY.csv"

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
FUNCTION_NAMES = {function: f"Function {function} · {dimension} dimensions" for function, dimension in DIMENSIONS.items()}
FUNCTION_COLOURS = {
    1: "#8ecae6", 2: "#8dd3c7", 3: "#c9b6e4", 4: "#f6c98d",
    5: "#f3a6b5", 6: "#a9c7e8", 7: "#a8d8b9", 8: "#d7b5dd",
}

BOOK_PAGES = {
    "Week story": ("PART I", "Thirteen rounds", 1),
    "Function story": ("PART II", "Eight hidden functions", 2),
    "Methods and Evolution": ("PART III", "Methods and decisions", 3),
    "Chapter Summary": ("PART IV", "What the evidence established", 4),
    "Extend and Evolve": ("EPILOGUE", "Beyond the assessed challenge", 5),
}

PAGE_LABELS = {
    "Visual home": "Home and reading routes",
    "Week story": "Book I: Week chapters",
    "Function story": "Book II: Function chapters",
    "Methods and Evolution": "Book III: Methods and evolution",
    "Chapter Summary": "Book IV: Chapter summary",
    "Extend and Evolve": "Epilogue: Extend and evolve",
    "Code laboratory": "Laboratory: Reproduce analyses",
    "Round dashboard": "Dashboard: Inspect each round",
    "Weekly progress": "Dashboard: Weekly progress",
    "Capstone retrospective": "Evidence: Retrospective",
    "Assessment evidence": "Evidence: Complete record",
}

WEEK_CONTEXT = {
    1: ("Opening exploration", "Establish the first benchmark and begin mapping eight unfamiliar response surfaces."),
    2: ("Function-specific strategy", "Exploit the strongest supported direction while allowing uncertain functions more exploration."),
    3: ("Ranking and movement", "Use ranking to organise attention but rely on change and movement to choose the next action."),
    4: ("Selective refinement", "Protect productive trajectories while continuing to gather evidence for weak functions."),
    5: ("Reassessment", "Reduce commitment to directions that deteriorated and protect the clearest gains."),
    6: ("Validation", "Use selective attention and a separate validation experiment to test whether the strategy remains defensible."),
    7: ("Responsive redirection", "Change direction when the newest evidence contradicts the earlier ranking."),
    8: ("Selective continuation", "Continue productive regions while reducing commitment to weakening directions."),
    9: ("Transparency and repeatability", "Add evidence documentation and introduce an explicit repeatability test."),
    10: ("Clustering and recovery", "Use recurring regions distances stability and plateaus to select the Week 11 actions."),
    11: ("PCA and method comparison", "Compare PCA structure with direct objective evidence before selecting Week 12."),
    12: ("Outcome validation", "Test repetition refinement recovery and boundary movement before the final round."),
    13: ("Final evaluation", "Balance controlled risk repeatability and sequential-decision reflection before stopping."),
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


@st.cache_data
def load_method_register() -> pd.DataFrame:
    return pd.read_csv(METHOD_REGISTER_FILE)


@st.cache_data
def load_capstone_story() -> pd.DataFrame:
    return pd.read_csv(CAPSTONE_STORY_FILE)


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


def navigate(
    page: str, *, function: int | None = None, week: int | None = None,
    remember: bool = True,
) -> None:
    # The sidebar radio owns ``session_state.page``.  Queue page changes and
    # apply them at the start of the next rerun, before that widget is built.
    current = st.session_state.get("page")
    if remember and current and current != page:
        history = st.session_state.setdefault("_page_history", [])
        if not history or history[-1] != current:
            history.append(current)
    st.session_state["_next_page"] = page
    if function is not None:
        st.session_state["selected_function"] = function
    if week is not None:
        st.session_state["selected_week"] = week


def section_label(kicker: str, title: str, text: str = "") -> None:
    st.markdown(
        f"<div class='section-label'><span>{kicker}</span><h2>{title}</h2><p>{text}</p></div>",
        unsafe_allow_html=True,
    )


def book_progress_header(page: str) -> None:
    """Add restrained book furniture to narrative pages."""
    if page not in BOOK_PAGES:
        return
    part, chapter, position = BOOK_PAGES[page]
    progress = position / len(BOOK_PAGES) * 100
    st.markdown(
        f"""<div class="book-progress">
        <div class="book-progress-copy"><span>{part}</span><strong>{chapter}</strong><small>{position:02d} / {len(BOOK_PAGES):02d}</small></div>
        <div class="book-progress-track"><i style="width:{progress:.0f}%"></i></div>
        </div>""",
        unsafe_allow_html=True,
    )


def page_navigation_controls(page: str, location: str) -> None:
    """Visible navigation for book pages, including collapsed mobile views."""
    if page == "Visual home":
        return
    with st.container(key=f"{location}_page_navigation"):
        previous_column, next_column, back_column, home_column = st.columns(4)
        if page == "Week story":
            item = int(st.session_state.get("selected_week", 13))
            if item > 1 and previous_column.button("← Previous", key=f"{location}_previous_week", width="stretch"):
                navigate(page, week=item - 1, remember=False); st.rerun()
            if item < 13 and next_column.button("Next →", key=f"{location}_next_week", width="stretch"):
                navigate(page, week=item + 1, remember=False); st.rerun()
        elif page == "Function story":
            item = int(st.session_state.get("selected_function", 1))
            if item > 1 and previous_column.button("← Previous", key=f"{location}_previous_function", width="stretch"):
                navigate(page, function=item - 1, remember=False); st.rerun()
            if item < 8 and next_column.button("Next →", key=f"{location}_next_function", width="stretch"):
                navigate(page, function=item + 1, remember=False); st.rerun()
        if back_column.button("↩ Back", key=f"{location}_back", width="stretch"):
            history = st.session_state.get("_page_history", [])
            destination = history.pop() if history else "Visual home"
            st.session_state["_page_history"] = history
            navigate(destination, remember=False)
            st.rerun()
        if home_column.button("⌂ Home", key=f"{location}_home", width="stretch"):
            st.session_state["_page_history"] = []
            navigate("Visual home", remember=False)
            st.rerun()


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
        <blockquote class="book-epigraph">
          <p>“Life is a stone. Sculpt yourself a masterpiece.”</p>
          <cite>Dr N T Pisharam, <em>Be and Become</em></cite>
        </blockquote>
        """, unsafe_allow_html=True,
    )
    section_label("CHOOSE A READING ROUTE", "Enter the visual book", "Read chronologically, follow one hidden function, or reproduce selected analytical experiments.")
    routes = {
        "Read by Week": ("Thirteen chronological chapters showing how the complete strategy developed.", "Week story", {"week": 1}),
        "Read by Function": ("Eight function chapters tracing inputs, outputs, turning points and winners.", "Function story", {"function": 1}),
        "Explore the Code": ("A controlled laboratory for reproducing and varying selected experiments.", "Code laboratory", {}),
    }
    selected_route = st.radio("Reading route", list(routes), horizontal=True, label_visibility="collapsed")
    description, target, arguments = routes[selected_route]
    st.markdown(
        f"<div class='route-card compact-route'><span>VISUAL BOOK</span>"
        f"<h3>{selected_route}</h3><p>{description}</p></div>",
        unsafe_allow_html=True,
    )
    if st.button(f"Open {selected_route} →", key="open_selected_route", width="stretch"):
        navigate(target, **arguments)
        st.rerun()
    # Keep the opening spread to one screen.  The detailed week, function and
    # method indexes live on their own navigable pages rather than below it.
    return
    section_label("CHRONOLOGICAL STORY", "Journey through the thirteen rounds", "Open any week to see all eight submissions, returned outputs and their place in the optimisation story.")
    week_columns = st.columns(7)
    for week in range(1, 14):
        with week_columns[(week - 1) % 7]:
            if st.button(f"WEEK\n{week:02d}", key=f"home_week_{week}", width="stretch"):
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
            if st.button(f"Open F{function} story →", key=f"home_function_{function}", width="stretch"):
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
    stage, rationale = WEEK_CONTEXT[week]
    view = st.radio(
        "Chapter spread", ["Overview", "Function detail", "Evidence table"],
        horizontal=True, key=f"week_{week}_spread",
    )
    if view == "Overview":
        st.markdown(
            f"<div class='chapter-banner'><span>CHAPTER PURPOSE · {stage.upper()}</span>"
            f"<h2>How the strategy was evolving</h2><p>{rationale}</p></div>",
            unsafe_allow_html=True,
        )
        if week > 1:
            changes = current.set_index("function").output - prior.output
            movement_values = []
            for function in range(1, 9):
                columns = [f"x{index}" for index in range(1, DIMENSIONS[function] + 1)]
                current_row = current[current.function == function].iloc[0]
                prior_row = evidence[(evidence.function == function) & (evidence.week == week - 1)].iloc[0]
                movement_values.append(float(np.linalg.norm(current_row[columns].to_numpy(float) - prior_row[columns].to_numpy(float))))
            evidence_metrics = st.columns(3)
            evidence_metrics[0].metric("Functions improved", int((changes > 0).sum()))
            evidence_metrics[1].metric("Functions unchanged", int((changes == 0).sum()))
            evidence_metrics[2].metric("Mean coordinate movement", f"{np.mean(movement_values):.4f}")
        else:
            st.info("The opening round established the first observation for each hidden function.")
    elif view == "Function detail":
        function = st.select_slider(
            "Choose a function", options=list(range(1, 9)), value=1,
            key=f"week_{week}_function", format_func=lambda value: f"F{value}",
        )
        row = current[current.function == function].iloc[0]
        delta = None if prior is None else float(row.output - prior.loc[function, "output"])
        delta_text = "Opening result" if delta is None else f"{delta:+.3g} from Week {week - 1}"
        st.markdown(
            f"<div class='week-result' style='--accent:{FUNCTION_COLOURS[function]}'>"
            f"<span>F{function} · {DIMENSIONS[function]} DIMENSIONS</span>"
            f"<strong>{format_number(row.output)}</strong><small>{delta_text}</small>"
            f"<small>{coordinate_text(row, function)}</small></div>",
            unsafe_allow_html=True,
        )
        if st.button(f"Open the complete F{function} chapter", key=f"week_{week}_open_f{function}"):
            navigate("Function story", function=function, week=week); st.rerun()
    else:
        table = current[["function", *[f"x{i}" for i in range(1, 9)], "output"]].copy()
        table["function"] = table.function.map(lambda value: f"F{value}")
        st.dataframe(table.dropna(axis=1, how="all"), hide_index=True, width="stretch", height=330)


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
            if st.button(f"F{candidate}", key=f"story_nav_f{candidate}", type="primary" if candidate == function else "secondary", width="stretch"):
                navigate("Function story", function=candidate); st.rerun()
    metrics = st.columns(4)
    metrics[0].metric("Dimensions", DIMENSIONS[function])
    metrics[1].metric("Best output", format_number(best.output))
    metrics[2].metric("Winning week", f"Week {int(best.week):02d}")
    metrics[3].metric("Week 13 output", format_number(final.output))
    spread = st.radio(
        "Function spread",
        ["Visual story", "Inputs and outputs", "Coordinate movement", "Week evidence"],
        horizontal=True,
        key=f"function_{function}_spread",
    )
    if spread == "Visual story":
        chart = frame[["week", "output"]].copy()
        chart["Cumulative best"] = chart.output.cummax()
        st.subheader("Output development")
        st.line_chart(chart.set_index("week").rename(columns={"output": "Weekly output"}), height=260, color=[FUNCTION_COLOURS[function], "#e6b95c"])
        st.markdown(f"<div class='winner-callout'><span>WINNING COORDINATE</span><strong>{coordinate_text(best, function)}</strong><small>Returned {format_number(best.output)} in Week {int(best.week)}</small></div>", unsafe_allow_html=True)
    elif spread == "Inputs and outputs":
        display = frame[["week", *coordinate_columns, "output"]].copy()
        display["Cumulative best"] = frame.output.cummax().to_numpy()
        st.dataframe(display, hide_index=True, width="stretch", height=300)
    elif spread == "Coordinate movement":
        st.line_chart(frame.set_index("week")[coordinate_columns], height=270)
        st.caption("Each line shows how one submitted coordinate changed across the thirteen rounds.")
    else:
        evidence_week = st.select_slider(
            "Choose one week", options=list(range(1, 14)),
            value=int(st.session_state.get("selected_week", 13)),
            key=f"f{function}_evidence_week",
        )
        row = frame[frame.week == evidence_week].iloc[0]
        st.markdown(
            f"<div class='week-result' style='--accent:{FUNCTION_COLOURS[function]}'>"
            f"<span>WEEK {evidence_week:02d}</span><strong>{format_number(row.output)}</strong>"
            f"<small>{coordinate_text(row, function)}</small></div>",
            unsafe_allow_html=True,
        )
        if st.button(f"Open complete Week {evidence_week:02d}", key=f"f{function}_week_open"):
            navigate("Week story", week=evidence_week); st.rerun()


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
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
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
    if st.button("Continue to Extend and Evolve →", width="stretch"):
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
    section_label(
        "THE SCULPTING FRAMEWORK",
        "From method to masterpiece",
        "A reflective structure for explaining how repeated analysis, adjustment and evaluation shaped the final work.",
    )
    st.markdown(
        """<div class="method-ribbon">
        <div><b>01</b><strong>Method</strong><span>Choose the analytical tool</span></div>
        <div><b>02</b><strong>Methodology</strong><span>Explain how and why it is used</span></div>
        <div><b>03</b><strong>Modulation</strong><span>Adjust the search using feedback</span></div>
        <div><b>04</b><strong>Modification</strong><span>Change the code or decision rule</span></div>
        <div><b>05</b><strong>Magnificence</strong><span>Bring the strongest evidence together</span></div>
        <div><b>06</b><strong>Masterpiece</strong><span>Present the complete evolving story</span></div>
        </div>
        <blockquote class="book-epigraph closing-epigraph">
          <p>“Life is a stone. Sculpt yourself a masterpiece.”</p>
          <cite>Dr N T Pisharam, <em>Be and Become</em></cite>
        </blockquote>""",
        unsafe_allow_html=True,
    )


def method_evolution_page(register: pd.DataFrame, capstone_story: pd.DataFrame) -> None:
    page_header("Methods and Evolution", "The analytical experiments, why they were introduced, and the evidence status of each claim.")
    st.markdown(
        """<div class="chapter-banner"><span>HOW THE WORK WAS SCULPTED</span>
        <h2>Tools were introduced to answer changing questions</h2>
        <p>Early rounds asked where to search. Later rounds asked how to interpret structure, tune decisions, reduce complexity and evaluate the remaining uncertainty.</p></div>""",
        unsafe_allow_html=True,
    )
    st.subheader("Week 1 to Week 13: focus and action")
    displayed_map = capstone_story.rename(columns={
        "week": "Week",
        "focus": "Focus",
        "what_we_did": "What we did",
        "evidence_shown": "What the evidence showed",
        "next_decision": "How it shaped the next decision",
    })
    displayed_map["Week"] = displayed_map["Week"].map(lambda value: f"Week {int(value)}")
    st.dataframe(
        displayed_map[["Week", "Focus", "What we did", "What the evidence showed", "How it shaped the next decision"]],
        hide_index=True,
        width="stretch",
    )
    st.info("This assessment-facing table is based on the weekly reflections and saved evidence from Week 1 to Week 13.")
    stages = [
        ("Surrogates and classification", "Weeks 1 to 3", "Bayesian optimisation, logistic improvement modelling, support vectors and kernels."),
        ("Neural experiments", "Weeks 4 to 6", "Function approximation, architecture comparison and a cautious convolutional experiment."),
        ("HPO and attention", "Weeks 7 to 9", "Tuning, attention-style ranking, scaling and emergence tests after the break."),
        ("Interpret and structure", "Weeks 10 to 12", "Transparency, clustering and principal component analysis."),
        ("Sequential decisions", "Week 13", "Bandit, MDP and Q-learning interpretations followed by final evaluation."),
    ]
    for number, (name, period, purpose) in enumerate(stages, 1):
        st.markdown(f"<div class='method-chapter'><b>{number:02d}</b><span>{period}</span><strong>{name}</strong><p>{purpose}</p></div>", unsafe_allow_html=True)
    decision_mask = register.status.str.contains(
        "Decision-influencing|Verified conceptual|verified later",
        case=False,
        regex=True,
    )
    decision_evidence = register[decision_mask].copy()
    supporting_evidence = register[~decision_mask].copy()
    decision_tab, supporting_tab = st.tabs(["Decision-influencing evidence", "Supporting and outcome evidence"])
    with decision_tab:
        st.success("These items have repository evidence, a documented later application, or a verified conceptual role in the final decision record.")
        st.dataframe(
            decision_evidence[["method", "family", "week_or_stage", "status", "confirmed_role", "confirmed_parameters", "evidence_path"]],
            hide_index=True,
            width="stretch",
        )
    with supporting_tab:
        st.info("These records support the strategy, validation, transparency, outcome analysis or stopping decision without claiming that each one directly selected the following coordinate.")
        st.dataframe(
            supporting_evidence[["method", "family", "week_or_stage", "status", "confirmed_role", "dashboard_action"]],
            hide_index=True,
            width="stretch",
        )
    st.subheader("Evidence rule")
    st.write("A method becomes part of the official visual story only when its data available at the time, parameter settings, code path, result and influence on the following decision can all be shown.")


def code_laboratory(evidence: pd.DataFrame, complete: pd.DataFrame) -> None:
    page_header("Explore the Code", "Reproduce an official analysis, change controlled settings and compare the result without altering the capstone record.")
    st.markdown("<div class='lab-notice'><strong>Safe experiment boundary</strong><span>Official evidence is read-only. Results created here are interactive demonstrations and are never presented as submitted competition outcomes.</span></div>", unsafe_allow_html=True)
    experiment = st.selectbox("Choose an experiment", ["Hyperparameter optimisation", "PCA coordinate analysis", "Movement classification", "Output progression"])
    function = st.selectbox("Function", list(DIMENSIONS), format_func=lambda value: FUNCTION_NAMES[value], key="lab_function")
    week = st.select_slider("Evidence available through", options=list(range(1, 14)), value=13, key="lab_week")
    coordinate_columns = [f"x{i}" for i in range(1, DIMENSIONS[function] + 1)]
    official = evidence[(evidence.function == function) & (evidence.week <= week)].sort_values("week")
    hpo_sources = ["starter", *[f"week_{value:02d}" for value in range(1, week + 1)]]
    hpo_evidence = complete[
        (complete.function == function) & complete.source.isin(hpo_sources)
    ].copy()
    hpo_evidence["source_order"] = hpo_evidence.source.map(
        {"starter": 0, **{f"week_{value:02d}": value for value in range(1, 14)}}
    )
    hpo_evidence = hpo_evidence.sort_values(["source_order", "sequence"])
    official_tab, variation_tab, source_tab = st.tabs(["Official reproduction", "Interactive variation", "Open the code"])
    with official_tab:
        st.success("OFFICIAL REPRODUCTION · Uses saved evidence and the dashboard's documented calculation.")
        if experiment == "Hyperparameter optimisation":
            st.markdown("### Clustering HPO reproduction for the Week 11 decision")
            st.write("The clustering analysis used evidence available through Week 10 to inform the Week 11 submission. It compared KMeans cluster counts `k=2` and `k=3`. Each candidate used `n_init=50` and `random_state=42`; the higher silhouette score selected the exploratory partition.")
            week10 = evidence[(evidence.function == function) & (evidence.week <= 10)].sort_values("week")
            values = week10[coordinate_columns].to_numpy(float)
            results, winner = tune_clustering(values, cluster_counts=(2, 3), n_init_values=(50,), random_state=42)
            metrics = st.columns(4)
            metrics[0].metric("Submission informed", "Week 11")
            metrics[1].metric("Observations", len(week10))
            metrics[2].metric("Selected k", int(winner["clusters"]))
            metrics[3].metric("Silhouette score", f"{winner['silhouette_score']:.4f}")
            st.dataframe(results, hide_index=True, width="stretch")
            st.caption("This reproduces analysis stored with the Week 10 evidence and used for the following submission. Clusters were an exploratory decision aid, not proof of the hidden function's true geometry.")
        elif experiment == "PCA coordinate analysis":
            allowed = ["starter", *[f"week_{value:02d}" for value in range(1, week + 1)]]
            values = complete[(complete.function == function) & complete.source.isin(allowed)][coordinate_columns].dropna().to_numpy(float)
            centred = values - values.mean(axis=0, keepdims=True)
            _, singular_values, components = np.linalg.svd(centred, full_matrices=False)
            variance = singular_values ** 2
            ratio = variance / variance.sum()
            pca = pd.DataFrame({"Component": [f"PC{i}" for i in range(1, len(ratio) + 1)], "Explained variance": ratio, "Cumulative variance": np.cumsum(ratio)})
            st.bar_chart(pca.set_index("Component")[["Explained variance"]], color=FUNCTION_COLOURS[function])
            st.dataframe(pca, hide_index=True, width="stretch")
            with st.expander("Component loadings"):
                st.dataframe(pd.DataFrame(components, columns=coordinate_columns, index=pca.Component), width="stretch")
        elif experiment == "Movement classification":
            threshold = 0.05 * np.sqrt(DIMENSIONS[function])
            values = official[coordinate_columns].to_numpy(float)
            movement = np.r_[np.nan, np.linalg.norm(np.diff(values, axis=0), axis=1)]
            roles = ["Opening query" if np.isnan(value) else "Confirmation" if value == 0 else "Local exploitation" if value <= threshold else "Broader exploration" for value in movement]
            st.metric("Documented movement threshold", f"{threshold:.6f}")
            st.dataframe(pd.DataFrame({"Week": official.week, "Movement": movement, "Observed role": roles, "Output": official.output}), hide_index=True, width="stretch")
        else:
            progression = official[["week", "output"]].copy()
            progression["Cumulative best"] = progression.output.cummax()
            st.line_chart(progression.set_index("week"), height=420, color=[FUNCTION_COLOURS[function], "#e6b95c"])
    with variation_tab:
        st.info("INTERACTIVE VARIATION · The settings below were not necessarily used in the official submission.")
        if experiment == "Hyperparameter optimisation":
            method = st.radio("Interactive HPO extension", ["Surrogate model", "Clustering"], horizontal=True, key="variation_hpo_method")
            values = hpo_evidence[coordinate_columns].to_numpy(float)
            if method == "Surrogate model":
                maximum_degree = st.slider("Maximum polynomial degree", 1, 4, 3)
                alpha_options = st.multiselect("Ridge alpha values", [1e-6, 1e-4, 1e-2, 1e-1, 1.0, 10.0, 100.0], default=[1e-4, 1e-2, 1.0, 10.0])
                if alpha_options:
                    results, winner = tune_surrogate(values, hpo_evidence.output.to_numpy(float), degrees=tuple(range(1, maximum_degree + 1)), alphas=tuple(alpha_options))
                    st.metric("Interactive winning configuration", f"degree={int(winner['degree'])}, alpha={winner['alpha']:g}")
                    st.dataframe(results, hide_index=True, width="stretch")
            else:
                maximum_clusters = st.slider("Maximum cluster count", 2, min(8, max(2, len(values) - 1)), min(6, max(2, len(values) - 1)))
                n_init_options = st.multiselect("n_init values", [5, 10, 25, 50, 100], default=[10, 25, 50])
                if n_init_options:
                    results, winner = tune_clustering(values, cluster_counts=tuple(range(2, maximum_clusters + 1)), n_init_values=tuple(n_init_options))
                    st.metric("Interactive winning configuration", f"c={int(winner['clusters'])}, n_init={int(winner['n_init'])}")
                    st.dataframe(results, hide_index=True, width="stretch")
        elif experiment == "PCA coordinate analysis":
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
            st.dataframe(pd.DataFrame({"Week": official.week, "Movement": movement, "Interactive role": roles}), hide_index=True, width="stretch")
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
        st.link_button("Open hpo_engine.py on GitHub", "https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/BBO_Dashboard/hpo_engine.py")
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
    st.dataframe(table, hide_index=True, width="stretch")

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
    st.dataframe(summary, hide_index=True, width="stretch")


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
        st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")

    tabs = st.tabs(["Overview", "History", "Submission", "Strategy", "PCA", "Diagnostics"])
    with tabs[0]:
        st.subheader(f"Function {function}, Round {week}")
        st.markdown("### Best observed input")
        st.dataframe(
            pd.DataFrame([[best[column] for column in coordinate_columns]], columns=coordinate_columns),
            hide_index=True, width="stretch",
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
        st.dataframe(history_table, hide_index=True, width="stretch")
    with tabs[2]:
        st.subheader("Submitted coordinate")
        st.dataframe(
            pd.DataFrame([[current[column] for column in coordinate_columns]], columns=coordinate_columns),
            hide_index=True, width="stretch",
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
        st.dataframe(pd.DataFrame(strategy_rows), hide_index=True, width="stretch")
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
            st.dataframe(pca_table, hide_index=True, width="stretch")
            with st.expander("Component loadings"):
                st.dataframe(
                    pd.DataFrame(
                        components, columns=coordinate_columns,
                        index=[f"PC{index}" for index in range(1, len(components) + 1)],
                    ),
                    width="stretch",
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
        diagnostic_rows["Result"] = diagnostic_rows["Result"].astype(str)
        st.dataframe(diagnostic_rows, hide_index=True, width="stretch")
        repeated = visible[visible.duplicated(coordinate_columns, keep=False)]
        if not repeated.empty:
            st.markdown("### Repeated-coordinate checks")
            st.dataframe(
                repeated[["week", *coordinate_columns, "output"]],
                hide_index=True, width="stretch",
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
    st.dataframe(comparison, hide_index=True, width="stretch")

    st.subheader("Complete thirteen-round record")
    table = frame[["week", *coordinate_columns, "output"]].copy()
    table["week"] = table.week.astype(int)
    st.dataframe(table, hide_index=True, width="stretch")
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
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")

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
    st.dataframe(pd.DataFrame(result_rows), hide_index=True, width="stretch")
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
    st.dataframe(pd.DataFrame(repeated_rows), hide_index=True, width="stretch")

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
    st.dataframe(filtered, hide_index=True, width="stretch", height=520)
    st.download_button(
        "Download filtered assessment evidence", filtered.to_csv(index=False).encode("utf-8"),
        file_name="Imperial_BBO_assessment_evidence.csv", mime="text/csv",
    )


def apply_style(reading_mode: bool = True, text_scale: int = 100) -> None:
    content_width = "1060px" if reading_mode else "1380px"
    body_size = text_scale / 100
    st.markdown(
        """
        <style>
        :root { --navy: #203a59; --gold: #e6b95c; --mint: #dff4ee; --blue: #e4f1f8; --lavender: #eee8f7; --peach: #fff0df; }
        .stApp { background: radial-gradient(circle at 88% 0%, #e8f6f4 0, transparent 30%), linear-gradient(180deg, #fffdfa 0%, #f3f7fa 100%); }
        .main .block-container { width:min(100%, __CONTENT_WIDTH__); max-width:__CONTENT_WIDTH__; padding:clamp(.55rem,1.4vh,1rem) clamp(.85rem,2.2vw,2.5rem) clamp(2.5rem,6vh,4rem); }
        .main .block-container p, .main .block-container li { font-size:__BODY_SIZE__rem; line-height:1.72; }
        .st-key-top_page_navigation { position:sticky; top:.35rem; z-index:999; padding:.38rem; margin:0 0 .45rem; border:1px solid #d8e3e7; border-radius:14px; background:rgba(247,251,252,.94); box-shadow:0 8px 24px rgba(32,58,89,.08); backdrop-filter:blur(12px); }
        .st-key-top_page_navigation [data-testid="stHorizontalBlock"] { gap:.38rem; }
        .st-key-top_page_navigation [data-testid="column"] { min-width:0 !important; }
        .st-key-top_page_navigation button { min-height:2.25rem; padding:.35rem .55rem; white-space:nowrap; }
        [data-testid="stSidebar"] { --sidebar-fluid:clamp(13.5rem,18vw,16rem); background: linear-gradient(180deg, #e7f1f7 0%, #edf5f1 55%, #f4eef8 100%); border-right: 1px solid #d4e1e8; min-width:var(--sidebar-fluid); max-width:var(--sidebar-fluid); }
        [data-testid="stSidebar"] > div:first-child { width:var(--sidebar-fluid); }
        [data-testid="stSidebar"] * { color: #29445f; }
        .sidebar-section { margin:.9rem 0 .45rem; color:#6b7f90; font-size:.64rem; font-weight:850; letter-spacing:.16em; }
        [data-testid="stSidebar"] [role="radiogroup"] label { border-radius:10px; padding:.34rem .45rem; margin:.08rem 0; }
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) { background:rgba(255,255,255,.72); box-shadow:0 3px 12px rgba(32,58,89,.08); }
        .stApp, [data-testid="stMarkdownContainer"] { color:#29445f; }
        h1, h2, h3, h1 span, h2 span, h3 span { color: var(--navy) !important; letter-spacing: -0.035em; }
        h1 { font-family:Georgia,'Times New Roman',serif; font-weight:650; }
        .lead { color: #53667d; font-size: 1.12rem; max-width: 780px; margin-top: -0.55rem; }
        .book-progress { margin:0 0 2.35rem; padding:.85rem 0 0; border-bottom:1px solid #d8e2e8; }
        .book-progress-copy { display:grid; grid-template-columns:auto 1fr auto; align-items:baseline; gap:1rem; padding-bottom:.72rem; }
        .book-progress-copy span { color:#5b918b; font-size:.69rem; font-weight:850; letter-spacing:.16em; }
        .book-progress-copy strong { color:#29445f; font-family:Georgia,'Times New Roman',serif; font-size:.92rem; font-weight:600; }
        .book-progress-copy small { color:#7a8998; font-variant-numeric:tabular-nums; }
        .book-progress-track { height:3px; background:#e1e9ed; }
        .book-progress-track i { display:block; height:100%; background:linear-gradient(90deg,#5b918b,#8672a5); }
        .chapter-rule { display:flex; align-items:center; gap:1rem; margin:2.8rem 0 1rem; color:#718196; font-size:.68rem; font-weight:800; letter-spacing:.15em; }
        .chapter-rule:before,.chapter-rule:after { content:""; height:1px; background:#d8e2e8; flex:1; }
        [data-testid="stMetric"] { background: rgba(255,255,255,.9); border: 1px solid #dbe5eb; border-radius: 18px; padding: 1rem; box-shadow: 0 10px 30px rgba(32,58,89,.06); }
        [data-testid="stMetricValue"], [data-testid="stMetricValue"] * { color: var(--navy) !important; }
        [data-testid="stMetricLabel"], [data-testid="stMetricLabel"] * { color:#64778a !important; }
        .stButton > button, .stDownloadButton > button { border-radius: 12px; border-color: #c9d9e2; color:#29445f; font-weight: 650; min-height: 2.75rem; background: rgba(255,255,255,.78); }
        .stButton > button p, .stDownloadButton > button p, [data-testid="stBaseButton-secondary"] * { color:#29445f !important; opacity:1 !important; }
        [data-testid="stBaseButton-secondary"] { color:#29445f !important; background:#f8fbfc !important; border-color:#c8d9e3 !important; }
        [data-testid="stBaseButton-secondary"]:hover { background:#e8f2f4 !important; border-color:#79aaa7 !important; }
        [data-testid="stBaseButton-primary"] { background:#f04f52 !important; border-color:#f04f52 !important; }
        [data-testid="stBaseButton-primary"] *, [data-testid="stBaseButton-primary"] p { color:#fff !important; opacity:1 !important; }
        [data-baseweb="tab"] { color:#5f7185 !important; }
        [data-baseweb="tab"] p { color:inherit !important; }
        .stButton > button:hover { border-color: #80b8b0; color: var(--navy); box-shadow: 0 5px 18px rgba(32,58,89,.10); }
        .hero { background: linear-gradient(125deg, #dff1f7 0%, #e5f4ef 48%, #eee7f6 100%); border:1px solid #d4e4ea; border-radius:clamp(16px,1.6vw,24px); padding:clamp(1.25rem,3.2vh,2.35rem) clamp(1.15rem,3.2vw,3rem); margin-bottom:clamp(1.1rem,2.5vh,1.8rem); box-shadow:0 18px 45px rgba(32,58,89,.09); position:relative; overflow:hidden; }
        .hero:after { content:""; position:absolute; width:280px; height:280px; right:-75px; top:-135px; border:1px solid rgba(53,107,126,.14); border-radius:50%; box-shadow:0 0 0 50px rgba(255,255,255,.25),0 0 0 100px rgba(255,255,255,.18); }
        .hero-kicker { color:#4f8982; font-weight:800; font-size:.7rem; letter-spacing:.15em; margin-bottom:.85rem; }
        .hero h1 { color:#203a59; font-size:clamp(2rem,min(3.6vw,6.2vh),3.85rem); line-height:1.02; margin:0 0 clamp(.55rem,1.4vh,.9rem); max-width:820px; }
        .hero h1 span { color:#8672a5; }
        .hero p { font-size:clamp(.88rem,1.15vw,1rem); color:#536a7e; max-width:720px; line-height:1.5; margin-bottom:0; }
        .hero-tags { display:flex; gap:clamp(.35rem,.7vw,.55rem); flex-wrap:wrap; margin-top:clamp(.7rem,1.8vh,1.2rem); }
        .hero-tags span { border:1px solid rgba(66,111,126,.20); background:rgba(255,255,255,.45); border-radius:999px; padding:.36rem .7rem; color:#3d6074; font-size:.78rem; }
        .book-epigraph { max-width:850px; margin:-.55rem auto 2.2rem; padding:.9rem 1.35rem; text-align:center; background:rgba(255,255,255,.72); border:1px solid #dde6eb; border-radius:18px; box-shadow:0 10px 28px rgba(32,58,89,.06); }
        .book-epigraph p { margin:0; color:#29445f; font-family:Georgia,serif; font-size:1.25rem; font-style:italic; }
        .book-epigraph cite { display:block; margin-top:.55rem; color:#718196; font-size:.82rem; font-style:normal; }
        .section-label { margin:3.4rem 0 1.25rem; }
        .section-label span { color:#5b918b; font-size:.74rem; font-weight:800; letter-spacing:.15em; }
        .section-label h2 { margin:.25rem 0 .3rem; font-size:2rem; }
        .section-label p { color:#627489; max-width:850px; margin:0; }
        .function-card { background:rgba(255,255,255,.9); border-radius:20px; padding:1.25rem 1.3rem; margin-top:.8rem; border-top:6px solid var(--accent); box-shadow:0 12px 32px rgba(32,58,89,.08); min-height:155px; }
        .route-card { background:rgba(255,255,255,.82); border:1px solid #dbe6eb; border-radius:20px; padding:1.35rem; min-height:178px; box-shadow:0 12px 30px rgba(32,58,89,.06); }
        .compact-route { min-height:0; padding:clamp(.75rem,1.5vh,1rem) clamp(.9rem,1.8vw,1.25rem); }
        .compact-route h3 { margin:.25rem 0; }
        .compact-route p { margin:.15rem 0 0; }
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
        .method-ribbon { display:grid; grid-template-columns:repeat(3,1fr); gap:.85rem; margin:1.25rem 0 2rem; }
        .method-ribbon div { display:grid; gap:.3rem; min-height:130px; align-content:center; padding:1.15rem; border:1px solid #d9e4e7; border-radius:17px; background:linear-gradient(145deg,#edf7f4,#f3eef8); }
        .method-ribbon b { color:#5b918b; font-size:.7rem; letter-spacing:.12em; }
        .method-ribbon strong { color:#29445f; font-size:1.05rem; }
        .method-ribbon span { color:#687c8e; font-size:.8rem; line-height:1.45; }
        .method-chapter { display:grid; grid-template-columns:48px 120px 210px 1fr; gap:1rem; align-items:center; padding:1rem 1.15rem; margin:.65rem 0; background:rgba(255,255,255,.82); border:1px solid #dbe6eb; border-radius:16px; }
        .method-chapter b { color:#5b918b; font-size:.76rem; letter-spacing:.1em; }
        .method-chapter span { color:#7a8998; font-size:.8rem; }
        .method-chapter strong { color:#29445f; }
        .method-chapter p { color:#65788a; margin:0; line-height:1.45; }
        .closing-epigraph { margin:2rem auto .5rem; background:linear-gradient(120deg,#fff3df,#f1eaf7); }
        [data-testid="stDataFrame"] { border-radius:16px; overflow:hidden; box-shadow:0 8px 25px rgba(32,58,89,.05); }
        @media(max-width:1200px) and (min-width:801px) { [data-testid="stSidebar"]{min-width:14.5rem;max-width:14.5rem}[data-testid="stSidebar"]>div:first-child{width:14.5rem}.main .block-container{padding-left:1.5rem;padding-right:1.5rem}.hero{padding:1.8rem 2.1rem}.hero h1{font-size:clamp(2rem,3.8vw,3.15rem)} }
        @media(max-height:900px) and (min-width:801px) { .hero{padding:1.8rem 2.5rem}.hero h1{font-size:clamp(2.1rem,3.25vw,3.35rem)}.hero p{font-size:.94rem}.hero-tags{margin-top:.9rem}.book-epigraph{margin:-.35rem auto 1.7rem}.section-label{margin:2.4rem 0 1rem} }
        @media(max-width:800px) { [data-testid="stSidebar"]{min-width:15rem;max-width:15rem}[data-testid="stSidebar"]>div:first-child{width:15rem}.main .block-container{padding:.45rem .65rem 1.4rem}.hero{padding:1.25rem 1rem}.hero h1{font-size:clamp(1.65rem,9vw,2.25rem)}.hero p{font-size:.88rem}.hero-tags{gap:.35rem}.hero-tags span{font-size:.7rem;padding:.45rem .65rem}.story-ribbon,.evolve-loop{display:grid}.story-ribbon i,.evolve-loop i{transform:rotate(90deg)}.method-ribbon{grid-template-columns:1fr}.method-chapter{grid-template-columns:42px 1fr}.method-chapter p{grid-column:1/-1}.book-progress{margin-bottom:1rem}.book-progress-copy{grid-template-columns:1fr auto}.book-progress-copy span{grid-column:1/-1}.st-key-top_page_navigation button{font-size:.72rem;padding:.3rem .2rem}.section-label{margin:1.25rem 0 .65rem} }
        </style>
        """.replace("__CONTENT_WIDTH__", content_width).replace("__BODY_SIZE__", f"{body_size:.2f}"),
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Imperial BBO Challenge", page_icon="◈", layout="wide",
        initial_sidebar_state="auto",
    )
    evidence = load_assessed_evidence()
    complete = load_complete_internal_evidence()
    method_register = load_method_register()
    capstone_story = load_capstone_story()
    if "page" not in st.session_state:
        st.session_state["page"] = "Visual home"
    pending_page = st.session_state.pop("_next_page", None)
    if pending_page is not None:
        st.session_state["page"] = pending_page
    with st.sidebar:
        st.markdown("## ◈ Imperial BBO")
        st.caption("A visual book and analytical companion")
        st.markdown("<div class='sidebar-section'>TABLE OF CONTENTS</div>", unsafe_allow_html=True)
        pages = [
            "Visual home", "Week story", "Function story", "Code laboratory",
            "Methods and Evolution", "Chapter Summary", "Extend and Evolve", "Round dashboard",
            "Weekly progress", "Capstone retrospective", "Assessment evidence",
        ]
        page = st.radio(
            "Navigate", pages,
            key="page",
            label_visibility="collapsed",
            format_func=lambda value: PAGE_LABELS[value],
        )
        st.divider()
        st.markdown("<div class='sidebar-section'>READING DISPLAY</div>", unsafe_allow_html=True)
        reading_mode = st.toggle(
            "Book reading width", value=True,
            help="Narrows narrative pages to a comfortable reading measure.",
        )
        text_scale = st.select_slider(
            "Text size", options=[90, 100, 110, 120], value=100,
            format_func=lambda value: f"{value}%",
        )
        st.divider()
        st.caption("Official Week 1 to Week 13 evidence only")
    narrative_page = page in BOOK_PAGES or page == "Visual home"
    apply_style(reading_mode=reading_mode and narrative_page, text_scale=text_scale)
    page_navigation_controls(page, "top")
    book_progress_header(page)
    if page == "Visual home":
        landing_page(evidence)
    elif page == "Week story":
        week_story(evidence)
    elif page == "Function story":
        function_story(evidence)
    elif page == "Code laboratory":
        code_laboratory(evidence, complete)
    elif page == "Methods and Evolution":
        method_evolution_page(method_register, capstone_story)
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
