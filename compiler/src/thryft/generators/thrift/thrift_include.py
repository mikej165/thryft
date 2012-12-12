from thryft.generator.include import Include
from thryft.generators.thrift._thrift_construct import _ThriftConstruct


class ThriftInclude(Include, _ThriftConstruct):
    def __repr__(self):
        return "include \"%s\"" % self.path
