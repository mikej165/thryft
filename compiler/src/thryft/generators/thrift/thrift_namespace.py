from thryft.generator.namespace import Namespace
from thryft.generators.thrift.thrift_named_construct import ThriftNamedConstruct


class ThriftNamespace(Namespace, ThriftNamedConstruct):
    def __repr__(self):
        return "namespace %s %s" % \
            (self.scope is None and '*' or self.scope, self.name)
