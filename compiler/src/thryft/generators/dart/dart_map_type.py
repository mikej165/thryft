from thryft.generator.map_type import MapType
from thryft.generators.dart._dart_container_type import _DartContainerType


class DartMapType(MapType, _DartContainerType):
    def dart_name(self):
        return "Map<%s, %s>" % (self.key_type.dart_name(), self.value_type.dart_name())
