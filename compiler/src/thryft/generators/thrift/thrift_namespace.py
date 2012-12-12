from thryft.generator.namespace import Namespace
from thryft.generators.thrift._thrift_named_construct import _ThriftNamedConstruct


class ThriftNamespace(Namespace, _ThriftNamedConstruct):
    def __repr__(self):
        return "namespace %s %s" % \
            (self.scope is None and '*' or self.scope, self.name)
