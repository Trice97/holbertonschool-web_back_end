#!/usr/bin/env python3
"""
This module provides runtime measurement utilities.

It contains functions to measure the execution time of asynchronous
operations and calculate performance metrics.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return average time.
    
    This function measures the total execution time for wait_n(n, max_delay)
    and returns the average time per operation by dividing total time by n.
    
    Args:
        n (int): Number of operations to execute
        max_delay (int): Maximum delay for each operation
        
    Returns:
        float: Average execution time per operation
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n