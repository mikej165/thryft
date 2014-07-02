from thryft.generator.set_type import SetType
from thryft.generators.sql._sql_sequence_type import _SqlSequenceType


class SqlSetType(SetType, _SqlSequenceType):
    pass
