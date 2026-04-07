from __future__ import annotations

import numpy as np


def make_correlated_normals(
    n_paths: int,
    rho: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    if n_paths <= 0:
        raise ValueError("n_paths must be positive")
    if not -1.0 <= rho <= 1.0:
        raise ValueError("rho must be between -1 and 1")

    z1 = rng.standard_normal(n_paths)
    z2 = rng.standard_normal(n_paths)

    z_v = z2
    z_s = rho * z2 + np.sqrt(1.0 - rho**2) * z1
    return z_s, z_v


def simple_returns_from_prices(stock_paths: np.ndarray) -> np.ndarray:
    if stock_paths.ndim != 2:
        raise ValueError("stock_paths must be 2D")
    if stock_paths.shape[1] < 2:
        raise ValueError("stock_paths must contain at least two time points")

    return (stock_paths[:, 1:] - stock_paths[:, :-1]) / stock_paths[:, :-1]


def discount(value: np.ndarray | float, rate: float, maturity: float):
    return np.exp(-rate * maturity) * value


def standard_error(samples: np.ndarray) -> float:
    if samples.size < 2:
        return 0.0
    return float(samples.std(ddof=1) / np.sqrt(samples.size))