from thryft.generator.typedef import Typedef
from thryft.generators.thrift._thrift_named_construct import _ThriftNamedConstruct


class ThriftTypedef(Typedef, _ThriftNamedConstruct):
    def __repr__(self):
        return "typedef %s %s;" % (self.type.thrift_qname(), self.name)
