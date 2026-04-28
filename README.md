# heston_mc

Monte Carlo pricing of variance swaps and variance options under the Heston stochastic volatility model, with control variates for improved efficiency.

> Course project on efficient Monte Carlo pricing of variance derivatives under the Heston model.

For a more detailed project description, see [`docs/PROJECT_SCOPE.md`](docs/PROJECT_SCOPE.md).

## What are variance derivatives?

Variance derivatives are contracts whose payoff depends on how much an asset fluctuates over time, rather than only on its final price. In this project, we focus on two examples:

- **Variance swaps**, whose payoff depends linearly on realized variance relative to a strike
- **Variance options**, whose payoff depends on the positive part of realized variance above a strike

This package is being built to simulate stock-price and variance paths under the Heston model, compute realized variance from **simple returns**, and use Monte Carlo methods to price these products. It also includes a control variate component to improve efficiency by reducing Monte Carlo noise.

## Model

Under the risk-neutral measure, the Heston model is

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
- $\kappa$ is the mean-reversion speed
- $\theta$ is the long-run variance level
- $\sigma$ is the volatility of variance
- $\rho$ is the correlation between the stock and variance shocks

## Installation

```bash
pip install heston-mc-variance-project
```

## Quick start

```python
from heston_mc.params import HestonParams, MonteCarloConfig, default_heston_params, default_mc_config
from heston_mc.interfaces import SimulationResult, PricingResult

params = default_heston_params()
config = default_mc_config()

print(params)
print(config)
```

This package is currently under active development. The main pricing workflow is being assembled across the following modules:

- `heston_mc.simulation`
- `heston_mc.realized_variance`
- `heston_mc.variance_swap`
- `heston_mc.variance_option`
- `heston_mc.control_variate`

## Demo notebook

An interactive demo will be available at `notebooks/demo.ipynb`:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AbbyFeng000/MATH5030GR-project/blob/main/notebooks/demo.ipynb)

## API reference

### `HestonParams`
Shared parameter class for the Heston stochastic volatility model.

| Parameter | Type | Description |
|---|---|---|
| `s0` | `float` | Initial stock price |
| `v0` | `float` | Initial variance |
| `r` | `float` | Risk-free interest rate |
| `q` | `float` | Dividend yield |
| `kappa` | `float` | Mean-reversion speed of variance |
| `theta` | `float` | Long-run variance level |
| `sigma` | `float` | Volatility of variance |
| `rho` | `float` | Correlation between stock and variance shocks |

### `MonteCarloConfig`
Shared Monte Carlo configuration.

| Parameter | Type | Description |
|---|---|---|
| `maturity` | `float` | Time to maturity |
| `n_steps` | `int` | Number of time steps |
| `n_paths` | `int` | Number of simulated paths |
| `seed` | `int` | Random seed |
| `periods_per_year` | `int` | Scaling used in realized variance |

### `SimulationResult`
Container for simulation output.

| Field | Type | Description |
|---|---|---|
| `stock_paths` | `np.ndarray` | Simulated stock-price paths |
| `variance_paths` | `np.ndarray` | Simulated variance paths |
| `dt` | `float` | Time step size |

### `PricingResult`
Container for pricing output.

| Field | Type | Description |
|---|---|---|
| `price` | `float` | Estimated derivative price |
| `std_error` | `float` | Monte Carlo standard error |
| `n_paths` | `int` | Number of simulation paths |
| `n_steps` | `int` | Number of time steps |
| `runtime_seconds` | `float` | Runtime in seconds |
| `method_name` | `str` | Name of pricing method |

### Module overview

- `heston_mc.simulation` — Heston path simulation
- `heston_mc.realized_variance` — realized variance from simple returns
- `heston_mc.variance_swap` — variance swap pricing
- `heston_mc.variance_option` — variance option pricing
- `heston_mc.control_variate` — control variate estimators
- `heston_mc.interfaces` — shared result containers
- `heston_mc.params` — shared parameter and Monte Carlo configuration objects

### References
Broadie, M., & Jain, A. (2008). Pricing and Hedging Volatility Derivatives. The Journal of Derivatives, 15(3), 7–24. https://doi.org/10.3905/jod.2008.702503

Fouque, J.-P., & Han, C.-H. (2004). Variance reduction for Monte Carlo methods to evaluate option prices under multi-factor stochastic volatility models. Quantitative Finance, 4(5), 597–606. https://doi.org/10.1080/14697680400020317

## License

MIT
