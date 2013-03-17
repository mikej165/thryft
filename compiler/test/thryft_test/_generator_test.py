from thryft.compiler import Compiler
from thryft_test import _test


class _GeneratorTest(_test._Test):
    def __init__(self, *args, **kwds):
        self.__generator_class = kwds.pop('generator_class', None)
        _test._Test.__init__(self, *args, **kwds)

    def _runTest(self, thrift_file_path):
        documents = Compiler().compile(thrift_file_path, generator=self.__generator_class())
        self.assertTrue(isinstance(documents, tuple))
        self.assertEquals(1, len(documents))
        repr(documents[0])
