from thryft.generator.const import Const
from thryft.generators.thrift.thrift_named_construct import ThriftNamedConstruct
from yutil import rpad


class ThriftConst(Const, ThriftNamedConstruct):
    def __repr__(self):
        return "%sconst %s %s = %s;" % (
                   self.comment is not None and rpad(repr(self.comment), "\n") or '',
                   self.type.thrift_qname(),
                   self.name,
                   isinstance(self.value, str) and '"%s"' % self.value or str(self.value)
                )
