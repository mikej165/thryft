from thryft.generators.java.gwt_rpc_server_java_generator import \
    GwtRpcServerJavaGenerator
from thryft_test import _generator_test


class GwtRpcServerJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtRpcServerJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtRpcServerJavaGeneratorTest.suite()
