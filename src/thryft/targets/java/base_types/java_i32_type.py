from thryft.target.base_types.i32_type import I32Type
from thryft.targets.java.java_base_type import JavaBaseType


class JavaI32Type(I32Type, JavaBaseType):
    def java_default_value(self):
        return '0'

    def java_hash_code(self, value):
        return "((int)%(value)s)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Integer' or 'int'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']
