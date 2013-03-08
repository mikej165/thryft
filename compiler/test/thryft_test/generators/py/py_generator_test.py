from thryft.generators.py.py_generator import PyGenerator
from thryft_test import _generator_test


class PyGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=PyGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return PyGeneratorTest.suite()
