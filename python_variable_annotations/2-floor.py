#!/usr/bin/env python3
"""
This module provides mathematical floor operations.

It contains functions to compute the floor of floating point numbers,
returning the largest integer less than or equal to the input value.
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of a float number.
    
    This function takes a floating point number and returns the largest
    integer that is less than or equal to the input value, using the
    math.floor() function from Python's standard library.
    
    Args:
        n (float): The floating point number to compute the floor of
        
    Returns:
        int: The floor of n as an integer
    """
    return math.floor(n)
