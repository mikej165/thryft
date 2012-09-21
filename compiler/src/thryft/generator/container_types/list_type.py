from thryft.generator.container_type import ContainerType


class ListType(ContainerType):
    def __init__(self, name, parent, element_type):
        ContainerType.__init__(self, name=name, parent=parent)
        self.__element_type = element_type

    @property
    def element_type(self):
        return self.__element_type

    def thrift_ttype_id(self):
        return 15

    def thrift_ttype_name(self):
        return 'LIST'
