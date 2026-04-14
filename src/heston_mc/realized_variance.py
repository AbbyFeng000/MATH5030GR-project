from __future__ import annotations

import numpy as np

from .utils import simple_returns_from_prices


def realized_variance_from_returns(returns: np.ndarray, dt: float) -> np.ndarray:
    if returns.ndim != 2:
        raise ValueError("returns must be 2D")
    if returns.shape[1] < 1:
        raise ValueError("returns must contain at least one time step")
    if dt <= 0:
        raise ValueError("dt must be positive")

    n_steps = returns.shape[1]
    maturity = n_steps * dt

    return np.sum(returns**2, axis=1) / maturity


def realized_variance_from_prices(stock_paths: np.ndarray, dt: float) -> np.ndarray:
    if dt <= 0:
        raise ValueError("dt must be positive")

    returns = simple_returns_from_prices(stock_paths)
    return realized_variance_from_returns(returns, dt)