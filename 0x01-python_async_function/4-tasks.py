#!/usr/bin/env python3

"""
Create an asyncio.Task that runs the wait_random coroutine multiple times.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create an asyncio.Task that runs the wait_random coroutine multiple times.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: The list of delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return await asyncio.gather(*tasks)

