from thryft.generator.base_types.byte_type import ByteType
from thryft.generators.py.py_base_type import PyBaseType


class PyByteType(ByteType, PyBaseType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()
