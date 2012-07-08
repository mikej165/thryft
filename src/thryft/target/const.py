from thryft.target.construct import Construct


class Const(Construct):
    def __init__(self, name, parent, type, value): #@ReservedAssignment
        Construct.__init__(self, name=name, parent=parent)
        self.__type = type
        self.__value = value

    @property
    def type(self): #@ReservedAssignment
        return self.__type

    @property
    def value(self):
        return self.__value
