from thryft.generator.i16_type import I16Type
from thryft.generators.py._py_base_type import _PyBaseType


class PyI16Type(I16Type, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
