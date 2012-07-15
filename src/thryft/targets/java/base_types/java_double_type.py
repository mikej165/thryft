from thryft.target.base_types.double_type import DoubleType
from thryft.targets.java.java_base_type import JavaBaseType


class JavaDoubleType(DoubleType, JavaBaseType):
    def java_hash_code(self, value):
        return "((int)(Double.doubleToLongBits(%(value)s) ^ (Double.doubleToLongBits(%(value)s) >>> 32)))" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Double' or 'double'
