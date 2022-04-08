from .main import stack_frame_analyzer


def foo_with_exception(baz):
    try:
        raise Exception
    except Exception:
        context = stack_frame_analyzer.get_caller_context()
        return context
