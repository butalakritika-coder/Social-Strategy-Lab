import numpy as np

from game_theory import (
    get_best_responses,
    find_nash_equilibria,
    calculate_total_payoff,
    find_mixed_equilibrium
)


# Original project payoff matrix
payoff_a = np.array([
    [8, 4],
    [9, 5]
])

payoff_b = np.array([
    [8, 9],
    [4, 5]
])


print("TEST 1: BEST RESPONSES")

best_a, best_b = get_best_responses(payoff_a, payoff_b)

print("Creator A:", best_a)
print("Creator B:", best_b)


print("\nTEST 2: PURE NASH EQUILIBRIUM")

equilibria = find_nash_equilibria(payoff_a, payoff_b)

print("Equilibria:", equilibria)


print("\nTEST 3: COMBINED PAYOFFS")

print(calculate_total_payoff(payoff_a, payoff_b))


print("\nTEST 4: MIXED EQUILIBRIUM")

mixed = find_mixed_equilibrium(payoff_a, payoff_b)

print("Mixed equilibrium:", mixed)


print("\nTEST 5: GAME WITHOUT A PURE EQUILIBRIUM")

matching_pennies_a = np.array([
    [1, -1],
    [-1, 1]
])

matching_pennies_b = -matching_pennies_a

print(
    "Pure equilibria:",
    find_nash_equilibria(matching_pennies_a, matching_pennies_b)
)

print(
    "Mixed equilibrium:",
    find_mixed_equilibrium(matching_pennies_a, matching_pennies_b)
)
