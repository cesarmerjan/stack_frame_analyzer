import unittest

from src.stack_frame_analyzer.exceptions import (
    FrameDepthOutOfRange,
    InvalidClassRepresentationNameType,
    InvalidCallerDepth,
    InvalidInstanceRepresentationNameType,
    InvalidProjectNameType,
    StackFrameAnalyzerException,
)


class TestStackFrameAnalyzer(unittest.TestCase):
    def test_invalid_frame_depth_exception(self):
        expt = InvalidCallerDepth()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)

    def test_frame_depth_out_of_range_exception(self):
        expt = FrameDepthOutOfRange()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)

    def test_stack_frame_analyser_exception(self):
        expt = StackFrameAnalyzerException()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)

    def test_invalid_project_name_exception(self):
        expt = InvalidProjectNameType()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)

    def test_invalid_instance_representation_name_exception(self):
        expt = InvalidInstanceRepresentationNameType()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)

    def test_invalid_class_representation_name_exception(self):
        expt = InvalidClassRepresentationNameType()
        self.assertIsInstance(expt.message, str)
        self.assertEqual(str(expt), expt.message)
