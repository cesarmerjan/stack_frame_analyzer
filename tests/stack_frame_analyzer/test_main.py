import inspect
import unittest

from src.stack_frame_analyzer import StackFrameAnalyzer
from src.stack_frame_analyzer.exceptions import FrameDepthOutOfRange, InvalidFrameDepth


class TestStackFrameAnalyzer(unittest.TestCase):
    def setUp(self):
        self.stack_frame_analyzer = StackFrameAnalyzer()

    def test_instantiation(self):
        self.assertIsInstance(self.stack_frame_analyzer, StackFrameAnalyzer)

    def test_default_parameters(self):
        self.assertEqual(self.stack_frame_analyzer.project_name, "stack_frame_analyzer")
        self.assertEqual(
            self.stack_frame_analyzer.project_name,
            self.stack_frame_analyzer.PROJECT_NAME,
        )
        self.assertEqual(self.stack_frame_analyzer.instance_representation_name, "self")
        self.assertEqual(self.stack_frame_analyzer.class_representation_name, "cls")

    def test_instantiaion_without_defaults(self):
        project_name = "service"
        instance_representation = "instance"
        class_representation = "this_class"
        stack_frame_analyzer = StackFrameAnalyzer(
            project_name, instance_representation, class_representation
        )

        self.assertEqual(project_name, stack_frame_analyzer.project_name)
        self.assertEqual(
            instance_representation, stack_frame_analyzer.instance_representation_name
        )
        self.assertEqual(
            class_representation, stack_frame_analyzer.class_representation_name
        )

    def test_get_frame(self):
        current_frame = inspect.currentframe()
        frame = self.stack_frame_analyzer._get_frame(1)
        self.assertEqual(current_frame, frame)

    def test_get_frame_error(self):
        with self.assertRaises(FrameDepthOutOfRange):
            self.stack_frame_analyzer._get_frame(100)

    def test_get_package_and_module(self):
        current_frame = inspect.currentframe()
        package, module = self.stack_frame_analyzer._get_package_and_module(
            current_frame
        )

        self.assertEqual(package, "tests.stack_frame_analyzer")
        self.assertEqual(module, "test_main")

    def test_get_class_name(self):
        current_frame = inspect.currentframe()
        class_name = self.stack_frame_analyzer._get_class_name(current_frame)

        self.assertEqual(class_name, "TestStackFrameAnalyzer")

    def test_get_callable_name(self):
        current_frame = inspect.currentframe()
        callable_name = self.stack_frame_analyzer._get_callable_name(current_frame)

        self.assertEqual(callable_name, "test_get_callable_name")

    def test_stringfy_armguments(self):
        args = {
            "project_name": "stack_frame_analyzer",
            "instance_representation_name": "self",
            "class_representation_name": "cls",
        }

        args_string = self.stack_frame_analyzer._stringfy_armguments(args)
        expected_string = "project_name=stack_frame_analyzer, instance_representation_name=self, class_representation_name=cls"

        self.assertEqual(args_string, expected_string)

    def test_get_callable_arguments(self, not_used_arg: str = None):
        not_used_arg
        current_frame = inspect.currentframe()
        args_string = self.stack_frame_analyzer._get_callable_arguments(current_frame)
        expected_args_string = "self=<instance>, not_used_arg=None"

        self.assertEqual(args_string, expected_args_string)

    def test_build_context(self):
        context = self.stack_frame_analyzer._build_context(
            "tests.stack_frame_analyzer",
            "test_main",
            "TestStackFrameAnalyzer",
            "test_build_context",
            "self=<instance>",
        )

        expected_context = "stack_frame_analyzer:tests.stack_frame_analyzer:test_main:"
        expected_context += "TestStackFrameAnalyzer:test_build_context(self=<instance>)"

        self.assertEqual(context, expected_context)

    def test_frame_out_of_range(self):
        with self.assertRaises(FrameDepthOutOfRange):
            self.stack_frame_analyzer.get_frame_context(100)

    def test_invalid_frame_depth(self):
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(-1)

        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(b"OK")
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context("2")
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context([])
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context({})
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(set([]))
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(1.2)
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(lambda: "function")
        with self.assertRaises(InvalidFrameDepth):
            self.stack_frame_analyzer.get_frame_context(type("MyClass", (object,), {}))
