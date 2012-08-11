from thryft.generators.java.java_type import JavaType


class JavaContainerType(JavaType):
    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def __repr__(self):
        return self.java_name()
