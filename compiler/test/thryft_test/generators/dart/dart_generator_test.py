from thryft.generators.dart.dart_generator import DartGenerator
from thryft_test import _generator_test


class DartGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=DartGenerator,
            generator_kwds={'package_name': 'thryft'},
            repr_method_name='dart_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return DartGeneratorTest.suite()
