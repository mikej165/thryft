from thryft.target.container_types.set_type import SetType


class JavaSetType(SetType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableSet<%s>" % \
                self.element_type.java_name(boxed=True)

    def __repr__(self):
        return self.java_name()
