from thryft.generator.container_types.set_type import SetType


class ThriftSetType(SetType):
    def __repr__(self):
        return "set<%s>" % self.element_type.qname
