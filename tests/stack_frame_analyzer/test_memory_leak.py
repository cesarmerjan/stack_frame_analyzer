import tracemalloc
import unittest

from .utils.main import stack_frame_analyzer
from .utils.memory_leak import BadClass


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.stack_frame_analyzer_package_module_name = "stack_frame_analyzer/main.py"
        self.memory_leak_package_module_name = "utils/memory_leak.py"
        self.one_megabyte = 1_000_000
        self.one_kilobyte = 1_000

    def test_if_leak(self):

        tracemalloc.start()

        stack_frame_analyzer.get_caller_context()

        snapshot1 = tracemalloc.take_snapshot()

        for _ in range(10000):
            stack_frame_analyzer.get_caller_context()

        snapshot2 = tracemalloc.take_snapshot()

        for _ in range(10000):
            stack_frame_analyzer.get_caller_context()

        snapshot3 = tracemalloc.take_snapshot()

        snapshot_diff_1_2 = snapshot2.compare_to(snapshot1, "lineno")

        snapshot_diff_2_3 = snapshot3.compare_to(snapshot2, "lineno")

        for stat in snapshot_diff_1_2:
            if self.stack_frame_analyzer_package_module_name in str(stat.traceback):
                self.assertLessEqual(stat.size_diff, self.one_megabyte)
                self.assertLessEqual(stat.count_diff, 2)

        for stat in snapshot_diff_2_3:
            self.assertNotIn(
                self.stack_frame_analyzer_package_module_name, str(stat.traceback)
            )

        tracemalloc.clear_traces()

        tracemalloc.stop()

    def test_force_leak(self):

        tracemalloc.start()

        server_is_running = True
        last_day_snapshot = None

        while server_is_running:
            for day in range(31):

                for request in range(500):
                    bad_class = BadClass()
                    bad_class.add_data("data")

                actual_day_snapshot = tracemalloc.take_snapshot()

                if last_day_snapshot:
                    snapshot_diff = actual_day_snapshot.compare_to(
                        last_day_snapshot, "lineno"
                    )

                    memory_diff_of_memory_leak = 0
                    memory_diff_of_stack_frame_analyzer = 0
                    for stat in snapshot_diff:
                        if self.memory_leak_package_module_name in str(stat.traceback):
                            memory_diff_of_memory_leak = max(
                                stat.size_diff, memory_diff_of_memory_leak
                            )

                        if self.stack_frame_analyzer_package_module_name in str(
                            stat.traceback
                        ):
                            memory_diff_of_stack_frame_analyzer = max(
                                stat.size_diff, memory_diff_of_stack_frame_analyzer
                            )

                    self.assertGreaterEqual(
                        memory_diff_of_memory_leak, self.one_megabyte
                    )

                    self.assertLessEqual(
                        memory_diff_of_stack_frame_analyzer, self.one_kilobyte
                    )

                last_day_snapshot = actual_day_snapshot

            server_is_running = False

        tracemalloc.clear_traces()

        tracemalloc.stop()
