from thryft.generator.construct import Construct


class Field(Construct):
    def __init__(
        self,
        name,
        parent,
        type,
        id=None,
        required=True,
        value=None
    ):
        Construct.__init__(self, name=name, parent=parent)
        self.__id = id
        self.__type = type
        self.__required = required
        self.__value = value

    @property
    def id(self): #@ReservedAssignment
        return self.__id

    @property
    def type(self): #@ReservedAssignment
        return self.__type

    @property
    def required(self):
        return self.__required

    @property
    def value(self):
        return self.__value
