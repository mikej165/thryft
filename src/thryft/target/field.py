class Field(object):
    def __init__(self, parent, name, type, id=None, required=True, value=None):
        self.__id = id
        self.__name = name
        self.__parent = parent
        self.__type = type
        self.__required = required
        self.__value = value

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def parent(self):
        return self.__parent

    @property
    def type(self):
        return self.__type

    @property
    def required(self):
        return self.__required

    @property
    def value(self):
        return self.__value
