from thryft.generators.java.jsonrpc_client_java_generator import \
    JsonrpcClientJavaGenerator
from thryft_test import _generator_test


class JsonrpcClientJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JsonrpcClientJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return JsonrpcClientJavaGeneratorTest.suite()
