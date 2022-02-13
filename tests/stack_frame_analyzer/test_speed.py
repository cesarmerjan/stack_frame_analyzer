import timeit
import unittest

from .utils.main import stack_frame_analyzer


class TestStackFrameAnalyzer(unittest.TestCase):
    def test_get_frame_context_speed(self):
        execution_time = timeit.timeit(
            stmt=stack_frame_analyzer.get_frame_context, number=1000
        )
        self.assertLessEqual(execution_time, 0.5)
