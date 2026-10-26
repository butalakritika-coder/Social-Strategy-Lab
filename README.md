# Social Strategy Lab

### Game Theory-Based Analysis of Social Media Content Competition

## About the Project

Social Strategy Lab is an interactive Python application that uses game theory to analyse strategic competition between two social media content creators.

Each creator has two strategies:

* **Original Content (O)**
* **Trend-Copying (T)**

The application analyses their choices using payoff matrices, best responses, and Nash equilibrium.

## Technologies Used

* Python
* Streamlit
* NumPy
* Matplotlib

## Features

* Interactive payoff matrix
* Best-response analysis
* Pure-strategy Nash equilibrium detection
* Interior mixed-strategy equilibrium calculation for supported cases
* Payoff comparison graphs
* Strategy recommendations
* Scenario comparison

## Default Payoff Matrix

| Creator A / Creator B | Original (O) | Trend (T) |
| --------------------- | -----------: | --------: |
| Original (O)          |       (8, 8) |    (4, 9) |
| Trend (T)             |       (9, 4) |    (5, 5) |

The first number represents Creator A's payoff, and the second represents Creator B's payoff.

For the default matrix, the pure-strategy Nash equilibrium is **(Trend, Trend)**, with payoffs of **(5, 5)**.

The payoff values are hypothetical and are not actual social media statistics.

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

### 3. Activate it on Windows PowerShell

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

If the browser does not open automatically, visit the local URL displayed in the terminal.

## Run Tests

```bash
python test_game.py
```

## Limitations

* The model considers two players with two strategies each.
* Payoffs are hypothetical.
* Real social media engagement depends on additional factors, including audience preferences and platform algorithms.
* Mixed-strategy calculations cover supported non-degenerate cases.

## Conclusion

Social Strategy Lab demonstrates how game theory can help analyse strategic decisions, identify stable outcomes, and compare alternative strategies through an interactive application.
