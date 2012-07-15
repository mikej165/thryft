from thryft.target.container_types.list_type import ListType
from thryft.targets.java.java_compound_type import JavaCompoundType


class JavaListType(ListType, JavaCompoundType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableList<%s>" % \
                self.element_type.java_name(boxed=True)
