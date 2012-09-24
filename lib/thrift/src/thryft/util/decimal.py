from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.compound_types.java_struct_type import JavaStructType
from thryft.generators.py.compound_types.py_struct_type import PyStructType


class JavaDecimal(JavaStructType):
    def java_declaration_name(self, boxed=False):
        return 'java.math.BigDecimal'

    def java_read_protocol(self):
        name = self.java_name()
        return "new java.math.BigDecimal(new %(name)s(iprot).getValue())" % locals()

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        name = self.java_name()
        return "new %(name)s(%(value)s.toString()).write(oprot);" % locals()


class PyDecimal(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, Decimal)" % locals()

    def py_imports(self, caller_stack=None):
        return PyStructType.py_imports(self, caller_stack=caller_stack) + \
               ['from __future__ import absolute_import; from decimal import Decimal, InvalidOperation']

    def py_read_protocol(self):
        qname = self.py_qname()
        return "Decimal(%(qname)s.read(iprot).value)" % locals()

    def py_read_protocol_throws(self):
        return ['InvalidOperation', 'TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "%(qname)s(str(%(value)s)).write(oprot)" % locals()
