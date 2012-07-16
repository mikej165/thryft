from thryft.target.type import Type


class BaseType(Type):
    def __init__(self, name):
        Type.__init__(self, name=name, parent=None)

    def thrift_ttype_name(self):
        return self.name.upper()
