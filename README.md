# Stack Frame Analyzer
This package was created to help improve the quality of application logs.

It's only uses building libraries, therefore, it has no external dependency.
It is also lightweight and thread-safe, which makes it ideal for use in services and micro-services.

However, the module has some limitations.
The most important thing to note in this scenario is that it only works with the **CPython** implementation.

The returned context is formatted according to the following pattern:
  *project_name:package_name:module_name:class_name:callable_name(callable_arguments)*

An example of the context returned could be:
  *authentication_service:src.domain.user:model:UserModel:has_permission(self=..., permission="add_user")*

## Typical usage example:


### Caller's Stack Frame Depth 1
```python
stack_frame_analyzer = StackFrameAnalyzer("my_service_name")

def foo(bar):
    try:
        ...
    except Exception as error:
        context = stack_frame_analyzer.get_frame_context()
        logging.error(context)
```

### Caller's Stack Frame Depth 2
```python
stack_frame_analyzer = StackFrameAnalyzer("my_service_name")

class MyException(Exception):
    def __init__(self):
        self.context = stack_frame_analyzer.get_frame_context(stack_frame_depth=2)
        super().__init__()


def foo(bar):
    try:
        ...
    except MyException as error:
        logging.error(error.context)
```

### Caller's Stack Frame Depth 3


------------

```python
class ExceptionWithContext(Exception):
    def __init__(self, message: str):
        self.message = message
        self.context = stack_frame_analyzer.get_frame_context(stack_frame_depth=3)
        super().__init__(self.message)


class FooException(ExceptionWithContext):
    '''Foo Exception'''

    def __init__(self, message: str = "message"):
        self.message = message
        super().__init__(self.message)


def foo(bar):
    try:
        raise FooException
    except FooException as error:
        logging.error(error.context)
```