from thryft.generators.java.gwt_client_java_generator import \
    GwtClientJavaGenerator
from thryft_test import _generator_test


class GwtClientJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtClientJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtClientJavaGeneratorTest.suite()
