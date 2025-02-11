# Authors: Florian Hofer
#
# License: BSD (3-clause)

import numpy as np

__all__ = [
    '_squared_moving_integration',
    '_thresholding',
]


def _squared_moving_integration(
    x: np.ndarray,
    window_length: int,
) -> np.ndarray: ...


def _thresholding(
    filtered_ecg: np.ndarray,
    integrated_ecg: np.ndarray,
    fs: float,
) -> np.ndarray: ...
