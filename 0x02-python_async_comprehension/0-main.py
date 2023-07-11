#!/usr/bin/env python3

"""
Test file for printing the yielded values from the async_generator coroutine.
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    """
    Asynchronous function to print the yielded values from the async_generator coroutine.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


asyncio.run(print_yielded_values())

