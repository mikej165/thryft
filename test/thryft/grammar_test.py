import os.path
import unittest

from thryft.grammar import Grammar


class GrammarTest(unittest.TestCase):
    def runTest(self):
        Grammar().function.parseString("void TestFunction1()", parseAll=True)

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

                print file_name,
                try:
                    tokens = \
                        Grammar().document.parseFile(
                            thrift_file_path,
                            parseAll=True
                        )
                    self.assertTrue(len(tokens) > 0)
                except:
                    print
                    raise
                print tokens
