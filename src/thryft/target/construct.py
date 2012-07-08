class Construct(object):
    def __init__(self, name, parent):
        self.__name = name
        self.__parent = parent

    @property
    def name(self):
        return self.__name

    @property
    def parent(self):
        return self.__parent

    @property
    def qname(self):
        from thryft.target.document import Document

        if isinstance(self, Document):
            return self.name
        elif not isinstance(self.parent, Document):
            return self.name
        else:
            return self.parent.name + '.' + self.name
