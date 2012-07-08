from thryft.target.base_types.binary_type import BinaryType


class ThriftBinaryType(BinaryType):
    def __repr__(self):
        return self.name
