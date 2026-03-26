from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HestonParams:
    """
    Shared Heston model parameter container.
    """

    s0: float
    v0: float
    r: float
    kappa: float
    theta: float
    sigma: float
    rho: float
    q: float = 0.0

    def validate(self) -> None:
        if self.s0 <= 0:
            raise ValueError("s0 must be positive")
        if self.v0 < 0:
            raise ValueError("v0 must be nonnegative")
        if self.kappa <= 0:
            raise ValueError("kappa must be positive")
        if self.theta < 0:
            raise ValueError("theta must be nonnegative")
        if self.sigma <= 0:
            raise ValueError("sigma must be positive")
        if not -1.0 <= self.rho <= 1.0:
            raise ValueError("rho must be between -1 and 1")

    def as_dict(self) -> dict[str, float]:
        return {
            "s0": self.s0,
            "v0": self.v0,
            "r": self.r,
            "q": self.q,
            "kappa": self.kappa,
            "theta": self.theta,
            "sigma": self.sigma,
            "rho": self.rho,
        }
