from .main import stack_frame_analyzer


class MyException(Exception):
    def __init__(self):
        self.context = stack_frame_analyzer.get_caller_context(depth_in_the_stack=1)
        super().__init__()


def bar_with_exception(foo):
    try:
        raise MyException
    except MyException as error:
        return error.context
