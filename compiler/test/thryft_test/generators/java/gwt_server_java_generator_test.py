from thryft.generators.java.gwt_server_java_generator import \
    GwtServerJavaGenerator
from thryft_test import _generator_test


class GwtServerJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtServerJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtServerJavaGeneratorTest.suite()
