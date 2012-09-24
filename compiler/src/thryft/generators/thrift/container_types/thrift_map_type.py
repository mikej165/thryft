from thryft.generator.container_types.map_type import MapType
from thryft.generators.thrift.thrift_container_type import ThriftContainerType


class ThriftMapType(MapType, ThriftContainerType):
    def __repr__(self):
        return "map<%s, %s>" % (self.key_type.thrift_qname(), self.value_type.thrift_qname())
