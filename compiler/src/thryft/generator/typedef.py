from thryft.generator._named_construct import _NamedConstruct


class Typedef(_NamedConstruct):
    def __init__(self, type, **kwds):  # @ReservedAssignment
        _NamedConstruct.__init__(self, **kwds)
        self.__type = type

    @property
    def type(self):  # @ReservedAssignment
        return self.__type
