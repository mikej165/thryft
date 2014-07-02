from thryft.generator.include import Include
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlInclude(Include, _SqlNamedConstruct):
    pass
