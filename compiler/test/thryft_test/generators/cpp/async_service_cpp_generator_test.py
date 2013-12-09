from thryft.generators.cpp.async_service_cpp_generator import \
    AsyncServiceCppGenerator
from thryft_test import _generator_test


class AsyncServiceCppGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=AsyncServiceCppGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return AsyncServiceCppGeneratorTest.suite()
