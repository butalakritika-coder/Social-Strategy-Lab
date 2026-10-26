import numpy as np


STRATEGIES = ["Original Content", "Trend-Copying"]


def get_best_responses(payoff_a, payoff_b):
    """
    Calculate the best responses of both creators.

    Rows represent Creator A's strategies.
    Columns represent Creator B's strategies.
    """

    payoff_a = np.asarray(payoff_a, dtype=float)
    payoff_b = np.asarray(payoff_b, dtype=float)

    best_responses_a = []
    best_responses_b = []

    # Creator A's best responses to each strategy of B
    for j in range(payoff_a.shape[1]):
        max_payoff = np.max(payoff_a[:, j])

        for i in range(payoff_a.shape[0]):
            if np.isclose(payoff_a[i, j], max_payoff):
                best_responses_a.append((i, j))

    # Creator B's best responses to each strategy of A
    for i in range(payoff_b.shape[0]):
        max_payoff = np.max(payoff_b[i, :])

        for j in range(payoff_b.shape[1]):
            if np.isclose(payoff_b[i, j], max_payoff):
                best_responses_b.append((i, j))

    return best_responses_a, best_responses_b


def find_nash_equilibria(payoff_a, payoff_b):
    """
    Find all pure-strategy Nash equilibria.
    """

    payoff_a = np.asarray(payoff_a, dtype=float)
    payoff_b = np.asarray(payoff_b, dtype=float)

    if payoff_a.shape != payoff_b.shape:
        raise ValueError("Both payoff matrices must have the same shape.")

    equilibria = []

    for i in range(payoff_a.shape[0]):
        for j in range(payoff_a.shape[1]):

            best_a = np.isclose(
                payoff_a[i, j],
                np.max(payoff_a[:, j])
            )

            best_b = np.isclose(
                payoff_b[i, j],
                np.max(payoff_b[i, :])
            )

            if best_a and best_b:
                equilibria.append((i, j))

    return equilibria


def calculate_total_payoff(payoff_a, payoff_b):
    """
    Calculate the combined payoff for each outcome.
    """

    payoff_a = np.asarray(payoff_a, dtype=float)
    payoff_b = np.asarray(payoff_b, dtype=float)

    if payoff_a.shape != payoff_b.shape:
        raise ValueError("Both payoff matrices must have the same shape.")

    return payoff_a + payoff_b


def find_mixed_equilibrium(payoff_a, payoff_b):
    """
    Calculate an interior mixed-strategy Nash equilibrium
    for a 2x2 game, if one exists.

    Returns:
        A dictionary containing probabilities, or None if
        no interior mixed equilibrium exists.
    """

    a = np.asarray(payoff_a, dtype=float)
    b = np.asarray(payoff_b, dtype=float)

    if a.shape != (2, 2) or b.shape != (2, 2):
        raise ValueError("Mixed-strategy calculation requires 2x2 matrices.")

    # Probability that B chooses column 0, making A indifferent
    denominator_a = a[0, 0] - a[0, 1] - a[1, 0] + a[1, 1]

    # Probability that A chooses row 0, making B indifferent
    denominator_b = b[0, 0] - b[0, 1] - b[1, 0] + b[1, 1]

    if np.isclose(denominator_a, 0) or np.isclose(denominator_b, 0):
        return None

    q = (a[1, 1] - a[0, 1]) / denominator_a
    p = (b[1, 1] - b[1, 0]) / denominator_b

    # An interior mixed equilibrium requires probabilities strictly
    # between zero and one for both players.
    if 0 < p < 1 and 0 < q < 1:
        return {
            "creator_a_original": p,
            "creator_b_original": q,
            "creator_a_trend": 1 - p,
            "creator_b_trend": 1 - q
        }

    return None