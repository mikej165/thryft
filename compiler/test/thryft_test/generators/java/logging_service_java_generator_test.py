from thryft.generators.java.logging_service_java_generator import \
    LoggingServiceJavaGenerator
from thryft_test import _generator_test


class LoggingServiceJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=LoggingServiceJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return LoggingServiceJavaGeneratorTest.suite()
