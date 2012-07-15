from thryft.target.base_types.string_type import StringType
from thryft.targets.java.java_base_type import JavaBaseType


class JavaStringType(StringType, JavaBaseType):
    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'String'
