from thryft.generator._type import _Type


class _CompoundType(_Type):
    def __init__(self, fields=None, **kwds):
        _Type.__init__(self, **kwds)
        self._fields = fields is not None and list(fields) or []
