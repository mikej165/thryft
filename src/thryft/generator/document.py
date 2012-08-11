from thryft.generator.construct import Construct
from thryft.generator.include import Include
from thryft.generator.namespace import Namespace
import os.path


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
    def includes(self):
        return [header for header in self.headers
                if isinstance(header, Include)]

    @property
    def namespaces(self):
        return [header for header in self.headers
                if isinstance(header, Namespace)]

    @property
    def path(self):
        return self.__path
