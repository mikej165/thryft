from thryft.generator.string_type import StringType
from thryft.generators.sql._sql_base_type import _SqlBaseType


class SqlStringType(StringType, _SqlBaseType):
    def sql_name(self):
        return 'VARCHAR'
