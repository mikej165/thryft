from thryft.target.container_type import ContainerType


class MapType(ContainerType):
    def __init__(self, name, parent, key_type, value_type):
        ContainerType.__init__(self, name=name, parent=parent)
        self.__key_type = key_type
        self.__value_type = value_type

    @property
    def key_type(self):
        return self.__key_type

    def thrift_ttype_id(self):
        return 13

    def thrift_ttype_name(self):
        return 'MAP'

    @property
    def value_type(self):
        return self.__value_type
