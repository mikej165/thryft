from thryft.generator.i32_type import I32Type
from thryft.generators.sql._sql_numeric_type import _SqlNumericType


class SqlI32Type(I32Type, _SqlNumericType):
    def sql_name(self):
        return 'INT'
