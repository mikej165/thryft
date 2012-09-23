from thryft.generator.named_construct import NamedConstruct

class Const(NamedConstruct):
    def __init__(self, type, value, **kwds): #@ReservedAssignment
        NamedConstruct.__init__(self, **kwds)
        self.__type = type
        self.__value = value

    @property
    def type(self): #@ReservedAssignment
        return self.__type

    @property
    def value(self):
        return self.__value
