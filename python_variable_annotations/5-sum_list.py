#!/usr/bin/env python3
"""
This module provides list summation operations.

It contains functions to compute the sum of numeric lists,
specifically for lists containing floating point numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all floats in a list.
    This function takes a list of floating point numbers and returns
    their total sum using Python's built-in sum() function.
    Args:
        input_list (List[float]): List of floats to sum
    Returns:
        float: The sum of all numbers in the list
    """
    return sum(input_list)
