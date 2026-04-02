# Efficient Monte Carlo Pricing of Variance Derivatives under the Heston Model

## Overview

This project studies Monte Carlo pricing of **variance-based derivatives** under the **Heston stochastic volatility model**. The main products considered are:

- **Variance swaps**
- **Variance options**

The numerical goal of the project is to evaluate these products efficiently using Monte Carlo simulation and to improve computational performance through a **control variate** technique.

Rather than focusing on standard European option pricing, this project focuses on **variance derivatives**, whose payoffs depend on the path of the asset through realized variance. This makes Monte Carlo a natural framework and makes variance reduction an important numerical issue.

---

## Project objective

The main objective of this project is to answer the following question:

> How can we efficiently price variance swaps and variance options under the Heston model using Monte Carlo, and how much improvement can be obtained from a control variate?

To answer this, the project will:

1. simulate stock-price and variance paths under the Heston model,
2. compute **realized variance** from simulated stock paths,
3. price a **variance swap** and a **variance option**,
4. compare **plain Monte Carlo** against **control-variate Monte Carlo**,
5. evaluate performance in terms of:
   - estimated price,
   - standard error,
   - runtime,
   - variance reduction.

---

## Modeling framework

### The Heston model

In the Black-Scholes model, volatility is constant. In the Heston model, variance evolves randomly over time, making the model more realistic for assets whose volatility changes over time.

Under the risk-neutral measure, the Heston model is written as:

$$
dS_t = (r-q)S_t dt + \sqrt{v_t} S_t dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) dt + \sigma \sqrt{v_t} dW_t^{(2)}
$$

$$
d\langle W^{(1)}, W^{(2)} \rangle_t = \rho dt
$$

where:

- $S_t$ is the stock price
- $v_t$ is the instantaneous variance
- $r$ is the risk-free rate
- $q$ is the dividend yield
- $\kappa$ is the mean-reversion speed of variance
- $\theta$ is the long-run variance level
- $\sigma$ is the volatility of variance
- $\rho$ is the correlation between the stock and variance shocks

---

## Key modeling note

Following the professor’s guidance, this project uses **simple returns**, not log returns, when computing realized variance.

For time grid points $(t_0, t_1, \dots, t_N)$, the simple return is defined as:

$$
R_i = \frac{S_{t_i} - S_{t_{i-1}}}{S_{t_{i-1}}}
$$

Realized variance is then computed from **squared simple returns** using a consistent scaling convention across the project.

This is an important modeling choice and will be used throughout the implementation.

---

## Variance derivatives in this project

### Variance swap

A variance swap is a contract whose payoff depends on the difference between realized variance and a fixed variance strike.

A simplified payoff form is:

$$
\text{Variance Swap Payoff} = RV - K_{\text{var}}
$$

where:
- $RV$ is realized variance,
- $K_{\text{var}}$ is the variance strike.

### Variance option

A variance option is an option written on realized variance. A basic variance call payoff is:

$$
\text{Variance Option Payoff} = \max(RV - K_{\text{var}}, 0)
$$

These payoffs depend on the **entire path** of the stock, not just the terminal stock price, which is why Monte Carlo is especially appropriate.

---

## Numerical method

### Plain Monte Carlo

The base pricing method in this project is standard Monte Carlo simulation:

1. simulate many Heston stock-price and variance paths,
2. compute realized variance on each simulated path,
3. evaluate the derivative payoff on each path,
4. discount the payoff back to time 0,
5. average across all paths.

This gives a flexible estimator, but it can be noisy and computationally expensive.

### Control variate Monte Carlo

To improve efficiency, the project introduces a **control variate**.

The purpose of the control variate is to reduce the variance of the Monte Carlo estimator so that:
- the same number of paths gives a more stable estimate, or
- the same accuracy can be achieved with fewer paths.

The exact control variate specification will be documented in the implementation and experiment sections once finalized.

---

## Project workflow

The project follows the pipeline below:

1. **Heston simulation**
   - simulate stock-price and variance paths under the Heston model

2. **Return computation**
   - compute simple returns from simulated stock-price paths

3. **Realized variance computation**
   - square simple returns and aggregate them consistently

4. **Derivative pricing**
   - price a variance swap
   - price a variance option

5. **Variance reduction**
   - apply a control variate

6. **Numerical evaluation**
   - compare plain MC and control-variate MC
   - report price, standard error, runtime, and efficiency gains

---

## Planned numerical experiments

The project will include experiments designed to evaluate both correctness and efficiency.

### 1. Baseline pricing experiment
For a baseline Heston parameter set:
- simulate paths,
- compute realized variance,
- price the variance swap,
- price the variance option.

### 2. Plain MC vs control-variate MC
For both products, compare:
- estimated price,
- standard error,
- runtime.

### 3. Path-count sensitivity
Study how results change as the number of paths increases.

Example values:
- 5,000 paths
- 10,000 paths
- 20,000 paths
- 50,000 paths
- 100,000 paths

### 4. Time-step sensitivity
Study how results change as the number of time steps increases.

Example values:
- 50 steps
- 100 steps
- 252 steps
- 500 steps

### 5. Parameter robustness
Test several Heston parameter sets, such as:
- moderate volatility of variance,
- higher volatility of variance,
- stronger negative correlation,
- longer maturity.

### 6. Efficiency summary
Report:
- plain MC price,
- control-variate MC price,
- standard errors,
- runtime,
- variance reduction ratio.

---

## Expected outputs

By the end of the project, the repository should contain:

- a Heston path simulator,
- realized variance computation from simple returns,
- variance swap pricer,
- variance option pricer,
- control variate estimator,
- numerical experiment scripts,
- plots and result tables,
- a final README report.

---

## Repository structure

```text
repo/
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
├── requirements.txt
├── docs/
│   └── PROJECT_SCOPE.md
├── src/
│   └── heston_mc/
│       ├── __init__.py
│       ├── params.py
│       ├── utils.py
│       ├── interfaces.py
│       ├── simulation.py
│       ├── realized_variance.py
│       ├── variance_swap.py
│       ├── variance_option.py
│       ├── control_variate.py
│       └── experiments.py
├── tests/
│   ├── test_params.py
│   ├── test_utils.py
│   ├── test_simulation.py
│   ├── test_realized_variance.py
│   ├── test_variance_swap.py
│   ├── test_variance_option.py
│   ├── test_control_variate.py
│   └── test_experiments.py
├── examples/
│   └── run_experiments.py
└── results/
