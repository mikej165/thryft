from thryft.generator.const import Const
from yutil import rpad


class ThriftConst(Const):
    def __repr__(self):
        return "%sconst %s %s = %s;" % (
                   self.comment is not None and rpad(repr(self.comment), "\n") or '',
                   self.type.qname,
                   self.name,
                   isinstance(self.value, str) and '"%s"' % self.value or str(self.value)
                )
