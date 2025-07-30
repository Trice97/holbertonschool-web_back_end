#!/usr/bin/env python3
"""
This module provides asyncio Task creation utilities.

It contains functions to create and manage asyncio Task objects
for better control over asynchronous operation execution.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for wait_random coroutine.
    
    This function creates and returns an asyncio Task object that wraps
    the wait_random coroutine for concurrent execution management.
    
    Args:
        max_delay (int): Maximum delay for the wait_random coroutine
        
    Returns:
        asyncio.Task: Task object wrapping wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
