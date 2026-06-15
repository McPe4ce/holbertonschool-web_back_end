#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    task = asyncio.create_task(wait_random(max_delay))
    return task


if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))