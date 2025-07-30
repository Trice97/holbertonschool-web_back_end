#!/usr/bin/env python3
"""Function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies by multiplier"""

    def multiply_function(x: float) -> float:
        """Inner function that does the multiplication"""
        return x * multiplier

    return multiply_function
