from thryft.target.base_types.float_type import FloatType
from thryft.targets.java.java_base_type import JavaBaseType


class JavaFloatType(FloatType, JavaBaseType):
    def java_hash_code(self, value):
        return "Float.floatToIntBits(%(value)s)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Float' or 'float'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']
