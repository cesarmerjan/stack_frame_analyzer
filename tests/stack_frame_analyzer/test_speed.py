import timeit
import unittest

from .utils.main import stack_frame_analyzer


class TestStackFrameAnalyzer(unittest.TestCase):
    def test_get_caller_context_speed(self):
        execution_time = timeit.timeit(
            stmt=stack_frame_analyzer.get_caller_context, number=1000
        )
        self.assertLessEqual(execution_time, 0.8)
