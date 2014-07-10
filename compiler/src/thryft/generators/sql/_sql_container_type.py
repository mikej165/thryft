from thryft.generators.sql._sql_type import _SqlType


class _SqlContainerType(_SqlType):
    def sql_name(self):
        return None
