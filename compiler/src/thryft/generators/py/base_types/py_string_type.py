from thryft.generator.base_types.string_type import StringType
from thryft.generators.py.py_base_type import PyBaseType


class PyStringType(StringType, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, basestring)" % locals()

    def py_name(self):
        return 'str'

    def py_repr(self, value):
        return "\"'\" + %(value)s.encode('ascii', 'replace') + \"'\"" % locals()
