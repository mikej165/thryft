from thryft.generator.field import Field
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlField(Field, _SqlNamedConstruct):
    pass
