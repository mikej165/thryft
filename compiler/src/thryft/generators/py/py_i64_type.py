from thryft.generator.i64_type import I64Type
from thryft.generators.py._py_base_type import _PyBaseType


class PyI64Type(I64Type, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, (int, long))" % locals()
