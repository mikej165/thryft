from thryft.generators.py.py_generator import PyGenerator
from thryft_test import _generator_test


class PyGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=PyGenerator,
            repr_method_name='py_repr',
            *args, **kwds
        )

    def _runTest(self, *args, **kwds):
        document_repr = _generator_test._GeneratorTest._runTest(self, *args, **kwds)
        compile(document_repr, '<string>', 'exec')


def load_tests(*args, **kwds):
    return PyGeneratorTest.suite()
