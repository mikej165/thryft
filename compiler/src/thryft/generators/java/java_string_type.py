from thryft.generator.string_type import StringType
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaStringType(StringType, _JavaBaseType):
    def java_default_value(self):
        return 'null'

    def java_from_string(self, value):
        return value

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'String'

    def java_to_string(self, value):
        return value
