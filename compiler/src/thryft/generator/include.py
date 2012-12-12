from thryft.generator._construct import _Construct


class Include(_Construct):
    def __init__(self, document, path, **kwds):
        _Construct.__init__(self, **kwds)
        self.__document = document
        self.__path = path

    @property
    def document(self):
        return self.__document

    @property
    def path(self):
        return self.__path
