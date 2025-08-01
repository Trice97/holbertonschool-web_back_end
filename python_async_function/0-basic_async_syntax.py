#!/usr/bin/env python3
"""
This module provides basic asynchronous operations.

It contains coroutines for generating random delays and demonstrating
the fundamentals of asynchronous programming with asyncio.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.
    This asynchronous coroutine generates a random floating point delay
    between 0 and max_delay (inclusive) and waits for that duration
    before returning the actual delay value.
    Args:
    max_delay (int): Maximum delay in seconds (default: 10)
    Returns:
        float: The actual delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
