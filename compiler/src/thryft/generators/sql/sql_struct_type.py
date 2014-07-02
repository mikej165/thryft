from thryft.generator.struct_type import StructType
from thryft.generators.sql._sql_compound_type import _SqlCompoundType


class SqlStructType(StructType, _SqlCompoundType):
    pass

