from thryft.generator.set_type import SetType
from thryft.generators.thrift._thrift_container_type import _ThriftContainerType


class ThriftSetType(SetType, _ThriftContainerType):
    def __repr__(self):
        return "set<%s>" % self.element_type.thrift_qname()
