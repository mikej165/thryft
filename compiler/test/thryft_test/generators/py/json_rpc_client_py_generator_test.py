from thryft.generators.py.json_rpc_client_py_generator import \
    JsonRpcClientPyGenerator
from thryft_test import _generator_test


class JsonRpcClientPyGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=JsonRpcClientPyGenerator,
            repr_method_name='py_repr',
            *args, **kwds
        )

    def _runTest(self, *args, **kwds):
        document_repr = _generator_test._GeneratorTest._runTest(self, *args, **kwds)
        compile(document_repr, '<string>', 'exec')


def load_tests(*args, **kwds):
    return JsonRpcClientPyGeneratorTest.suite()
