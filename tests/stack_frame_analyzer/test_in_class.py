import unittest
from .utils.baz import Baz


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.baz = Baz()

    def test_on_method(self):
        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:baz:Baz:get_baz(self=<instance>, baz=baz)"
        context = self.baz.get_baz("baz")
        self.assertEqual(context, expected_context)

    def test_on_classmethod(self):
        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:baz:Baz:get_baz_cls(baz=baz)"
        context = Baz.get_baz_cls("baz")
        self.assertEqual(context, expected_context)

    def test_on_staticmethod(self):
        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:baz::get_baz_static(baz=baz)"
        context = Baz.get_baz_static("baz")
        self.assertEqual(context, expected_context)
