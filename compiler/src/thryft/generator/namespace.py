from thryft.generator._named_construct import _NamedConstruct


class Namespace(_NamedConstruct):
    def __init__(self, scope=None, **kwds):
        _NamedConstruct.__init__(self, **kwds)
        self.__scope = scope

    @property
    def scope(self):
        return self.__scope
