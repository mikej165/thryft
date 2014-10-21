from thryft.generators.java.gwt_rpc_client_java_generator import \
    GwtRpcClientJavaGenerator
from thryft_test import _generator_test


class GwtRpcClientJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=GwtRpcClientJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return GwtRpcClientJavaGeneratorTest.suite()
