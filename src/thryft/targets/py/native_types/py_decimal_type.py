from thryft.target.native_types.decimal_type import DecimalType
from thryft.targets.py.py_native_type import PyNativeType


class PyDecimalType(DecimalType, PyNativeType):
    def py_check(self, value):
        return "isinstance(%(value)s, Decimal)" % locals()

    def py_imports(self):
        return ['from decimal import Decimal, InvalidOperation']

    def py_name(self):
        return 'java.math.BigDecimal'

    def py_read_protocol(self):
        return "Decimal(iprot.readString())"

    def py_read_protocol_throws(self):
        return ['InvalidOperation', 'TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeString(str(%(value)s))" % locals()
