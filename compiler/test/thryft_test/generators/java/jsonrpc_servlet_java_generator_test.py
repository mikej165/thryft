from thryft.generators.java.jsonrpc_servlet_java_generator import \
    JsonrpcServletJavaGenerator
from thryft_test import _generator_test


class JsonrpcServletJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JsonrpcServletJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return JsonrpcServletJavaGeneratorTest.suite()
