from thryft.targets.java.java_type import JavaType


class JavaBaseType(JavaType):
    def java_is_reference(self):
        return False

    def __repr__(self):
        return self.java_name()
