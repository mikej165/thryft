from thryft.compiler import Compiler
from thryft_test import _test


class _GeneratorTest(_test._Test):
    def __init__(self, *args, **kwds):
        self.__generator_class = kwds.pop('generator_class', None)
        _test._Test.__init__(self, *args, **kwds)

    def _runTest(self, thrift_file_path):
        document = Compiler(generator=self.__generator_class()).compile(thrift_file_path)
        self.assertNotEquals(len(repr(document)), 0)
