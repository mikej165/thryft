from thryft.generators.java.gwt_rpc_client_async_java_generator import \
    GwtRpcClientAsyncJavaGenerator
from thryft_test import _generator_test


class GwtRpcClientAsyncJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtRpcClientAsyncJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtRpcClientAsyncJavaGeneratorTest.suite()
