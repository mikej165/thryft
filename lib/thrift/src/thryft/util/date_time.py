from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.compound_types.java_struct_type import JavaStructType
from thryft.generators.py.compound_types.py_struct_type import PyStructType



class PyDateTime(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, datetime)" % locals()

    def py_imports(self, caller_stack=None):
        return PyStructType.py_imports(self, caller_stack=caller_stack) + \
               ['from datetime import datetime', 'from time import mktime']

    def py_read_protocol(self):
        qname = self.py_qname()
        return "datetime.fromtimestamp(%(qname)s.read(iprot).timestamp_ms / 1000)" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "%(qname)s(long(mktime(%(value)s.timetuple())) * 1000l).write(oprot)" % locals()


class JavaDateTime(JavaStructType):
    def java_declaration_name(self, boxed=True):
        return 'org.joda.time.DateTime'

    def java_read_protocol(self):
        name = self.java_name()
        return "new org.joda.time.DateTime(new %(name)s(iprot).getTimestampMs())" % locals()

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        name = self.java_name()
        return "new %(name)s(%(value)s.getMillis()).write(oprot);" % locals()
