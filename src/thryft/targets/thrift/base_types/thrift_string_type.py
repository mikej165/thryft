from thryft.target.base_types.string_type import StringType


class ThriftStringType(StringType):
    def __repr__(self):
        return self.name
