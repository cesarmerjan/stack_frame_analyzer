from .main import stack_frame_analyzer


def foo(baz):

    context = stack_frame_analyzer.get_frame_context()
    return context
