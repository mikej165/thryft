from thryft.generator.include import Include


class ThriftInclude(Include):
    def __repr__(self):
        return "include \"%s\"" % self.path
