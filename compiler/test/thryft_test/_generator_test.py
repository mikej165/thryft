from thryft.compiler import Compiler
from thryft_test import _test


class _GeneratorTest(_test._Test):
    def __init__(self, *args, **kwds):
        self.__generator_class = kwds.pop('generator_class', None)
        self.__generator_kwds = kwds.pop('generator_kwds', {})
        self.__repr_method_name = kwds.pop('repr_method_name', None)
        _test._Test.__init__(self, *args, **kwds)

    def _runTest(self, thrift_file_path):
        document =\
            Compiler().compile(
                generator=self.__generator_class(**self.__generator_kwds),
                thrift_file_path=thrift_file_path
            )
#         import os.path
#         thrift_file_name = os.path.split(thrift_file_path)[1]
#         if thrift_file_name.endswith('_type.thrift') and not 'struct' in thrift_file_name and not 'enum' in thrift_file_name and not 'exception' in thrift_file_name:
#             print repr(documents[0])
        return getattr(document, self.__repr_method_name)()
