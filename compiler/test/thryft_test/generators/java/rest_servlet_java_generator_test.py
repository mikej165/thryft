from thryft.generators.java.rest_servlet_java_generator import \
    RestServletJavaGenerator
from thryft_test import _generator_test


class RestServletJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=RestServletJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return RestServletJavaGeneratorTest.suite()
