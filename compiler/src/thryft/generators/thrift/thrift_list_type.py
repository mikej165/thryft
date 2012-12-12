from thryft.generator.list_type import ListType
from thryft.generators.thrift._thrift_container_type import _ThriftContainerType


class ThriftListType(ListType, _ThriftContainerType):
    def __repr__(self):
        return "list<%s>" % self.element_type.thrift_qname()
