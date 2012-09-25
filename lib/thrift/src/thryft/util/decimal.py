from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.compound_types.java_struct_type import JavaStructType
from thryft.generators.py.compound_types.py_struct_type import PyStructType


class JavaDecimal(JavaStructType):
    def java_declaration_name(self, boxed=False):
        return 'java.math.BigDecimal'

    def java_read_protocol(self):
        return "(iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readDecimal() : new java.math.BigDecimal(iprot.readString())" % locals()

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeDecimal(%(value)s); } else { oprot.writeString(%(value)s.toString()); }" % locals()


class PyDecimal(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, decimal.Decimal)" % locals()

    def py_imports(self, caller_stack=None):
        return PyStructType.py_imports(self, caller_stack=caller_stack) + \
               ['from __future__ import absolute_import; import decimal']

    def py_read_protocol(self):
        return "iprot.readDecimal() if hasattr(iprot, 'readDecimal') else decimal.Decimal(iprot.readString())" % locals()

    def py_read_protocol_throws(self):
        return ['decimal.InvalidOperation', 'TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeDecimal(%(value)s) if hasattr(oprot, 'writeDecimal') else oprot.writeString(str(%(value)s))" % locals()
