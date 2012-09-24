from thryft.generator.base_types.i64_type import I64Type
from thryft.generators.py.py_base_type import PyBaseType


class PyI64Type(I64Type, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, (int, long))" % locals()
