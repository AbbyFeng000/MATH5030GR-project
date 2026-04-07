import numpy as np
import time

from .interfaces import SimulationResult, PricingResult
from .utils import discount, standard_error
from .realized_variance import realized_variance_from_prices


def variance_swap_payoff(rv: np.ndarray, strike: float) -> np.ndarray:
    return rv - strike


def price_variance_swap(
    sim_result: SimulationResult,
    strike: float,
    rate: float,
    maturity: float,
) -> PricingResult:

    start = time.time()

    rv = realized_variance_from_prices(sim_result.stock_paths, sim_result.dt)

    payoff = variance_swap_payoff(rv, strike)

    discounted = discount(payoff, rate, maturity)

    price = float(np.mean(discounted))
    se = standard_error(discounted)

    runtime = time.time() - start

    return PricingResult(
        price=price,
        std_error=se,
        n_paths=sim_result.stock_paths.shape[0],
        n_steps=sim_result.stock_paths.shape[1] - 1,
        runtime_seconds=runtime,
        method_name="plain_mc_variance_swap",
    )