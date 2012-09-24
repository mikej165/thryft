from thryft.generators.thrift.thrift_type import ThriftType


class ThriftBaseType(ThriftType):
    def __repr__(self):
        return self.name
