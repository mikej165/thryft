from thryft.generators.py.jsonrpc_client_py_generator import \
    JsonrpcClientPyGenerator
from thryft_test import _generator_test


class JsonrpcClientPyGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JsonrpcClientPyGenerator, *args, **kwds)

    def _runTest(self, *args, **kwds):
        document_repr = _generator_test._GeneratorTest._runTest(self, *args, **kwds)
        compile(document_repr, '<string>', 'exec')


def load_tests(*args, **kwds):
    return JsonrpcClientPyGeneratorTest.suite()
