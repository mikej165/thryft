from thryft.generators.java.java_generator import JavaGenerator
from thryft_test import _generator_test


class JavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return JavaGeneratorTest.suite()
