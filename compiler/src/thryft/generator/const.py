from thryft.generator._named_construct import _NamedConstruct

class Const(_NamedConstruct):
    def __init__(self, type, value, **kwds):  # @ReservedAssignment
        _NamedConstruct.__init__(self, **kwds)
        self.__type = type
        self.__value = value

    @property
    def type(self):  # @ReservedAssignment
        return self.__type

    @property
    def value(self):
        return self.__value
