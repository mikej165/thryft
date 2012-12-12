from thryft.generator.struct_type import StructType
from thryft.generators.java.java_struct_type import JavaStructType
from thryft.generators.py.py_struct_type import PyStructType


class JavaDateTime(JavaStructType):
    def java_declaration_name(self, boxed=True):
        return 'org.joda.time.DateTime'

    def java_read_protocol(self):
        return "(iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readDateTime() : new org.joda.time.DateTime(iprot.readI64())" % locals()

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeDateTime(%(value)s); } else { oprot.writeI64(%(value)s.getMillis()); }" % locals()


class PyDateTime(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, datetime)" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return ['from datetime import datetime', 'from time import mktime']

    def py_read_protocol(self):
        return "iprot.readDateTime() if hasattr(iprot, 'readDateTime') else datetime.fromtimestamp(iprot.readI64() / 1000.0)" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeDateTime(%(value)s) if hasattr(oprot, 'writeDateTime') else oprot.writeI64(long(mktime(%(value)s.timetuple())) * 1000l)" % locals()
