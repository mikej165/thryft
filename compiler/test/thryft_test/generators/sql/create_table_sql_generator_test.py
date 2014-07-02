from thryft.generators.sql.sql_generator import SqlGenerator
from thryft_test import _generator_test


class CreateTableSqlGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=SqlGenerator, *args, **kwds)

    def _runTest(self, *args, **kwds):
        document_repr = _generator_test._GeneratorTest._runTest(self, *args, **kwds)
        compile(document_repr, '<string>', 'exec')


def load_tests(*args, **kwds):
    return CreateTableSqlGeneratorTest.suite()
