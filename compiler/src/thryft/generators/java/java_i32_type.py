from thryft.generator.i32_type import I32Type
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaI32Type(I32Type, _JavaBaseType):
    def java_default_value(self):
        return '0'

    def java_hash_code(self, value):
        return "((int)%(value)s)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Integer' or 'int'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_to_string(self, value):
        return "Integer.toString(%(value)s)" % locals()
