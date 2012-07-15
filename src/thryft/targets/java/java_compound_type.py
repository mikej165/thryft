from thryft.targets.java.java_type import JavaType


class JavaCompoundType(JavaType):
    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True
