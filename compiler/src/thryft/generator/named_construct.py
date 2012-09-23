from thryft.generator.construct import Construct


class NamedConstruct(Construct):
    def __init__(self, name, **kwds):
        Construct.__init__(self, **kwds)
        assert name is not None
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def qname(self):
        return self.name
