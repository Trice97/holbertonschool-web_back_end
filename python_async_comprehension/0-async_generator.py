#!/usr/bin/env python3
"""
Module that contains an asynchronous generator.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, waits 1 second asynchronously,
    then yields a random number between 0 and 10.
    Yields:
        float: Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
