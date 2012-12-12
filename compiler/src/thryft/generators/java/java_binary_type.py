from thryft.generator.binary_type import BinaryType
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaBinaryType(BinaryType, _JavaBaseType):
    def java_default_value(self):
        return 'null'

    def java_from_string(self, value):
        return "java.nio.ByteBuffer.wrap(%(value)s.getBytes())" % locals()

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'java.nio.ByteBuffer'

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()
