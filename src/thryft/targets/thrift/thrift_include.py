from thryft.target.include import Include


class ThriftInclude(Include):
    def __repr__(self):
        return "include \"%s\"" % self.path
