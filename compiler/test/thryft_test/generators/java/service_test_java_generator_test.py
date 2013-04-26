from thryft.generators.java.service_test_java_generator import \
    ServiceTestJavaGenerator
from thryft_test import _generator_test


class ServiceTestJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=ServiceTestJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return ServiceTestJavaGeneratorTest.suite()
