from .main import stack_frame_analyzer


class MyException(Exception):
    def __init__(self):
        self.context = stack_frame_analyzer.get_frame_context(stack_frame_depth=2)
        super().__init__()


def bar_with_exception(foo):
    try:
        raise MyException
    except MyException as error:
        return error.context
