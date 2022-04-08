from .main import stack_frame_analyzer


class Baz:
    @classmethod
    def get_baz_cls(cls, baz):
        context = stack_frame_analyzer.get_caller_context()
        return context

    def get_baz(self, baz):
        context = stack_frame_analyzer.get_caller_context()
        return context

    @staticmethod
    def get_baz_static(baz):
        context = stack_frame_analyzer.get_caller_context()
        return context
