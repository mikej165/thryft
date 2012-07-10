from thryft.target.container_types.list_type import ListType


class JavaListType(ListType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableList<%s>" % \
                self.element_type.java_name(boxed=True)

    def __repr__(self):
        return self.java_name()
