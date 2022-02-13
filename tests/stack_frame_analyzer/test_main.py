import unittest

from stack_frame_analyzer import StackFrameAnalyzer


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.stack_frame_analyzer = StackFrameAnalyzer()

    def test_instantiation(self):
        self.assertIsInstance(self.stack_frame_analyzer, StackFrameAnalyzer)

    def test_default_parameters(self):
        self.assertEqual(self.stack_frame_analyzer.project_name, "stack_frame_analyzer")
        self.assertEqual(self.stack_frame_analyzer.instance_representation_name, "self")
        self.assertEqual(self.stack_frame_analyzer.class_representation_name, "cls")
