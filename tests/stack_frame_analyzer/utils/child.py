from .parent import Parent


class Child(Parent):
    def get_baz(self, baz: str):
        return self.context

    @classmethod
    def get_foo(cls):
        return cls._get_context()
