import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from game_theory import (
    find_nash_equilibria,
    calculate_total_payoff
)


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Social Strategy Lab",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Social Strategy Lab")

st.subheader(
    "Game Theory-Based Analysis of Social Media Content Competition"
)

st.write(
    "Explore how two competing content creators make strategic "
    "decisions using payoff matrices and Nash equilibrium analysis."
)

st.info(
    "The payoff values are illustrative utility points, "
    "not real social media engagement statistics."
)


# ---------------- PAYOFF MATRIX ----------------

st.header("1. Configure the Payoff Matrix")

st.write(
    "Each cell contains the payoffs for Creator A and Creator B."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Creator A's Payoffs")

    a_oo = st.number_input("A: Original, B: Original", value=8)
    a_ot = st.number_input("A: Original, B: Trend", value=4)
    a_to = st.number_input("A: Trend, B: Original", value=9)
    a_tt = st.number_input("A: Trend, B: Trend", value=5)

with col2:
    st.subheader("Creator B's Payoffs")

    b_oo = st.number_input("B: Original, A: Original", value=8)
    b_ot = st.number_input("B: Trend, A: Original", value=9)
    b_to = st.number_input("B: Original, A: Trend", value=4)
    b_tt = st.number_input("B: Trend, A: Trend", value=5)


payoff_a = np.array([
    [a_oo, a_ot],
    [a_to, a_tt]
], dtype=float)

payoff_b = np.array([
    [b_oo, b_ot],
    [b_to, b_tt]
], dtype=float)


# ---------------- DISPLAY MATRIX ----------------

st.header("2. Payoff Matrix")

st.write(
    "Rows represent Creator A's strategy. "
    "Columns represent Creator B's strategy."
)

matrix_data = {
    "Creator A / Creator B": [
        "Original Content",
        "Trend-Copying"
    ],
    "Original Content": [
        f"({payoff_a[0, 0]:g}, {payoff_b[0, 0]:g})",
        f"({payoff_a[1, 0]:g}, {payoff_b[1, 0]:g})"
    ],
    "Trend-Copying": [
        f"({payoff_a[0, 1]:g}, {payoff_b[0, 1]:g})",
        f"({payoff_a[1, 1]:g}, {payoff_b[1, 1]:g})"
    ]
}

st.table(matrix_data)


# ---------------- NASH EQUILIBRIUM ----------------

st.header("3. Nash Equilibrium Analysis")

equilibria = find_nash_equilibria(payoff_a, payoff_b)

strategies = ["Original Content", "Trend-Copying"]

if equilibria:

    st.success(f"Found {len(equilibria)} pure-strategy Nash equilibrium(s).")

    for i, j in equilibria:

        st.write(
            f"**Creator A:** {strategies[i]}  \n"
            f"**Creator B:** {strategies[j]}  \n"
            f"**Payoffs:** ({payoff_a[i, j]:g}, {payoff_b[i, j]:g})"
        )

else:

    st.warning(
        "No pure-strategy Nash equilibrium exists for these payoffs. "
        "Mixed-strategy analysis may be required."
    )


# ---------------- TOTAL PAYOFF ----------------

st.header("4. Individual vs Combined Payoffs")

total_payoffs = calculate_total_payoff(payoff_a, payoff_b)

outcomes = [
    "Original / Original",
    "Original / Trend",
    "Trend / Original",
    "Trend / Trend"
]

individual_a = [
    payoff_a[0, 0],
    payoff_a[0, 1],
    payoff_a[1, 0],
    payoff_a[1, 1]
]

individual_b = [
    payoff_b[0, 0],
    payoff_b[0, 1],
    payoff_b[1, 0],
    payoff_b[1, 1]
]

combined = total_payoffs.flatten()

fig, ax = plt.subplots(figsize=(10, 5))

x = np.arange(len(outcomes))
width = 0.25

ax.bar(x - width, individual_a, width, label="Creator A")
ax.bar(x, individual_b, width, label="Creator B")
ax.bar(x + width, combined, width, label="Combined Payoff")

ax.set_ylabel("Payoff Units")
ax.set_title("Comparison of Creator Payoffs")
ax.set_xticks(x)
ax.set_xticklabels(outcomes, rotation=15, ha="right")
ax.legend()

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)


# ---------------- STRATEGY RECOMMENDATION ----------------

st.header("5. Strategy Recommendation")

opponent_strategy = st.selectbox(
    "Select Creator B's strategy:",
    ["Original Content", "Trend-Copying"]
)

if opponent_strategy == "Original Content":
    column = 0
else:
    column = 1

best_payoff = np.max(payoff_a[:, column])

best_strategies = [
    strategies[i]
    for i in range(2)
    if payoff_a[i, column] == best_payoff
]

st.write(
    f"**Creator A's best response:** {', '.join(best_strategies)}"
)

st.write(
    f"**Maximum available payoff:** {best_payoff:g}"
)

st.caption(
    "Recommendations depend on the specified payoff matrix "
    "and do not predict actual social media performance."
)