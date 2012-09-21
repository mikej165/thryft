from thryft.generator.typedef import Typedef


class ThriftTypedef(Typedef):
    def __repr__(self):
        return "typedef %s %s;" % (self.type.qname, self.name)
