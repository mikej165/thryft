from thryft.generator.function import Function
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlFunction(Function, _SqlNamedConstruct):
    pass

