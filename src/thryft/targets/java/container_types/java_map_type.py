from thryft.target.container_types.map_type import MapType
from thryft.targets.java.java_container_type import JavaContainerType


class JavaMapType(MapType, JavaContainerType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableMap<%s, %s>" % (
                   self.key_type.java_name(boxed=True),
                   self.value_type.java_name(boxed=True)
               )
