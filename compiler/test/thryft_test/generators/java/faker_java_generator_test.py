from thryft.generators.java.faker_java_generator import FakerJavaGenerator
from thryft_test import _generator_test


class FakerJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=FakerJavaGenerator, *args, **kwds)

    def _runTest(self, thrift_file_path):
        repr_ = _generator_test._GeneratorTest._runTest(self, thrift_file_path=thrift_file_path)
        if thrift_file_path.endswith('struct_type.thrift'):
            print repr_
        return repr_


def load_tests(*args, **kwds):
    return FakerJavaGeneratorTest.suite()
