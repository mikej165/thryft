from thryft.target.container_types.list_type import ListType


class ThriftListType(ListType):
    def __repr__(self):
        return "list<%s>" % self.element_type.qname
