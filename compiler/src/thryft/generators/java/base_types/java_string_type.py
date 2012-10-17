from thryft.generator.base_types.string_type import StringType
from thryft.generators.java.java_base_type import JavaBaseType


class JavaStringType(StringType, JavaBaseType):
    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'String'

    def java_to_string(self, value):
        return value
