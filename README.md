# Social Strategy Lab

### Game Theory-Based Analysis of Social Media Content Competition

## About the Project

Social Strategy Lab is an interactive application that uses game theory to analyse strategic competition between two social media content creators.

Each creator has two strategies:

* **Original Content (O)**
* **Trend-Copying (T)**

The application analyses their decisions using payoff matrices, best responses, and Nash equilibrium.

## Objectives

* Model strategic interactions between two content creators.
* Calculate the best responses of both players.
* Identify pure-strategy Nash equilibria.
* Calculate interior mixed-strategy equilibria where applicable.
* Visualise and compare individual and combined payoffs.
* Explore alternative scenarios by changing payoff values.

## Technologies Used

* Python
* Streamlit
* NumPy
* Matplotlib

## Features

* Interactive payoff matrix.
* Best-response analysis.
* Nash equilibrium detection.
* Mixed-strategy equilibrium calculation for supported cases.
* Payoff comparison graphs.
* Strategy recommendations.
* Scenario comparison.

## Default Payoff Matrix

| Creator A / Creator B | Original (O) | Trend (T) |
| --------------------- | -----------: | --------: |
| Original (O)          |       (8, 8) |    (4, 9) |
| Trend (T)             |       (9, 4) |    (5, 5) |

The first value represents Creator A's payoff, and the second represents Creator B's payoff.

For the default matrix, the pure-strategy Nash equilibrium is **(Trend, Trend)**, with payoffs of **(5, 5)**.

These payoffs are illustrative utility values and are not actual social media platform statistics.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/butalakritika-coder/Social-Strategy-Lab.git
cd Social-Strategy-Lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not, open the local URL displayed in the terminal.

## Run Tests

To run the included test script:

```bash
python test_game.py
```

## Limitations

* The model considers two players and two strategies per player.
* Payoffs are hypothetical rather than real-world measurements.
* Actual social media performance depends on additional factors, including audience preferences and platform algorithms.
* Mixed-strategy calculations are limited to supported non-degenerate cases.

## Future Scope

* Extend the model to more players and strategies.
* Explore repeated games.
* Incorporate real-world data where available.

## Conclusion

Social Strategy Lab demonstrates how game theory can be used to analyse strategic decision-making, identify stable outcomes, and compare alternative strategies through an interactive application.
