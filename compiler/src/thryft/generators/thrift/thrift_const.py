from thryft.generator.const import Const


class ThriftConst(Const):
    def __repr__(self):
        return "const %s %s = %s;" % (self.type.qname, self.name, str(self.value))
