from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.compound_types.java_struct_type import JavaStructType
from thryft.generators.py.compound_types.py_struct_type import PyStructType


class JavaDecimal(JavaStructType):
    def java_declaration_name(self, boxed=False):
        return 'java.math.BigDecimal'

    def java_read_protocol(self):
        return "new java.math.BigDecimal(iprot.readString())"

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()


class PyDecimal(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, Decimal)" % locals()

    def py_imports(self, caller_stack=None):
        return ['from decimal import Decimal, InvalidOperation']

    def py_name(self):
        return 'java.math.BigDecimal'

    def py_read_protocol(self):
        return "Decimal(iprot.readString())"

    def py_read_protocol_throws(self):
        return ['InvalidOperation', 'TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeString(str(%(value)s))" % locals()
