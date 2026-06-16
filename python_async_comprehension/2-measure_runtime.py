#!/usr/bin/env python3
"""Module that measures the run time using gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measures the run time using gather"""
    start_timer = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = time.perf_counter() - start_timer
    return total_time
