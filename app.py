import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from game_theory import (
    get_best_responses,
    find_nash_equilibria,
    calculate_total_payoff,
    find_mixed_equilibrium,
)

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Social Strategy Lab",
    page_icon="🎮",
    layout="wide",
)

st.title("🎮 Social Strategy Lab")

st.subheader(
    "Game Theory-Based Analysis of Social Media Content Competition"
)

st.write(
    "Explore how competing content creators make strategic decisions "
    "using game theory, payoff matrices, and equilibrium analysis."
)

st.info(
    "The payoff values are illustrative utility points, "
    "not real social media engagement statistics."
)

strategies = ["Original Content", "Trend-Copying"]

# ---------------- PAYOFF MATRIX INPUT ----------------

st.header("1. Configure the Payoff Matrix")

st.caption(
    "Each cell contains the payoffs (Creator A, Creator B). "
    "Rows represent Creator A's strategies; columns represent Creator B's."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Creator A's Payoffs")

    a_oo = st.number_input(
        "A: Original | B: Original", value=8, key="a_oo"
    )
    a_ot = st.number_input(
        "A: Original | B: Trend", value=4, key="a_ot"
    )
    a_to = st.number_input(
        "A: Trend | B: Original", value=9, key="a_to"
    )
    a_tt = st.number_input(
        "A: Trend | B: Trend", value=5, key="a_tt"
    )

with col2:
    st.subheader("Creator B's Payoffs")

    b_oo = st.number_input(
        "B: Original | A: Original", value=8, key="b_oo"
    )
    b_ot = st.number_input(
        "B: Trend | A: Original", value=9, key="b_ot"
    )
    b_to = st.number_input(
        "B: Original | A: Trend", value=4, key="b_to"
    )
    b_tt = st.number_input(
        "B: Trend | A: Trend", value=5, key="b_tt"
    )

payoff_a = np.array([
    [a_oo, a_ot],
    [a_to, a_tt],
], dtype=float)

payoff_b = np.array([
    [b_oo, b_ot],
    [b_to, b_tt],
], dtype=float)

# ---------------- DISPLAY PAYOFF MATRIX ----------------

st.header("2. Payoff Matrix")

matrix_rows = []

for i, strategy_a in enumerate(strategies):
    row = {"Creator A / Creator B": strategy_a}

    for j, strategy_b in enumerate(strategies):
        row[strategy_b] = (
            f"({payoff_a[i, j]:g}, {payoff_b[i, j]:g})"
        )

    matrix_rows.append(row)

st.table(matrix_rows)

# ---------------- BEST RESPONSE ANALYSIS ----------------

st.header("3. Best-Response Analysis")

best_a, best_b = get_best_responses(payoff_a, payoff_b)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Creator A")

    for j, opponent_strategy in enumerate(strategies):
        responses = [
            strategies[i]
            for i, jj in best_a
            if jj == j
        ]

        st.write(
            f"**If B chooses {opponent_strategy}:** "
            f"{', '.join(responses)}"
        )

with col2:
    st.subheader("Creator B")

    for i, opponent_strategy in enumerate(strategies):
        responses = [
            strategies[j]
            for ii, j in best_b
            if ii == i
        ]

        st.write(
            f"**If A chooses {opponent_strategy}:** "
            f"{', '.join(responses)}"
        )

# ---------------- PURE NASH EQUILIBRIUM ----------------

st.header("4. Nash Equilibrium Analysis")

equilibria = find_nash_equilibria(payoff_a, payoff_b)

if equilibria:
    st.success(
        f"Found {len(equilibria)} pure-strategy Nash equilibrium(s)."
    )

    for i, j in equilibria:
        st.write(
            f"**Creator A:** {strategies[i]}  \n"
            f"**Creator B:** {strategies[j]}  \n"
            f"**Payoffs:** "
            f"({payoff_a[i, j]:g}, {payoff_b[i, j]:g})"
        )
else:
    st.warning(
        "No pure-strategy Nash equilibrium exists. "
        "Check the mixed-strategy analysis below."
    )

# ---------------- MIXED-STRATEGY ANALYSIS ----------------

st.header("5. Mixed-Strategy Analysis")

mixed = find_mixed_equilibrium(payoff_a, payoff_b)

if mixed is not None:
    st.success("An interior mixed-strategy Nash equilibrium exists.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Creator A — Original Content",
            f"{mixed['creator_a_original']:.1%}",
        )
        st.metric(
            "Creator A — Trend-Copying",
            f"{mixed['creator_a_trend']:.1%}",
        )

    with col2:
        st.metric(
            "Creator B — Original Content",
            f"{mixed['creator_b_original']:.1%}",
        )
        st.metric(
            "Creator B — Trend-Copying",
            f"{mixed['creator_b_trend']:.1%}",
        )

    st.caption(
        "These probabilities describe an equilibrium strategy, "
        "not predicted real-world posting behaviour."
    )
else:
    st.info(
        "No interior mixed-strategy equilibrium was found. "
        "A pure equilibrium may exist, or the game may require "
        "special handling for boundary or degenerate cases."
    )

# ---------------- PAYOFF COMPARISON ----------------

st.header("6. Individual vs Combined Payoffs")

total_payoffs = calculate_total_payoff(payoff_a, payoff_b)

outcomes = [
    "Original / Original",
    "Original / Trend",
    "Trend / Original",
    "Trend / Trend",
]

individual_a = payoff_a.flatten()
individual_b = payoff_b.flatten()
combined = total_payoffs.flatten()

# ---------------- PAYOFF COMPARISON GRAPH ----------------

x = np.arange(len(outcomes))
width = 0.24

fig, ax = plt.subplots(figsize=(8, 3.6))

# Plot all payoff values
ax.bar(
    x - width,
    individual_a,
    width,
    label="Creator A"
)

ax.bar(
    x,
    individual_b,
    width,
    label="Creator B"
)

ax.bar(
    x + width,
    combined,
    width,
    label="Combined Payoff"
)

# Titles and labels
ax.set_title(
    "Individual vs Combined Payoffs",
    fontsize=12,
    fontweight="bold",
    pad=12
)

ax.set_ylabel("Payoff Units", fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(
    outcomes,
    rotation=0,
    ha="center",
    fontsize=8
)

ax.tick_params(axis="y", labelsize=8)

# Automatically adjust the Y-axis to the current data
all_values = np.concatenate([
    individual_a,
    individual_b,
    combined
])

y_min = min(0, float(np.min(all_values)))
y_max = max(0, float(np.max(all_values)))

y_range = y_max - y_min

# Add padding, including when every payoff is identical
padding = max(y_range * 0.12, abs(y_min) * 0.05, abs(y_max) * 0.05, 1)

ax.set_ylim(y_min - padding, y_max + padding)

# Clean appearance
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.20),
    ncol=3,
    frameon=False,
    fontsize=8
)

