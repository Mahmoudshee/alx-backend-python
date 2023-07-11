#!/usr/bin/env python3

"""
This module contains a coroutine that measures the total runtime of executing async_comprehension four times in parallel.
"""

import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time()

    return end_time - start_time
