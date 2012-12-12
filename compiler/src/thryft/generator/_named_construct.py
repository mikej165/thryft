from thryft.generator._construct import _Construct


class _NamedConstruct(_Construct):
    def __init__(self, name, **kwds):
        _Construct.__init__(self, **kwds)
        assert name is not None
        self.__name = name

    @property
    def name(self):
        return self.__name

    def thrift_qname(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + '.' + self.name
