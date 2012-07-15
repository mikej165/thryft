from thryft.target.native_types.decimal_type import DecimalType
from thryft.targets.java.java_native_type import JavaNativeType


class JavaDecimalType(DecimalType, JavaNativeType):
    def java_name(self, boxed=False):
        return 'java.math.BigDecimal'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()
