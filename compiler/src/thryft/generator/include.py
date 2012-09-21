from thryft.generator.construct import Construct


class Include(Construct):
    def __init__(self, document, name, parent, path):
        Construct.__init__(self, name=name, parent=parent)
        self.__document = document
        self.__path = path

    @property
    def document(self):
        return self.__document

    @property
    def path(self):
        return self.__path
