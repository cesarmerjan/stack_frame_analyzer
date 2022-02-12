from .main import stack_frame_analyzer


class Parent:
    @property
    def context(self):
        return stack_frame_analyzer.get_frame_context(2)

    @classmethod
    def _get_context(cls):
        return stack_frame_analyzer.get_frame_context(2)
