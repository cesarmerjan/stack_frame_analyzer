import unittest

from .utils.child import Child


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.child = Child()

    def test_on_method_with_depth_two_frame(self):
        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:child:Child:get_baz(self=<instance>, baz=baz)"  # noqa
        context = self.child.get_baz("baz")
        self.assertEqual(context, expected_context)

    def test_on_classmethod_with_depth_two_frame(self):
        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:child:Child:get_foo()"
        context = self.child.get_foo()
        self.assertEqual(context, expected_context)
