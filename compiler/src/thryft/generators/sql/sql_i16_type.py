from thryft.generator.i16_type import I16Type
from thryft.generators.sql._sql_numeric_type import _SqlNumericType


class SqlI16Type(I16Type, _SqlNumericType):
    pass

