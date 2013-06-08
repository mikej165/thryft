from thryft.generators.thrift.thrift_generator import ThriftGenerator
from thryft_test import _generator_test


class ThriftGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=ThriftGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return ThriftGeneratorTest.suite()
