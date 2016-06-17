from thryft.generators.java.properties_java_generator import \
    PropertiesJavaGenerator
from thryft_test import _generator_test


class PropertiesJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=PropertiesJavaGenerator,
            generator_kwds={'project_name': 'test'},
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return PropertiesJavaGeneratorTest.suite()
