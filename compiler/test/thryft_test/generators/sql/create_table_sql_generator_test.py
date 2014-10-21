from thryft.generators.sql.create_table_sql_generator import CreateTableSqlGenerator
from thryft_test import _generator_test


class CreateTableSqlGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=CreateTableSqlGenerator,
            repr_method_name='sql_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return CreateTableSqlGeneratorTest.suite()
