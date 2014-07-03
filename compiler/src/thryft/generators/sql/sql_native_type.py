from thryft.generator.native_type import NativeType
from thryft.generators.sql._sql_type import _SqlType


class SqlNativeType(NativeType, _SqlType):
    pass
