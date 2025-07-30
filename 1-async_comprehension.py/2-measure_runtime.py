#!/usr/bin/env python3
"""
Module that measures runtime for parallel async comprehensions.
"""

import asyncio
import time
from importlib import import_module

async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.
    
    Returns:
        float: Total runtime in seconds
    """
    start_time = time.time()
    
    # Exécution en parallèle de 4 async_comprehension
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.time()
    return end_time - start_time