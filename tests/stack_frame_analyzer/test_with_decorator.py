import unittest
from .utils.foo_with_decorator import foo_decorated


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:foo_with_decorator::foo_decorated(baz=baz)"

    def test_on_function(self):
        context = foo_decorated("baz")
        self.assertEqual(context, self.expected_context)
