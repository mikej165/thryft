from thryft.generators.java.json_rpc_servlet_java_generator import \
    JsonRpcServletJavaGenerator
from thryft_test import _generator_test


class JsonRpcServletJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=JsonRpcServletJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return JsonRpcServletJavaGeneratorTest.suite()
