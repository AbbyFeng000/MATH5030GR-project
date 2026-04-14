from __future__ import annotations

import time

import numpy as np

from .interfaces import PricingResult, SimulationResult
from .realized_variance import realized_variance_from_prices
from .utils import discount, standard_error


def variance_swap_payoff(realized_variance: np.ndarray, strike: float) -> np.ndarray:
    if realized_variance.ndim != 1:
        raise ValueError("realized_variance must be 1D")

    return realized_variance - strike


def price_variance_swap(
    sim_result: SimulationResult,
    strike: float,
    rate: float,
    maturity: float,
) -> PricingResult:
    if maturity <= 0:
        raise ValueError("maturity must be positive")

    start_time = time.time()

    realized_variance = realized_variance_from_prices(
        sim_result.stock_paths,
        sim_result.dt,
    )

    payoff = variance_swap_payoff(realized_variance, strike)
    discounted_payoff = discount(payoff, rate, maturity)

    price = float(np.mean(discounted_payoff))
    std_err = standard_error(discounted_payoff)
    runtime = time.time() - start_time

    return PricingResult(
        price=price,
        std_error=std_err,
        n_paths=sim_result.stock_paths.shape[0],
        n_steps=sim_result.stock_paths.shape[1] - 1,
        runtime_seconds=runtime,
        method_name="plain_mc_variance_swap",
    )