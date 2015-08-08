from thryft.generators.java.validating_service_java_generator import \
    ValidatingServiceJavaGenerator
from thryft_test import _generator_test


class AbstractServiceJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=ValidatingServiceJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return AbstractServiceJavaGeneratorTest.suite()
