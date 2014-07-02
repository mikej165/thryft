from thryft.generator.byte_type import ByteType
from thryft.generators.sql._sql_numeric_type import _SqlNumericType


class SqlByteType(ByteType, _SqlNumericType):
    pass
