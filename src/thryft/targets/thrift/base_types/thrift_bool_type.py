from thryft.target.base_types.bool_type import BoolType


class ThriftBoolType(BoolType):
    def __repr__(self):
        return self.name
