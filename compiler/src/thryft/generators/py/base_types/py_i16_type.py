from thryft.generator.base_types.i16_type import I16Type
from thryft.generators.py.py_base_type import PyBaseType


class PyI16Type(I16Type, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
