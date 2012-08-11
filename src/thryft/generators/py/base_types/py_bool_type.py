from thryft.generator.base_types.bool_type import BoolType
from thryft.generators.py.py_base_type import PyBaseType


class PyBoolType(BoolType, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, bool)" % locals()
