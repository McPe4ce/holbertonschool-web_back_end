#!/usr/bin/env python3
"""Script that returns a task and does use the asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Script that returns a task and does use the asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
