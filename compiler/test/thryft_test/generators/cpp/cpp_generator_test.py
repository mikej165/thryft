from thryft.generators.cpp.cpp_generator import CppGenerator
from thryft_test import _generator_test


class CppGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=CppGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return CppGeneratorTest.suite()
