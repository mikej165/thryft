from thryft.generator.construct import Construct


class Const(Construct):
    def __init__(self, type, value, **kwds): #@ReservedAssignment
        Construct.__init__(self, **kwds)
        self.__type = type
        self.__value = value

    @property
    def type(self): #@ReservedAssignment
        return self.__type

    @property
    def value(self):
        return self.__value
