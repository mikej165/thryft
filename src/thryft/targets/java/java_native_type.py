from thryft.targets.java.java_type import JavaType


class JavaNativeType(JavaType):
    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()
