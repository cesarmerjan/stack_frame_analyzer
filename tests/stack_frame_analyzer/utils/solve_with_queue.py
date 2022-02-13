from queue import Queue
from typing import Any, Callable


def solve_with_queue(func: Callable[[Any], Any], queue: Queue):
    def wrapper(*args, **kwagrs):
        context = func(*args, **kwagrs)
        queue.put(context)

    return wrapper
