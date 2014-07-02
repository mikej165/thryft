from thryft.generator.map_type import MapType
from thryft.generators.sql._sql_container_type import _SqlContainerType


class SqlMapType(MapType, _SqlContainerType):
    pass
