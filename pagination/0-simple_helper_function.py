#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for the given pagination parameters.
    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end