# Preserve spacing for labels and legend
fig.tight_layout()

st.pyplot(fig, use_container_width=False)
plt.close(fig)

# ---------------- STRATEGY RECOMMENDATION ----------------

st.header("7. Strategy Recommendation")

opponent_strategy = st.selectbox(
    "Select Creator B's strategy:",
    strategies,
)

column = strategies.index(opponent_strategy)

best_payoff = np.max(payoff_a[:, column])

recommended = [
    strategies[i]
    for i in range(2)
    if np.isclose(payoff_a[i, column], best_payoff)
]

st.success(
    f"Recommended best response for Creator A: "
    f"{', '.join(recommended)}"
)

st.write(f"Maximum available payoff: **{best_payoff:g}**")

st.caption(
    "Recommendations depend on the supplied payoff matrix. "
    "They do not predict actual social media engagement."
)
# ---------------- SCENARIO COMPARISON ----------------

st.header("8. Scenario Comparison")

st.write(
    "Explore how changing the payoff values affects "
    "the strategic outcome."
)

with st.expander("Configure an alternative scenario"):

    st.caption(
        "Enter the alternative payoffs for each strategy combination."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Creator A")

        alt_a_oo = st.number_input(
            "A: Original | B: Original",
            value=9,
            key="alt_a_oo"
        )

        alt_a_ot = st.number_input(
            "A: Original | B: Trend",
            value=4,
            key="alt_a_ot"
        )

        alt_a_to = st.number_input(
            "A: Trend | B: Original",
            value=8,
            key="alt_a_to"
        )

        alt_a_tt = st.number_input(
            "A: Trend | B: Trend",
            value=3,
            key="alt_a_tt"
        )

    with col2:
        st.subheader("Creator B")

        alt_b_oo = st.number_input(
            "B: Original | A: Original",
            value=9,
            key="alt_b_oo"
        )

        alt_b_ot = st.number_input(
            "B: Trend | A: Original",
            value=8,
            key="alt_b_ot"
        )

        alt_b_to = st.number_input(
            "B: Original | A: Trend",
            value=4,
            key="alt_b_to"
        )

        alt_b_tt = st.number_input(
            "B: Trend | A: Trend",
            value=3,
            key="alt_b_tt"
        )


# Build the alternative payoff matrices

alt_payoff_a = np.array([
    [alt_a_oo, alt_a_ot],
    [alt_a_to, alt_a_tt]
], dtype=float)

alt_payoff_b = np.array([
    [alt_b_oo, alt_b_ot],
    [alt_b_to, alt_b_tt]
], dtype=float)


# Calculate equilibria

alt_equilibria = find_nash_equilibria(
    alt_payoff_a,
    alt_payoff_b
)

st.subheader("Comparison Results")

comparison_data = []

# Current scenario

current_equilibrium = (
    ", ".join(
        f"{strategies[i]} / {strategies[j]}"
        for i, j in equilibria
    )
    if equilibria
    else "No pure equilibrium"
)

comparison_data.append({
    "Scenario": "Current",
    "Pure Nash Equilibrium": current_equilibrium,
    "Equilibrium Combined Payoff": (
        max(
            payoff_a[i, j] + payoff_b[i, j]
            for i, j in equilibria
        )
        if equilibria
        else None
    )
})


# Alternative scenario

alternative_equilibrium = (
    ", ".join(
        f"{strategies[i]} / {strategies[j]}"
        for i, j in alt_equilibria
    )
    if alt_equilibria
    else "No pure equilibrium"
)

comparison_data.append({
    "Scenario": "Alternative",
    "Pure Nash Equilibrium": alternative_equilibrium,
    "Equilibrium Combined Payoff": (
        max(
            alt_payoff_a[i, j] + alt_payoff_b[i, j]
            for i, j in alt_equilibria
        )
        if alt_equilibria
        else None
    )
})

st.table(comparison_data)

st.caption(
    "Equilibrium payoffs are shown only when a pure-strategy "
    "Nash equilibrium exists. The mixed-strategy section above "
    "analyses the current scenario."
)