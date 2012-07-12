from thryft.target.base_types.string_type import StringType


class JavaStringType(StringType):
    def java_hashCode(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'String'

    def __repr__(self):
        return self.java_name()
