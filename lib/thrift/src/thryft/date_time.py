from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.compound_types.java_struct_type import JavaStructType
from thryft.generators.py.compound_types.py_struct_type import PyStructType



class PyDateTime(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, datetime)" % locals()

    def py_imports(self, caller_stack=None):
        return ['from datetime import datetime', 'from time import mktime']

    def py_name(self):
        return 'datetime'

    def py_read_protocol(self):
        return "datetime.fromtimestamp(iprot.readI64() / 1000)"

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeI64(long(mktime(%(value)s.timetuple())) * 1000l)" % locals()


class JavaDateTime(JavaStructType):
    def java_declaration_name(self, boxed=True):
        return 'org.joda.time.DateTime'

    def java_read_protocol(self):
        return "new org.joda.time.DateTime(iprot.readI64())"

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeI64(%(value)s.getMillis());" % locals()
