#!/usr/bin/env python3
"""Module that measures the run time using gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of running async_comprehension
    four times in parallel."""
    start_timer = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start_timer
