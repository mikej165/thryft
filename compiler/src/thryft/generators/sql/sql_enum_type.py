from thryft.generator.enum_type import EnumType
from thryft.generators.sql._sql_type import _SqlType


class SqlEnumType(EnumType, _SqlType):
    pass

