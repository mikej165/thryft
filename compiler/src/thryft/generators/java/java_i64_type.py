from thryft.generator.i64_type import I64Type
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaI64Type(I64Type, _JavaBaseType):
    def java_default_value(self):
        return '((long)0)'

    def java_hash_code(self, value):
        return "((int)(%(value)s ^ (%(value)s >>> 32)))" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Long' or 'long'

    def java_read_protocol_throws(self):
        return ['NumberFormatException']

    def java_to_string(self, value):
        return "Long.toString(%(value)s)" % locals()
