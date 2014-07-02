from thryft.generator.i64_type import I64Type
from thryft.generators.sql._sql_numeric_type import _SqlNumericType


class SqlI64Type(I64Type, _SqlNumericType):
    pass
