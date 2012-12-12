from thryft.generator._type import _Type


class _BaseType(_Type):
    def __init__(self, name):
        _Type.__init__(self, name=name, parent=None)

    def thrift_ttype_name(self):
        return self.name.upper()
