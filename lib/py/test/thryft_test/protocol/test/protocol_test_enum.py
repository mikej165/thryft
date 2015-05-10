class ProtocolTestEnum(object):
    ENUMERATOR1 = None
    ENUMERATOR2 = None

    def __init__(self, name, value):
        object.__init__(self)
        self.__name = name
        self.__value = value

    def __int__(self):
        return self.__value

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

    @classmethod
    def value_of(cls, name):
        if name == 'ENUMERATOR1' or name == '1':
            return getattr(ProtocolTestEnum, 'ENUMERATOR1')
        elif name == 'ENUMERATOR2' or name == '2':
            return getattr(ProtocolTestEnum, 'ENUMERATOR2')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (ProtocolTestEnum.ENUMERATOR1, ProtocolTestEnum.ENUMERATOR2,)

ProtocolTestEnum.ENUMERATOR1 = ProtocolTestEnum('ENUMERATOR1', 1)
ProtocolTestEnum.ENUMERATOR2 = ProtocolTestEnum('ENUMERATOR2', 2)
