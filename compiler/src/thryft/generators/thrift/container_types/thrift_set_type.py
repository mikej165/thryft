from thryft.generator.container_types.set_type import SetType
from thryft.generators.thrift.thrift_container_type import ThriftContainerType


class ThriftSetType(SetType, ThriftContainerType):
    def __repr__(self):
        return "set<%s>" % self.element_type.thrift_qname()
