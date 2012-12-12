from thryft.generator.byte_type import ByteType
from thryft.generators.py._py_base_type import _PyBaseType


class PyByteType(ByteType, _PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
