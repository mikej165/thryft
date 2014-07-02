from thryft.generator.const import Const
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlConst(Const, _SqlNamedConstruct):
    pass
