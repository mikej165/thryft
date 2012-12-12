from thryft.generator.struct_type import StructType
from thryft.generators.java.java_struct_type import JavaStructType
from thryft.generators.py.py_struct_type import PyStructType


class PyMixed(PyStructType):
    def py_check(self, value):
        return 'True'

    def py_read_protocol(self):
        return "iprot.readMixed()" % locals()

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeMixed(%(value)s)" % locals()


class JavaMixed(JavaStructType):
    def java_declaration_name(self, boxed=True):
        return 'java.lang.Object'

    def java_read_protocol(self):
        return "((org.thryft.protocol.Protocol)iprot).readMixed()" % locals()

    def java_write_protocol(self, value, depth=0):
        return "((org.thryft.protocol.Protocol)oprot).writeMixed(%(value)s);" % locals()
