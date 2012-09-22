from thryft.generator.construct import Construct


class Typedef(Construct):
    def __init__(self, type, **kwds): #@ReservedAssignment
        Construct.__init__(self, **kwds)
        self.__type = type

    @property
    def qname(self):
        return self.parent.name + '.' + self.name

    @property
    def type(self): #@ReservedAssignment
        return self.__type
