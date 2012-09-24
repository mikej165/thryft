from thryft.generator.include import Include
from thryft.generators.thrift.thrift_construct import ThriftConstruct


class ThriftInclude(Include, ThriftConstruct):
    def __repr__(self):
        return "include \"%s\"" % self.path
