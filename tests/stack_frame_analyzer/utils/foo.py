from .main import stack_frame_analyzer


def foo(baz):

    context = stack_frame_analyzer.get_caller_context()
    return context
