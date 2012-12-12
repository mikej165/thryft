from thryft.generator.bool_type import BoolType
from thryft.generators.py._py_base_type import _PyBaseType


class PyBoolType(BoolType, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, bool)" % locals()
