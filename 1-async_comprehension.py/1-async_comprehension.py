#!/usr/bin/env python3
"""
Module that contains async comprehension functionality.
"""

from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator.
    
    Returns:
        List[float]: List of 10 random numbers
    """
    # Utilisation d'une async comprehension au lieu d'une boucle async for
    return [number async for number in async_generator()]