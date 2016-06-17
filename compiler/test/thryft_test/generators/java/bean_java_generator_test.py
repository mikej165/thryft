from thryft.generators.java.bean_java_generator import \
    BeanJavaGenerator
from thryft_test import _generator_test


class BeanJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=BeanJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return BeanJavaGeneratorTest.suite()
