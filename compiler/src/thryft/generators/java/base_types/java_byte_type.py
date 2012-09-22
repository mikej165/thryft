from thryft.generator.base_types.byte_type import ByteType
from thryft.generators.java.java_base_type import JavaBaseType


class JavaByteType(ByteType, JavaBaseType):
    def java_default_value(self):
        return '((byte)0)'

    def java_hash_code(self, value):
        return "((byte)%(value)s)" % locals()

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_name(self, boxed=False):
        return boxed and 'Byte' or 'byte'
