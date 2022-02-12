from setuptools import setup, find_packages


setup(
    name="Stack Frame Analyser",
    python_requires=">3.6",
    version="0.8.0",
    description="It helps to get the context of a frame from the caller's stack. Can be used to improve service and microservice logs.",
    url="https://github.com/cesarmerjan/stack_frame_analyzer",
    author="Cesar Merjan",
    author_email="cesarmerjan@gmail.com",
    license="Apache License 2.0",
    include_package_data=True,
    packages=find_packages(
        exclude=["tests", "__pycache__/", "__pycache__/**/*", "**/*__pycache__/**/*"])
)
