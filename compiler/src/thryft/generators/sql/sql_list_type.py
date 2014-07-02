from thryft.generator.list_type import ListType
from thryft.generators.sql._sql_sequence_type import _SqlSequenceType


class SqlListType(ListType, _SqlSequenceType):
    pass

