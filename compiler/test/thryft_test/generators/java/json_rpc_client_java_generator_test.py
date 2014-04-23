from thryft.generators.java.json_rpc_client_java_generator import \
    JsonRpcClientJavaGenerator
from thryft_test import _generator_test


class JsonRpcClientJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JsonRpcClientJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return JsonRpcClientJavaGeneratorTest.suite()
