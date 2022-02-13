from .main import stack_frame_analyzer


class BadClass:
    DATA = []  # bad class attribute

    def add_data(self, data: str):
        context = stack_frame_analyzer.get_frame_context()  # noqa
        # the instance attribute DATA is referring to the class attribute DATA
        self.DATA.append(data * 500)


DATA = []


def leak_memory():
    context = stack_frame_analyzer.get_frame_context()  # noqa
    global DATA
    bad_data = ["data"] * 100
    DATA += bad_data
    return "leak"
