from thryft.generator.base_types.i64_type import I64Type
from thryft.generators.java.java_base_type import JavaBaseType


class JavaI64Type(I64Type, JavaBaseType):
    def java_hash_code(self, value):
        return "((int)(%(value)s ^ (%(value)s >>> 32)))" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Long' or 'long'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']
