import unittest
from .utils.foo import foo
from .utils.bar import bar


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:foo::foo(baz=baz)"

    def test_on_function(self):
        context = foo("baz")
        self.assertEqual(context, self.expected_context)

    def test_on_second_level_function(self):
        context = bar("baz")
        self.assertEqual(context, self.expected_context)
