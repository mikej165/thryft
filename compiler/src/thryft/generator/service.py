from thryft.generator._named_construct import _NamedConstruct


class Service(_NamedConstruct):
    def __init__(self, extends=None, functions=None, **kwds):
        _NamedConstruct.__init__(self, **kwds)
        self.__extends = extends
        self.__functions = functions is not None and list(functions) or []

    @property
    def extends(self):
        return self.__extends

    @property
    def functions(self):
        return self.__functions
