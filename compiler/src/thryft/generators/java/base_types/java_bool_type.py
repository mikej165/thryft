from thryft.generator.base_types.bool_type import BoolType
from thryft.generators.java.java_base_type import JavaBaseType


class JavaBoolType(BoolType, JavaBaseType):
    def java_default_value(self):
        return 'false'

    def java_hash_code(self, value):
        return "(%(value)s ? 1 : 0)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Boolean' or 'boolean'

    def java_to_string(self, value):
        return "Boolean.toString(%(value)s)" % locals()
