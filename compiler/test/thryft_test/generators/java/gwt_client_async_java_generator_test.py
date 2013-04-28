from thryft.generators.java.gwt_client_async_java_generator import \
    GwtClientAsyncJavaGenerator
from thryft_test import _generator_test


class GwtClientAsyncJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtClientAsyncJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtClientAsyncJavaGeneratorTest.suite()
