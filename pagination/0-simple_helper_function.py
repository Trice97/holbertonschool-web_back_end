#!/usr/bin/python3

def index_range(page: int = 1, page_size: int = 15) ->tuple[int, int]:
    """function to return that takes 2 int"""
    assert page > 0 
    assert page_size > 0

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
