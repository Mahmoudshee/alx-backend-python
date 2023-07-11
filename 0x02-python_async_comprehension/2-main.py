#!/usr/bin/env python3

"""
Test file for printing the total runtime of executing the measure_runtime coroutine.
"""

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """
    Asynchronous function to print the total runtime of executing the measure_runtime coroutine.
    """
    return await measure_runtime()


print(asyncio.run(main()))

