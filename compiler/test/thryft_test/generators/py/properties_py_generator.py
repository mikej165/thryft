from thryft.generators.py.properties_py_generator import \
    PropertiesPyGenerator
from thryft_test import _generator_test


class PropertiesPyGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=PropertiesPyGenerator,
            generator_kwds={'project_name': 'test'},
            repr_method_name='py_repr',
            *args, **kwds
        )

    def _runTest(self, *args, **kwds):
        document_repr = _generator_test._GeneratorTest._runTest(self, *args, **kwds)
        compile(document_repr, '<string>', 'exec')


def load_tests(*args, **kwds):
    return PropertiesPyGeneratorTest.suite()
