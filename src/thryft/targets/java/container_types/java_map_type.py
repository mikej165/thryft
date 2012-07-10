from thryft.target.container_types.map_type import MapType


class JavaMapType(MapType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableMap<%s, %s>" % (
                   self.key_type.java_name(boxed=True),
                   self.value_type.java_name(boxed=True)
               )

    def __repr__(self):
        return self.java_name()
