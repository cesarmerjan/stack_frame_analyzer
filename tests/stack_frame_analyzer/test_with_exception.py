import unittest

from .utils.foo_with_exception import foo_with_exception


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer.utils:foo_with_exception::foo_with_exception(baz=baz)"  # noqa

    def test_on_function_with_exception(self):
        context = foo_with_exception("baz")
        self.assertEqual(context, self.expected_context)
