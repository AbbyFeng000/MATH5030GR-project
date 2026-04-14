import numpy as np

from heston_mc.interfaces import SimulationResult, PricingResult
from heston_mc.variance_swap import price_variance_swap

def test_variance_swap_basic():
    stock_paths = np.array([
        [100.0, 110.0, 121.0],
        [100.0, 90.0, 99.0],
    ])
    variance_paths = np.zeros_like(stock_paths)
    dt = 0.5

    sim_result = SimulationResult(
        stock_paths=stock_paths,
        variance_paths=variance_paths,
        dt=dt,
    )

    result = price_variance_swap(
        sim_result=sim_result,
        strike=0.015,
        rate=0.0,
        maturity=1.0,
    )

    assert isinstance(result, PricingResult)
    assert result.n_paths == 2
    assert result.n_steps == 2
    assert result.std_error >= 0.0