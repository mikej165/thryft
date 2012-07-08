from thryft.target.base_types.numeric_type import NumericType


class ThriftNumericType(NumericType):
    def __repr__(self):
        return self.name
