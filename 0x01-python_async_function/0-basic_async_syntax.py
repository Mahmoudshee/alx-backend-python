#!/usr/bin/env python3

"""
Asynchronous coroutine that waits for a random delay between 0 and max_delay (included)
seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): The maximum delay value (default: 10).

    Returns:
        float: The random delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

