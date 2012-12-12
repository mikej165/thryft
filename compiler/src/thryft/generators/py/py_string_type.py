from thryft.generator.string_type import StringType
from thryft.generators.py._py_base_type import _PyBaseType


class PyStringType(StringType, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, basestring)" % locals()

    def py_name(self):
        return 'str'

    def py_repr(self, value):
        return "\"'\" + %(value)s.encode('ascii', 'replace') + \"'\"" % locals()
