#!/usr/bin/env python3

"""
This module contains a coroutine that collects random numbers using async comprehensions.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehensions.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
