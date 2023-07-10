#!/usr/bin/env python3

"""
Create an asyncio.Task that runs the wait_random coroutine.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: The task for running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

