from thryft.target.base_types.string_type import StringType
from thryft.targets.py.py_base_type import PyBaseType


class PyStringType(StringType, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, basestring)" % locals()
