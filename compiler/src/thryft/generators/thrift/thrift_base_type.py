from thryft.generators.thrift._thrift_type import _ThriftType


class ThriftBaseType(_ThriftType):
    def __repr__(self):
        return self.name
