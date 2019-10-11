# Copyright 2018 John Reese
# Licensed under the MIT license

"""
AsyncIO version of the standard multiprocessing module
"""

__author__ = "John Reese"
__version__ = "0.6.1"

from .core import (
    Pool,
    Process,
    QueueID,
    RandomScheduler,
    ShardedPool,
    ShardedPoolScheduler,
    TaskID,
    Worker,
    set_context,
    set_start_method,
)
