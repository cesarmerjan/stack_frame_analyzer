from functools import wraps

from .main import stack_frame_analyzer


def foo_decotator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@foo_decotator
def foo_decorated(baz):
    context = stack_frame_analyzer.get_caller_context()
    return context
