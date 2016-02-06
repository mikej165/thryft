from thryft.generator.double_type import DoubleType
from thryft.generators.sql._sql_numeric_type import _SqlNumericType


class SqlDoubleType(DoubleType, _SqlNumericType):
    def sql_name(self):
        return 'FLOAT'
