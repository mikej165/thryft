from thryft.generator.typedef import Typedef
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlTypedef(Typedef, _SqlNamedConstruct):
    pass

