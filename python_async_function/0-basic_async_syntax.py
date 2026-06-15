#!/usr/bin/env python3
"""Script that uses an asynchronous coroutine that prints with a delay"""

import asyncio
import random


async def wait_random(max_delay=10):
    da_delay = random.uniform(0, max_delay)
    await asyncio.sleep(da_delay)
    return da_delay
