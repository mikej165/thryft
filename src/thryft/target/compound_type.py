from thryft.target.type import Type


class CompoundType(Type):
    def __init__(self, name, parent, fields=None):
        Type.__init__(self, name=name, parent=parent)
        self.__fields = fields is not None and list(fields) or []

    @property
    def fields(self):
        return self.__fields

    @property
    def qname(self):
        return self.parent.name + '.' + self.name
