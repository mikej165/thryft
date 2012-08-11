from thryft.generator.container_types.map_type import MapType


class ThriftMapType(MapType):
    def __repr__(self):
        return "map<%s, %s>" % (self.key_type.qname, self.value_type.qname)
