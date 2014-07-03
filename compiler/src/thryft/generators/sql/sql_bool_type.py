from thryft.generator.bool_type import BoolType
from thryft.generators.sql._sql_base_type import _SqlBaseType


class SqlBoolType(BoolType, _SqlBaseType):
    def sql_name(self):
        return 'TINYINT'
