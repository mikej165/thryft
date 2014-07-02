from thryft.generator.service import Service
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlService(Service, _SqlNamedConstruct):
    pass
