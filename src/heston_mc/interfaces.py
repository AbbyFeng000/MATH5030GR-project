from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class SimulationResult:
    stock_paths: np.ndarray
    variance_paths: np.ndarray
    dt: float


@dataclass
class PricingResult:
    price: float
    std_error: float
    n_paths: int
    n_steps: int
    runtime_seconds: float
    method_name: str
