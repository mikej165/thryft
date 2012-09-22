from thryft.generator.type import Type


class CompoundType(Type):
    def __init__(self, fields=None, **kwds):
        Type.__init__(self, **kwds)
        self._fields = fields is not None and list(fields) or []

    @property
    def qname(self):
        return self.parent.name + '.' + self.name
