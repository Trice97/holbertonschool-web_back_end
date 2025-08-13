#!/usr/bin/env python3
"""
Module containing index_range function for pagination
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple containing start index and end index 
    for pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    
    return (start, end)