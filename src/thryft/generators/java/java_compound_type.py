from thryft.generators.java.java_type import JavaType


class JavaCompoundType(JavaType):
    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return getattr(self, 'name')
