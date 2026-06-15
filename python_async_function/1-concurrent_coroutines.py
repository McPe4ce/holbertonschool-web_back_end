#!/usr/bin/env python3
"""Script that spawn wait_random n times with the specified max_delay"""

from basic_async_syntax import wait_random
import asyncio


async def wait_n(n, max_delay) -> float:
    """ Return the list of all the delays"""
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delayed = await task
        delays.append(delayed)
    return delays
