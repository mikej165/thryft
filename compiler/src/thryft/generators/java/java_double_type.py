from thryft.generator.double_type import DoubleType
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaDoubleType(DoubleType, _JavaBaseType):
    def java_hash_code(self, value):
        return "((int)(Double.doubleToLongBits(%(value)s) ^ (Double.doubleToLongBits(%(value)s) >>> 32)))" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Double' or 'double'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_to_string(self, value):
        return "Double.toString(%(value)s)" % locals()
