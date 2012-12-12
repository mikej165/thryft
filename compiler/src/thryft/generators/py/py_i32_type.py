from thryft.generator.i32_type import I32Type
from thryft.generators.py._py_base_type import _PyBaseType


class PyI32Type(I32Type, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
