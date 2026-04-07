import numpy as np
from .utils import simple_returns_from_prices


def realized_variance_from_prices(stock_paths: np.ndarray, dt: float) -> np.ndarray:
    """
    Compute realized variance from stock price paths.

    Parameters:
        stock_paths: shape (n_paths, n_steps+1)
        dt: time step size

    Returns:
        realized variance per path, shape (n_paths,)
    """
    if dt <= 0:
        raise ValueError("dt must be positive")

    returns = simple_returns_from_prices(stock_paths)

    n_steps = returns.shape[1]
    T = n_steps * dt

    rv = np.sum(returns**2, axis=1) / T

    return rv