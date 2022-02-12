from asyncio import tasks
import unittest
from threading import Thread
from queue import Queue
from .utils.solve_with_queue import solve_with_queue
from .utils.foo import foo
from .utils.baz import Baz


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:foo::foo(baz=baz)"

    def test_get_frame_context_with_threads(self):
        tasks = [
            Thread(target=solve_with_queue(foo, self.queue), args=("baz",))
            for _ in
            range(50)
        ]

        [task.start() for task in tasks]

        [task.join() for task in tasks]

        threads_result = set()

        while self.queue.qsize() > 0:
            threads_result.add(self.queue.get())
            self.queue.task_done()

        self.assertEqual(len(threads_result), 1)

        context = threads_result.pop()

        self.assertEqual(context, self.expected_context)

    def test_get_frame_context_with_threads_with_two_different_functions(self):

        tasks_foo = [
            Thread(target=solve_with_queue(foo, self.queue), args=("baz",))
            for _ in
            range(50)
        ]

        baz = Baz()

        tasks_baz = [
            Thread(target=solve_with_queue(
                baz.get_baz, self.queue), args=("baz",))
            for _ in
            range(50)
        ]

        tasks = tasks_foo + tasks_baz

        [task.start() for task in tasks]

        [task.join() for task in tasks]

        threads_result = set()

        while self.queue.qsize() > 0:
            threads_result.add(self.queue.get())
            self.queue.task_done()

        self.assertEqual(len(threads_result), 2)
