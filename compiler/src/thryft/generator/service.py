from thryft.generator.named_construct import NamedConstruct


class Service(NamedConstruct):
    def __init__(self, extends=None, functions=None, **kwds):
        NamedConstruct.__init__(self, **kwds)
        self.__extends = extends
        self.__functions = functions is not None and list(functions) or []

    @property
    def extends(self):
        return self.__extends

    @property
    def functions(self):
        return self.__functions
