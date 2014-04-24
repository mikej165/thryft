from thryft.generators.java.gwt_json_rpc_client_java_generator import \
    GwtJsonRpcClientJavaGenerator
from thryft_test import _generator_test


class GwtJsonRpcClientJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtJsonRpcClientJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtJsonRpcClientJavaGeneratorTest.suite()
