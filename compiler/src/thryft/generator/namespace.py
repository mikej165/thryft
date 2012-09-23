from thryft.generator.named_construct import NamedConstruct


class Namespace(NamedConstruct):
    def __init__(self, scope=None, **kwds):
        NamedConstruct.__init__(self, **kwds)
        self.__scope = scope

    @property
    def scope(self):
        return self.__scope
