#!/usr/bin/env python3
"""Scrip that returns a random num from an async_generator"""
import asyncio
import random


async def async_generator():
    """Scrip that returns a random num from an async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
