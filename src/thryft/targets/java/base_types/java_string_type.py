from thryft.target.base_types.string_type import StringType


class JavaStringType(StringType):
    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return 'String'

    def __repr__(self):
        return self.java_name()
