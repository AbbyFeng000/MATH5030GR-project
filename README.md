# MATH5030GR-project
# Numerical Comparison of Heston Monte Carlo Schemes: Euler, Full Truncation, and QE

## Project goal

This project implements and compares three published Monte Carlo discretization schemes for the Heston stochastic volatility model in Python: Euler, Full Truncation Euler, and Quadratic-Exponential (QE). The goal is to study their numerical efficiency for pricing European call options, with a focus on pricing accuracy, numerical stability, robustness, and execution speed.

## Why this topic fits the course

This project matches the course requirements in several ways:

- It studies an advanced quantitative finance model, the Heston stochastic volatility model.
- It implements published numerical methods from the literature rather than using machine learning or data science.
- It focuses on efficient numerical methods through comparisons of accuracy, bias, robustness, and runtime.
- It uses academic papers as the main reference for both the model and the numerical schemes.
- It is organized as a reusable Python package with a clear GitHub repository structure.

## Model background

In the Black-Scholes model, volatility is assumed to be constant. In the Heston model, volatility is allowed to change randomly over time. More precisely, the variance follows its own stochastic process and can be correlated with the stock-price process.

Under the risk-neutral measure, the Heston model is

\[
dS_t = (r-q)S_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)}
\]

\[
dv_t = \kappa(\theta - v_t)dt + \sigma \sqrt{v_t}\,dW_t^{(2)}
\]

with

\[
d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
\]

where:

- \(S_t\) is the stock price
- \(v_t\) is the variance
- \(r\) is the risk-free rate
- \(q\) is the dividend yield
- \(\kappa\) is the mean-reversion speed
- \(\theta\) is the long-run variance level
- \(\sigma\) is the volatility of variance
- \(\rho\) is the correlation between the stock and variance shocks

## Planned numerical methods

This project will compare the following three Monte Carlo discretization schemes:

1. Euler
2. Full Truncation Euler
3. Quadratic-Exponential (QE)

The comparison will focus on:

- pricing accuracy
- numerical stability
- robustness under different parameter settings
- runtime and computational efficiency

## Planned validation

The Monte Carlo prices will be compared against benchmark European option prices under the Heston model. We will also study convergence as the number of paths and time steps increases.

## Planned robustness tests

The methods will be tested under multiple parameter settings, including more challenging cases such as:

- high volatility of volatility
- strong negative correlation
- longer maturity
- coarse time discretization

## Repository structure

```text
repo/
├── README.md
├── pyproject.toml
├── requirements.txt
├── examples/
├── results/
├── src/
│   └── heston_mc/
│       ├── __init__.py
│       ├── params.py
│       └── utils.py
└── tests/
