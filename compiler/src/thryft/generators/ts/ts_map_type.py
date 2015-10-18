from thryft.generator.map_type import MapType
from thryft.generators.ts._ts_container_type import _TsContainerType


class TsMapType(MapType, _TsContainerType):
    def ts_qname(self):
        return "{[index: %s]: %s}" % (self.key_type.ts_qname(), self.value_type.ts_qname())
