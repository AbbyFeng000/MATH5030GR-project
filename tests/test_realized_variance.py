import numpy as np

from heston_mc.realized_variance import realized_variance_from_prices

def test_realized_variance_basic():
    stock_paths = np.array([
        [100.0, 110.0, 121.0],
        [100.0, 90.0, 99.0],
    ])
    dt = 0.5

    rv = realized_variance_from_prices(stock_paths, dt)

    expected = np.array([
        (0.1**2 + 0.1**2) / 1.0,
        ((-0.1)**2 + 0.1**2) / 1.0,
    ])

    assert rv.shape == (2,)
    assert np.allclose(rv, expected)