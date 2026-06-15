#!/usr/bin/env python3
"""The code is nearly identical to wait_n, task_wait_random is being called."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Does the same as wait_n"""
    delays = []
    waiter = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(waiter):
        delayed = await task
        delays.append(delayed)
    return delays


if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
