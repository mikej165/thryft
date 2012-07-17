from thryft.target.base_types.i32_type import I32Type
from thryft.targets.py.py_base_type import PyBaseType


class PyI32Type(I32Type, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
