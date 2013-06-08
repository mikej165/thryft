from thryft.generators.java.gwt_servlet_java_generator import \
    GwtServletJavaGenerator
from thryft_test import _generator_test


class GwtServletJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=GwtServletJavaGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return GwtServletJavaGeneratorTest.suite()
