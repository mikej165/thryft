from thryft.generator.container_types.set_type import SetType
from thryft.generators.java.java_container_type import JavaContainerType


class JavaSetType(SetType, JavaContainerType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableSet<%s>" % \
                self.element_type.java_name(boxed=True)
