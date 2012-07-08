from thryft.target.namespace import Namespace


class ThriftNamespace(Namespace):
    def __repr__(self):
        return "namespace %s %s" % \
            (self.scope is None and '*' or self.scope, self.name)
