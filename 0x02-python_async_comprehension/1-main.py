#!/usr/bin/env python3

"""
Test file for printing the result of the async_comprehension coroutine.
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    """
    Asynchronous function to print the result of the async_comprehension coroutine.
    """
    print(await async_comprehension())


asyncio.run(main())
