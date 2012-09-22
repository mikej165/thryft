from thryft.generator.construct import Construct


class Namespace(Construct):
    def __init__(self, scope=None, **kwds):
        Construct.__init__(self, **kwds)
        self.__scope = scope

    @property
    def scope(self):
        return self.__scope
