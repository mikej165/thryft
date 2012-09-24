from thryft.generator.container_types.list_type import ListType
from thryft.generators.thrift.thrift_container_type import ThriftContainerType


class ThriftListType(ListType, ThriftContainerType):
    def __repr__(self):
        return "list<%s>" % self.element_type.thrift_qname()
