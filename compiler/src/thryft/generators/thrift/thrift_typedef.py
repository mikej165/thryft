from thryft.generator.typedef import Typedef
from thryft.generators.thrift.thrift_named_construct import ThriftNamedConstruct


class ThriftTypedef(Typedef, ThriftNamedConstruct):
    def __repr__(self):
        return "typedef %s %s;" % (self.type.thrift_qname(), self.name)
