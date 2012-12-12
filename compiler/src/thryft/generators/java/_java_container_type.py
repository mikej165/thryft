from thryft.generators.java._java_type import _JavaType


class _JavaContainerType(_JavaType):
    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()
