from thryft.generator.exception_type import ExceptionType
from thryft.generators.sql._sql_compound_type import _SqlCompoundType


class SqlExceptionType(ExceptionType, _SqlCompoundType):
    pass

