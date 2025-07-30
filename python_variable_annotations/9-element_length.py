#!/usr/bin/env python3
"""
This module provides iterable analysis operations.

It contains functions to analyze sequences and iterables,
specifically for computing the length of elements within collections.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.
    This function takes an iterable of sequences (like strings, lists, etc.)
    and returns a list where each element is a tuple containing the original
    sequence and its length. This is useful for analyzing collections of
    variable-length sequences.
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences that
                                 have a length (strings, lists, tuples, etc.)
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
                                   contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
