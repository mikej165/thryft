import os.path
from thryft.target.construct import Construct


class Document(Construct):
    def __init__(self, path, definitions=None, headers=None):
        self.__path = os.path.abspath(path)
        Construct.__init__(
            self,
            name=os.path.splitext(os.path.split(self.__path)[1])[0],
            parent=None
        )
        self.__definitions = \
            definitions is not None and list(definitions) or []
        self.__headers = headers is not None and list(headers) or []

    @property
    def definitions(self):
        return self.__definitions

    @property
    def headers(self):
        return self.__headers

    @property
    def path(self):
        return self.__path
