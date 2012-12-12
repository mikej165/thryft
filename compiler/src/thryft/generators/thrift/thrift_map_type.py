from thryft.generator.map_type import MapType
from thryft.generators.thrift._thrift_container_type import _ThriftContainerType


class ThriftMapType(MapType, _ThriftContainerType):
    def __repr__(self):
        return "map<%s, %s>" % (self.key_type.thrift_qname(), self.value_type.thrift_qname())
