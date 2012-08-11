from thryft.compiler import Compiler
from thryft.generators.thrift.thrift_generator import ThriftGenerator
import os.path
import unittest


class CompilerTest(unittest.TestCase):
    def runTest(self):
        generator = ThriftGenerator()
        compiler = Compiler(generator=generator)

        for dir_path, _, file_names in \
            os.walk(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    'grammar_tests'
                )
            ):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.thrift':
                    continue
                thrift_file_path = os.path.join(dir_path, file_name)

                print file_name
                try:
                    compiler((thrift_file_path,))
                except RuntimeError:
                    if file_name != 'include.thrift':
                        raise
                except:
                    print
                    raise
