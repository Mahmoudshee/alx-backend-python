#!/usr/bin/env python3

"""
This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
