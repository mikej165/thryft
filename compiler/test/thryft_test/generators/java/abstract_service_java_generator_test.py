from thryft.generators.java.abstract_service_java_generator import \
    AbstractServiceJavaGenerator
from thryft_test import _generator_test


class AbstractServiceJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=AbstractServiceJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return AbstractServiceJavaGeneratorTest.suite()
